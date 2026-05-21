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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 01:43:23</div>
<hr>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E29o9no41s3aKqD4rRe8-p4Zx6P2ShOKUtbjeh5T-pglQhneK1X3UF02vfLJnpOi1ZmrrOB6I2f5BWyZ3qIw15taIA03kmdXlqsyhq48-XIIf6zq6JgxTAuhFf4XV7wqgI_sSN81S9zGkzx0vMLh6BB0YjH8BKoGzmGB13JuVyHe6HjxVjjeLUSwwTt_Jpp8EX63Ij1cslG5Zeu_ISGmZomr9h8EpEfVEjXnUTYPYtNmkeCuQHKowjs_T3SGmFjwZYIujXvMwCC4y0e7qxnb5DLf09AgH8IkYajwllVTZV-77OX4TM-5gqh_swtmhim7t41z33-b2gToIFrLWVkaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OC4GxLukLytdnRYhqriDygh2eZGGTnBOvkUD-YcvFLI9RcsQ6SZ56rCI-JUKBoCZ5U0liPXmeCLVY9N6lQgL9gN1kgOdYfI0XtLwMHkN-oO6BqoaUuR1mp_wIhTgvbEsnc4__-19_mrPMqzWYVA1lEevbYznq4j2BXHMi4C8Bu9uMnORuZ9R81gBB54sONhSQh8wbfFITVP8NDSGRkZIumzV9SvQZ8PKdoSHacPBpbF9cm64zXDbLNkDuKrLkxAt4fFquhSec-ZRHPbDwX4dPfzptyvR8Ros0sHRvW27xWud1QRcduoDCfXaa8fl4uIY4uLpLOGOTo8B8ks0nF5geQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COa_DSpBnwP3Oes85QVPsMo3KtRfciq14s2uMiU5ZsUF8j_9Q8U6zSuT7rbu9krRrx1K2kR0kf6i_kT_xskdHduQ_6a5U6f_W9JytZxe6WnT57AC8oxpwGYcO2IDp4CRYgHvav46bavNn326zHjZv8TnsCwLLzQRQgJMEPUSq9SpnHByWSfVUybrcDj-h6IdXLVZ1ftYwpJk4_8CmFtwiRzAeEZKAXubMVcUJZRbdZwItR4g--KPKObZS9a_659uXb3cgWI6D73KHB2Xl9hUUuDVtF307I-s5ptYJlgm50ddqCEsI7kx5AzsFAky-WTro7IYDNK4X62YWNrVNnm_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3NsPUbdrLJqzw0v9b5gQPrAEVXTCYX2WARHi6xepxBx7vOlxbOT4tgKfoBIaCcZfP6roIipr1Uj8VhDubXyAE6BNJ6WXciqnRdWIxgQnaXEiyPzA9wVqTCHP1tnHASs391r8ON-CYsptq90G4oRNBDq65IvHkkQq5iB8WqvI3uOZ4sYZQ9kSp69IEhjZnmEmmtEGLDVQM-cby8JU_egCe4BMQnWOu8Dore4PoUifNF1mnvA_AK36nSOZhTHq2Dh4uzUj6PODsETdw1tGUQFg3pBn9pVF_PkQd9l4lZjYyPkGtMSnXu7OSnwi_12F9wI2BKALRwZoN0rTCvsxiBZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8fuiwl9SurRB_3zT4JZT56EJvvFoFy3q9ChJf1Pu__vtXqs05Esp1HZxrWkuT1j2wZZJfGsoo6YoBeFdBINpAZbyfhY3q7ZxeMzs3JYRDtgQ8mXewdgUDSVgGvxKqCkQ4u4Na1B9xArpK63m0BswcwavfMLyh4AFdQQ24LUL6Jjcf9TMJ-Wz51tSTztXUfHsFiY1-Y2DEsNxU4SZetF9D6nX4gWLes_fVclwDfCyMUoZce-DY6nYsX6rZF1Tb-p-vQ3iaCqeAEiNgjIaw7raprW4fce_bzDp499DTJREtJzPKXooBrjrYvaee2B-eci79ZJ_8LQQ_ZcJmFXajLHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S6e80wzT9j9TOTj_9CSMgFXs3zL-KqGB-0SU29efo2HDop4HRm3QsDRlOFzK3my0B-Od6BLOo1dgU4Ch4VE_Li9ksYAQRDa8734iLCTw3LM5xu23w6WvgROpQC8RGSO2BKKVXGCyosisphONyhYzwfU-YTChfBQFhHsHCmv6B_M3uwVsEWzF2plL4fb3JYqfd6pOkYnBZr9lpG8oTjnVjK5KL6rpcNCs9kAzE_h5YqMAIMlO-PVPhavnEhCBZCnVNkX7Xik2TS3Hn2kIhavRKnsWzNkqa78Auc2CECRao1nATnK-CCr0gtCVt-XXmIt-euvrm8M7WJTZ76e9MBn5UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F1iwg92upy5UfaJRVxU6qfOzIRtdnYdX-ZnbHhd0m8TFTweKak0wbqNi7EP9mQj6iXINA01pItR7jkXZXl3afaPrEmfk9-m_8dK7CzyMWz6Fg3H6o2g_PKdgCdYnFjraoJr3LuOyvH-cKCuPdaC0z0vBgkKfRC_MbjM-B1nNjzehkHjhXmei4U7jgOG82oqzjJKfPtYAo6kFqe7nWlKM4tY1ma9f8zLS82KxT6WM1V3ln_R-1DsyJ15o-YgTjbSWfaUbo57TV__7CcdDKXtLMtQnV-wj2UqXJ9g_r9ACUymg-W7p274nppjHswIGArTJ9r_-HkLfJOaplNaL7KbbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUNOsJbXPFG7H-EisUNfekXVutEgiYAJBSPaCxFK8kBaBxqpZMg01-aTh-gHG1Pf-1AgxR8oUvpa3mcqATqproUmUokMd0oMjRfZwuqTVo48oozkeBtQxChg2qfKygB-Q3BxjF5kYYTqcBsNFB5ZnlJg5e5a9nt7TfuCundlqyCn5o0R1qBO8W5N3NoyrZPev3libRQ1MIJ6j0gVztZvhcZVEJXSYyKJPsZJSL0EkumR6lufZ1z0FCxvvihP6aVBO1bCzdc8Ra9ODVjk7XGJ8BMAVWxjFnBIVbbs04UV_6AIRpWkP00HjGWHiAJl4js8QGrVOP6KSXRt33kXVccI1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLX1C8ljrMnTRMmGioQUkd9mpbZ61FY1XQifzdzEHpZcyOyuwDVWlsbu0hqZdxZotflSG5sr36SZsXL0RKxSRdYcDe0E94v6PIc8t4rTVXmIkgBcdqmnS4LeA_u3TkdwAJXTN3fF98WxUdXBJ4r-rDerRmOUTpaUcj7-hztn7IZ5FQNDktSJ0iyYleYLBBnBLWNVbqIE1L5x7MCbe3s1ZgNkJSgHeyyaHNpz_33lvHlqisQ-dwHdi0krhHQMXy7RYw4FTt5oYA1LmOvA8vRlxuGp7wrqKNOKn2kl6QcSdljFLe-ZCYlbAoNj2qLKK3JTOHJc9B2bXV6ZdtXJgsOEJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqdFlHv2uZB-J7MgoVBpyjZ2UHL6kwAlCkdFYl4EKmi0Nly2-QNzMGZJXpkOKLogwIqCfLK3GaK87oYsw4vhpgpdI_WHk9BB4KG2w01BivihXY55GOPSirxkrs39CLajUO81CcZYU3eSmKa40pi0ObaIgKZ79uYEj8xmdsBZNKXLr3r-B4ufjl71G_MHdaqnc3nowQMKyNE02h1ZvM5GjwYr3KdLzw09U4bfdVUuSarAhYORl9C1C0wHpBdyoRdYaxffFHo57Odzzr9oBeIpTYklUnruizHE8jYLzWtgVfH-SSgxzgMhcKxKJ74k7xr61aSMPwX5xcisFT1WEap0IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urh-aH7X0qDLo_wPPHCRU2TlvQsGPDfz6YoEuBL1VmDz7_RWp1istOt4v8Oen0deBUFBawHJJNouRVPjlV1AOfJC7ht320KiwI51s7tz1vmXn8tGrR2zJG5tnO0lK8tcKhnmVf17mimrfL-BjogmoR7-qqL_QSod7J8PVfNo5C0vtuxG21QZ_xWGymPn7mTVDRFa0shFxv7p5WIa-OGkgtZDSnquU_sdiKQu0oS1qLMVEJ60Rn7SkevVzE91qHhmYdO7hM_tIV6x6hLxgL8-D7IxtwY6-2ONuEiJd-jOpwS96W6n-0aYe5igyd9QGMD66H5Rxq05rD8zSHB9gVzWlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=HvOrVZ0kh3aD597E1neJ7tMjtnAa5GwpxORZpFBVAh1z4e60IsXLXNJqzJ-1ojlW-NX8d1IZHivXNryU-ios78rIlnE9RGbgi4lkvTVwohwETpe8FQXJB6mBx82eb5t5aHdM8oTvgwQFMN__GtZFvwhTftoW4Iv8OUKe1w9IZonCAPoXU8nD5bH7zT6ckMkIGayf3mGvO-R9E8ogK5pDTun_lVIrFZzqaIfPt2S2Vxc-9X7Pw9uGf8DFSeTuYYRWKTSQx1lf7u_9AzKUbap-vvI-c7Js0qjzc9nEeP9PsgJCrCx6QJkVOpgBGq2LKEYWftv-m0N92zZyjIDqHiMi4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=HvOrVZ0kh3aD597E1neJ7tMjtnAa5GwpxORZpFBVAh1z4e60IsXLXNJqzJ-1ojlW-NX8d1IZHivXNryU-ios78rIlnE9RGbgi4lkvTVwohwETpe8FQXJB6mBx82eb5t5aHdM8oTvgwQFMN__GtZFvwhTftoW4Iv8OUKe1w9IZonCAPoXU8nD5bH7zT6ckMkIGayf3mGvO-R9E8ogK5pDTun_lVIrFZzqaIfPt2S2Vxc-9X7Pw9uGf8DFSeTuYYRWKTSQx1lf7u_9AzKUbap-vvI-c7Js0qjzc9nEeP9PsgJCrCx6QJkVOpgBGq2LKEYWftv-m0N92zZyjIDqHiMi4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0CuHFwYpqzNk9KzMBfVvVm31NkGStnMqMKRp9usgue42IZD086gE_hb3NkmqeyvH3CIcmUS-t65r9ueOP2J44ekRG2s5AyoGrIy5aY5jI3pFwkGE2GxuGqxONrwc9G0RvtOFBN15fmyiRW9uSoSZvAcIPDcHDtbtqgiomRgew-tez1JJS8V2hjbP_f_ZOO3im_LTcvM7FZ9VHhpPhxcN6yv_fIRQSOxDs2Mwoh6bqOiPStzkBVz2d3oTIT2_-3gO1jAaNDN6_rMk9Gomj1vIXa1o9SQsVTk9_JVYVEZduuWdr26xsnLN9j91yJ1Mb_4klDnqqV38j0S4feoshzJJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRI305oqTefUXpnpeNxPfz4WUwQio_p7fZel50RYUpj3qmX_ko5qBXBb0eNNI1c85ihLv4fUhMBp3vkn6p1d-joYfsY7zGjWwtTa04yOwllZkNwnT9hDrJV1FTqGe6B1CEMPMSetZzFkePhS_iIvi8xUHpXC28z2o3I0qdpYPEzF6_gdGgRqQCl0eSZCbwtTZoViHN3l2kXYEhfvYH_WFNjS9AIuO6oWbAVRse2o-9xBKXpderRWVh-Cwz-ofHdXTSkprOHw2eqYcWTxTbWrGGNdTAX66wBhd7WlYywPRB-m88cCFxyoKJPteWcm7mi8cOSQ2MpscQMz5QST-TUbeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrRqoWOxn9LSTnN6Zyvzo9HlP2wIuZv9qt6MeZ2q4MmdW7vP787oFO4K_URUFq_D6T2RF2RASL9pFa5Ldl9vnHgGDqPkCCDW5w4G3GvXx5duq5dESSLkrWabOq_zHwpKidVu_1-e7SMyZHWLcLQEaHXbygJsrL-CcF1iy33cr8EzG9x3nrt1XFmM8wbTuGpHxCZqA4n1Gwg04X_Sp2lcUhOS2okJwSu77opRrw7ZnURBLrEC7Cecc35e6uCDsyKe4px0wMeeAPStn3__E4Wt3fOxdJx4911c6qBFuMOH6i43actXEFrGIPjQzMb0o03kmlqtt16mWAuXIiZwOkGb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8QvnNDKz1xeRfDfKBi48ewcGyxtlws7Z_U7BVTVBabVH_DpWqPAG7S0froXYxymjhA3ud6qYtBrQExWagEeS-O-7K0e0ieVVhrutVWds7FA6NK3GZOuD3RDs4pYrrujOwyE4roozXlyVcwQtBfVn8K1srH0GUUyF5_5kWD_K8egFWeA1OzmE7PxinubL3Ft61TG1h3WQ1GZHx9wtOgA4m9pm4lQRxGnMOFZTL6kWEcVh_nablA9rJWdh9eYkXKJtL7RsnXTNxgCAsG0v41YrcydbNOMTb4wmvazaPJbpK_ffJ1TomVM2MAJ49NhD20DVZKtH0uPvtlX-63IAz8JHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Um6MzQndTDcPFtJ_7_JBK4CFXPu7kEuFaWph-QP-RdCXoLjNwHEa4--vZuMEzmmqiUZCRzMDMI55NPZ2xVHLgDn3IhYKtRWZ9NjnEzewwnm4aUetpSUFce9bA1Tqbvv3iXBDgZKCCKajlKJ7swFQgPm5Chd5LLuZiBoSbaBd34qlqvUQHCFgXkbWMxlKHj2B4P6eqik2qQvq-hzTtXImLPfDWyWpE12XqnaFsQIr7NPW4CMOUFYhAE_5hH3-dtMAWsGaJ3b5fCua6GxVOtvMEhF281IPQqJsUywQm953uB3n6l8fevlandZqxRObOMX0R1TcvdiT65K6fpX8Ceq48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/es0WHjw7KVOwLS6bBgb3SeKm9j8hwP172T4IkKoDoB_CFBo_UQQ3g6a4W0HXRTWZGIGFJ8cMZsrEkFKKNytsn8kbdfQ6FHF5omI7_bI7IVNN2I1itUJperyixA4WZ_YH19l-Sh-Na_cSIdAVDJYDBkvcvkP2_rmXjvG9Ra59s_JQB5MJTdmdtjD_q324M-dQNB9h3vM-orwWb9IWO26VYbDWUszpsOEVu1ngZFsKT46fUEhdANAuwZWq4_IbqMITKe9kXUoQ7CRwEk0IK_-L6qykIiGOwK3tjBGqggBgfqLAfD6iz0YUOPfjbpVO0Uk2d02YHcwtAr1A1fvinkkV-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=KpQ-YUpWl4x56m__UerCFhTheodQFOlaBbUrvmkF9cWMyCsOvQF-zIGL6zV0yBoaO3jku_XvmNqZpRbWGY_9o_smgFGZMplzJ25pWKcuVrUKjhA6RCFGUeNQz9e5sSJVawK8E3-TyHBwpYSxDF3UgqrCctg8GG-2GFnSNUkjTzuGw7TwE30ffy_tHChuOOn02oY39wr5fs_MNDhZrMBkOXS83_21xzpSLie9W1TvJJXGXJMa1NCRfI8l1iUmBRNr2RMV2SXKg5boqbBpfhzuq-dJ49RpcmA01Rke2Wo8FtwIQF9MxwLYzgTTF41wEoos81egAVL_C9y8TEfk8TTWYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=KpQ-YUpWl4x56m__UerCFhTheodQFOlaBbUrvmkF9cWMyCsOvQF-zIGL6zV0yBoaO3jku_XvmNqZpRbWGY_9o_smgFGZMplzJ25pWKcuVrUKjhA6RCFGUeNQz9e5sSJVawK8E3-TyHBwpYSxDF3UgqrCctg8GG-2GFnSNUkjTzuGw7TwE30ffy_tHChuOOn02oY39wr5fs_MNDhZrMBkOXS83_21xzpSLie9W1TvJJXGXJMa1NCRfI8l1iUmBRNr2RMV2SXKg5boqbBpfhzuq-dJ49RpcmA01Rke2Wo8FtwIQF9MxwLYzgTTF41wEoos81egAVL_C9y8TEfk8TTWYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3NRX66bajE2A6sCjNzEB1YJxtYIjxLyWreqZfb00LkLZZvykBkq2R6fLz1aT4x8eQ3hsmLbjYLWiazHx4YrDy7ToLdc7K-bc_xtpM-KwVHfgK098JtwFKfabONBpGFluDYpJrBYevmRWhNbTyoQXYmTdgtcJV5p-IWwkNiTQ4A7ttqk1qArQJW19obYHfs5T77qKE0zzobjjbycB2M-lndmA31DvHT6G7DnjMyH_NMf4FfaBAgT6oA19PXTBF-lqjXVehFpkUZ15l5_e5U6IzIjhIFSFrhmucLPiutOkE4X1ZJS-LCcq5i_y-mCc9AbaOJo2Wks2l0ZCoV_f64loQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kskBScICm3hPoC_rnFb3zsMIjy9pPymcyxM-vLZQ3TxHZTJzDY8QkPpbE7aVTiHtia6vqMPqqGpkEJkDFunRRoLia8Ae_C1m2EViBmMh7AspoXkgAXXtauubDBs6ZSkfWU_4OMfCL9SgQAyNHbInfzNE91UbwKcKPUH0BdItkZWKST4M-b4holkdWBs-Q9rlQ1WS4KjmJYnFrPkUB7QqTqU-PIDu5veS8kpa1NMcjPH5tbAo1nGMwaBrJmGfXkFmoOjFySmsGfXJakfJfaLkvlak5bexhC61raZc2Vvb3wTg7VzjSlZpcC7EMQGKwDVQmtZgecKr2yjwnucpyUTMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SInCdffEPolbx1YdIBuTTYtvGdaG4xRvhfeJAIrE2Y0S7UkBe6pYeE3LAH9YKdRAOrf_XwGYvXniCHrUx3uE4qUM_FT_PsYHdB65xdbcnOl7XzCIuRByji81fzRslYo0u1Z8zX1n-s_a6ww2SdmkkznQEGazBquxftVXWAaepHU-LAM1-8L2763ywFpi8hB4A_TDxfVr-GMJF39Ii5qPqdt6IiYAhvKKvQAuxOtFc5TsK9ZkJWMfb-mWyGXwLMIbs97ZRZzMCBbNM7zlfOxcv6DY14OsBNIWjvBbJJSb56TqcK9H1beygXJ4mMwxdghWW5ikWT7C90NGlUAaxrRtUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gev8v-w1p7-PydB0Ol_OxdEivfBBM_-zNx9y-vr_qZoQ3oBuexE18k5yqf1dLQ4lTSOj9g9TEOp30M4evGeF3fl_0iTKt7VxB0noKRpH0H4ho9bn4I6M-0sdZ7FaOA4QKqwI-pnN04jbZqtHa7x2hcddtCox5wXYSIecufHMoQbzYIuYH33du7i-TM_OBt9wIq5JxmcQhqE47FHG0e4KuLg2ojmIphAXW6JoMpBq2W3T4kkmdkWKXYCbFgTAyEyMYL14ZHgK2wB25H2qjEFZYdfFJnNfBYkLdCUeuYbLqiMyDZwEFy-wUMLdK_WOCFYsNV23Gaivb1d96ipV9Od2OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=er0t0cqEzSsfbGPL1Olaa9mhIBSRd4I5HAzm6rIY1j18LSs6EgMO933xM0vnsmzBr7AUd_mvZahwVd3aIootw8M1BovyrNW1R0xGtlg9Wq_6BfPqwIs1aTBpS301yLT9_51U7rvg5INurQ8e6KKnoR2G3pIXpEfnsIak0vghtzLF2xJ0SRIVY8jI6eFxK5dweE0s_k7iAmnJtkv0qjceax5fjUz53gtnkl1kFvV1sxB49DnxhGdnpPVjLtV_SKZ3eGI47i6KuEy22gtrlc8JU3un3boCbnEPlK-SEPLcydOmE-wWlWLkrnHxVJWQFLyLMJFWKXB7nkmLk7tk9XlBCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=er0t0cqEzSsfbGPL1Olaa9mhIBSRd4I5HAzm6rIY1j18LSs6EgMO933xM0vnsmzBr7AUd_mvZahwVd3aIootw8M1BovyrNW1R0xGtlg9Wq_6BfPqwIs1aTBpS301yLT9_51U7rvg5INurQ8e6KKnoR2G3pIXpEfnsIak0vghtzLF2xJ0SRIVY8jI6eFxK5dweE0s_k7iAmnJtkv0qjceax5fjUz53gtnkl1kFvV1sxB49DnxhGdnpPVjLtV_SKZ3eGI47i6KuEy22gtrlc8JU3un3boCbnEPlK-SEPLcydOmE-wWlWLkrnHxVJWQFLyLMJFWKXB7nkmLk7tk9XlBCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBqaJPFPXnFpLPYvuEjb6nDEnrPTlS5wDgtSllX5mOmUCaQ1uiDE5QUyjW--94lSQmUblHHfUVs06_YsVMB0RsI_1PjqrizzQ79E2HfRva5YkHXy6qenMgzBMJTv1uwNpWFqrG4PwpyOtyxEi-wOCGz-fvNaUpzbGKfb8FQGGc5Os5eqv6nrZCXLeHj8qhMT6-ReNdUUlADlVDJWLll6NTCmw2QtOhnR4he4Ddjz2WTRnQPfctOoIP3wUVal5yhB5fPh3ayy29veKJW1gIpbw6WaOgGW08SWnKbeeKRQZIauHTYqHj4jbhg5apLC7P2onMWx8rSDGuf99LKksyk0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvTDXcTCHr1_8Uz4nCkh78U45wW3A_vqa6aoOjjle81NwPdRXNoxEXIkyqTtIZZ9VIEQH71Lg7MFwjCSEzwfgG5WljDdXttkeL2kzo3YJP5GlMwgQSSPT6l8-FcAWq9ajd7QDB5gORd6jSZHkB4IpnIfeK12WqRX89s2Cn2BrWuXmc5Z0n5MddCi8dsDsGRe_pAVz7PLQ_OX1ecAlnQEtXA8x5SCi732sUfor31dXbQDeISR5SZipNvw4h5y76xIyddjG1ly5gPxqSdDfAbGjwnyQPsPGW68yrZnFzeIaPEmvE0VxotCe8tJmj6ltR-9sIhWTGQy-Fedz4rL3P38Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxnsfq_fOxgHy2Y1bp9W3gV3RWZMjy-DEwfYRiOCk2nZ9WPj9Kw0RybXSUsr9zgdYjR_Mvro48FW51BRuUa-453e9xqPbqNTpCdmw14ZODZg7W8VXcVj7y6JE-r7P37YBy-rp_kIhZOn_fj7rJ_B--vWbvn27Vvsb6XzP6OuTIHwzFM3eipC5LdrVH4Eff4e-atpAKq0-enbVGOd1nYdHOS6GzvIOif5DI-sEH6sQMsU5PirAHBInOmQE2he44a3CDC7IPEpNJYOiR-vLYSURu6VVHYgDcuPauya1_OoKtfNvR4JRbLiqw9kSJNTjjUBSMR5k58MNWSVNbLFgqyNPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkIO-SzNaxDiS-7gmq9blF6nS3sxbG97tw7RPwnlFjmEhx0FKKuj3G2HnaRbDe98354BO2aLC8TwPWsgUKuGCj-PUFV3qJJrPLytASU6S_V3rtAMAQvek-ZsHoQvJ2zIfZjShbWaImovsXpkpFrjS1wzhe__ohpS8Q1xLg675cUG-rV04g_jpjk4pqzxvIfE5ycd4qqB-sRN3UBxwzDn2DeMf5ySS0VPQfhn9olMNysPCUqMFaAcy08gp4vFn2lvPhJkze45a59bo-ofhrFAx55mIp1uQXbTZ_6c98kubL-rf_-AJqnbGols9PQWIy_RXJR13lRFwRoVBGN6Xlx0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJqX2nRUIKQ-jxYmOO4Hrwfe4dwfdDHcCw37w-7pyEFbRL20k58mxyV2-eRx_Oey3ypfZ0YBnqZ_cTVAKPHGXlCAvvFQ8tkIL1E25QkwBCPLyiBP5Newk_yLiVMlMhH-0vK0LKk_BFxzLBDiVsRbqby3Ib6u2WNr_VCMIYf6cbPIZIXlnpOAps72B4v2pmTXNaVlCnkDzWcDQQCwDYi0ecsMWw1hDZNuQisz-u9ok0H1j2BKKwdw-YUy4b6gWjZBVyEzKYevhvC40VLYMzl3hU9C7bAVm5DrHtE5uLoqjjBbKnnLrgUFZa_838oiINfl4kqArA6o1bK4ba7gLyxkww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=LR51UKrgjLCoyD18PCMwyReSsl0WwR5L2XsH6Ly_xNpHPtwy_ZI2I47VnKIH53F-2cSilBlFacvpNRs3aAyZ62LQQU42t05yGjBcP2HScP5fv99Qx2Keb_UvIHD12I4yvFfYU8hGSKMvF2jLPEP13JZdplu0pb09jbpeE2TjU9ovl2zLYBXFwR8Ndf2ZHiuAqn6vVKElUzfWcXqp0ckx2mHj-iQvevSXOdKtWZ5SmT53y0Y8rhLxMOG2SfKTvqTkWPPzyMGBuDWb4VzPjuZzJfNLCkbK2ULsgF2JpA5fNCPfWJAGRUg7UWILctbE3PEcE9IXVnPf2oQN7x7Cbfz9DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=LR51UKrgjLCoyD18PCMwyReSsl0WwR5L2XsH6Ly_xNpHPtwy_ZI2I47VnKIH53F-2cSilBlFacvpNRs3aAyZ62LQQU42t05yGjBcP2HScP5fv99Qx2Keb_UvIHD12I4yvFfYU8hGSKMvF2jLPEP13JZdplu0pb09jbpeE2TjU9ovl2zLYBXFwR8Ndf2ZHiuAqn6vVKElUzfWcXqp0ckx2mHj-iQvevSXOdKtWZ5SmT53y0Y8rhLxMOG2SfKTvqTkWPPzyMGBuDWb4VzPjuZzJfNLCkbK2ULsgF2JpA5fNCPfWJAGRUg7UWILctbE3PEcE9IXVnPf2oQN7x7Cbfz9DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ :  از طرف امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس امارات متحده عربی، محمد بن زاید آل نهیان، درخواست شده که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازیم.
آن‌ها اعلام کردند که مذاکرات جدی در حال انجام است و به نظر آن‌ها، به عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همه کشورهای خاورمیانه و فراتر از آن، بسیار قابل قبول خواهد بود.
این توافق مهم‌ترین بخشش این است که
ایران هرگز سلاح هسته‌ای نخواهد داشت!
با احترامی که برای این رهبران قائل هستم، به وزیر جنگ، پیت هگسث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای مسلح ایالات متحده دستور دادم که حمله برنامه‌ریزی‌شده فردا به ایران انجام نشود.
اما همزمان به آن‌ها دستور دادم که برای انجام یک حمله تمام‌عیار و گسترده به ایران، در هر لحظه‌ای که لازم باشد، کاملاً آماده باشند، در صورتی که توافقی قابل قبول حاصل نشود.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=TM-cLK79tX0A3OLkI6epKz6HyAnNukKh2dVs3HJO_3kctA8t6qTVF3IwNuaJVtJ0uYQvQhXbTxbgnnKcoYXGVLWl8gUtHeauWXCNiDTGLQr0X59HCxE4NQqq6niUGkEHtN2Sa4AFE0Qt1IrEyVF2owWEvGNHbH8e0xtMVfUQeirhORff-qrUDeGPI1S6IG5oHUylgQbxCKKeEOghra8wP7AkSYs7GjXcdT4PHXehZRGkerXdo-LQsv7Wl5cDJGnHYXGhh1pS5v_qIAQQVxVYxfxsDv2R3d18XDmNyyVJJEJN9DkRgHitCLNGho4g1G7XVZoSmHzbpzHvzvzQXBvWWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=TM-cLK79tX0A3OLkI6epKz6HyAnNukKh2dVs3HJO_3kctA8t6qTVF3IwNuaJVtJ0uYQvQhXbTxbgnnKcoYXGVLWl8gUtHeauWXCNiDTGLQr0X59HCxE4NQqq6niUGkEHtN2Sa4AFE0Qt1IrEyVF2owWEvGNHbH8e0xtMVfUQeirhORff-qrUDeGPI1S6IG5oHUylgQbxCKKeEOghra8wP7AkSYs7GjXcdT4PHXehZRGkerXdo-LQsv7Wl5cDJGnHYXGhh1pS5v_qIAQQVxVYxfxsDv2R3d18XDmNyyVJJEJN9DkRgHitCLNGho4g1G7XVZoSmHzbpzHvzvzQXBvWWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏رویترز: پاکستان [کشور میانجی‌گر میان ایران و آمریکا]  در چارچوب پیمان دفاعی، یک اسکادران جنگنده، ۸۰۰۰ نیرو و سامانه پدافند هوایی به عربستان سعودی اعزام کرده است!
سامانه پدافند هوایی برای مقابله با موشک‌های جمهوری اسلامی است لابد!
پیش از این
مصر هم یک اسکادران جنگنده و خلبان در امارات
مستقر کرده بود و به ایران هشدار داره بود.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsHlXqkv12u8sdeIwBlqm9y1wsWdHAcyZzT5Blhfr6Ek6uNq5Q9mg4_7Ka5MNiGUQ_q55bz70DU5qU9rY63pxH_rJlrXYLLRowZ8QTdFZalDH5EIulQnSCxi3S2MZlWbPrv8wnM57qUe4C2gAPNlwHaHXk2FPsWS-WnTNqZASyUsGTCRnKEDRcoaNibHM-deUnwdR48Rd-e4ipJtQrzcUdcjNIYflg-g4so4D3ZgPUT0C7K_zYW0E88H7bw21Oobpjl7Zmidj4WvKPuRkKyIEdlIGWiu-bvoizmTl-AvXCQyU5kaWhzAvSoZFLEN9mVuEB-Tr2fppLgz7O-F4mymyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsQHOFM6E8UJqt7PkyEPzePFKczQasUAMOkHJFkdpfoIko9yUh4ZhaKoOf_SoPpiBb_z8ijugsS565lKcp9x10Rkm4q6bhLiMsUzm5uDyd17j0NZEzID9dycqcX3AkV8mUpV9wQti_HKtnDESkzEj8r96294K2BqTSqUSTYt3Whb0aOzxJWzLyOINaNfNv7ZPSQC-TA0wE2Hlyc9xXvkmJ6JMnKx7aJllB81gUoIcXMtJajgZ1o-FR1pnLiAn8w48JJ6JX_I0ST0e91vo9otdq1oLjRiiIrR01h54MgaWBW02qQfAS23-EutOtabReFTBenoOWzXUxV80fsk0QEjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEXKapFCOmsB0Asg6qJoqdBNonf0ixg0nnGKKT0HrKB6ScZa0wTmJWOPRbRcPRB1ZwqqwV39bYtVdbFeAMvR0d6ITm5yYbfA_oyhtxRmi9DqQtvZ9KKiSg0quFwNYZ7ebM9EAyJPAVtldmE7S7qG9-CpqwdU8t-bK8RDy4GzvVz8pxNaColx85xh7BlQymYnFmnb-8wCz1ksnsvI0KAEkIyqxrhg8U7PaxjJJkMTkkWzd_zaVRU6JK-_ps5v13PiggjThe0j-8pI79rNO9tS26VXDAC8OOZ64mZHE7sIAMuuoAw-1huy9SSlBcdZLnSu0bry9ZQxCvURV72PZTfHCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S98r-f633OWB9t1JuW-OT9LlvaBf4VGGDZy1n2n-rogCzb_IZ3uvcd-VvemjwlASRBWGGVhYMPoOMx8yau0q-Za4G1T8dKFCrQU1SiXh8-RWhOZLKOumOKLeIBClUYe1F7NpTI_59lGHzm3xT2zv07Zj1nrVGGRKC7JClbYS_TtINIWePRTQWLHcspD8vRT7OHK8uAsYUrrkh1XT-K8_SHhs5OMoUnjQrY4KCSh-jIkBnXSDO1rZcYccK9FJAh4a2tNpEZ-bT0G_JcDQGaAPV5-063NJ_HiP4PTmLJ7skvx1MDLtgatkqEbyh2vRDy9jl7MmbMnc3UXQajSqBtCFCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=H3QACzJkAd_2Mklz-3Y4cXkTUZ2HdKAZyIcwy6A1iUWTKlzsj0MgdlmlFvB1iW-bXpu1dstKTmGO2FwPEeySIS4Cla2Iqji79ru2cnq1o2cbakkSAh80mU1AUGiGt24y2JOfdyY-sJxnyJRGwlhPvWbWLrf1HovCiF2XiYY3uSx7VTtEs5eAu9BI0sR43maQ7IgvB8EAyX7xNuOVROBD2LvoTA7I41lfGlwFCeD6Vej3uu3aophuG_3Bh0Px9el4qYAJ_GYIBklKdLZwZb9OlJr5S5yXVvpSoX2i30rr67wAed-SBgeSvqweMIPflzxpvsPdjMvM5jiQmwvrpmW_rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=H3QACzJkAd_2Mklz-3Y4cXkTUZ2HdKAZyIcwy6A1iUWTKlzsj0MgdlmlFvB1iW-bXpu1dstKTmGO2FwPEeySIS4Cla2Iqji79ru2cnq1o2cbakkSAh80mU1AUGiGt24y2JOfdyY-sJxnyJRGwlhPvWbWLrf1HovCiF2XiYY3uSx7VTtEs5eAu9BI0sR43maQ7IgvB8EAyX7xNuOVROBD2LvoTA7I41lfGlwFCeD6Vej3uu3aophuG_3Bh0Px9el4qYAJ_GYIBklKdLZwZb9OlJr5S5yXVvpSoX2i30rr67wAed-SBgeSvqweMIPflzxpvsPdjMvM5jiQmwvrpmW_rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=sffGitKiaz9_BdJr4jMhxLzxt7j1JhrBhGbUTLxkhMjKKCESZXecfDLTS2gY29hOf9Qeb8l2qdXbybaf6eWdbbk38WveNObtQBbXe_qfNeYcmfvA_yQPacraVKX0hJQzmxFDgDVuuxhScFOWcafLF2Sca7GILZ6fc6L7ijpzC4fhkQ82uKTscOlFJgTvq0_9WMHxFt-tzNohB_o8RrhVCWWb9mYLTBcw00YcrQ1IjXUKB-Khp8JKveg0vN2W6wpxfVgd9eD9ie6zH2BMNW6a3MlMzPQtcf9CeaeDG5OetNn76pyFiVaQx0E_nRICq7lM70jWcnqUhysvKUZNzUZ8VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=sffGitKiaz9_BdJr4jMhxLzxt7j1JhrBhGbUTLxkhMjKKCESZXecfDLTS2gY29hOf9Qeb8l2qdXbybaf6eWdbbk38WveNObtQBbXe_qfNeYcmfvA_yQPacraVKX0hJQzmxFDgDVuuxhScFOWcafLF2Sca7GILZ6fc6L7ijpzC4fhkQ82uKTscOlFJgTvq0_9WMHxFt-tzNohB_o8RrhVCWWb9mYLTBcw00YcrQ1IjXUKB-Khp8JKveg0vN2W6wpxfVgd9eD9ie6zH2BMNW6a3MlMzPQtcf9CeaeDG5OetNn76pyFiVaQx0E_nRICq7lM70jWcnqUhysvKUZNzUZ8VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8tizznYzuhswT7jJHTkF5qL9IVYTAh9ZRxyCRFdfhJtF_B5MpLPMZINjBMzdkAu0YiG-DVnwpi42w-ElPvg6xdqygT-iBz21mRNDxQuAEd5Hp_z-40JyFv8EXSrkDJonzUg2OzPMnmaCt4GFEYrh2YYgLoT3V9Ny-l8amQFbhchkYaPMauCgwGNAPe1WtoyXdXpKNMl6ibMYGaeZeB075iCo3blCPSAFqUyKXsSuMjfK7PdaCwGwLFSNLzV167R7PyFjbNdtdINk9nixTGmvK2UdpN2kzawQUPhxEMFcJHAV5V3I9h-v9X9yehaMWdVHV50z-EyC27fDNC7RLdAOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiNk1hPaMoXWCMSAoqN2bNNGhhCTDSiHr6fZLIp_XQ-X9KA2DcH6lh6md2TaxNWmjLHavE5uza_ez5_KYq3K2-pNROHfWHzZwBqCIQogCP8f0tRcBZaLXFooOtP7DccCsLz2r-YNYbZprJlOtnyS5IwBHb9l1FBA9Ww9pjqk-xqKvUHa82ZJaanv9QrzMlvX1SYggIVaTFLuLqLvdmq6j85S1YtVAPj7QbOqUwNLe3Rcg5Tg50YDhsljqHHLyIHp2T0cugZeUxLZIeMpxDIt-6xLhnnfuqCSUxTWvX3RCZ8Ei7p87eUEYTfT66UUAFIosz0J6b85HE39Qw1sG46t8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBYWjutIEiBVsMWE9vGirE7CJE41pQkXP9SbygRKX1x9shdxzYsQ0TQxR-AgvgPbhOK0KW4B9z4J0e06_RsdMkG6Xmgigee0HDlLy6vmBGT4Q2byU6hbKogw7A5KrMovoQokBvW0Hi1Z2pGVDnkWf2OMuE5sOn5VaXauh6VpclT5wFdwKPjN2A70rY5Q5sPQxiB8WpyIvO8CTJxB786udspkrbWGvrIgvRj2RXy2PCxcv607ymY0ML7LZDrlxQFbrnnAPcAG6V8FQEUaBNRAKclpBiDtVfeMyLLhickXcuu2tNV-J8lmpL97Sad99RP9NJr0z9GPI2oVUOAfWjZ-uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbC-e2xPQSkwb3EsPjbwllIsxiBsr9Eb72WvfDKUYyAmT-noXA981te8C91eCe8IPjCbLBm_pIikvF3jyPJCSqPxTEziFHsTxwxCgvNUMGpLBGnsZsM2i4cchVmJBOmLXeZvdTLeFneeTLbOobfGXF481_eEp3BlX5MCAAza6q88_WhGX5qEuulGQCpre9C6lvDAonxVKGh9bmP1iHrv3_iKRnMKnaboXzadZKTUTXUSJxwGOLG7qZqqTdcr1emvG5OlEI9mcdZ_AmqYjOS13NzcE6u82o-7jpLPQkU-9Qp5hZYusFUtDMGY0E9nvdXPA4IdzpA7F95UTZLb9rxYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=jR-b8537XgJnhwjhRQxVIfEJIiky07HFIqlMOP4V9mgTnDDTcILh3O1W3KapSiri16N4T3S4hpdQtHDZ2J6MWCoEf7itgdYLvQ9xMS8R_j17O1e7HLmwB6Egb8aJLStbH1HPPX4Bf_lPb0yUEv3KcW6v0ig4wvL6_ADHW0GfyFHcLbZytU24VeqlyB0xaQazSWIhqpFEn01rTKlsrJV7rHxtzpZC7bVT3o5bg57f4tOQc2P17ptMVfJT0pKnOu7t4Nuxv_U1EyoRwhsGiUR2doOFWb4nWEXHJImx1wck-FMfEw-czhCv8fNHxB1dRxjT_rsQ4ncAybzX-UxHIFtV_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=jR-b8537XgJnhwjhRQxVIfEJIiky07HFIqlMOP4V9mgTnDDTcILh3O1W3KapSiri16N4T3S4hpdQtHDZ2J6MWCoEf7itgdYLvQ9xMS8R_j17O1e7HLmwB6Egb8aJLStbH1HPPX4Bf_lPb0yUEv3KcW6v0ig4wvL6_ADHW0GfyFHcLbZytU24VeqlyB0xaQazSWIhqpFEn01rTKlsrJV7rHxtzpZC7bVT3o5bg57f4tOQc2P17ptMVfJT0pKnOu7t4Nuxv_U1EyoRwhsGiUR2doOFWb4nWEXHJImx1wck-FMfEw-czhCv8fNHxB1dRxjT_rsQ4ncAybzX-UxHIFtV_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fA520eEQzxw1BS-SPFc7Tg5Jpt3foIDA5odaV9I7nO9bUwNc_dGUb5WcmKdifV8B9jeZkH_JXLWYtYoUgQUyhefm0ZG8AMgNWvWzgqXC7Ny9XFCs24f6zeasvOyvrmQNEpIuYPrW1SHdjmN_kBK0cRdA91FczkTh9w_-5rSOSZejJY8Acvr8ZNVuoWwyoO5hP5NjrMfq1QfWEAAOfTEZZ3vXEzkEVvVBlgDG6rqM8LxqBR2iLjLpKeOCUBO2sznJXD-DvUB51lek2OElUDpnFH5sl4NrC5kyDf0PAZMFawp45Ppdmy4fLKzUFVN3GGwA08Dsi6PyGAACyC8sTur5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOODIZGP_bFqkHlNiICMozfqLg386n0Ns_YQAY0lvxJMMKDVQG1U7zi9t5kg_w8OKB7OTct2bRHGKcukvMe_W5O0Y9YjChQOe9KJ_zApeT6T_8iur715YIvvu2iJLXWHOrlKKep_ji3QtgTn0KZh3toPN52oug-5j4iJe2-hcClesvjLUBjCvEhLG1NHPjROjAXocEF0L_8XT9DYv7whFEXHFg2wvMR7-wKHs0iqoHJDxT5m3hKdTKNL0bi01MpPbOl7KvWcepul3rmNGIhVTrCCH2bGlOOrzxMWQw5cXIranlWEP3L-hpKbm6SroJyfoeME43QobyyG3r9g11D1JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=rLkdVeUgtWyJoYj4xXmsvvGsbl8TtEgBiBCZGNZ7bL7hANUJDuzf43VfZPobW0ZlmvKu-qeqhuizldfh0B1EeFO3FdijKiz2a8QuN_W36LN16EFdBQP4NP28nqVRdWSAPhf67Wt_a59NHhCJ782VbOZUVEI2aeK-t_LEKgLReXOCALxlwIt29Vj_wzGL2c380LKsfvrNzRgZeYr2rzt_OslgpqV2FQCUVGOW46Xg0g5WzskiHA66skQvCgf83NvBdARxIVcat9sTOMothvInRXWjwVKmYAWDDybFRQPW6DBLyrfIb2B6siQSzuO7Y-Vl5hs8j7dhyQ59X-q4XqZZGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=rLkdVeUgtWyJoYj4xXmsvvGsbl8TtEgBiBCZGNZ7bL7hANUJDuzf43VfZPobW0ZlmvKu-qeqhuizldfh0B1EeFO3FdijKiz2a8QuN_W36LN16EFdBQP4NP28nqVRdWSAPhf67Wt_a59NHhCJ782VbOZUVEI2aeK-t_LEKgLReXOCALxlwIt29Vj_wzGL2c380LKsfvrNzRgZeYr2rzt_OslgpqV2FQCUVGOW46Xg0g5WzskiHA66skQvCgf83NvBdARxIVcat9sTOMothvInRXWjwVKmYAWDDybFRQPW6DBLyrfIb2B6siQSzuO7Y-Vl5hs8j7dhyQ59X-q4XqZZGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5020" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3Lhli7h7_pV5L1SxNn0fhf0ZUDho8D9VGzfJuxmSgZCekwugLzpGAk_BM4049uJpGHulA8gQ9mut-JVV5CL3taKaC43TDIrBYn6FIxzv7fmI0-tlZjP23IwIlKRbQujA548tZdFDAB3nO4QqHHv_FL8JVjHaaLYYSZtQ3purObMcFSkX2jBk5jG_ePASXpHtlI4YJKlejeULscB3A9vJUimw0mV91SMwCfKn9FaTAxqqoypQ09SHXqLm6pLddWLtc6zAlXo04BehKWTpoSILi6CYjljgGV5tnGsRPvuHgByEa_QbO7rC42FkT23iAPtS3X2waOyIsiTh4klN7rhXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !
‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا
‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا
‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای
‏۴️. عدم آزادسازی حتی ۲۵٪ از دارایی‌های بلوکه‌شده
‏۵️. توقف جنگ در همه جبهه‌ها [لبنان] فقط منوط به مذاکره است ‌‌دست یابی به توافق!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5016" target="_blank">📅 14:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=M8zxWj5M-JuqaoF5EgxvKmUk3i0e7rLyJeqiiLJKeWN-L9Aw2JEvNsVS_aLAHA3BlXP3AvivHi_10qYZYPZBbKx4sTuVg1T-w6X6kwAFNv0f14lYEkt9iwkBw1vDQiujhXDBadn-t6MSYTSnHuB5HsLI5Au9lM9zl2Xn98UTGKDvioShskCtVKT4xQa_IIt_qLLk3tfpZwACxDa50hW8NZK9b3AQKUI5IWs6H8Y9ZWmAc1-r79Zf5wSmM7pFOo6dsDWY_zuiCL4KaJ3s0F8jhl4_HEy4Q3c5JRzfoGRwzI7KQRabahGNaRzxWyViUewwIHvMMMUDPHcojpuiNdNWzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=M8zxWj5M-JuqaoF5EgxvKmUk3i0e7rLyJeqiiLJKeWN-L9Aw2JEvNsVS_aLAHA3BlXP3AvivHi_10qYZYPZBbKx4sTuVg1T-w6X6kwAFNv0f14lYEkt9iwkBw1vDQiujhXDBadn-t6MSYTSnHuB5HsLI5Au9lM9zl2Xn98UTGKDvioShskCtVKT4xQa_IIt_qLLk3tfpZwACxDa50hW8NZK9b3AQKUI5IWs6H8Y9ZWmAc1-r79Zf5wSmM7pFOo6dsDWY_zuiCL4KaJ3s0F8jhl4_HEy4Q3c5JRzfoGRwzI7KQRabahGNaRzxWyViUewwIHvMMMUDPHcojpuiNdNWzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشه عنبر خانم!
ولی روی این حرف‌هاتون بمونید
فردا که به خاطر ۴۰۰ کیلو اورانیوم
نیروگاه برق و پتروشیمی و پالایشگاه و… رو زد، نیایید بگیم ما مظلوم دو عالمیم و نیت اینها تجزیه خاک ایرانه و… !
اون وقت برو پوست پرتغال بخور و عنبر نسا دود کن .
تا می‌تونید از این ویدئوها پر کنید و یادآور بشید جنگی که بر ایران تحمیل کردید بر سر هوا و هوس‌های هسته‌ای تون بود و دشمنی‌تون با جهان!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=t3DmgCzqC93X2q7MX2zhwWSAParGWI84bPUPWJMH-WfzJGKE_uHQL2F15K22lcKsLi15Hz2Zx6wn3uuGOyLDVDsgVH-fHB8JzoF2ysg_tUkjKlRwZaEmO1hldATBncXbHMXzgKPQ04CjCdkTXv1fuaPDG59ahHtFHlblRlKIIreJ-8hE8GGms42tAlbfdMSz5sNbRfmysuQiiGvgBXAiA9RpXh6A0-QnDP5rW8uIYxwDKN2gcr31IFaolUbWSJJAhFe0V-DxiOX13ULWqCgSE1D2Xgj_rcE74iZZcJ62fQKWrLb1WK7pBoIbcyJlbcqAZK8vX_ELn9M71Y99uKwZAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=t3DmgCzqC93X2q7MX2zhwWSAParGWI84bPUPWJMH-WfzJGKE_uHQL2F15K22lcKsLi15Hz2Zx6wn3uuGOyLDVDsgVH-fHB8JzoF2ysg_tUkjKlRwZaEmO1hldATBncXbHMXzgKPQ04CjCdkTXv1fuaPDG59ahHtFHlblRlKIIreJ-8hE8GGms42tAlbfdMSz5sNbRfmysuQiiGvgBXAiA9RpXh6A0-QnDP5rW8uIYxwDKN2gcr31IFaolUbWSJJAhFe0V-DxiOX13ULWqCgSE1D2Xgj_rcE74iZZcJ62fQKWrLb1WK7pBoIbcyJlbcqAZK8vX_ELn9M71Y99uKwZAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=FTopBQhd7WpH9TTNG89vV9QzlTruqTlUivkQGp1Bt38JNnrfhP_UJmHHJy7GSEkCcZdWDoGMEVHnrrbXGvI1jxHmVf6it7XUJwWnKtQOVyl4QsI809hRYkjnVyuQH6Bf1tYesFmD1cQKg4v-micBOKkw10Oa1mtxicNyCLRmEHKj9B8v2rF0mGhb8s6o0KrGTepEYGkXEcDQXwfvuZRzTqFSBvUMssnkfWhJzD1I2I2UaH84GfN8Xhf3ldCLF4OoPwVpX1pDhB6RpEc2svaeIFkoGaaIeCcuxnITUR2zU8DCSzxZnZXmXVRF-g-bJFuWQc6NISjC5Sh2U9f1lJN7ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=FTopBQhd7WpH9TTNG89vV9QzlTruqTlUivkQGp1Bt38JNnrfhP_UJmHHJy7GSEkCcZdWDoGMEVHnrrbXGvI1jxHmVf6it7XUJwWnKtQOVyl4QsI809hRYkjnVyuQH6Bf1tYesFmD1cQKg4v-micBOKkw10Oa1mtxicNyCLRmEHKj9B8v2rF0mGhb8s6o0KrGTepEYGkXEcDQXwfvuZRzTqFSBvUMssnkfWhJzD1I2I2UaH84GfN8Xhf3ldCLF4OoPwVpX1pDhB6RpEc2svaeIFkoGaaIeCcuxnITUR2zU8DCSzxZnZXmXVRF-g-bJFuWQc6NISjC5Sh2U9f1lJN7ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=QZ7MWVjW3A_9r2fOmhWev_IOLRY7wGMx5rZ8vWmsBNAli1-DckURw45YyWFKZ-Gbc-iFjPVhvVXGtBn6qLNmKB18i8BY_OZjMSBRYifNfVmMgShxC0QE8qqKHlDEAUbA_6rouUISP_hZvP4weAYtAF6qUwTyWCnFVla7Fac09kO4bthWlP69u5AVN-nJEJ_G0GnNSGSYPccw-SF7cA5O0qqpK20fQ9ws7e2Og8ufq1Qm6ZcUTO5vbRuQ7eaB3pblooYwsHFgrXUyZxJO3J1hwUeq2ug8tpTANlmodMGps-8Xific1WS7hjl1rfGmUX-B7pgj6nNCJh7SG5jv-AjmuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=QZ7MWVjW3A_9r2fOmhWev_IOLRY7wGMx5rZ8vWmsBNAli1-DckURw45YyWFKZ-Gbc-iFjPVhvVXGtBn6qLNmKB18i8BY_OZjMSBRYifNfVmMgShxC0QE8qqKHlDEAUbA_6rouUISP_hZvP4weAYtAF6qUwTyWCnFVla7Fac09kO4bthWlP69u5AVN-nJEJ_G0GnNSGSYPccw-SF7cA5O0qqpK20fQ9ws7e2Og8ufq1Qm6ZcUTO5vbRuQ7eaB3pblooYwsHFgrXUyZxJO3J1hwUeq2ug8tpTANlmodMGps-8Xific1WS7hjl1rfGmUX-B7pgj6nNCJh7SG5jv-AjmuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=os55sM-IyiSpdA_y_zhLvKx46raMUVCB-61KaksDF65WTSUzCQdE4uiCFliyIebobIN6EWT1u0v22gqXGVtTYhz--wb731HD6C4pd4ivSUYFA6GgTxeYtAU_tLBV_FEnxSVfYiUBXAxFQl1u233bzYWIO5tiayAWBA57aipEzECu7Iq-kVaff8WVLIlUuOpxO-w3AYgcRLLJmD6dFGx-GmaO-CDe1YlaPtevk2vZB7gNFIAiRzWoW8jRJLorWQ8j1dc8hsDBluqGrAEjJrEPRiYu25qpm8xMAoTId--TJZddQ4jCOBLkfAiglmEcbxKyY5MIjG-vT0aeAPlYRoq-tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=os55sM-IyiSpdA_y_zhLvKx46raMUVCB-61KaksDF65WTSUzCQdE4uiCFliyIebobIN6EWT1u0v22gqXGVtTYhz--wb731HD6C4pd4ivSUYFA6GgTxeYtAU_tLBV_FEnxSVfYiUBXAxFQl1u233bzYWIO5tiayAWBA57aipEzECu7Iq-kVaff8WVLIlUuOpxO-w3AYgcRLLJmD6dFGx-GmaO-CDe1YlaPtevk2vZB7gNFIAiRzWoW8jRJLorWQ8j1dc8hsDBluqGrAEjJrEPRiYu25qpm8xMAoTId--TJZddQ4jCOBLkfAiglmEcbxKyY5MIjG-vT0aeAPlYRoq-tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJtTaBOK56cKzl0dTEI037Cy6xfOw40hV4MCaOOMfPCX3W8QeLS0_aouqMPlSXuHpkdgCXN7tLqZpcH7cQTjmx6KXS-5prUxYykibDdUq-Yq-OWg1nJMWwf5GgYg_3hM1eYn8rpJ17K9odvR79LbgY7rEuXbwQnbFFaxoB0QfaJEM1rpHleFSqNAjh-jpTOnXk-sodILfqo409kiGNb7agbs3yGFx1cPuXXBUrxEFnnQHlKA-O_v4zikZ3IVxHBFXONMEol1cvlo3gbQhYtuyAAT17aLvcGKZDuwje-vCG8pAkCWAjrd53PTSWQn0sTxjmgwk2INDJPDGI6QVLFLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AeqfkJ8bLX_xMVpxgtyVAVgcZAGHveRjUFgoJ3jRlNOq6MJ8pyq1k_P3flFea7jfx2OiYHFN3GT_oHIr9FgaRxrxtk4gILoO6dfJmvvSF0g8r9j_UO4iG3Tn0EAXpQ1i9k2o5Zobqf5s9MxAEkBj7j3lf052PwdTO41Y_sTA_STvhL2u9G0QRNOIaKfLpH9fptdO5rV6bxlsUWR_v-sb0f-KPX5EHYucVciuCeyiONchq7kzYzxKg093aP0w5ZrDRC7e_dukMJO-xP7q6qbg93BInNHRdNvFdPSpFqe8ne3mSjUeixlr59TK7LXcl16ZNOd21A5DV2Ry3Zsbydkf4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mNIpBOOQEPshWFNXwApBxz8G1PxsHDe6fHQ7-EhdVQdc4u8noRXHTnEvJZ3qmucKsT3Q6DruN681tsnm-7CvE-8wbGubdg8WyUImzUFn75YolOz82AmRw3bNYeJGA7OovbR1GDWspoPbLKD5TtloGM1lGW74TFbegXSJ1faKVqz_R4_skM_OzLsF2lfYrzRnVgq_hriVhgceJ8vT0glAwlnJ5xI8TJvoR8oUfSGR1AAfCGAFmx4d1L53kIKNWpRA8suNZb-hWQUxSx7PQCZENANjpnM8g0m3McGMI3OOgBI9JsRm6UOJ6ysTerLLQVwo9alvhrfkWoOhYrt06fzDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KgDyI2OCsXC3XYORW6dSc5xWmM-YGyjc9r0ZkF7GL-TDTpXXbX9rXRsR_iRPY0aQAv6ZilbylDQxXqyCyquSYz9jqEXPI5AS-iwHE09rk2g491HqcTG3gimO5FVPzaBB33zmZQytibzwPUq663QqZ46VBmV5WZX73gzW8Y_PRPFF8i6ecmCCfRKgK-wP6rkiYdwWgQEqd5WInvjjKVy3zblD_iZI81VlfPch0LB1jJ1x3VGFvGDDdfwJEVCsapE1ojWpKCz2phDcm0PKGCgZjc25oJ56NH0cLoGyrU8ZWPMpF4UXn-4WcmhDkJx7G2Z6xJhyM-rcLCEyosROjWNpHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=CkDYkE1sd230zug8EzC0ZQD3NttIFbMa0EkBneEREWig5Qu0tx27CmjBt0O-86TKe0zqFgrSmk6A8IiE7GdaLdJVvoysL-_8a8TUahAV8uW0LTVwgx00cSdSpjYqORCKIXbxCpz-xGa3dzz0ai9NbhDCclh5B35WyxtAfHT8wi6l4juZ0Nxpz2_xWDv7HMEXg85A7V6fVx4iZMeqIrc5OJfp24XlRpMWdRemoSTc4GbZ6M1Z9-xNNh7EIFtbo6Ev4BR9ST-03E7z36ts12-3kgryoDWz9SsQarewWsxcG6Bbq_K7Dv5rcl5g9cWGbNOHWF-RTJAPgjdq1oUwi19FDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=CkDYkE1sd230zug8EzC0ZQD3NttIFbMa0EkBneEREWig5Qu0tx27CmjBt0O-86TKe0zqFgrSmk6A8IiE7GdaLdJVvoysL-_8a8TUahAV8uW0LTVwgx00cSdSpjYqORCKIXbxCpz-xGa3dzz0ai9NbhDCclh5B35WyxtAfHT8wi6l4juZ0Nxpz2_xWDv7HMEXg85A7V6fVx4iZMeqIrc5OJfp24XlRpMWdRemoSTc4GbZ6M1Z9-xNNh7EIFtbo6Ev4BR9ST-03E7z36ts12-3kgryoDWz9SsQarewWsxcG6Bbq_K7Dv5rcl5g9cWGbNOHWF-RTJAPgjdq1oUwi19FDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=hP0xVQoI23zwkABhlbOhjW9_q9o5cP1h-yYkiYPkFC5xh8gNSW8eTjHOK7qiCZOjVocD0DL-svcqXyAzLPFKRdnhT87SITgZjjAeLQWFtQTmXb9vBQC3ohnH8aBZXUk2AC82YwQkTrzhdOs3SZj0za6LQjyxhwS3yNcirTwo04OxeyHvWa_eT3WAwq741WrWviRLd35o7XeV1_nZuhKCQhkXlDw2LpFO-d7rM34Pneuwtk59fTxJn0z99iYlqSzEsNneVRRlfNbDKyspxC9awaKozOePP4_He9IWe38CYMZGixXOZfOUGSN-uVtge9fpU7o79qT2geNs-KA2Xl56RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=hP0xVQoI23zwkABhlbOhjW9_q9o5cP1h-yYkiYPkFC5xh8gNSW8eTjHOK7qiCZOjVocD0DL-svcqXyAzLPFKRdnhT87SITgZjjAeLQWFtQTmXb9vBQC3ohnH8aBZXUk2AC82YwQkTrzhdOs3SZj0za6LQjyxhwS3yNcirTwo04OxeyHvWa_eT3WAwq741WrWviRLd35o7XeV1_nZuhKCQhkXlDw2LpFO-d7rM34Pneuwtk59fTxJn0z99iYlqSzEsNneVRRlfNbDKyspxC9awaKozOePP4_He9IWe38CYMZGixXOZfOUGSN-uVtge9fpU7o79qT2geNs-KA2Xl56RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=Kg-AGnWV1vI5MNiykxXHmwvkLWKpviMq2gYC_9k-yfvo5q8E1bawJEsqkw--xNG4jkN7ytK538YwkSyTl6XlVEnsBe6tg6oBKW2TmYRLaUIVtu7tG4d42LLBoG4sESMyjObVj4CCY5Jy4eeJezG5U3rfNGydxBa4u4KvK8bDazrU2SIZBq_y3AEc6px45iGrUKvkhpV4VOL1ud9w4GtrYfBEfeBbih42jkNKMaLP8r6VWLlD5FtlNoS5EocS0nAXiKE8FNNQ2So3LGhaZT-SZuszycxpoZCXbIa-5z81WWCtPhbN_a2ZrTmzuu7tqDvH03LeDvcsQGuHAVsk_A55Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=Kg-AGnWV1vI5MNiykxXHmwvkLWKpviMq2gYC_9k-yfvo5q8E1bawJEsqkw--xNG4jkN7ytK538YwkSyTl6XlVEnsBe6tg6oBKW2TmYRLaUIVtu7tG4d42LLBoG4sESMyjObVj4CCY5Jy4eeJezG5U3rfNGydxBa4u4KvK8bDazrU2SIZBq_y3AEc6px45iGrUKvkhpV4VOL1ud9w4GtrYfBEfeBbih42jkNKMaLP8r6VWLlD5FtlNoS5EocS0nAXiKE8FNNQ2So3LGhaZT-SZuszycxpoZCXbIa-5z81WWCtPhbN_a2ZrTmzuu7tqDvH03LeDvcsQGuHAVsk_A55Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.
و نتونستن چیزی پیدا کنیم …..
این همون حادثه‌ای است که میگن
مجتبی فقط کمی زخمی شده
این همون حادثه‌ای که توی
صدا و سیما گفتن همسر خامنه‌ای (مادر مجتبی) هم کشته شده
، بعد از ۱۰ روز  گفتن نه! زنده است!
یعنی وقتی داستان زنده موندن مجتبی رو پررنگ کردن، داستان مادرش رو هم تغییر دادن!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5001" target="_blank">📅 15:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5000">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sy5aGQPpmiDjgNHomyt2OjghvNUTnRVe7BHhU1C9dx1LXw3exy82_Vwymy4FiFwIyA60AbFXvL07QNB6CAl7dYaa9VA9ca8xiK6_zRIPpLMY-yopPl4pyCpovREb7JqJaon-QPATVnsF7WBpWyxRVYB-WNgciGEEOCEmvQ9-1213EY4hoRxR3zDi23C9QoVTwCCeYGh6iZkh-4R-XCdzyrFfMHF2np3zynuSPFAxNr-kIr7jaCGdfoksbSTGM6mziga6vlITDCwY-4PMVk1NXpvBgKWJKZ-nIH6-w4wcMxXa6Pnn115Wg43my4-hzjUergI0NpPidMhPW0sWzM3EQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=Jq6uBC3SvmxgZju6rghMqnydEHnMOeRD1oi5rWuaXeM5GLHapnDaWGNWuovqW-Z5PP-ILHKOgO5RlziAEORMVJ179bEuW10MTEulRzl-zVrRWHVY_eFyh8yQ5bhhzosFpU64_1Oje878fhOVCBdritoV9HrSmsPVSIOqPJ7Qdlhai_EewYH339WHBAK_83h_GCzYvUC3Zd1O0F_d5iYFBglXprMykq3FKMEUZxo8Trt_WYh-zYAwuQtaBzggqHiNV4GJcjnayyQL4d1Dg4hNjzOkhW0JjUz3Q_Wi1zKqFeIGmhvHgr4-prBNdhXveodQRKEefY15b-pKQvgih9O17raeWy8AkMty7iAQ0C-e8Ye6aHbCStEXQFXSEKC_aC9AX34Rhc54tZOFmURcmIpTbXZqlXd3C6--aHsb_LNrqmWzfdn4bEs2esPhoqzRUBlqLuJRVQOpOw6Y2OJWZE6IvSogmTJjYwCSVeFcSjp0zH-7IBPpRecxLrRjnrQt6VRGF24x7udX1WgxhSKg62XLc6GKEpTNm83CUzrZu41R56o7bCrYjZaNyZboENHQW1Ff45L3W9_OmZ5Io_aOxDS15bM4VQotSnkVBPrcdeY1mPMym0ePfZRn64s9fgvAYc8x_ncYQO9g1Dzo_WYfnTiLKnHJW7lG5Abay0JNHtz7gUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=Jq6uBC3SvmxgZju6rghMqnydEHnMOeRD1oi5rWuaXeM5GLHapnDaWGNWuovqW-Z5PP-ILHKOgO5RlziAEORMVJ179bEuW10MTEulRzl-zVrRWHVY_eFyh8yQ5bhhzosFpU64_1Oje878fhOVCBdritoV9HrSmsPVSIOqPJ7Qdlhai_EewYH339WHBAK_83h_GCzYvUC3Zd1O0F_d5iYFBglXprMykq3FKMEUZxo8Trt_WYh-zYAwuQtaBzggqHiNV4GJcjnayyQL4d1Dg4hNjzOkhW0JjUz3Q_Wi1zKqFeIGmhvHgr4-prBNdhXveodQRKEefY15b-pKQvgih9O17raeWy8AkMty7iAQ0C-e8Ye6aHbCStEXQFXSEKC_aC9AX34Rhc54tZOFmURcmIpTbXZqlXd3C6--aHsb_LNrqmWzfdn4bEs2esPhoqzRUBlqLuJRVQOpOw6Y2OJWZE6IvSogmTJjYwCSVeFcSjp0zH-7IBPpRecxLrRjnrQt6VRGF24x7udX1WgxhSKg62XLc6GKEpTNm83CUzrZu41R56o7bCrYjZaNyZboENHQW1Ff45L3W9_OmZ5Io_aOxDS15bM4VQotSnkVBPrcdeY1mPMym0ePfZRn64s9fgvAYc8x_ncYQO9g1Dzo_WYfnTiLKnHJW7lG5Abay0JNHtz7gUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duPlZLjDlGNbYopQQclXRjH-bkcAS_3XvZw6ZGy5nkbtf5wSO1ARjxRaUjfiemwYyz4E0So4yMfFZW_djQU83-eqFJs3Zzv0TVq78ZEinLb8E1bawMiTBW9-4q3Y6EUYT7DzCNYmj3f6kI-aOMJiNvlFPIGTCUMky5MqKXjHE77HMuuRHHkFuDwQ1c9A7GYr3Ins5UqsmsLfJlagwLxZD8askrarAoqC8zTgo95gd7B-e3CwxG9wxc8OFDzpqz21gPqDo6jb9KLiJd5BcenMlZaF-4jzxNzKAdcGzuzvtU-y8jkbxosElQ1ukFAWRTWDBFvDk4Fr8oQLauND4mYLjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=Rm3k-bipco3e_xedTLoZrvC8ZJ81sCoCnFloZoicT7lk8rsKW7nZUIAMrmgLm__h9tDV0jiLQqBaUAqMvpCqHUeJMfIUQAODEhr6UCK5boQeMIYrU_0zLmSILE57Oo0bCzHEGgmc0g9O3ewRAwixr4csmHLngc_fZpMv6NEeYicl4DVNkos9WuCazhRVgn0l0dcr94GkLqfiNAUbAlCdd8dJfEoG_PpOtK32bVur_oLzneVgd8pMGs3wL6owy8JVc4xca8K2pIys5mFyyVfV1mJ6LCFV_tIp5mDeoTO6H-hH2vjMvnsnVU-IZYObNV3-Uxs8Ezm1od6zBF3ciUF9DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=Rm3k-bipco3e_xedTLoZrvC8ZJ81sCoCnFloZoicT7lk8rsKW7nZUIAMrmgLm__h9tDV0jiLQqBaUAqMvpCqHUeJMfIUQAODEhr6UCK5boQeMIYrU_0zLmSILE57Oo0bCzHEGgmc0g9O3ewRAwixr4csmHLngc_fZpMv6NEeYicl4DVNkos9WuCazhRVgn0l0dcr94GkLqfiNAUbAlCdd8dJfEoG_PpOtK32bVur_oLzneVgd8pMGs3wL6owy8JVc4xca8K2pIys5mFyyVfV1mJ6LCFV_tIp5mDeoTO6H-hH2vjMvnsnVU-IZYObNV3-Uxs8Ezm1od6zBF3ciUF9DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM_Tl5TfgHNjUgmubIXXYGN5hmruscun6AnKGzjtJn7f9dTMtHbrVaND6dGR2ocEx5NX3qq6AEW1_8tziEboKb9OQ8fZte6ve0QStDki5sYDBuZykmTmA5G-4EGaW7ejIB7ItF4zRgHvu-Yn6s7tqHKS7oCGhUzN_ceI5XgOSs0ej1TVhzZ48U98oNEd2t0uG0sZ7dlTumhwZXjaG3E8z4F0Cc9RYC0B2_wUk9vNLcxyfZsIwRFUGJ8_pLoWuEPVTLyJTQcVda79L0kl8UmkogmY0NfbjiWTYlisllL8Vm-PugM0CrQqzHwexxBlNFfXjjoX2UNcJ4-hOXC2dd99xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve6KLlFOf81KZSpgaU2Wua8F02EjMYDGtMTkeJXwQR_IVCrqka8Kw6BKPaOeOBPom0u2rmyHwHdQoaqenm8UsII2mPBYHxbDtbaXohOEONqe5wW5jY-Ai0lAURDarrYghTaebTdsQUlh19Rp8yGccJ6I-TZ8ab96NkWAjtrA_sTdaHsS8Pj1zV9Rc4m_VVoO8msGJFW5dVRdFlpZlSt00Q2WKRYpF3B2F8Zx_yCFDxNCwEjpGrQujH0jPPx9bek3l5vEd-s5jCEHnE1IG2WnVGVPXh3qB1e9gTKi8mo_l8g4bktGV3FRRjlt47o10pAqiuN5ATaF88NDZ8s-aD98SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L14dRhsy_LZBVH_8PNqlWm9wZlktwc4siZXenfHgvyH_0rDb7dqw-2Jy2DOQgBu8Hy-LQXK0uGJCenCYR8HT6s_jJ_2n2zceqoObXzB3_5P2KwJVsFyubwC_88WnRGW1S7wGAAZJ6AcuxwUL8NdEFUusolnAYVkkSFPZASBMv0WuJTZryEM2Ob5STu1MLnkWcu78g22QN-FJcDn1Id7ooDQTAUc1QQBIMzmsi1L1KQXRtdR3MWIG17amgejICHcM8C5gMKGW9EJsTs2xnjkBapE_vBXpfPeXWlbJZCez4nt2N5kQfv9tvUkM5fzhyFC7arpcO_D7551jnF8Ic67Mvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubdS8NoYL0p0oC-qnQn1iGKPLunBnOlAVGOh8zJ2pb9PXyey2TmyF6y4F_ldZvFV6I3TaI5qjvLOGodnasz85eJ5z1kOi-8UtCi7zrdpBg6kB3pJW_RjhlqmxlwmqQyIWNbNG4W5wYj7LjCUajS1Wmj539nK6YqRTSpcuBEtX31wtEaKojfmtj2CR1VpKvGE2FhEk_yLWA9PM1YpRfB0bzKD9Jk6LbsV-pGlmRsxLFhb5iw1dtj7mfqv7WPoPvr0Nf2JM6jInybS4ohS2WPdxcbbOU-tWiZMLW-d-q-pwKP0A-aGFHje6Fhfna3aG-x33lALgOj-Zfp0X-8k1N_5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0WvPY1e77Rj5ykJWEP940rSENFQKUcCi64WluIVm6B-8CpzYZt-yKJ4WSjZ-uz2e08axEF00uO2euCwgNRhuVRFzE9Wwj_ijGhoplK4FI-YBaVgUxHVBPECUPhhuIRPSL1c-5nxTDWhKsWagQWzBDBbmW2Jb5Q7eZgK-VVxNk4MsSifGwTpJOWJPWsRvk0kDgfvnZRuIZF4Tb03w5wt_uNI_I5GtsFlp7Jd5NsEKDtSy9ftdfMXBs6wOyfMK2OECx_A3C5oGKfXJ2lrUnvUHUUDnasPfPgUZfb3S1_V5MoqRV0lfpBoGqAmjUvzoq9KZ_2bingPeku1Cvyk-uTthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYnJ0aTLjPa995k7zbiTXi7JZVClFsVRWBR7wKXON9_YnJU646zzMFRRKpWDzpIW9ZSG83rnH08qilKs5-wfafdwWxrRxSU3WNUavptqCwxurtq9uiev5CvZL5qYqC9IRxMRsGQHL8jFfZutvjvbLIFzlIGMrssVeDdbSF5u7HgOaKxZ9Qa4h5rWmaToIuPu0rs4p83G5qPs46W7aHAne4RK6Wceb73rGK7cgx88i5t2SF7A7rw1GRpRmUl0EMPyRZZ5gB8jwREuOxEf_rGVr0DEZHoadWSR6chT2yuUwMycjILPJSwL1noI2WxM-rar8XCvp2FK6GzY-_RfTyh-lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cv9JBSngqGFshPupbacvYzN14TPuy0K4e1HPEDtP52F0lFsAQ_qQFoG1Kxezv6QAOppr0UT3IUyHsRxGdQuK8yXw80f4HmvKhAVtzOx2IfXtvXUTPNBJxl_5UuNlWRNpo5fxfSuS0HXn_YFI5mS6jmhCeysTlNgQ24GN8nsfbeCeH0ZyO3ZW-nit1SsIfs_Ilg-HvWWRrBT728llLnU9YEFQ44DaElZoLDQ-2VsguDmE7a9c2__4FXH2Pd8etYSv3aGr8kOvXQHeemQ5zcKf5mSqmgbWLOGGwv4uTUL-ZjRA7TAdDxUzh23kp8Y5Yyu6VZw9YnSptr7E9DVPfNQWCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=eQj6o6dJILPvspb6dVzdNPT1tKYLWcSEQjKYxsvPGUMFP8ILESsztqdgDrMrcK4fcVO6QihG3U2ESHx520rMsj-axiKT-2fiiA9RBQk8r8cJSn3s8XplMDwFZX3hMYHeFB5zAgOgFB42xYYCFQnB6C1GzJz3QBRa5r3YIVY2eR22QIAQatQruqLPpAEPUQHWX1np7YS_peXmqov7TUVVElvFcdpLfZ4E-r0SXAIN8mL6MoBRQOffWiS1kDCQMKe9PFnKanPKkD4XWM3Oakm1HrZ8fR2QpQVI4L1ayiR8rB__TFEvc3UKzasiR4V02eS9TjhlO_9iVzm4inb2TIN0Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=eQj6o6dJILPvspb6dVzdNPT1tKYLWcSEQjKYxsvPGUMFP8ILESsztqdgDrMrcK4fcVO6QihG3U2ESHx520rMsj-axiKT-2fiiA9RBQk8r8cJSn3s8XplMDwFZX3hMYHeFB5zAgOgFB42xYYCFQnB6C1GzJz3QBRa5r3YIVY2eR22QIAQatQruqLPpAEPUQHWX1np7YS_peXmqov7TUVVElvFcdpLfZ4E-r0SXAIN8mL6MoBRQOffWiS1kDCQMKe9PFnKanPKkD4XWM3Oakm1HrZ8fR2QpQVI4L1ayiR8rB__TFEvc3UKzasiR4V02eS9TjhlO_9iVzm4inb2TIN0Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/4989" target="_blank">📅 11:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpxMiwJv5OJnUEdH9eaOFSOoa3fEWnW94Jj3GoRqdtY4ndkHW89lRUGQwFkasNQyZZEsVdWuUoIwKYJu8JP_yTUXIm5fyZv4AbyZhfGSSv4fo4sEEFitOlBp3a5U7dahZ0Ztq_vpPdBo1nL0bERo-rxeO8ua0GkwcD8tfAcdLc8YdyQlwdX0OPA68AaJtcM9P1rL4ecqSl_TBt0i1OAyM3cOdPU_BpP6eZrQXtaC-EQ8AzOKgLvDU7iUTXP8e6a7rgrgBdAiOcQ5aS_G5Htw-QtSfHIT8VQqOFjD7BZamV93e_CpD6LyG-M3PgA7amAW5v9b7c-k9zB5HWDEp--CAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AibsDLcnPwPm4nJ0cpY3B4I0mnGuE5BGCSm5cKNtD0uFj6CKeQwKJwOsipOaLuSQ9yD_mDkdlyOn9FuX9C8tsvjt4eHyNwYMNHf6nmYq5tD_udKD5HCVfeX2DXnEa1hLgY1i8eCPQyvTeu4jzPPiQljwekEqr3e4XVft2sZLXAoemEpNqOYXoDIMAhm5OoCWp0mBgl0WWMjdiR4vwbbSJhiLSJt2ZQUzNHNCNCMcW1NTraD5XkmqLeKZpdoq6ulW4xcurAgqqV8JNSUvV7WJENWeL4-7nmtTG-u2fDgLMUfJc7u8u5xje79WNG424S2fuKWg4UivWOh5kLXsmMiqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4987" target="_blank">📅 10:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=eIfDymCfjDw2xbZyTqKQpLsXOZpJIVPaQDWjFvmG5W24gc3j7rPm_BN8eHYJi86oGDKvBoC9BAilwPrWOmQQV561w7X7VguPB9TzNf231QGF9klDrIJ1tFLyhyl3X_vAy7p9zIshgpXvHJhWisN2MZuLxxFGedP2MbfIFppOZACV9HExR5PIlVB3ok35ZY-P_fioLURhM8mqowu9m7ObJXTFbzHZm_mB6qbuSCyifRSpwhr1NdgqtG3-D3xJKx4Gy7_JfdzoO28LVNXu3BPe7QUp8vyxfsoKTTl_KE6uJIaOEljFDbvnoxdo171_KyT1HxhHr2YtmztTCu0QPuWgpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=eIfDymCfjDw2xbZyTqKQpLsXOZpJIVPaQDWjFvmG5W24gc3j7rPm_BN8eHYJi86oGDKvBoC9BAilwPrWOmQQV561w7X7VguPB9TzNf231QGF9klDrIJ1tFLyhyl3X_vAy7p9zIshgpXvHJhWisN2MZuLxxFGedP2MbfIFppOZACV9HExR5PIlVB3ok35ZY-P_fioLURhM8mqowu9m7ObJXTFbzHZm_mB6qbuSCyifRSpwhr1NdgqtG3-D3xJKx4Gy7_JfdzoO28LVNXu3BPe7QUp8vyxfsoKTTl_KE6uJIaOEljFDbvnoxdo171_KyT1HxhHr2YtmztTCu0QPuWgpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین یکتا، همون چهره‌ای است که قبل از شروع کشتار ۱۸ دیماه اومد تلویزیون و گفت خون هر کس ریخته بشه پای خودشه و بعدا گلایه نکنید!…
این همونیه که اومد حامیان رژیم رو دعوت کرد که هر شب برید توی خیابون‌ها
حالا هم در کنار تیم ملی فوتبال، در یک اجتماعی اینگونه رسوا، داره مجری‌گری میکنه و میدان ‌داری.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4986" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمملکته</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=LDBpac2LpBhE9313yla-waQ-OqPWNewcB0ujdSD8FvyeYDSJC0w_9XNvkIodCZGkeohPIoY_X6G0mbVkZMbO3thL2JYinyxtRdRWwDvUyQ0GhwwzAakCNUO-3rwwR-tsPK2l484lP0UUSSiLSe0GAYVZENhzqNk85Z_6WVRRlxR4bkVRhytdskLvzY95CDgOyxkYPDXGhkLYAsPbX8GJZmgp9lJS8OFNpuysrTtOj2MU-mQiSfV_9Sr6gKTNVXAxagptt0sH2tgt2skb6w7GrxI9t3DQil-XtmffuP-y-aXdaAZXe-ma9Ce94q9wcmslh16rpMdOJN8uEuHkl1FnKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=LDBpac2LpBhE9313yla-waQ-OqPWNewcB0ujdSD8FvyeYDSJC0w_9XNvkIodCZGkeohPIoY_X6G0mbVkZMbO3thL2JYinyxtRdRWwDvUyQ0GhwwzAakCNUO-3rwwR-tsPK2l484lP0UUSSiLSe0GAYVZENhzqNk85Z_6WVRRlxR4bkVRhytdskLvzY95CDgOyxkYPDXGhkLYAsPbX8GJZmgp9lJS8OFNpuysrTtOj2MU-mQiSfV_9Sr6gKTNVXAxagptt0sH2tgt2skb6w7GrxI9t3DQil-XtmffuP-y-aXdaAZXe-ma9Ce94q9wcmslh16rpMdOJN8uEuHkl1FnKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
