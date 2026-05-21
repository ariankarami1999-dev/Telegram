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
<img src="https://cdn4.telesco.pe/file/QpzIRx6W7kpfbSUkGfBpe9d8FAl2Zx1zv4ndjG-oQ77b7khfY79b3-oZGHJCl4PtGS_pz3XEW6Xtsp5GL4IPszB5B5XQWesp0AVVZnNoP4AybYabeEVKCr0Eq93PV56raYJh4Uitk5zbwf8iNhygMSIrW_V1QmhczYiox0QOBzsxv45NAqQa9M3f5fjyOrjjTf3U9JWdLGKf6ZLpOJvGkODfNLv2nKKTPyAqkNFu9Br8hgyc1aMyKaiGE9Ft_gMm8m0mbcF7H8BQyWveiOlYd4NZQ2RoTAFL__E6ICO9MTeQLF-Mc5WtUzM2VZvi-Q-DECC0xw_Tilfo5NUa5KIK7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 20:07:52</div>
<hr>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3NsPUbdrLJqzw0v9b5gQPrAEVXTCYX2WARHi6xepxBx7vOlxbOT4tgKfoBIaCcZfP6roIipr1Uj8VhDubXyAE6BNJ6WXciqnRdWIxgQnaXEiyPzA9wVqTCHP1tnHASs391r8ON-CYsptq90G4oRNBDq65IvHkkQq5iB8WqvI3uOZ4sYZQ9kSp69IEhjZnmEmmtEGLDVQM-cby8JU_egCe4BMQnWOu8Dore4PoUifNF1mnvA_AK36nSOZhTHq2Dh4uzUj6PODsETdw1tGUQFg3pBn9pVF_PkQd9l4lZjYyPkGtMSnXu7OSnwi_12F9wI2BKALRwZoN0rTCvsxiBZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8fuiwl9SurRB_3zT4JZT56EJvvFoFy3q9ChJf1Pu__vtXqs05Esp1HZxrWkuT1j2wZZJfGsoo6YoBeFdBINpAZbyfhY3q7ZxeMzs3JYRDtgQ8mXewdgUDSVgGvxKqCkQ4u4Na1B9xArpK63m0BswcwavfMLyh4AFdQQ24LUL6Jjcf9TMJ-Wz51tSTztXUfHsFiY1-Y2DEsNxU4SZetF9D6nX4gWLes_fVclwDfCyMUoZce-DY6nYsX6rZF1Tb-p-vQ3iaCqeAEiNgjIaw7raprW4fce_bzDp499DTJREtJzPKXooBrjrYvaee2B-eci79ZJ_8LQQ_ZcJmFXajLHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S6e80wzT9j9TOTj_9CSMgFXs3zL-KqGB-0SU29efo2HDop4HRm3QsDRlOFzK3my0B-Od6BLOo1dgU4Ch4VE_Li9ksYAQRDa8734iLCTw3LM5xu23w6WvgROpQC8RGSO2BKKVXGCyosisphONyhYzwfU-YTChfBQFhHsHCmv6B_M3uwVsEWzF2plL4fb3JYqfd6pOkYnBZr9lpG8oTjnVjK5KL6rpcNCs9kAzE_h5YqMAIMlO-PVPhavnEhCBZCnVNkX7Xik2TS3Hn2kIhavRKnsWzNkqa78Auc2CECRao1nATnK-CCr0gtCVt-XXmIt-euvrm8M7WJTZ76e9MBn5UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F1iwg92upy5UfaJRVxU6qfOzIRtdnYdX-ZnbHhd0m8TFTweKak0wbqNi7EP9mQj6iXINA01pItR7jkXZXl3afaPrEmfk9-m_8dK7CzyMWz6Fg3H6o2g_PKdgCdYnFjraoJr3LuOyvH-cKCuPdaC0z0vBgkKfRC_MbjM-B1nNjzehkHjhXmei4U7jgOG82oqzjJKfPtYAo6kFqe7nWlKM4tY1ma9f8zLS82KxT6WM1V3ln_R-1DsyJ15o-YgTjbSWfaUbo57TV__7CcdDKXtLMtQnV-wj2UqXJ9g_r9ACUymg-W7p274nppjHswIGArTJ9r_-HkLfJOaplNaL7KbbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUNOsJbXPFG7H-EisUNfekXVutEgiYAJBSPaCxFK8kBaBxqpZMg01-aTh-gHG1Pf-1AgxR8oUvpa3mcqATqproUmUokMd0oMjRfZwuqTVo48oozkeBtQxChg2qfKygB-Q3BxjF5kYYTqcBsNFB5ZnlJg5e5a9nt7TfuCundlqyCn5o0R1qBO8W5N3NoyrZPev3libRQ1MIJ6j0gVztZvhcZVEJXSYyKJPsZJSL0EkumR6lufZ1z0FCxvvihP6aVBO1bCzdc8Ra9ODVjk7XGJ8BMAVWxjFnBIVbbs04UV_6AIRpWkP00HjGWHiAJl4js8QGrVOP6KSXRt33kXVccI1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLX1C8ljrMnTRMmGioQUkd9mpbZ61FY1XQifzdzEHpZcyOyuwDVWlsbu0hqZdxZotflSG5sr36SZsXL0RKxSRdYcDe0E94v6PIc8t4rTVXmIkgBcdqmnS4LeA_u3TkdwAJXTN3fF98WxUdXBJ4r-rDerRmOUTpaUcj7-hztn7IZ5FQNDktSJ0iyYleYLBBnBLWNVbqIE1L5x7MCbe3s1ZgNkJSgHeyyaHNpz_33lvHlqisQ-dwHdi0krhHQMXy7RYw4FTt5oYA1LmOvA8vRlxuGp7wrqKNOKn2kl6QcSdljFLe-ZCYlbAoNj2qLKK3JTOHJc9B2bXV6ZdtXJgsOEJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqdFlHv2uZB-J7MgoVBpyjZ2UHL6kwAlCkdFYl4EKmi0Nly2-QNzMGZJXpkOKLogwIqCfLK3GaK87oYsw4vhpgpdI_WHk9BB4KG2w01BivihXY55GOPSirxkrs39CLajUO81CcZYU3eSmKa40pi0ObaIgKZ79uYEj8xmdsBZNKXLr3r-B4ufjl71G_MHdaqnc3nowQMKyNE02h1ZvM5GjwYr3KdLzw09U4bfdVUuSarAhYORl9C1C0wHpBdyoRdYaxffFHo57Odzzr9oBeIpTYklUnruizHE8jYLzWtgVfH-SSgxzgMhcKxKJ74k7xr61aSMPwX5xcisFT1WEap0IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rkskz-j4x3cRiKbTbaJyCtRUeRPGIeCeNrQ1Obnz3JVvkXpUbNkI-T_R59PmwohAwW5eYJbiy1bEhhkfbZJwEZmIY0eHhUV1Fl2YD1dGh8C9BaFABG3iSziU8k1Yergh8d7oz-ugdwsMuEKdX0dfpEmeBi69Xns-aLDMcr8rbK215B91_aO7ZnmewjYbTWqdcgYtC5_fHgWrXyeJ04hA2GQOtrKWRfr3KV66MKqygqKiwXjlCaVQNAaO07lw_VlgR3vzlyEL2sH59Ypqr6HfC9VULLxSSmaTeHhIOASjallhQ-DGZ53QgqyPECJkptIKXYoJfHFWmcELkYbdwPT0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=HvOrVZ0kh3aD597E1neJ7tMjtnAa5GwpxORZpFBVAh1z4e60IsXLXNJqzJ-1ojlW-NX8d1IZHivXNryU-ios78rIlnE9RGbgi4lkvTVwohwETpe8FQXJB6mBx82eb5t5aHdM8oTvgwQFMN__GtZFvwhTftoW4Iv8OUKe1w9IZonCAPoXU8nD5bH7zT6ckMkIGayf3mGvO-R9E8ogK5pDTun_lVIrFZzqaIfPt2S2Vxc-9X7Pw9uGf8DFSeTuYYRWKTSQx1lf7u_9AzKUbap-vvI-c7Js0qjzc9nEeP9PsgJCrCx6QJkVOpgBGq2LKEYWftv-m0N92zZyjIDqHiMi4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=HvOrVZ0kh3aD597E1neJ7tMjtnAa5GwpxORZpFBVAh1z4e60IsXLXNJqzJ-1ojlW-NX8d1IZHivXNryU-ios78rIlnE9RGbgi4lkvTVwohwETpe8FQXJB6mBx82eb5t5aHdM8oTvgwQFMN__GtZFvwhTftoW4Iv8OUKe1w9IZonCAPoXU8nD5bH7zT6ckMkIGayf3mGvO-R9E8ogK5pDTun_lVIrFZzqaIfPt2S2Vxc-9X7Pw9uGf8DFSeTuYYRWKTSQx1lf7u_9AzKUbap-vvI-c7Js0qjzc9nEeP9PsgJCrCx6QJkVOpgBGq2LKEYWftv-m0N92zZyjIDqHiMi4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=vT1NgiN9x42yLefXLom9FpgtSUMOiRTPuaf1B80_Zu92Qko38bleoNBibstch29jhvS1gfDnvx8zitH5ZTv3jL9NeFNbL-wISnoHThcvCRmE9Hg0dNiCPpQ1GabaeS1fW6mZWYk7AZhAfA52tERWIcZOvTJmx79Urz1wcv2U5RxsZgfG-iFjQF7lXVgbYRizv34vrpivlxLCcLNNykeYJiLDDIMB1eTShBI9c7eVYwqS8jjTwYArwNe9vmSWLG_xnyJfRK8uTUixCkK93ntljamuRfI-sAX0NqEiogfCSt8z0AfnTcyYxrAJQFjUPhBd8BsuVj0MaUP2qMRVQOU2vA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=vT1NgiN9x42yLefXLom9FpgtSUMOiRTPuaf1B80_Zu92Qko38bleoNBibstch29jhvS1gfDnvx8zitH5ZTv3jL9NeFNbL-wISnoHThcvCRmE9Hg0dNiCPpQ1GabaeS1fW6mZWYk7AZhAfA52tERWIcZOvTJmx79Urz1wcv2U5RxsZgfG-iFjQF7lXVgbYRizv34vrpivlxLCcLNNykeYJiLDDIMB1eTShBI9c7eVYwqS8jjTwYArwNe9vmSWLG_xnyJfRK8uTUixCkK93ntljamuRfI-sAX0NqEiogfCSt8z0AfnTcyYxrAJQFjUPhBd8BsuVj0MaUP2qMRVQOU2vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n52tx1l46jMBb2kqpouEV-YKEXHwVbD-Ywopbk-Hf1guB5TT1DM9DnFZRLXWNdliDxnuYUbadlffvcpZvMxjMfQTeVOmW3b0BmHNe3cBSx0QnfgKFpTBrOS0NUk14Z86nAiVXO2gw1ElF9bfhPl3gH41dIqnp2dZJA70kE_NKhzuWIOoB4pHHh0Eq6GBGvqa3zH8o6dB_iMgnxRIHhGG5Jgn6XEC1XP47LqSpI6OhaRrZFgjAGhicYbRKRR7KVIbQqCbCdnm-j2cvhUgMyY_wO9fz6rUr0Xhd4yZsEJcP82yDFrCXwIL5YfnBBEtLrlhD2pgMsDR2ZK6dzOpiY5WEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaZCU2PM0fs9u5vnx7xfW0bBPIeXSi3L2sCReExhTAqF15hBXf_SvNxhO--SBaiIT6WUfQHEDvLD5BasiPINEXEouWkaGxYi-5nGkRdj7Kx6465fkP6WjBQz1yrDibT0e6DaDxW0EZ700zF-etWYi7qxQkTrxE-T8JR6Q34p2_lkujKTef8IYVl7yo4ynMcMtSx2rpeX9x9mO0FAC7HEI7_ZVPnuhH40yropf7JZ8i6mSfURsToRDFKJqh3_K1_YTELsNQaaw9sbWsAwzmn4QBOdVgjiA-ynN895f6-EY6VrJPd4MrvQ2j9Ynk3I6_KqpOpH3WbdgY4dwqREl257fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OubCY5GU7yQEJpjOY7oooY8uXa6m6i9LS2_HVEtmiUpmdqQiLmhiq-wMfaCJY80s7CHd04Srrojb25PmaBU1QveD0oLx7SiqHGy7g-BSGT9RY-lZGa5SUvkTvSGzkpxsq9kNM_dPRW3pesVEHmgw7cLXKxqe5OiQAmiJltmRU1Fbas_PXShDtJyJvmMWYBLNk8ZJ0qtWmsyCynflptU-hpcmYIjyQEQ6fcuLMIQrl8DXqUpGoHihOrdEqkyQOEyXZkso83NzpA2dwnUk3R550ZJWtN3NrkT7KrPmet2I8hO1IJZUUP6fjyT8mG888xFVrDksUPky40bvZ1I3JQ3oRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrZ4FQ9xCD6U5nNAzOufJhjRe3n-kJD3KXf2C4OwHDQqiJSBOyVUNTPz9Qcbykb_56tohF73ex3YuLB_qPgZXjmZq6JWj75KBN6D-ir-GHntssBhpT1MrL2_Ejj8ZBge1GDOv0wVs7-BuiQFVzuRioQ8kqHEbyGkShEW23EAIGlU7vOgS8I25yQNFJDSpgcrJEK0mocTaTVyMeNKzrVGoSUoze6FRlleVz-uk8OoGcIkSCPosBOiKZE-4DWHQFiOKbLimt6oSBgg6-tk5bqt4ZBhprHBXpYXW6j5kigoWNxCpSvwsmznpb6eP79c_lZegehgC57xI0VoZ3o7dp0I_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLIgdhGwjNmIDQxN-B3Hsaqfp0R_F7v6sQzGiapropNgD4RQBtrcjTeovPMpyJob-XKA8ktRkNqUAGinzycZl3Uu81TlSuz-AKotg7Mw9md5BSoqgi-ZyWpqczrnEzo-HMIizun1EcaDuBVNCBqcTdXPF4aM5HPqW5bQ_GrHEFDT2o4eIHJMlpue5_c4XZXrT33aioO3shDHDXlpEPQeCnTs8rosByifk1znDk_VHXtozEE_FpnPX7Q_8GniiVhqFPXpHLUQ5L0ZbZLXpaBqygK2STQ8Ja_qYwUIPfa3LZU-0-cSdhQS2xbDbVlVSOGkwobjdbU8yxw7KOkRWVf5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0S70r-SS7fkuIM9mOmm6udk3PIkwDGrX9ZgZFCYTk4o1CMOtC-Rntu4Voas3wvZFKpYVcriOjCXIQpCmMM4WjX-iRkqtfChTOZYTdVF4TcCvr-O-_HYo6O7lUOaKiYdu4YkKFoEJ--lJlGDWDLpLSfK-_6cV_xd2mpavdZcgCbpvsQyaS6MHGz7ixKI6N65ktooFhOR8eo0bYsc4Thx1k4oOv2HIgt2RLztKMN6UJe1OH2Z9HAUHTybxA-ff5oqLXxdaUh1_4ucVpCB9S8sJTqNpMjMC7byFPifKc7lcWIpR4KdsHNNCryBB56BSRBpk902-P0sgnXOeXa3i_i5wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=SRJxTLxH8o2isi1QQCKTjFRCTvdHAyuou-VyTgOUMTB1WElRe9N0zzI1zWQiHxUNr78MPBDQttDVHrco0ZOldbZNCxJ5Zq2lUig33iIrc4Umd1mXAIKWKC2H5yKeZ4k3PJhng6jKkEmeZvJCCQYFWUBKN8JZrBupA3P-fMaDWhGOejnFXsPYWzozvcUS4AtX-mltwvH7w41TKR0hyYfQ1cpaETot181WYuzwllRdf6Ry1qZSpYvLisPHjBMBwFCg0XOVTI27RqXZe6sglp_BsNwpAHRRlQZUl62by3YsvjXzrJn5b9Ejp0LG6D54rl2h7cgu_GP-P8m87GELfy0I0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=SRJxTLxH8o2isi1QQCKTjFRCTvdHAyuou-VyTgOUMTB1WElRe9N0zzI1zWQiHxUNr78MPBDQttDVHrco0ZOldbZNCxJ5Zq2lUig33iIrc4Umd1mXAIKWKC2H5yKeZ4k3PJhng6jKkEmeZvJCCQYFWUBKN8JZrBupA3P-fMaDWhGOejnFXsPYWzozvcUS4AtX-mltwvH7w41TKR0hyYfQ1cpaETot181WYuzwllRdf6Ry1qZSpYvLisPHjBMBwFCg0XOVTI27RqXZe6sglp_BsNwpAHRRlQZUl62by3YsvjXzrJn5b9Ejp0LG6D54rl2h7cgu_GP-P8m87GELfy0I0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhlx1Yjmr5cfnetRNgy1tRCsg4GtGudCGkyl6AeS0deOYp0HTMJIRTrUdPw7-1fMXIwi6WS7BzU8s6Wx_vJz9Ql0GezXARY41moR6xJTrA2H3iREtb71KH-T8OhUqiGAch7ZxowujNWcY-KhNQTznPDQAE5X_7Wtn54QCZI6esGLlMIW-7DWCECKEwcd0rqgd6SAAHI1nS8TBs45m5xosivLc855vkZf1TQ9HzPUUq3mZnVmrvHVnXHm9LxLEvWp-zRWAlm7YF_5znvgXy692qFvbh54Oh1LjIpIJxtcvmNRejF5H2yMps60P2J0rxYrL3xUSgu818vhTHAcq1_11A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgjhI3gpSekxTW68wFP4N-gaf2jfX1YcWVk8JaggoelgWiW9hrqaYEt7I1LHNOx2D9ALD7w0SAtKZ4DNg1GJFDj33BVsljEQhcHHiojyDkEEk5CuzPYOA7LW0VcU1Jn7gH1MUXDivqtGYlVaRtiRfL0qUqv8TTyXU48rZbMSk31W53AkeX8W9CNDZf0nxyqcN0Vdv8yEBLWr5CTPYlE69NsdNj3-OtnTU0TRSzHmcu49VXYHHvYx0r5gMvMOhF7VmhKxD0ylTaRaur_GWDCa_SkWU9SBVuE5tdDrrhD6qBIeYPcjGzmuAJi4mDHHdNYCxfSR_gE3dx8Dj7xHxQzfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4Q2_FHHSA83bGCB24o2Tb3y5_XbVl7enkBQUUpyaK4DzDDfjATtag4jdWDiKO4OmkBENLLv_hhZ4yrojEkYTDe3OqUvIwazon1OlAERyOnP7gpTiVon9VquG-EkSdjPvyedGwz-zjZ7sdEBITZcdS48dFTU26ymTXXtE2741caRRI3wjPN3NJ2YPpPb4y-tWI9eUoZwYnN249mbRQV6YQuoPK3r61gAMiUv2Yqnl9FEwxGDKrxanAXyJjPcvwQLg8RwXvGXL56J2rMkfSs17i2tYSb6WKsufMCVIMkfddjWhygBSfv_Je8V6Wgjtjt8TFRExiO-XK1-ojZ2Z9mIGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4LY6-_ZY05NpWGT2VIlQ_Xl9UGUzpBt04EkyWvHdrz_1OxL6iQqI8nhTVDBGGgB3bvqQhFnByKOMqsrRAYWLVFM0aJzayDC1H2YOS4ge3HQSwt8dSDxZDU7l0RQF_ly8X_3ZsL1KZiLn6ItiP4E0SdGlp-cNIUknNPcETZCmwqpskVfULuV6glJT4_JIDtvlVvzGkDJskI4-k_dX0Tj1Z_is-3Q_LmAB6iDjfu3ThbSPlO4y_9wqy7q2udL2WMFp-RsNXMAs07qQdJsnrtWWKabDF99E7S0gTWjS86U582w_okQ-eUjc6ntL66nprTRQ9FNOX45P8QFFGPC_g_OUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=LvXgFy0UVLPFRDKBSbZeIfNnVNvu-i8zZg11J6ig4bl5i6WL4f07h3Kt6mEWYX_rCRHwSo4F-W35vAYnp6-p5CoWbaEfcKneJ-XTVRlQWBVRvadow8-Um3qqcyuLyo7CLBzIwOagEtKLJSzEoH79axtTWvBUUtEo_SwURtAPaEoxy7t8kEYaG4nL_0BKfEANkgYo-3uDqSwdziKxv-PK_7j1-_yUQzSwSQLdDrHkY_xbS1ZxuSCdT6zSNmPEo4ET2GQfLwVAGRy-2rXj-0npARsYWj8MetCNygyex_a3ar55-1RJ5t26rEQqY7hBGQgeW5tt-cjJARd60U8xhsIhyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=LvXgFy0UVLPFRDKBSbZeIfNnVNvu-i8zZg11J6ig4bl5i6WL4f07h3Kt6mEWYX_rCRHwSo4F-W35vAYnp6-p5CoWbaEfcKneJ-XTVRlQWBVRvadow8-Um3qqcyuLyo7CLBzIwOagEtKLJSzEoH79axtTWvBUUtEo_SwURtAPaEoxy7t8kEYaG4nL_0BKfEANkgYo-3uDqSwdziKxv-PK_7j1-_yUQzSwSQLdDrHkY_xbS1ZxuSCdT6zSNmPEo4ET2GQfLwVAGRy-2rXj-0npARsYWj8MetCNygyex_a3ar55-1RJ5t26rEQqY7hBGQgeW5tt-cjJARd60U8xhsIhyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUe0HkyP9jn6UngUFPJt_E2eSai_BLv1g8nc4SpMGGtZ06p-fTsyKvWwtHq3Lk11wu6yL3BX3xoI0FJPPkRwzx9QdOzDRDzqkJ2Zm2g9NrOBtfYZGn7CXi-lKTIjrHRz02GdQYfwH4-MKDyxCDBQ6AQEzb6RhfHJDrtK5icGMlokdQ8_26VVk49LXynOMn7SIVrqKHHPjHE9bhChVSu0fy-M5WJiRGZXXVE1Bo_baBD5f2zPVrDOlhV0ETVmmmACjKl9gLEgzFTuYb4Lr5ldej1grd_-NkQ6uewEjjX9ILgPF65Qd-CuC58HlWrLgK0YNWNBV3Vmrvw20esqKk1q8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCi6knZghMMysciIBj25JykD3Ti88eJlW63-YTri-UJwKxC6WVV984sjcl0f_jMxBq9MrH3bnVi4NO3YrxLvd1ekCkiprPQmw4qeLU_hGESGCVVp5GTCH_isqyKSwzO-VnY_-B85e_znpOIlX7blHrc0xPSKh3CHGU0vZ3yH2rfLkLco6fCW3L5FRfR-OmzZ2TeJvMQoyyo9BlcJiZq2E19bVbPqYaX1-GOkYiuXLARuuD2xygt8qDeIwgZy14lyKJXpVgzCzgl1FHp79ZkxxXGtwAjjU8Py3E0EZyL8jt6uNleTJOkQEjdUEssLjxEG8m3I1cHGiHKRREZDzthANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0tshe2MF2dwUeNBDic_ucgsN_TeROlpo4DDbvEbcdXT9pjoDKJsDeFqEqw5c1-lXBwSBpM4wLo5LmvUBk09m6WgJZDXhqKUSf_mIofVVhywLM1-6sm37m_g6hYAkrOKp327hqQRkz6Se66utTVgzTpbLNtusbJKzx_vOSpx_0byqftcXQz2O2H3sCoRFuwxy18QBPMkNvPNW5-Atwe1MUWCWa2mcCAfFmrDmXu2le32o2hb08Ewb08-CZGpZUswRQmZR0iIwEnKmfRpQrUnlDwO06UqpHjWx4XHcyuqAOTJ8sT_J2CURpEcgpMM4-qXDEXKdUvl7UYYi3lpBGOrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jD-WNw-saFfPu579ERUMMCR5nd7PwnjQClcbeMH7j_nxy-Jy3MjgUnMRDCNON6u0EJrgKZmCN_iHw-vyXM9CPCXPJFTzuNGDkWYOD-okXlxYOulourACK1pVDYWCApGSPWtZorWSBb1NLkV0X4rz5fobleuMZpC8HudNgG_QIpJBHdNIO7VGD73CWNNhuYV-08AzJFWeZeDs6eTDyNAor3E6PsG4ln4MaBDjc8ohv0alzzLwQM1qUSFPydGQZvjA6QkIgpwyDGy50My5oErQhG8VdLIWmXG19MvCHoy-L467ooo3fkO6Z2fpDomGYQRRlJqBRZUvFiYA3zixjZCZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmI-3ZTlkcxRxlH4S_DOqZspmmkJJKjyU45kI92xepRlVL390txtZI7SoDKiP8P60WUKHjPmBMnpbuV0gBorXubzeBfxGyEOUGO3BJTfPdVZFyRl0VnrsjwjOmw-WO4JCynfs9tt9fqA2bG2FfUCbYrUwFiF2lm4FomGlIYfBxBgKgxWetwLVGfBg2u_XZoKz8PWFDwpvWFI9xwG60MjjRVzK523u---Jx8ePw7Ykxjr29h4fPGAfb0SFumM6ubcdP9gFCMnXX1I6fI_LxXpvo8OaJ1fUxcMrH-EW6P-lxgbrMjz-jTI56vanLnGq4UyyNx9TpdHI5Qnq6_Jlk2Uyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=R0KDL3K1hSpomf8pGu9ThYw8uH4w5VhhKA-jVtzZ95j-mKSaSPr-Uq8Dz953xzYlot9VvnN1P7bqOtTNTRgWu0tHMzXHhe-BoeryT_xWCYZWfpsS1JkxqFCBXA5yKmP75JWHzONiWD-39gkkp-k_uTRGYeJBqwJY_xLNHfL-CyCkKewQqBBWXvkuLZvUGg5aW6btyOrmvlyH1OvvO6Ec6k2mH7pZBy60zhm68exGnWzWf3e26_ufVIcY2LVv1QUjYsbzQ96pjrcJlIGgDC4XM4Zl7FLb4p4FcTpzJKpBQGSRMdntDp2m9xADixPA6aQC5KbKZvufiQlN1IhAm1f-Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=R0KDL3K1hSpomf8pGu9ThYw8uH4w5VhhKA-jVtzZ95j-mKSaSPr-Uq8Dz953xzYlot9VvnN1P7bqOtTNTRgWu0tHMzXHhe-BoeryT_xWCYZWfpsS1JkxqFCBXA5yKmP75JWHzONiWD-39gkkp-k_uTRGYeJBqwJY_xLNHfL-CyCkKewQqBBWXvkuLZvUGg5aW6btyOrmvlyH1OvvO6Ec6k2mH7pZBy60zhm68exGnWzWf3e26_ufVIcY2LVv1QUjYsbzQ96pjrcJlIGgDC4XM4Zl7FLb4p4FcTpzJKpBQGSRMdntDp2m9xADixPA6aQC5KbKZvufiQlN1IhAm1f-Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=NladRImnYRDj1lYmE_VyTPjn8p1TNWbkU13x-TLynLZQXUgBmVdbrqjo9h7sup28_A6LJForVI2wqoboesyxT-G85SY97XYuDNX1XTUsZo8Nm50AgzuFtWzUTX28CQH01RqmNl1wuW_A9qPaOPugDGm1lmCEK63-joJ5iFMNXnnhqgk0fCZZKiJwoX3yeHFhP_cvHASxMJz17GaoSakeRlXVRHtHF1ynGUgTWf5HNjxXStAivYWZUrNbnTI280w--WD31aDly7ANLxCsx_VKkazWK78xngJmEiso3a2XKnk2SuPntde-dfLm49UZ4NDVYYYq5YUXKKZYK2egctHkiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=NladRImnYRDj1lYmE_VyTPjn8p1TNWbkU13x-TLynLZQXUgBmVdbrqjo9h7sup28_A6LJForVI2wqoboesyxT-G85SY97XYuDNX1XTUsZo8Nm50AgzuFtWzUTX28CQH01RqmNl1wuW_A9qPaOPugDGm1lmCEK63-joJ5iFMNXnnhqgk0fCZZKiJwoX3yeHFhP_cvHASxMJz17GaoSakeRlXVRHtHF1ynGUgTWf5HNjxXStAivYWZUrNbnTI280w--WD31aDly7ANLxCsx_VKkazWK78xngJmEiso3a2XKnk2SuPntde-dfLm49UZ4NDVYYYq5YUXKKZYK2egctHkiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7kZtUwAVZIbdJxSs3iJlRfLs9-rMLkWPbPE6t55DDU-05IZ7U4THooxOHQQSLlQGZWtXQBAzocovec7ry-V3BQuX3D2IKLye0opzt6G5-MurcfaeHqnoA68RfBMMLv53zlqtwqCQiRD8zIDLbTa90tCebCbXDleTknQEOef5s4Xb4QV8gtloAmYyOlCcBLLF2Burdj1-C5F08S1httQ7xgJZXteK-oV7t_zJADhE43-Pdjct9_kBqNKwx_AJeA0IHq265--BSIiWWgomTOvzgY7-5kp1l305R0HkqW7E-DOVG0H9O-ZeiLqLNFnvk020Bt64Mqc84kzlMR6Lf906Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LG1T6HSYvLdM6mqDdZ_fOG8ovmd27U5ARxh5Vfcv7IJBXlKKeLE3usb4KtNVvj1Hw6iRPqXEIWWjowxTTB9I3xvBMnALYQ0I_uY_Q68eyWdcBTWgQbJK0zTIKZBua9pKbFm0mOPo0Iwn2Cr0bkknVSm6r76Lkw9rAHn_iFKalwOfCKTFkv0u6So7Xg-l8_riL5_CJqccMRx711cqNnCiYiwwL_QSQpBtdYbXJdHkhhBwr6qTl-XHYd2eYCLKIb1TEqj_LgDa1M06Bb2lSlmjgJadQU0JpCUupRAKidRHOwBoxu5rTTLHNSdlAXM-G4-HImOMJ39umz2AX-EdsdrCqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTTW2sTe6TRHmjmCIW0M-qJ6vqTt1BAE3nA6mYRO3myrAHNPbgrpKAZtO5x_oqYjkczyJ_pwDpepTyKE8fXG6_ZpSsTmhI227x91YFyqPGu4yrHf2nIGUD2CY-G5xrd8nkWZoqR2WRRS2VJbMFmHeeC3NiHUmVDM7zYoE__lhvreICSdgTdb_xnCW_2Ez5vb20K_PXSBG_Fw5TkBEeGvRP4SiH5VK1fn1Mwm_Bdlzp1mu0n0lhaDpchUI14OQcDMNA50Lz6AJG8UO9gzRbr2ucevpm98XU3BfEgXC48aIGNsSWN7WIYxl7oP3E4FvTeFVf8FcpfU0UQJSM1GGxk7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLEw6i3TOLF1qrz3WdCot1vFcq-6GMy16Zll8-1YYz_H7__hov8zvB4WR92HyXB1WoqvZJHzuL2xO-dwEZaDjx5yHec6zOAXZ2U8OCN9gqA5fcd_IVbwGBBlTlE7GG4xci9khYjYIroFBg_2hlgwK3zXrPUpvg6kc01DFLmQVccz07D3ZMVxF9QZYBVu2Mh__ixlA5DoQBqeoF0Z30J___gBCjJo0QBfPvK828wqnMWbjEQkAZISK9B-hPpOeiKFJicph7JboXc3WWU4M2Y9A5q_xecbcWrYfAwMfy6KwiA2spuI6juuvmBIOzqXZXnKVL0DQ4ayFqcS5-q-tRjftA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=iP6iT6QoX1xt7Qau-LUN9De7vsQ9fZ8O3ibmrhC7sQt3jGNrXVl0ovW9qR5n1Rpzp_SyowNg6sTYQ1HUVaDnDqvyLTw8hJ3963bEUexeGVZ3aO3A1n2Pn_U_bsTuh1xl9DNuPO-WFMSu6D35-tTgNb6Dlu7eQtgHFR8NZiIwClD-wj1UC1SlpmPHcWB2NvKhD6cRyjsa0-fd5ne9Ey3adpejyAliGAjSqZuRcXIkAGwajkeivhAewNnFSEX05INcp5Q0LoY8qnWmGHoo-bGXe_6gQ_uqrZJfIjAxDobue3VUTGAEVGOqiKEfBKP2rjh_kBRg4URxRHgvtHS3Bmo-CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=iP6iT6QoX1xt7Qau-LUN9De7vsQ9fZ8O3ibmrhC7sQt3jGNrXVl0ovW9qR5n1Rpzp_SyowNg6sTYQ1HUVaDnDqvyLTw8hJ3963bEUexeGVZ3aO3A1n2Pn_U_bsTuh1xl9DNuPO-WFMSu6D35-tTgNb6Dlu7eQtgHFR8NZiIwClD-wj1UC1SlpmPHcWB2NvKhD6cRyjsa0-fd5ne9Ey3adpejyAliGAjSqZuRcXIkAGwajkeivhAewNnFSEX05INcp5Q0LoY8qnWmGHoo-bGXe_6gQ_uqrZJfIjAxDobue3VUTGAEVGOqiKEfBKP2rjh_kBRg4URxRHgvtHS3Bmo-CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=DTZeGYBtUjQpOlhIG191lRsZ7v97ZcA6Jdej_mQcUJBuf78dkxvtZ0BJ8g-D8Cel_A4_dPHwilxS2rpxyymadhy_R_dNV9uUKkyvpVcPkyJQJTSU6UOGhqMfsfTFG9eu2KrU5Ln3zajYpHbB2_IU0pvQ-FX_Z5MVIytpzR2A9ipQpadtRw1hnnQkjxZt0BfMycq68kt7iSJcWx6nDHAEpDx52YwC0N5eovkl3eiecxv2cksjrs5V9Q62LZsKrlyawcx832Umv5vusIzIMZkVUN8RBimtSrs2A05VTdBlTsqmqRL9kHUGxPD8Mv0NwoVQUBzBrGcjTzKqL8i_yVswUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=DTZeGYBtUjQpOlhIG191lRsZ7v97ZcA6Jdej_mQcUJBuf78dkxvtZ0BJ8g-D8Cel_A4_dPHwilxS2rpxyymadhy_R_dNV9uUKkyvpVcPkyJQJTSU6UOGhqMfsfTFG9eu2KrU5Ln3zajYpHbB2_IU0pvQ-FX_Z5MVIytpzR2A9ipQpadtRw1hnnQkjxZt0BfMycq68kt7iSJcWx6nDHAEpDx52YwC0N5eovkl3eiecxv2cksjrs5V9Q62LZsKrlyawcx832Umv5vusIzIMZkVUN8RBimtSrs2A05VTdBlTsqmqRL9kHUGxPD8Mv0NwoVQUBzBrGcjTzKqL8i_yVswUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_9qJuyc11yJyqugP4aylysWMtLjVsqrMM4f4inz4_7Opl_iDRjT4xSkRNBPrJEJngCfsrqxnt_NnjGF2Ttx8OvkA58XSLRQPWoPmF-_KEyT6UujCs3ZxqYCz7sBF9wNh2G9DRhwmEXf3pypLjJ7-hZ8FaQ0OBN9YWV4WclXELa06MYFJVF1eT_PLiaio4i8N4Iv6fRx6eX_Uhy3Dxl7aExPU9XwuDzkau_Wjpf_KikbOPsiluUcKxH_n1rzrD4YxFAM2M1bIMfbUNOd5UYMVc11d5rvdTl3RC7ywZ_SdCfDkOXr8x-yrqhwQTq4nQdsOiyqrEEUdz0uLXDcFuxg0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbktXbccjnKtrs_vVhs3mfaVltPRzvm3gzMRKJFG628P71rDwbbMsmunvA7KAV3Y-AqCwuchZYb1Rnz9BY8SJm6N3MdNcfNv-ap-ZgjFRTc640F2VAHKSFIijtmtPBq_q4JlYHQUAmPbLDWP1ekgJu9glXU2tt4qCmaQVtQUr-f5UC8YKyNCPThYLsrUbR-eu59mZEgC07AwwTgveewMA2cP4hzdDxS4XwljieUHFJ-0YR0FbGbWwVQSO4-v_95R6ilIIAckmptdwPpoJVdnJoPApNrLs-sY9-w3mVFJ6cKCfvSqalLgj4SNq76cYF1PBmdtd0zWNZ5PuEcyJ7sY_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8GJrZO0VP15_U77KajI1PObzEwffm_nsP35ZKlysavWR3zCPwkVIxgwz_YvopwFZbeMdb51zNSVuKmtIn6dciBA5eY-yTWAeTQ4A1N0SXx6HPAMPWgKjKjxfBwJZA2eOCJuMxSXx4mlv_-b0Z0Zg0rGWsLmL8YU251LftcWkKAB5TpY7iiL3PUogplSaP3sTYrY74MqiKHL0d7D372ns7RSLKD90NAsjdmFsXBYEb2vzaWzZ1Nvb_z9BbTDW2aNLZ-a1HCRKkl2qY_hOMG19qRhucWKzQ2As3hpKpgpLRqOa2RPh4Olwj3zzatNgTQ7ZXgDoCoikzVt7K9jLlTqgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7G_hpzhxE7as_PNqjgglJsWWc43TF6gjCN4lEqA9LQRwAHo9BXW2R_QYLPtgznx24hKCGl3rmiXycddu50oJEJtty_rU59gW9-rtR4N5P5fp0B8t6J_FhVjFnYztX8KniiyMfdhQlzZR14cjz6dKEdHMpG5A2myP-WnBDUhmR27X-hzEa7059p7VNXmSsZ0jjnO9X7NRx7P_BEC0hcLq8IPWxJktWvKJwfEEALlABL1T_xDwk-oXkCID8DjuC6NyUV3ziST8jo4BaYRJRW84mhBO5hGrZeYHDI5JRS4WQaSOU1HO9DWJ9xLfUKVJC9G7mRp14UoOsproplLre6x6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=HoykBwYWnCnG4u0a0r9J8cTkeki_yEF0UTfVjmG18YSItSMHaot2YfKylHWSgv-CKpfxvVheCvbY9qFnqlwzn1PXsQRyWd4qDHy19nBpFoUvXb8v-FxeDFFqTpkJvpcHuIG7xDVo28kGIVZ2LKV6SsuHRm8TBjEwIgpL9svRSQQjw_uUqp9Y-wtBunSEImD9Ea4yHMg_XkOPVN7dZrjKVxw0xMnZa-gMk6ib2KiTQraU9ofFzNbep0xWXFeidVj7_v_CpNavXSs3CFYZtV5PfdxkiDrY16u3YtuT5VH3oYQVpeGFFQKnK1tJh4PWALzHG_S3vQprGuh5vTfYNj-3aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=HoykBwYWnCnG4u0a0r9J8cTkeki_yEF0UTfVjmG18YSItSMHaot2YfKylHWSgv-CKpfxvVheCvbY9qFnqlwzn1PXsQRyWd4qDHy19nBpFoUvXb8v-FxeDFFqTpkJvpcHuIG7xDVo28kGIVZ2LKV6SsuHRm8TBjEwIgpL9svRSQQjw_uUqp9Y-wtBunSEImD9Ea4yHMg_XkOPVN7dZrjKVxw0xMnZa-gMk6ib2KiTQraU9ofFzNbep0xWXFeidVj7_v_CpNavXSs3CFYZtV5PfdxkiDrY16u3YtuT5VH3oYQVpeGFFQKnK1tJh4PWALzHG_S3vQprGuh5vTfYNj-3aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFTZIApXRTEOMEKYYcd2dwKdobDyeMNmiyKxL4wBjoeWHg1FaOQUGWjy4jcxMvlbDR6Zu1TLlx6JlZFNXbzLw5J6vONEOgt75DuiIs2oWvWKbBZ0M7cMw8ebDNtn1kSxnr_FbTQd0bVqQj7iJHtopH8hFgxUWkrtbKoQbzDrpUcg0QH1T0Oyd4Uxa9FhiUm_inz6Uc1n94z8M6P8XLM-xy4LHN751ovuF0pj7MWOLsnB9WtvCelDOd9lZtp9p65WpdbAoNtCHa5rlZ3HF1NfefSUUGJU4sg-FvYCJAt7sU40M-oTRJAag1dsL3huSTmeLtYrKQEUONjNbaFpDd1lig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpJPQUFKOVNEaoqrZCEDD5pEazrUydDnstKI6EZZjedYTUztJfmQPbhQK3HmUp-OgjOo6sZgWYfy4CHzxZgBsmZMmvSXdPdZqaZvdVrC1GZuaU2LxWPRLulJNAjCjJSYATOxsd_ogyVv8pIz3G7nrR4WXDuiSWEK4Wr6yf_46wSfBH083NMRTv-RrdLFXYbgZ8GkcfFutxpPwZKzss-twDbU30Q2VB4xcvkXQQPCx-G205qugjvULMgCtxIlwSQ7MxOkWBq9nIQD-OBii8e6rtXyYBCMfYVRI7A_KwZm_hrjQsIhIJyKbX7plPmvwWTue-LhX8hreXDVImdlDCTWfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=pxsRtTEneVssgneV1pZibwyBbSFUyfGGdfpSqHRqkJhdJF1IM1p4uLbKOlOZCEp5O6TYK8QHjtL0V6A14sesxQG_A2uAZdaLxzfW8yzy9aVFbOllRjYGoxHKdeWDpI8C0t0cwd47sWUFjDvisXjUodaKca84sXbv1YWyyLoPmPj589zsFivn4lISXnhI0VDb-T7Hy1C1XSVdl29sJazGntKXMTwfIkUExZayY-PNfPgpz1z2FUw4ziJklCJq545STlyJrWgF8hAzHWeMdNtjc7oe8DTHkHZKsBC2Agi7cEA8SncDIub-j52naHPXaM4kLONBT-1dHz7I1OQEc9z4fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=pxsRtTEneVssgneV1pZibwyBbSFUyfGGdfpSqHRqkJhdJF1IM1p4uLbKOlOZCEp5O6TYK8QHjtL0V6A14sesxQG_A2uAZdaLxzfW8yzy9aVFbOllRjYGoxHKdeWDpI8C0t0cwd47sWUFjDvisXjUodaKca84sXbv1YWyyLoPmPj589zsFivn4lISXnhI0VDb-T7Hy1C1XSVdl29sJazGntKXMTwfIkUExZayY-PNfPgpz1z2FUw4ziJklCJq545STlyJrWgF8hAzHWeMdNtjc7oe8DTHkHZKsBC2Agi7cEA8SncDIub-j52naHPXaM4kLONBT-1dHz7I1OQEc9z4fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGWCYXX-9Jtcf5BXqtA-o7vA_QkLCc1wUzStADc77WqB6YGdERE4OZ8OBwvjJMR7wQzipdg5TbV4JX8dlfjc5i0ha_-mHGmULwBNEapJKWS5JRmihvoNGaFUit_ZMGo3LhI9RicSOS791Vh9horBkNIshapGl9pOrGZtbvOqXGsFRtFH8miczEgYjhnALzcwqBR7MWLztkyHN7PR8r8RtwRxsKMyBPWrYgKerkWx2A6rvedIxcXxU1VOJeglzPpFQY6-_RgF-ZEwt9msdv0LtD3jBlsvDLE6MjgdYirtv0gql1ryPvvDN5IBWbv-T3n7guRRnRTlgRoFdlgImPb9Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=aL5nW4Et3laBB34Z07JbydeZvOhuO2hS7wRghnPRuwHIozszrkHZzpXbY3xx4GGZJnCdaxnRMjX8_cJ7d5XZy3b_msqwcUY0R8YiQ-gUwe9kZNEQcFUWPYjPAf83aSOa_zaQAFf-bNwipKchGfxvL7cf4E7xFfw50PT00JV3aCS7XB52MKHxyJupcPvJL_rYA9EqE9nKnMur4iskE071Cp2ebvzLillFm5UTBkpeOmhBColAIn4RfESfD7Wu3nYeZgUWEIt51MzCF13pcL-_mm2qWRZLlFo93J_gRvrHYFr05jdx6sjR1az7HdUEWFRxKGvz49mqDIZI7D_lu_oKeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=aL5nW4Et3laBB34Z07JbydeZvOhuO2hS7wRghnPRuwHIozszrkHZzpXbY3xx4GGZJnCdaxnRMjX8_cJ7d5XZy3b_msqwcUY0R8YiQ-gUwe9kZNEQcFUWPYjPAf83aSOa_zaQAFf-bNwipKchGfxvL7cf4E7xFfw50PT00JV3aCS7XB52MKHxyJupcPvJL_rYA9EqE9nKnMur4iskE071Cp2ebvzLillFm5UTBkpeOmhBColAIn4RfESfD7Wu3nYeZgUWEIt51MzCF13pcL-_mm2qWRZLlFo93J_gRvrHYFr05jdx6sjR1az7HdUEWFRxKGvz49mqDIZI7D_lu_oKeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=GE-hUa6sU_93O7rcrMRlc8QrDSkMZ_5MVXzLkkDeBIB_vQZhgp0QE-eBMc4up0lb3zBrsUTJlQvwcbccX0OVj6UXCYw0_aWphNiB29H6LEGRNpxaqcxtn7LvaxGqN4Ap-dYrDvDHHhK_FRgaO7jRxrOhSuInILaeUSgHJqQk9hhAx6jF3IffYxrukkNmUchrp1wM2utWFEY1G24OL4v89dEP5h-dml7Mh-9L-ZimAR9fD_lO4SOwuV1veqw0ZmAlxBb09G7gwclWrQEijbBB8TreX9Z8xVYyjbyAfbdeyQ25jWKFP5TuUBIKx_Lk4vzxEb3KHV8v2oBGpgAc8u6FkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=GE-hUa6sU_93O7rcrMRlc8QrDSkMZ_5MVXzLkkDeBIB_vQZhgp0QE-eBMc4up0lb3zBrsUTJlQvwcbccX0OVj6UXCYw0_aWphNiB29H6LEGRNpxaqcxtn7LvaxGqN4Ap-dYrDvDHHhK_FRgaO7jRxrOhSuInILaeUSgHJqQk9hhAx6jF3IffYxrukkNmUchrp1wM2utWFEY1G24OL4v89dEP5h-dml7Mh-9L-ZimAR9fD_lO4SOwuV1veqw0ZmAlxBb09G7gwclWrQEijbBB8TreX9Z8xVYyjbyAfbdeyQ25jWKFP5TuUBIKx_Lk4vzxEb3KHV8v2oBGpgAc8u6FkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=iBAWf2NzGrfcsHajiFm9PpIzl4JXjNfuEaigcyDyoFOOk_mKZSSYwjdI5lbSQgFTpsFTu7aKarLHTQ4n-HQLAkLsuvjMnlc-E6fSAwXAEtLK3JEwCz26VJ0g7IqcDY2F58UG8BRuiBgYFrfIhz1dBZSkcM1cp2B7JY539L07QovOtaiW2wqHs5CTDQtOHa6ZVLJ4kzDHzGWiAGnOgjg5jXtDrHvbXaF2h8svGFsqEtpubZi859oQQjHfdv7FyNn3vAtZMNBNLwWGq_Jg5Sd8Uij_iST3QoZuTVpPs5MGNDERhT3hoskamZ-r-bfDWMo2CdYsoLXULx6XPt3YshZU_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=iBAWf2NzGrfcsHajiFm9PpIzl4JXjNfuEaigcyDyoFOOk_mKZSSYwjdI5lbSQgFTpsFTu7aKarLHTQ4n-HQLAkLsuvjMnlc-E6fSAwXAEtLK3JEwCz26VJ0g7IqcDY2F58UG8BRuiBgYFrfIhz1dBZSkcM1cp2B7JY539L07QovOtaiW2wqHs5CTDQtOHa6ZVLJ4kzDHzGWiAGnOgjg5jXtDrHvbXaF2h8svGFsqEtpubZi859oQQjHfdv7FyNn3vAtZMNBNLwWGq_Jg5Sd8Uij_iST3QoZuTVpPs5MGNDERhT3hoskamZ-r-bfDWMo2CdYsoLXULx6XPt3YshZU_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=GKwls_iGZ30syjJTZY9pXtnLG4eWVT7phQGyPbeOEW40SxesqERfp0dpgvjhNl01Ddj8dIxpITZWEcRJInHgM20G_uGt94-Q-5CBL34XKEzAbqwcQL-gebbghZ4tFl3yFtIhNxC5fVy19Ffdf_2VRQcVERprfeBID9uYSCpRm2iD_xcPsgOwBhoPKWOs5fMjYCdrvicja6qngpuiLDmMJiy1gMHh2Fadhpi5U_Io1VqCDHirxxMcyiRC3AGms6UluLT707iTXbYqg-OkKz1NIKPjoMi-ATUfU3LL218bQdSLzioAkX1ZmNGGN1b5TjtAuWSq_bRiXNv_rd13wsIS1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=GKwls_iGZ30syjJTZY9pXtnLG4eWVT7phQGyPbeOEW40SxesqERfp0dpgvjhNl01Ddj8dIxpITZWEcRJInHgM20G_uGt94-Q-5CBL34XKEzAbqwcQL-gebbghZ4tFl3yFtIhNxC5fVy19Ffdf_2VRQcVERprfeBID9uYSCpRm2iD_xcPsgOwBhoPKWOs5fMjYCdrvicja6qngpuiLDmMJiy1gMHh2Fadhpi5U_Io1VqCDHirxxMcyiRC3AGms6UluLT707iTXbYqg-OkKz1NIKPjoMi-ATUfU3LL218bQdSLzioAkX1ZmNGGN1b5TjtAuWSq_bRiXNv_rd13wsIS1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=UJrctWKR-TyJW_fIzgltkEfjKfCibTphO-omaJXt_F2HOhx88Z7EB6HHAxhOkPmO9pdvAhMsngvnfg3bpSbkVoEAqkqszmQT75my6pYV0n_FZOzuxiKMCabQRAmckaAwxwpXO_eiFnLFV0L52SFbGGI7c6c0y3Zac2Ezmb33gwzNvPfYtr2lzu7gsSwLZwlg23lrr9B2Kp-mt5Zwt1FplFaxhm6JRFT_LB0CNwkKPuRTYDiOiQQGmTHbXqE78CM7c0J23NVimTZzoov8RWe8N_nlIFf8OhsVmCOgddckR2Ew8LpZVEmSG7j9RtZNX05_2lfwnXxwVvxImz0vCtzeNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=UJrctWKR-TyJW_fIzgltkEfjKfCibTphO-omaJXt_F2HOhx88Z7EB6HHAxhOkPmO9pdvAhMsngvnfg3bpSbkVoEAqkqszmQT75my6pYV0n_FZOzuxiKMCabQRAmckaAwxwpXO_eiFnLFV0L52SFbGGI7c6c0y3Zac2Ezmb33gwzNvPfYtr2lzu7gsSwLZwlg23lrr9B2Kp-mt5Zwt1FplFaxhm6JRFT_LB0CNwkKPuRTYDiOiQQGmTHbXqE78CM7c0J23NVimTZzoov8RWe8N_nlIFf8OhsVmCOgddckR2Ew8LpZVEmSG7j9RtZNX05_2lfwnXxwVvxImz0vCtzeNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJtTaBOK56cKzl0dTEI037Cy6xfOw40hV4MCaOOMfPCX3W8QeLS0_aouqMPlSXuHpkdgCXN7tLqZpcH7cQTjmx6KXS-5prUxYykibDdUq-Yq-OWg1nJMWwf5GgYg_3hM1eYn8rpJ17K9odvR79LbgY7rEuXbwQnbFFaxoB0QfaJEM1rpHleFSqNAjh-jpTOnXk-sodILfqo409kiGNb7agbs3yGFx1cPuXXBUrxEFnnQHlKA-O_v4zikZ3IVxHBFXONMEol1cvlo3gbQhYtuyAAT17aLvcGKZDuwje-vCG8pAkCWAjrd53PTSWQn0sTxjmgwk2INDJPDGI6QVLFLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rC7COPsm-3uoCYgjRxoQWFK3jeZ75FX9W0Tqa6X6Kj7d7RSosXqbcMes7OSLft6XnEtKqqWWOtuZW96COL_qUKA63VWsPCqA9TlXA5R62WWDUUgeQdbMEZdegO2DV8YMwgv3ll_ecdkBlwlrUTNEcVUzMUXbKxVnywbwKDCI8d9N8pwfMOY1fkKurqxlk7ivCyGfpwXrjpDueV7nENrQShA5sKUS9tKu_UzIJhwnSB4hImjcCyhMCEuz52OH6yG9yXUGPJcSGA-52uGA1EEQ8P7RbgsYEzgp1lNiJ1-jv4BQC0fGfo6idT1nzdd8LUTDgTGLRbkMBJrx5Nlz4UdIkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BptJhXQtJHeJ0TkKV_NszRqrFaFwQ33GpxpPY9xWuuJfu0Tr44UaxozcfLqsNvKJAqkP4prKwDrvEdJw7TNYRjc1aHMEXRYaLFxGQ-abX6fnZpZh-GykIMCMwfzYHYR5pH7UKeXLcJGIzC05Bpj5nW8Dq9N4mZO4m_D0rYAmsXeqbVLU4J7UN9XkZe_sRXW8jdFts1e91KU0MMiEtt6WxQfBq3a_rfu9_sqLBWGhZqym4pHNG-6CaIwpU9Mm2tvj_Yqu3yzDSh0d4_VzvKg0H8feEGEFQ8vOKEh-EdKI9AG5rSgCHk-QwTE9BuGceRL2bP1uNlktGP_hmlzYHwmIUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xqj1zrQdtv3kjbBa4f6rhqgOedbdioTdYFWNiUmbhXUYdPdKQTXJ9Oe3i_eUlTYPzNCq0iKQXK7X7k0GDLmi-U1g-mUDLAqQwPnMpmGCjzPHm6dBRaLFDoJPZfstgHwoq_T07DpPRoek8vJVTVKgJDRgwLdvCqEu9_10f_95TGln1wlWNC-eek5_FyqSU5trlRQeNsNVrtCRlIdHrLaOX46IyfIqtn8risE787fk3AabowQrxS8F4kjHCiQ6eK1SnuzkwMbSrEk6EHPw_KB3YdeFHNHwZ50yz3u4WArfa8eQoUpH-ZbVScBga90TXTsY-CRwT_8yeRyn5pVFwh8mtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=NPSoju0d7HGB7kO3aFaUfFmsYqOYK4yf1BhpQGvkK-HTK5JEHxMKmSh0ELS67QHg0tV_Z1qMKhU168VjSsRcmdX63AFmKjA-DGesz36MxVctE0D_xlxFo1Sy2Ng8uTJllzNoqhy_rFbWZPYSAv9e71QdP8p8Kv6wQq3DyEe8jOkQsLT8hiOjZ7hW7ixujFLv4JmThiOVbq7FcgLE0Viae8eHaaN3DmH9gVtgJkfuhz0Ylc1NoXJU9QI5cgbXrdJFZgNZA4YpeRPID9ZAPgunB7UwsU1v0WbXD73blB9sfytWNUQD8kVPTZBwYNA_Ze634d8CzmfBleozN2Me_jsf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=NPSoju0d7HGB7kO3aFaUfFmsYqOYK4yf1BhpQGvkK-HTK5JEHxMKmSh0ELS67QHg0tV_Z1qMKhU168VjSsRcmdX63AFmKjA-DGesz36MxVctE0D_xlxFo1Sy2Ng8uTJllzNoqhy_rFbWZPYSAv9e71QdP8p8Kv6wQq3DyEe8jOkQsLT8hiOjZ7hW7ixujFLv4JmThiOVbq7FcgLE0Viae8eHaaN3DmH9gVtgJkfuhz0Ylc1NoXJU9QI5cgbXrdJFZgNZA4YpeRPID9ZAPgunB7UwsU1v0WbXD73blB9sfytWNUQD8kVPTZBwYNA_Ze634d8CzmfBleozN2Me_jsf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=IysbRL_GMXtlp_dYvHrsUzUFDi7zUJl8XHBtEqfU8M52NPFaSyK9CnU-53unsXZ4hJTzlPLZFHfas5mcRy4x-taVUR6HfR6TWZjHUPH5eJoJ_QfPxprdhnh-T-1ybSbv48Ty8JuXIS9pwnd_vOyjnXGwzieqLVA6E1ke6sX4QXoZR4kIxo-mnElIoZyOew7aGosANPRSSMrxyPNgh5uZk_3cjr4s90w7CXSp5PaPnCrtl-V4fVuIZ_VXK1O0WNYksVsM2Fn0mocK1XCL9MOhKj6aFL8k6Y6Ycn13mWGNwGmQQB8nceG6p6g9mUC_JA6fIS4fY5hECxAheMxfRdb3Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=IysbRL_GMXtlp_dYvHrsUzUFDi7zUJl8XHBtEqfU8M52NPFaSyK9CnU-53unsXZ4hJTzlPLZFHfas5mcRy4x-taVUR6HfR6TWZjHUPH5eJoJ_QfPxprdhnh-T-1ybSbv48Ty8JuXIS9pwnd_vOyjnXGwzieqLVA6E1ke6sX4QXoZR4kIxo-mnElIoZyOew7aGosANPRSSMrxyPNgh5uZk_3cjr4s90w7CXSp5PaPnCrtl-V4fVuIZ_VXK1O0WNYksVsM2Fn0mocK1XCL9MOhKj6aFL8k6Y6Ycn13mWGNwGmQQB8nceG6p6g9mUC_JA6fIS4fY5hECxAheMxfRdb3Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=XHpnMfpFhlUS9B2Gv4CCQKjvfzgAjJPgve9MHnl9XKZpa6IfS2o-EyOV8admzfflUQaY1dXOxWNt7_vUtEIYo10-68dykL3qtYoVAjtefEp91l4dK-kYLB5ZydmOm8TYww2N_2Xh4GMWs92SAP6Xwr08XagpzqE6P7GqF_QUL9FiIkXe67qw3EeVwJXUhNM0sJEcKKbcA4KqapZ5SwWsYXe9CbW_ZqqRWusBmH8ekkZxu4xrlGSZUaHcni2eKFAZAe4tsF4BLREJsFvWXUNKb2vJGEVxvtkdCa_0appl1P3h02-2AUahsV7aWcJ784PzmBWszDq7LY4xv1Y3Nxt89w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=XHpnMfpFhlUS9B2Gv4CCQKjvfzgAjJPgve9MHnl9XKZpa6IfS2o-EyOV8admzfflUQaY1dXOxWNt7_vUtEIYo10-68dykL3qtYoVAjtefEp91l4dK-kYLB5ZydmOm8TYww2N_2Xh4GMWs92SAP6Xwr08XagpzqE6P7GqF_QUL9FiIkXe67qw3EeVwJXUhNM0sJEcKKbcA4KqapZ5SwWsYXe9CbW_ZqqRWusBmH8ekkZxu4xrlGSZUaHcni2eKFAZAe4tsF4BLREJsFvWXUNKb2vJGEVxvtkdCa_0appl1P3h02-2AUahsV7aWcJ784PzmBWszDq7LY4xv1Y3Nxt89w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjrT5MP10XnxGqallNg3Ddzt320HzT7Lpn1Kq3VbqoK6FflYHzMxoBCR0n9smPDdiPAXxWudayhcCgoJNlBTV5qEFe9hmjrEXCIT7b4UM3M1JLVwzmD8x2UQmsMdKCa5XB_WQT9uCCAW2yg3NzfkI34mBiyxZSoC4VEnweh7b5NCNJ26GTPPDC4d76ISW2A0bn1cq7UFGj6iQhNzgc5fcShOhEELtOVmsK-rBs7kE18_uQps4p7PJDNZ2egj2bk6leeQiomjvYDFkp68tHCdlRAJOuPnvR7dUyiBbu26yjSL33bF6Dsgc0SfP5bp39x9IZ0u8mmfoPFDn3QwFvqLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=a9lxMNQCgnzdXWIZboNkMYf7yY8PcjdPN2kdi_vzXtDJc3rvcao1yKmHsAZpqLZAOY3i1R4oQii48dcf0FI68RYvpY7lUZiS6EaRLpwHgdI_DByP5XWvOyKe65oppDCUyIBc8iBzMEIqwbVJAB_v0Aj4rZ-HJ5bBe57hOiI4H-xL4Yn7OE7hw8JR2bu-iZ4DuViDgD4nO6BsCAD6NroP4jm9eQ4bS7LqRcgzOAy_0Mj0qSl6i7L9tXJaOai4iy6zTRNIZ-qmEviZ-y4femxX1J2fNVc6jurJNFd3eREA4lAOwJOR6srIv0PbErSyjKiBai3F5sWgkBNdl-e3rE5vHRKW7nQA5pIjvWe2W3zRT21lXqubTDH9ZvPjjlVHda5MCYFRB6ACkQaf7R2o8uLrpKmq7zuo8bzhsgezjGtc3KIQDYc_kNxaAv0CJtjccL_Q4zeg7z5sj7QcsoK3QjQ6T_VFFHYP7Ex-BqgTqROcXDkvncNpkA3hbjYwJqxZfnnGHEszipzgsVKqPJHDjS1PANTGUCfFzt-co1o-V9gjsF3UkQi2ZLnzBERhXj4IRPRaOeJHM_ttnQZzOwA53cXNCe4v15F_xF2CaEu9XTs8rgXQyYbYvw0Ni5NPTX3XIhxPRozWuM-H08Bq_B5kkj99yz2iM2Y6rW1khRR3E9-vWwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=a9lxMNQCgnzdXWIZboNkMYf7yY8PcjdPN2kdi_vzXtDJc3rvcao1yKmHsAZpqLZAOY3i1R4oQii48dcf0FI68RYvpY7lUZiS6EaRLpwHgdI_DByP5XWvOyKe65oppDCUyIBc8iBzMEIqwbVJAB_v0Aj4rZ-HJ5bBe57hOiI4H-xL4Yn7OE7hw8JR2bu-iZ4DuViDgD4nO6BsCAD6NroP4jm9eQ4bS7LqRcgzOAy_0Mj0qSl6i7L9tXJaOai4iy6zTRNIZ-qmEviZ-y4femxX1J2fNVc6jurJNFd3eREA4lAOwJOR6srIv0PbErSyjKiBai3F5sWgkBNdl-e3rE5vHRKW7nQA5pIjvWe2W3zRT21lXqubTDH9ZvPjjlVHda5MCYFRB6ACkQaf7R2o8uLrpKmq7zuo8bzhsgezjGtc3KIQDYc_kNxaAv0CJtjccL_Q4zeg7z5sj7QcsoK3QjQ6T_VFFHYP7Ex-BqgTqROcXDkvncNpkA3hbjYwJqxZfnnGHEszipzgsVKqPJHDjS1PANTGUCfFzt-co1o-V9gjsF3UkQi2ZLnzBERhXj4IRPRaOeJHM_ttnQZzOwA53cXNCe4v15F_xF2CaEu9XTs8rgXQyYbYvw0Ni5NPTX3XIhxPRozWuM-H08Bq_B5kkj99yz2iM2Y6rW1khRR3E9-vWwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXiAjXKvL1Bym1_8xlq_gVcb1T479SbpDjgI3QThWy5CVo3xzVY722RsrtTUB1je2zHygyJUzm0jiW-4K4pzq9pC7MZ42fHgcJaCwhuI-No1U2R-rU7Yf0KFo-TPszv1Z51q2gMWo_c80pMrYFZTOXasNhea9kT9809Yymaxctv8oM5i4KvYFmqMTBIphk76yATTlIRK60My4auGE-lVOQ2Bti2eIZl04RcUDiR3B3vaVlrb_9-lcxoDlpep4knCtsruRKiFyoUS_ebYS9ap6zovmEo6gPPXSp03nfRKrjMDPxJTtsCjNc_hPbV1rb5KiynQdyaOw1r7qMRYIM7bpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=iN7Ts9XiOE3NZ4warzYTqZeDW-4vsZbxWz7VBEEdjOf7rNq3bb_Ayfs4UtzJUVIde_FjvJyg3es3qRYwDpeyBnWmkVeNjZR2VxvB98LZZDHBYPZcDWZzHndZbrTNa9y9zOKIPg53rbNcNlE9MXWbt5vxrqEgJvn_uHsvxt987EW1NAjuitL6jqzF5PQsyk1iBxGmF_0hInKQw9h6KSrPbyMd-VgeVXW784MSbrzaMo3pj0qTIKkaNZ4fZaTsDuR7kGugovDeTTjI7lLP2kamGr-9Eux-_iceKhAIuCD8vLzJjk6xCOTkeNOYH2OOB9qIAhuZ6-_WxzhVzrDYK0i8Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=iN7Ts9XiOE3NZ4warzYTqZeDW-4vsZbxWz7VBEEdjOf7rNq3bb_Ayfs4UtzJUVIde_FjvJyg3es3qRYwDpeyBnWmkVeNjZR2VxvB98LZZDHBYPZcDWZzHndZbrTNa9y9zOKIPg53rbNcNlE9MXWbt5vxrqEgJvn_uHsvxt987EW1NAjuitL6jqzF5PQsyk1iBxGmF_0hInKQw9h6KSrPbyMd-VgeVXW784MSbrzaMo3pj0qTIKkaNZ4fZaTsDuR7kGugovDeTTjI7lLP2kamGr-9Eux-_iceKhAIuCD8vLzJjk6xCOTkeNOYH2OOB9qIAhuZ6-_WxzhVzrDYK0i8Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGtcq-MrZf3JbMaR9SknVjRL8JB0ItR4olnY-gbU76P_lyM6_1jbwQe2-FXtBJ-Q8ibtWPupAHs5aQ490s6qUbWEFMcenEHVhbQh4VHrkf7QiSF91qeVQ5b-hO9Hp-34J41hUztpGR1zJYkNwT8r2LmLWNQwi5_8n4HODoYo4gBrL9SzP0BAsMmL7ZlQE4ylCeuYDOncWTOx3H3fmIqTXqjlzzsRiAn8wwjF4JPDdvFJquYAlCrSQnNAbKySf0APkw_RBdo6Wla7iT5r3gwzopSlvxmA0QlZa-KxCvVAlpMui_Gpbkgu090toZ4Y1ZdHEgtTBV0McSRKR2wV9tENGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZnTVuCBpgyx7rYaSGRRheifrkQ-5layAKNss5lcD-NK7H490QtGOTTS69WuMMaNN-opNmyxGHrNnPUfHed20udqhrceaudzKCRUi6Wx1yGO4_U5k9PegBIzzii0mtqhY1cU5VjHCqXEperob4rx7RqTQAkCNZa_XfV7VnE-OYoq87a0PaM2JMkINO3USwGB1eEqwDFDjAtoyGIQbE_yuEmMWwP-eyT-J4UH5raAUC0izyGemCXCDCW0SoZMmjINIFbYl4Hld_ZzdoCDaIZIqTD44OPwarJrU_YXq1T0vcxmoPoDKf56wCdIMEBKhx6MjQ2Chrvaf7bxhvJz9XP0zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/md7pri8SXv96dktSZQh5hazbMYPiDpjnHi1M548LvDM56QKLylwG7HVhwaG10A8s3JGkxQ-IWO2_Le3RFa8v8gjHxZYbOGCkaFGWselbof_xOAoqZIq3sOfPSax1jRjD7fjj0SfO3qyF4PAylufCAG24D_XdwjzCJrCIvXMdT7KJe6Ae3aVZC3W6M2iyFwzKvOsHKEIbZkJBkd-zpC5XfasdYmyijoRSUKPnbRNZ5CyKZD6oHDPD28WhJKJbSaZsdyBfoXnj0rjd2TuH0A5rVvN2xs9IXUCQ4ArUjsP7XitB_xxu7z8NMuC6suktbf1uIyHpgyHY14W_oow_Y2BBGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNtFH0C79YrfkXJKX3WNKF_HtTzaGQEcwkfFBGY0h1EDuFG_ZTAB3tqDFxlmd4hpNeVPGKn_b_YW_414Z0eUeQfCpBE9EDAX6iZke0P6y3tC592qQvSTBOyt9dQYpCv2zzKVUFfRjG6yjnApXPVYGKMLS9HBFRDBj4Ouk2TAWQsIOM1grhbAaqoNvV_J4206lR7VVpBh8ZcKw3JLDtxFzovBWglTk3pH-Zdcu3bJ1xBeTFvIin66VwzE5O-FgGAhmSrU_L9X3HxTqGpJy7ol4mBwVjIpAWGbvC__7lObMbfMOG3rPMzK9Y6CLo73ZG2bv_9KA1HNodXvae1Y-h55VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPyku0ng3_ff2DBouJNIKzGFhwx47Fk8AF8yRQc9Z38oAgEVW71pDrRENPHkIhI0hBGhTG2GzujCAh9H9Lp0vVbp71xW3gsbaftoBDm66rIMk4dxg_XN8Ns6JuiZoAQ1bXffKqXasod2pvzw7FpzKIAQA6kHZ-fq5IYFftoDioKIOjswXRBp4EZqEQ3MAU4kVH_oogOYtxOoWlm-YCFn8UwMG8el9XEIOVGxPH2ioz-se7Hr-TzKfk2hTeQskzZ5UHah-1fYLYhPvvXb7e3bHdEVYqsxAHenkZxAO01sN0yaczts1DIAiNXJx0k-Szd6bAFyO1E3DyhDEi_43onBvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpSgAfqEWbWTpq8SJ3ECccfCzmgnTlF1tRCJQiHdhKFTLOaTexTTO942Xfl9bOATJCl6VDuJmtJE-YmWsvWyq9ptAPOhcPSc4zgTMwLm0OFJslXUO048ugeWkl9rYdVezmI5NZvxVmOY6GgjbBJSEV2cMRnFP6snwMDPJAaVBh919P7vak79a-3DHQm8sMjhhapNOse-Wh8eWr98Koa8BZQ613a0xaNWb2aGYaGKZh_aBV5cgkkAFXcZB3SlYaaqfSqFiTHD-kz_5drLDwsxIsDfhd5zZ37E09qcWXPNmpyDO1h4oSSmnT2nHajmtOqb1puy1Wdac9PPqEtG0vB-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gghbPgCPueCNd0C2dFuFiX9p7dCLfszwjpqv3cPlb5f8mYddfTrB4fc_Lh-fL7j0iLMukR6L3Z025iR_TTrBGtwxcGHNXdlCm7IJxJtqqQPO0H7Hip7o3Bxnb5GHRM4ab9Mcc1L6pfAve5JE0qaZM4z528xGEUeh2kKtM_3uLnX7O6Gthp-zQMTgeVFqWijdITHOGSHc-1ezOOKd79JNcYrnmOS-26IXRqAET8s_C19AEktEnnneBldZkaT1JTRjyo9NQrQeQisuk7nF2zGN7L69FZweK_1HuxGeIAu0XLWhLNikxkbmUie7e3KiVRdr9CnwFCUqLx7Bu_xzIhEdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=J-UNE-k32PDypSl4VjvuEojKd2AtsQ3dt1Jzh_zE2B1N8f3X3Mn9kvcEYY2q3KwkIUO1P3cnZ-MOi7EtfmpPZX1zlTvYjfIwQ6myyl3Jt_tflBkFiyXF2FZkLgu0QO1smbBD5AaQiLIyJcW3lemlhg7IeNG_k8UNmKc64P5fI6eHg9SmocSXpRtnDN8lMejPismlyAZ_qDl0s3iZQKgtO-2yXiDiSL8VnEYHLdf9nVDJI95ZPc_RihGYDoqHY_SGETn6L88vgLj0PVtw_e78FHzemMZ4J1giNkgMhQ7Jim4777LSWUGmUsCuSfeQFUIf9-cptGtZWAjf65RFvwy5aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=J-UNE-k32PDypSl4VjvuEojKd2AtsQ3dt1Jzh_zE2B1N8f3X3Mn9kvcEYY2q3KwkIUO1P3cnZ-MOi7EtfmpPZX1zlTvYjfIwQ6myyl3Jt_tflBkFiyXF2FZkLgu0QO1smbBD5AaQiLIyJcW3lemlhg7IeNG_k8UNmKc64P5fI6eHg9SmocSXpRtnDN8lMejPismlyAZ_qDl0s3iZQKgtO-2yXiDiSL8VnEYHLdf9nVDJI95ZPc_RihGYDoqHY_SGETn6L88vgLj0PVtw_e78FHzemMZ4J1giNkgMhQ7Jim4777LSWUGmUsCuSfeQFUIf9-cptGtZWAjf65RFvwy5aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnr3IrwyKPOJ6R77_atXWaeyVYr2-dQ2K3vlMujzNZqpmwH9OidywsMZs7guvLMoPESgjoOZPEsFSgwOYuKLRfOCHFcJPER-WY4Oh-YIkONAbJUgKDntJf6d-QxDtaSnVsE9-eLPJ0GCPiNi4xLGBDAV5NW8VKcm9gtgTcnIx4Eg1lcz_Mj6QmkyahWKLj6udwmPSzKdUFrIU4qC16WqSEufBQEHaDliEf7eZRtAXDgiltMH4RjeiTQnyTpQDgwLgBm-hTHyy1JiiCqBSvgaHjca_qgzgtXS3NHr6_RxBuqWmsCsBDkr6nVs3NjslvVovSdHri6hch5pNHPwiy_RgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAH8hyDY16Uu0J3r9PHtiyC7CCFgltvatNCzTrpy7hkwKej5kaOgJgJj8ef2s3dSa80oSqeV-tJ0n0hbskKzzeesAQJdQxPT2o85QtljJOe8BN4Ris4VID-P7BVIebKc4k29-s6rr7i7mWUHdHhtQxgoAxw5rspH0LeOoBz8N1TBle2NUWFRRUAsRHuIpYAol55XgSlVBIn2jRmiZXll-E6vC-kiltoTeb_QsxomX9fp7l4rFjdQk83Lf41ndnQ3ypyTdaYaBIAuob0YAI06PBGbneddCDWzRhIOKDoNVj3pkKzAN3mljF-0RJlp1F-WWm2rszOeGSNVeSb8Pry80w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4987" target="_blank">📅 10:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=pSnq6UUf3nO-xzbOvv99NOVhWQL402y0hFkpyonEw3tgE7x7eEh2-5LGrAK3Z12sh39VnVwiZlpZH26y8w69-obGI-rOEgNMuHwvwWPdzO4FjCJcV3cwHeyrY3jVndetZA4z7Tx5u9hOGCllO6Fn7W9f5EeX0cvmM1ks2KQLD_30Do5o0w1UgnqXivLZKGc4DCtOvO_7knvSq_Y00pus52qn_7nQxiAx0B0d_OMOSi4pdunHGE3cdq0MXOiQaBsH_h9b5Z_0NUeAtIOPiYZOin3gcldv89EUSmTuIgBK6ssjRCOVD92oXEhn8zY_J5UVK0MvRrB4Ln8W0WlsoV3ajg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=pSnq6UUf3nO-xzbOvv99NOVhWQL402y0hFkpyonEw3tgE7x7eEh2-5LGrAK3Z12sh39VnVwiZlpZH26y8w69-obGI-rOEgNMuHwvwWPdzO4FjCJcV3cwHeyrY3jVndetZA4z7Tx5u9hOGCllO6Fn7W9f5EeX0cvmM1ks2KQLD_30Do5o0w1UgnqXivLZKGc4DCtOvO_7knvSq_Y00pus52qn_7nQxiAx0B0d_OMOSi4pdunHGE3cdq0MXOiQaBsH_h9b5Z_0NUeAtIOPiYZOin3gcldv89EUSmTuIgBK6ssjRCOVD92oXEhn8zY_J5UVK0MvRrB4Ln8W0WlsoV3ajg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین یکتا، همون چهره‌ای است که قبل از شروع کشتار ۱۸ دیماه اومد تلویزیون و گفت خون هر کس ریخته بشه پای خودشه و بعدا گلایه نکنید!…
این همونیه که اومد حامیان رژیم رو دعوت کرد که هر شب برید توی خیابون‌ها
حالا هم در کنار تیم ملی فوتبال، در یک اجتماعی اینگونه رسوا، داره مجری‌گری میکنه و میدان ‌داری.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4986" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمملکته</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=Pyg9gOw5FgQYT8Gk6K7acUwHVe7iJoATzLGLaAOaGXI68MgbwCer-ZMY4w5LRfKEdssSvnRkWaRDbfEY8eSQgOol6HlmSjzYoJ1id2b4bANvDsT4Je_tw6E19TsEisy0rGhRZxldOdlKwJWGHXhQ5MglnTxe1HCZC3s0tRH8jQNCTyBreN7Nnr8zKpW047WlHvM7GeJmh3sprEAJRNrEg1piM7JVqWjXlmsCbAKeSn92Jpj8ykwAkHS-e6ePnh381rVJsxj_OoDS2pC7-76ORYEqEdqZdOqu35W3q4e17s4EGyugxn1dyYsyOxXkdEPj-u8ly7yInL3IX7Zr6Zng7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=Pyg9gOw5FgQYT8Gk6K7acUwHVe7iJoATzLGLaAOaGXI68MgbwCer-ZMY4w5LRfKEdssSvnRkWaRDbfEY8eSQgOol6HlmSjzYoJ1id2b4bANvDsT4Je_tw6E19TsEisy0rGhRZxldOdlKwJWGHXhQ5MglnTxe1HCZC3s0tRH8jQNCTyBreN7Nnr8zKpW047WlHvM7GeJmh3sprEAJRNrEg1piM7JVqWjXlmsCbAKeSn92Jpj8ykwAkHS-e6ePnh381rVJsxj_OoDS2pC7-76ORYEqEdqZdOqu35W3q4e17s4EGyugxn1dyYsyOxXkdEPj-u8ly7yInL3IX7Zr6Zng7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/effFKRIhgRPC1XSb_KzWjjqqSF8fs2HNYTcE59ZP-T1E0UXHI4bxG4mmjfMzmsd1LqZ53Z8t5F4cUAblDivpQJokQMVDemACKx4Loa-hosrsU2gL_yLLv1Dd2LMmGZC2Yj4gRr8TItWvlP96ZVdPQIvt6ydhtTF4GkblYYlnUV-1uyDVVWZUWU4RvGxXEf4k7FkeXfe0VSCVSffWTCwg0epE6qaCkXtLkZPz2ImJICKX1XD8k-9Bfibs4pE0FdEPaJCWxMVUKt3BBRpvkhVRhGg-IX2a6N7jHrkoSC02VzZcZrIxo2uuyw-vKOwJgQrD6dzZ45jc2o9XVtGZzWkeYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=e544bICKOI_SxTPDkJPdU_WPEEVDg9c1Z_TNQD4EhSlLfSTxduJocPurNzjYyZHJRGHIuC24SnOH5xpsIqa1Yr3DwD908BDNQQhJRtcFZMoLo_oATd1qjG7VeA-VpGbo-f0VcoHbMOOwceIZBnF3cTsA64X44yW5qR4Ly2udxMm4FG8bYFmjU7dQws6JPdVhlpMo_dpzj9DZI7a_ywbteo3H6QHrEaQ5RCJPJa-vfOTddZaO-8uGL4uwT33IsGbOBCXUV1fJS59tgSxbWQ1Mfn-5coaNkHIF3Ybo-HJlnPUMWIFuZ-nruo8W5AoF-zXywAm_hGYGhT9kE81G5gcVoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=e544bICKOI_SxTPDkJPdU_WPEEVDg9c1Z_TNQD4EhSlLfSTxduJocPurNzjYyZHJRGHIuC24SnOH5xpsIqa1Yr3DwD908BDNQQhJRtcFZMoLo_oATd1qjG7VeA-VpGbo-f0VcoHbMOOwceIZBnF3cTsA64X44yW5qR4Ly2udxMm4FG8bYFmjU7dQws6JPdVhlpMo_dpzj9DZI7a_ywbteo3H6QHrEaQ5RCJPJa-vfOTddZaO-8uGL4uwT33IsGbOBCXUV1fJS59tgSxbWQ1Mfn-5coaNkHIF3Ybo-HJlnPUMWIFuZ-nruo8W5AoF-zXywAm_hGYGhT9kE81G5gcVoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/4983" target="_blank">📅 09:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏ترامپ: امشب، به دستور من، نیروهای شجاع آمریکایی و نیروهای مسلح نیجریه، مأموریتی بسیار پیچیده و با برنامه‌ریزی دقیق را برای از بین بردن فعال‌ترین تروریست جهان از میدان نبرد، بی‌نقص اجرا کردند.
ابو بلال المینوکی، نفر دوم فرماندهی داعش در سطح جهانی، فکر می‌کرد که می‌تواند در آفریقا پنهان شود،
اما نمی‌دانست که ما منابعی داریم که ما را در جریان کارهای او قرار می‌دهند. او دیگر مردم آفریقا را ترور نخواهد کرد یا به برنامه‌ریزی عملیات برای هدف قرار دادن آمریکایی‌ها کمک نخواهد کرد. با حذف او، عملیات جهانی داعش به میزان زیادی کاهش یافته است.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4982" target="_blank">📅 09:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=RcxDNx3SREraS9UbU7Elw-yvvn652l6nWMYnr6XzDr3NlzLY7iUHy2YTd5qLYPpTkxn1RoheYxCT6Urtudh2aImIH_WJ0sBsPBjlR-6YEhDOx2svYsptLveWweEXzAM722gLWOT-klg709WE_EyGxLowYn5ZyHBEgV73J6rqv2xThlMY7cW2-RzIhxHWNDeRp82J2ztioeXXbPl5yUjDFjgyuVfGd7rfWXq2A7g5Ht4yWqAnTuxa29_dG4JRTm24BE5wFaMvVe0EuJ9v8affXsS50ajhja1fN59u6rbI8XdgNCjBbCY7SmdCXg50RjES-wxe4L3wTlAEMd1IfR4QZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=RcxDNx3SREraS9UbU7Elw-yvvn652l6nWMYnr6XzDr3NlzLY7iUHy2YTd5qLYPpTkxn1RoheYxCT6Urtudh2aImIH_WJ0sBsPBjlR-6YEhDOx2svYsptLveWweEXzAM722gLWOT-klg709WE_EyGxLowYn5ZyHBEgV73J6rqv2xThlMY7cW2-RzIhxHWNDeRp82J2ztioeXXbPl5yUjDFjgyuVfGd7rfWXq2A7g5Ht4yWqAnTuxa29_dG4JRTm24BE5wFaMvVe0EuJ9v8affXsS50ajhja1fN59u6rbI8XdgNCjBbCY7SmdCXg50RjES-wxe4L3wTlAEMd1IfR4QZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlKD0xgXtyRo63w3YJNZ3eIyMxNGzYnBvcnjbfbelMZPXQVGsMgS2d4UqubbcClF8Pz8WR-RoGfH5-HtlO6MvrlgfxMS9lZXegBcajIm1iWLPfEHSHrNH070AvgTDlcrJ65N5i-U-xRoITAXJVr4Ta1-1WS0FRjoBzBWOxiC8ZjRYrog6-l9Y4gl8I2BST5OnQ01uSYnNSl2Wksji9bHpoME0pNZOwICfhOV8YSrl3FoRLvRg6CJTvSqEKhCW8P1u-9RO6cfToDYXdSYOfSbka_4UEHiUSHNXLox9b-d8sN_ir2iNxZS50ihCkh14jmFtryr5PLRwAyAIVm-i_yxKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفت‌وگو با فاکس‌نیوز با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او 'گفت: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا گفت شی جین‌پینگ، رییس‌جمهوری چین، برای کمک به حل بحران ایران و بازگشایی تنگه هرمز اعلام آمادگی کرده، اما تاکید کرد واشینگتن «به کمک نیاز ندارد.»
ترامپ گفت چین «۴۰ درصد نفت خود» را از منطقه تنگه هرمز دریافت می‌کند و افزود: «اگر او بخواهد کمک کند، عالی است. اما ما به کمک نیاز نداریم. مشکل کمک این است که وقتی کسی به شما کمک می‌کند، همیشه در مقابل چیزی می‌خواهد.»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4980" target="_blank">📅 08:36 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
