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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 10:11:43</div>
<hr>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E29o9no41s3aKqD4rRe8-p4Zx6P2ShOKUtbjeh5T-pglQhneK1X3UF02vfLJnpOi1ZmrrOB6I2f5BWyZ3qIw15taIA03kmdXlqsyhq48-XIIf6zq6JgxTAuhFf4XV7wqgI_sSN81S9zGkzx0vMLh6BB0YjH8BKoGzmGB13JuVyHe6HjxVjjeLUSwwTt_Jpp8EX63Ij1cslG5Zeu_ISGmZomr9h8EpEfVEjXnUTYPYtNmkeCuQHKowjs_T3SGmFjwZYIujXvMwCC4y0e7qxnb5DLf09AgH8IkYajwllVTZV-77OX4TM-5gqh_swtmhim7t41z33-b2gToIFrLWVkaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OC4GxLukLytdnRYhqriDygh2eZGGTnBOvkUD-YcvFLI9RcsQ6SZ56rCI-JUKBoCZ5U0liPXmeCLVY9N6lQgL9gN1kgOdYfI0XtLwMHkN-oO6BqoaUuR1mp_wIhTgvbEsnc4__-19_mrPMqzWYVA1lEevbYznq4j2BXHMi4C8Bu9uMnORuZ9R81gBB54sONhSQh8wbfFITVP8NDSGRkZIumzV9SvQZ8PKdoSHacPBpbF9cm64zXDbLNkDuKrLkxAt4fFquhSec-ZRHPbDwX4dPfzptyvR8Ros0sHRvW27xWud1QRcduoDCfXaa8fl4uIY4uLpLOGOTo8B8ks0nF5geQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COa_DSpBnwP3Oes85QVPsMo3KtRfciq14s2uMiU5ZsUF8j_9Q8U6zSuT7rbu9krRrx1K2kR0kf6i_kT_xskdHduQ_6a5U6f_W9JytZxe6WnT57AC8oxpwGYcO2IDp4CRYgHvav46bavNn326zHjZv8TnsCwLLzQRQgJMEPUSq9SpnHByWSfVUybrcDj-h6IdXLVZ1ftYwpJk4_8CmFtwiRzAeEZKAXubMVcUJZRbdZwItR4g--KPKObZS9a_659uXb3cgWI6D73KHB2Xl9hUUuDVtF307I-s5ptYJlgm50ddqCEsI7kx5AzsFAky-WTro7IYDNK4X62YWNrVNnm_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3NsPUbdrLJqzw0v9b5gQPrAEVXTCYX2WARHi6xepxBx7vOlxbOT4tgKfoBIaCcZfP6roIipr1Uj8VhDubXyAE6BNJ6WXciqnRdWIxgQnaXEiyPzA9wVqTCHP1tnHASs391r8ON-CYsptq90G4oRNBDq65IvHkkQq5iB8WqvI3uOZ4sYZQ9kSp69IEhjZnmEmmtEGLDVQM-cby8JU_egCe4BMQnWOu8Dore4PoUifNF1mnvA_AK36nSOZhTHq2Dh4uzUj6PODsETdw1tGUQFg3pBn9pVF_PkQd9l4lZjYyPkGtMSnXu7OSnwi_12F9wI2BKALRwZoN0rTCvsxiBZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8fuiwl9SurRB_3zT4JZT56EJvvFoFy3q9ChJf1Pu__vtXqs05Esp1HZxrWkuT1j2wZZJfGsoo6YoBeFdBINpAZbyfhY3q7ZxeMzs3JYRDtgQ8mXewdgUDSVgGvxKqCkQ4u4Na1B9xArpK63m0BswcwavfMLyh4AFdQQ24LUL6Jjcf9TMJ-Wz51tSTztXUfHsFiY1-Y2DEsNxU4SZetF9D6nX4gWLes_fVclwDfCyMUoZce-DY6nYsX6rZF1Tb-p-vQ3iaCqeAEiNgjIaw7raprW4fce_bzDp499DTJREtJzPKXooBrjrYvaee2B-eci79ZJ_8LQQ_ZcJmFXajLHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=DfXrmMP3BgSvyS_MtZp2hG4puF1irqhOgl3i0gTA3_H9BxhnU-uSYrcy0iuFDJS9PaJfMpAn5xUHI9ke9cEAOLvtlwEw0zL3hsIgRKZnlESd3UcDJYl_FFGZKrNtIjVWOwK_piI7ZmxZlgDbJjexDl1BQdB_2EW_DmYmd0qzYpJFkecL7TKjWfbGClsDI9KdoZe5aKsxBqRPGdIwDJjKjcjWrCuuqBmDmjEhSi6e5SLTNBnNJltzjs-cBw9KHW9S6QAvgXtuA0SJYjGCmmIeCyJ1kYY_6q8UCfOR4IvNl7jJXGW5IfxZSVW3zC40sgOHPTRVLpmZsDvvu2PIC6ItyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=DfXrmMP3BgSvyS_MtZp2hG4puF1irqhOgl3i0gTA3_H9BxhnU-uSYrcy0iuFDJS9PaJfMpAn5xUHI9ke9cEAOLvtlwEw0zL3hsIgRKZnlESd3UcDJYl_FFGZKrNtIjVWOwK_piI7ZmxZlgDbJjexDl1BQdB_2EW_DmYmd0qzYpJFkecL7TKjWfbGClsDI9KdoZe5aKsxBqRPGdIwDJjKjcjWrCuuqBmDmjEhSi6e5SLTNBnNJltzjs-cBw9KHW9S6QAvgXtuA0SJYjGCmmIeCyJ1kYY_6q8UCfOR4IvNl7jJXGW5IfxZSVW3zC40sgOHPTRVLpmZsDvvu2PIC6ItyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urh-aH7X0qDLo_wPPHCRU2TlvQsGPDfz6YoEuBL1VmDz7_RWp1istOt4v8Oen0deBUFBawHJJNouRVPjlV1AOfJC7ht320KiwI51s7tz1vmXn8tGrR2zJG5tnO0lK8tcKhnmVf17mimrfL-BjogmoR7-qqL_QSod7J8PVfNo5C0vtuxG21QZ_xWGymPn7mTVDRFa0shFxv7p5WIa-OGkgtZDSnquU_sdiKQu0oS1qLMVEJ60Rn7SkevVzE91qHhmYdO7hM_tIV6x6hLxgL8-D7IxtwY6-2ONuEiJd-jOpwS96W6n-0aYe5igyd9QGMD66H5Rxq05rD8zSHB9gVzWlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=nmniCmzVZT1fBZscaulNG39N6zsp9MVeKCezMswxPZcc0yDaRzqoR0GynlP5KMoFgFfZtxma0McA2sdS7vidwiisAcoTlj9Hc_Cqn2DSAqbfP809VEx-cqnewAoqobEwIA4n8Z1jGzSiQe2QnyHevIPyCOzzg1x2AVjcn8knCxnhfx5mAr0EcE9IEtROOPSPAI-3axvgvYvQc_0b_8P9uNg1sxWiYxqfYfQycLR3pV2kInw5bgVekkVSG-JVPcjpwLWKZNHHcXYkj-g75_7Qcs14KUlXBZ6sVSZYP7px4EIrI6xkPjbE8s9NiKVnUhgza85dXkdeKB87U2Npl0ywaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=nmniCmzVZT1fBZscaulNG39N6zsp9MVeKCezMswxPZcc0yDaRzqoR0GynlP5KMoFgFfZtxma0McA2sdS7vidwiisAcoTlj9Hc_Cqn2DSAqbfP809VEx-cqnewAoqobEwIA4n8Z1jGzSiQe2QnyHevIPyCOzzg1x2AVjcn8knCxnhfx5mAr0EcE9IEtROOPSPAI-3axvgvYvQc_0b_8P9uNg1sxWiYxqfYfQycLR3pV2kInw5bgVekkVSG-JVPcjpwLWKZNHHcXYkj-g75_7Qcs14KUlXBZ6sVSZYP7px4EIrI6xkPjbE8s9NiKVnUhgza85dXkdeKB87U2Npl0ywaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=S55VTpEpQuMBqqJI7ylsDfY88PIYgA1ujMaf7hG9aalobfB_bgq00iJXt_0UHsDGJlT4MQVfBgQFHfdwW3ZJc_rXk62jTZ4KVFnz8XbVS4ldk4fq5tgorF-zt_Zw_kw_B8Sfo74wkTyt5jhNCWmEoyxzXQSWYXuGXz8iXdCCZSpGUEx6jTEBO23w_1Fdu4M0B_DDycDdg3OqYMjYhuR1ij9mFOi7CrNS48fkf-di9_6zMYgRCamxpRdFAkGQ_sesF1EOoI1Da18pPHxi4yT0Ozy9Z5HebrIkQSwYsZq9MzwZ9Xd9fz7KA5I8LwJNsXRKxZVrbpUDbsADY1WmP3Zw_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=S55VTpEpQuMBqqJI7ylsDfY88PIYgA1ujMaf7hG9aalobfB_bgq00iJXt_0UHsDGJlT4MQVfBgQFHfdwW3ZJc_rXk62jTZ4KVFnz8XbVS4ldk4fq5tgorF-zt_Zw_kw_B8Sfo74wkTyt5jhNCWmEoyxzXQSWYXuGXz8iXdCCZSpGUEx6jTEBO23w_1Fdu4M0B_DDycDdg3OqYMjYhuR1ij9mFOi7CrNS48fkf-di9_6zMYgRCamxpRdFAkGQ_sesF1EOoI1Da18pPHxi4yT0Ozy9Z5HebrIkQSwYsZq9MzwZ9Xd9fz7KA5I8LwJNsXRKxZVrbpUDbsADY1WmP3Zw_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0CuHFwYpqzNk9KzMBfVvVm31NkGStnMqMKRp9usgue42IZD086gE_hb3NkmqeyvH3CIcmUS-t65r9ueOP2J44ekRG2s5AyoGrIy5aY5jI3pFwkGE2GxuGqxONrwc9G0RvtOFBN15fmyiRW9uSoSZvAcIPDcHDtbtqgiomRgew-tez1JJS8V2hjbP_f_ZOO3im_LTcvM7FZ9VHhpPhxcN6yv_fIRQSOxDs2Mwoh6bqOiPStzkBVz2d3oTIT2_-3gO1jAaNDN6_rMk9Gomj1vIXa1o9SQsVTk9_JVYVEZduuWdr26xsnLN9j91yJ1Mb_4klDnqqV38j0S4feoshzJJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrRqoWOxn9LSTnN6Zyvzo9HlP2wIuZv9qt6MeZ2q4MmdW7vP787oFO4K_URUFq_D6T2RF2RASL9pFa5Ldl9vnHgGDqPkCCDW5w4G3GvXx5duq5dESSLkrWabOq_zHwpKidVu_1-e7SMyZHWLcLQEaHXbygJsrL-CcF1iy33cr8EzG9x3nrt1XFmM8wbTuGpHxCZqA4n1Gwg04X_Sp2lcUhOS2okJwSu77opRrw7ZnURBLrEC7Cecc35e6uCDsyKe4px0wMeeAPStn3__E4Wt3fOxdJx4911c6qBFuMOH6i43actXEFrGIPjQzMb0o03kmlqtt16mWAuXIiZwOkGb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C073jBLaNrdZo5PWtSOmwX3qgO0b-abQsE8L4AD_zKw_S-4Seis0fPBQrTksQHcKb7oIbMLhorlQtfIOibPK5KgE0C_SCHIBwN-PrB1PMw2unpWxS3j4BHDXqPt6qkN-dB5NAlmdt2gVX46VyPV38bjHk2ZF9MGGoCHy-Z3ybzqYnHO_6uivoz4um5fG_Dv7dVw69G4t0cDAH87wnuPwZWoL7wTYUDZWV3cRuvhuwcrr5OjuoPLnJwNH856AZelXVi2Y_g98pMieRn534hL8QX1FfWl_ZimaDK1jLEpNxxV2iCMTZ3_zGS9QTYeOEp0dOEtqaVeSv5aRiZEs7N141w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Um6MzQndTDcPFtJ_7_JBK4CFXPu7kEuFaWph-QP-RdCXoLjNwHEa4--vZuMEzmmqiUZCRzMDMI55NPZ2xVHLgDn3IhYKtRWZ9NjnEzewwnm4aUetpSUFce9bA1Tqbvv3iXBDgZKCCKajlKJ7swFQgPm5Chd5LLuZiBoSbaBd34qlqvUQHCFgXkbWMxlKHj2B4P6eqik2qQvq-hzTtXImLPfDWyWpE12XqnaFsQIr7NPW4CMOUFYhAE_5hH3-dtMAWsGaJ3b5fCua6GxVOtvMEhF281IPQqJsUywQm953uB3n6l8fevlandZqxRObOMX0R1TcvdiT65K6fpX8Ceq48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/es0WHjw7KVOwLS6bBgb3SeKm9j8hwP172T4IkKoDoB_CFBo_UQQ3g6a4W0HXRTWZGIGFJ8cMZsrEkFKKNytsn8kbdfQ6FHF5omI7_bI7IVNN2I1itUJperyixA4WZ_YH19l-Sh-Na_cSIdAVDJYDBkvcvkP2_rmXjvG9Ra59s_JQB5MJTdmdtjD_q324M-dQNB9h3vM-orwWb9IWO26VYbDWUszpsOEVu1ngZFsKT46fUEhdANAuwZWq4_IbqMITKe9kXUoQ7CRwEk0IK_-L6qykIiGOwK3tjBGqggBgfqLAfD6iz0YUOPfjbpVO0Uk2d02YHcwtAr1A1fvinkkV-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3NRX66bajE2A6sCjNzEB1YJxtYIjxLyWreqZfb00LkLZZvykBkq2R6fLz1aT4x8eQ3hsmLbjYLWiazHx4YrDy7ToLdc7K-bc_xtpM-KwVHfgK098JtwFKfabONBpGFluDYpJrBYevmRWhNbTyoQXYmTdgtcJV5p-IWwkNiTQ4A7ttqk1qArQJW19obYHfs5T77qKE0zzobjjbycB2M-lndmA31DvHT6G7DnjMyH_NMf4FfaBAgT6oA19PXTBF-lqjXVehFpkUZ15l5_e5U6IzIjhIFSFrhmucLPiutOkE4X1ZJS-LCcq5i_y-mCc9AbaOJo2Wks2l0ZCoV_f64loQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SInCdffEPolbx1YdIBuTTYtvGdaG4xRvhfeJAIrE2Y0S7UkBe6pYeE3LAH9YKdRAOrf_XwGYvXniCHrUx3uE4qUM_FT_PsYHdB65xdbcnOl7XzCIuRByji81fzRslYo0u1Z8zX1n-s_a6ww2SdmkkznQEGazBquxftVXWAaepHU-LAM1-8L2763ywFpi8hB4A_TDxfVr-GMJF39Ii5qPqdt6IiYAhvKKvQAuxOtFc5TsK9ZkJWMfb-mWyGXwLMIbs97ZRZzMCBbNM7zlfOxcv6DY14OsBNIWjvBbJJSb56TqcK9H1beygXJ4mMwxdghWW5ikWT7C90NGlUAaxrRtUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I738WLoRyWd3yqrF6e3HG_ou5EMoXGKjfQUdgckmFcd8yGh58Zcjp8S8CCAWudSuGRuvJWMTShQEo-Z47jAGuIEsV7yY72Ts0h98g0QUjwdDp6F-4a8wTmDKfLKk_TVqo1vl5fgI88uCRbP8RdFmww4EzfaMuWE9BUx4nEnsBc_g24oNJNeUW6WGQgG3YWvS8smzlQz_pzX577IU_f6w_cDAlJkqJpZLd-XL2fuZASxLTAB0AMX_x6Gl3i0LDLZyXgmmF0rjUEVeY3MHeinBNY8Oq_xm8tME0XSmxwF50XOCAudq91mb_T-zy1skFcC333v26x8d8ZP9xq8-DrpziQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=jc-mq5UedwWUXhq3x1PUqilek-8ykL68CAJLCzTvVAJ6yyJ_aGaKXf5HgEk7xNSJXqcxcW-ZBBk_GK59XbF-2LZU-dr2AY95Mw5j8jpoO7ImJsa_Mvl7ImWAmG4Qwy1KVOacA2Qs_DO0XGE6JFNmGz1Z9s9pB7-4AQHbBBjQbG1CNiZapDoAITI6GNooDBMrVfzSMdsJIF70PNY-6LDwAF5ZZb4lMv9dyucaw3Pu-bkubqHoI5lP12BpVCEJ7J_1HphKI0KshNqbDL45ZPBWxjic-phP45Ii0-49BZH6TdRidyaJFHHazzMDja_wkw5FM9ypFqUui2BV4n5PmKTsmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=jc-mq5UedwWUXhq3x1PUqilek-8ykL68CAJLCzTvVAJ6yyJ_aGaKXf5HgEk7xNSJXqcxcW-ZBBk_GK59XbF-2LZU-dr2AY95Mw5j8jpoO7ImJsa_Mvl7ImWAmG4Qwy1KVOacA2Qs_DO0XGE6JFNmGz1Z9s9pB7-4AQHbBBjQbG1CNiZapDoAITI6GNooDBMrVfzSMdsJIF70PNY-6LDwAF5ZZb4lMv9dyucaw3Pu-bkubqHoI5lP12BpVCEJ7J_1HphKI0KshNqbDL45ZPBWxjic-phP45Ii0-49BZH6TdRidyaJFHHazzMDja_wkw5FM9ypFqUui2BV4n5PmKTsmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ME6Sj4Q2y253R2mcuPR8jl7JibQycPmYBfMqNi4Aypx1e6PPXZTRN315j_8INwjJj_63HjG-AJhGE6apJmIv03std9h1kEQoAIKYDxKaAEP6EavHRHnzHQTZj9VoT8NkwT9dBE42tVCDyHusChwrYBxm5bFMgUSDfufQrCIvUYb6xQ1SdQQd5td-KGFYeqICn8A4U62oTJbnZxq7izpnwBRxRg-U-CnlZlWQ4fOS_uqLTkOOJETD8Wr2IIbbRqf8NZuSn50wZK9NhyG1ZepW7bsbYZLLDmPTHhdBdTA6UBjMDZahH_yr_M6PDdIR8ARt_fiQgTAHvPjQSMnl59xAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyjs8F_aa-nXslN3jtUJLObmpVkuDfp1vb5ewmkWUICYD7MKoUoeMNX9oHP2ZhHXkuSRSXHxie7FNOY-OtymXbjDjID1HEZFUFmlsCouAhAPubgJkrX_dzPdvQsO16b-Oz3Oa9Muqtzbwyl73VR986E3mJV9cezDJbqKUe7-Hf4EGmOclh3VNhyabo34D_X1NGZc1yZ1jD5nA5zlRx1oZXbS9bLpMfOMGlnLxo3CEr4k5d0L5vuDRWRRV6yo45m-60TMDt29-tybiMr2UK8E6nAIvkzlh40_Fpe-NBQjPy_GIrd5-VoG_4OMUpoWd6eSUi1JPgKoRgH3EONoiF0KOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5zT7QXT7cK-VWpBcyKe2MHKsS5DNa0Kp4Z7cflUSKdllzawdLJZw20SMHbeXEkw6AZV4GDDAijBl_ESLYeGqVqd_MZn24sKKc7H6-FgmA2jYdkZ7hPu_pASA8fF7nG1YXA1snLKU5qbpZs8Xqou53a--EEOH042yxXD00wf7qlr3X3FnzlTmvXpZuw8yOL--_WNqp7L9VHhWh2kDf0r_aAtWh5oU0y3spNGk0yc8ws4i01GN6EKh1XCCxffhcgwiSFM7-g07uhGgeusQo7KVKhfG3L1vSgEKNin_DizOnNyZMAo1cBPnDhQsVEAVngMwcbMkjqflh2QpbSW4N-fNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuX01PmgDAF3dsuB7KngK8NwFMPaMx9gA9ZLFQI5JIRNeVYRDDf2RypbULjQyx7Z9V1mafwUcTnXMs1yfLGu-sX9haDpz_cSFq-M6ho__VSnxM32EamvHuaqfeYtu1bHv7XBX_u1oNk1Dd4lV4kyYSRDcC-HOiLpp4NHxl0j-PQRw7RJ9erti3sqEd4mg1iqpe2zvc7o8QOYzMfjY6fOXNNGrUwplIYsIWNrnC3InC74oguoEh0ajO7IxKOeAZnUeBat8FBp9bByedcG6_cdKa00havCnVUNOMgysXZMCFUqa5271M16XctHrgV9AEoix7pUpL8r5yD-dLUELB3Q5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=F6hgPJO4K49IH3Akyp1nC8sRsfs-bXI9DtdIsjjPsWC27eWRNhHwZhq8EuO6pBGscs2IJO6fHFD4XIJybx20MtHPwt2fc-s15evhhaOkLhcf2IWnIqj_Py1YLT6bd7XzEyy92mXduUCIaGVDANlJSAmjbiIi-wB1WMo11IM3YFK1uAwyGFkLgZf4Ar01NtfhGYmFYy2sD9SDLch56uJEjllGDTCrdYqKA-9Rk19fo8uCHCLs3pE5mwj3_aTBfEHySgwOAKhT-BYXSAEy6USvyrSuS6H1alox-Bmbd9A5xLuD5oO-8UjZfudIYbCuimgX73HEmjjhERTdQfCtS2scNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=F6hgPJO4K49IH3Akyp1nC8sRsfs-bXI9DtdIsjjPsWC27eWRNhHwZhq8EuO6pBGscs2IJO6fHFD4XIJybx20MtHPwt2fc-s15evhhaOkLhcf2IWnIqj_Py1YLT6bd7XzEyy92mXduUCIaGVDANlJSAmjbiIi-wB1WMo11IM3YFK1uAwyGFkLgZf4Ar01NtfhGYmFYy2sD9SDLch56uJEjllGDTCrdYqKA-9Rk19fo8uCHCLs3pE5mwj3_aTBfEHySgwOAKhT-BYXSAEy6USvyrSuS6H1alox-Bmbd9A5xLuD5oO-8UjZfudIYbCuimgX73HEmjjhERTdQfCtS2scNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=jQCvTyqyo3pTmEfRqqfDLEQ0mBse-fuk5m-JUoqY5zZ7SbE6Xp2vJCh8mScrxUh1Jq4FqzcRKYP3uXWZrFyIr7WQKGHVrVraZaviFQw6KVIz-kbC9UYmSRiX3zUjiL8Oc_sAvXwro87uVf8D7UmAtK3H-aa9ipThS3tgYK2X6YhaOCILv_DrXdY9E_b7vryr6D3Tm8FRXp_eKpfR6iH5mJRynZ94Oca98W6gUp5c9MIAfWpEiYG4C-fE8_Cc9ZZcd-ieRri1BdWryVopf3Hp0FNcgE2XyMGT9LQ-BTU5l1aCSf515sbeOD01PVDCBdIupx2-3jURZotShmiIs4IPBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=jQCvTyqyo3pTmEfRqqfDLEQ0mBse-fuk5m-JUoqY5zZ7SbE6Xp2vJCh8mScrxUh1Jq4FqzcRKYP3uXWZrFyIr7WQKGHVrVraZaviFQw6KVIz-kbC9UYmSRiX3zUjiL8Oc_sAvXwro87uVf8D7UmAtK3H-aa9ipThS3tgYK2X6YhaOCILv_DrXdY9E_b7vryr6D3Tm8FRXp_eKpfR6iH5mJRynZ94Oca98W6gUp5c9MIAfWpEiYG4C-fE8_Cc9ZZcd-ieRri1BdWryVopf3Hp0FNcgE2XyMGT9LQ-BTU5l1aCSf515sbeOD01PVDCBdIupx2-3jURZotShmiIs4IPBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏رویترز: پاکستان [کشور میانجی‌گر میان ایران و آمریکا]  در چارچوب پیمان دفاعی، یک اسکادران جنگنده، ۸۰۰۰ نیرو و سامانه پدافند هوایی به عربستان سعودی اعزام کرده است!
سامانه پدافند هوایی برای مقابله با موشک‌های جمهوری اسلامی است لابد!
پیش از این
مصر هم یک اسکادران جنگنده و خلبان در امارات
مستقر کرده بود و به ایران هشدار داره بود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bp6ClBnD0K9q6HcECw7UeyBawvAPcSzQvaaNz7nHgQuvSF9okNvU32XAT5dKPgD0f8y-Ib-Ew2z0h6epTt2vYTsYkt4nM6bBKChVi45qqGXpJlQRVuGEN1JHcu5Eh5peQ1Tgc84tDkJC7e9DSOGX4I9swe07spfPxot9dfolmPDUoqQxiWtI6shMeQZU5k7LEb6KtigGb2SRpb0xHAGP6-Sj4ENW0DT4uoHXbgSh8eFmee78ubiXNhTZ_ofnwqoxEKg5bFwYc1WoZTH1orqxiyvMLGAPyvevBuoiHPrSoNDp_Kbck6o_VeCDcPAyOCEVqMD7Fc1ia9grWBEhxor9xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpYrMh4j_c1zefnkS1D9n9ykHGItt4hWSrCItjwiy0nkoViiTmJar3YbMZrA92blnfD7CXDU7lZAcGvZ3Vkp1UliFSZQzA-OY2FDneaevw5t0Jrac6dDTPLokkfdTXDhYFN17OZ-fBuMp99Hp6y31SNYlNCT7vV3-zbTYAxZtNQ7YHQ9lywO4evIJj7mTn3oXs5vHtuxWZKIsP-4xl70o4J_AXtv-YqgqAL-ersNXES9WT6WDYAfczjGFwOWqIYM4b0GsAgIBQX7zncMmlMAQ61JvWxhqHvs-xlTN_mzHqIu6a6KDgsEaJeHuggpeRFTn1HAgO8xoVLmjaNCNo7tRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AuBCisShCIo-F9HlvbWgeA65jrD7k0iryI-U-pC5bgxuCiH-h060MAPCHWFnm5ZdS8hFLWCzaOvnN0HkBW-AV6jCHp354e8lS5NFSMHYbFRJlPsToM9xQisC7X6D4mHd105gTBRi8f2pmItLNtiVeNrd6Wg3nLhZUBpDucVFgFrJx-W2ibp0sQQ4tsUHhVdrzTnKWPkQBCPhhUYSr6DiBRN5vK7QgFRaXadyjJfKyE-4myyzZXiMMrETtVLsxZMvH1BxX8yTiQAKx4VHbAL7S0mnMhmEGWI0mKBru1_N10xfdzX084kw1VSIp44bRstOcTwYgCaD4nAfcc4numfL7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-y0ZOd2C2Z29s24X90DxSNvFIEHCzXGvY3BivQlU8ZKvFvzEBF0ZcIgmhlDB8YD1SxIm96sVnKwu2XIMJrYR7iUswyw6UlyvqZisOYPgi6y3j5bH_Wj6_1cQMNab4o41C9Lb9UYRDFXe8cXDWIJ9ZqoL-HSohbADc1FOTnuI0vwQlb1FICT0qqWP9uXV6SUGTB8Ncje2pXg59B3zY980cFkKndz7bLJz0KnlnL_Pvt-KCJz--WaB-izAhHAJEI0WSMzYejpvtejJrPN4pK5SO5dbOqAsD2pEHH0NiOrXqm4MtqGfvn81Axhm7AUlgMr6gGobNKXs_jb7gHgp9hMcw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=IFH8N0oPg_UtF6nehvBob-XbB2__pkLEDqVoggaGCAK60rlsg2L7aMR0uLhzwxU4yWqieHnpOAoFkaFVQemQMfpuX90L6Jl4Mi2QnIPYGjp82PSd8tD1k07-GRpIy6_Nc76z_asuSV0FiM-PvXraLR3gf6CFXZJ_4Y-m5RktPCRUlEqRXE3NhF67i0-o2eek26sHQdzFm-v40HQmL1xrWxU2MXfZWZCiUZeSNvAGJAXtDBWpKayYG4GgROjgIlR6RGYeKk3ry7dqmRpkGg6fHRHJvuW3pWtZHT5EUyndKEhakGbNP73wxHobstrGrXsie0r_YqFLj80PAP3vVPFymA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=IFH8N0oPg_UtF6nehvBob-XbB2__pkLEDqVoggaGCAK60rlsg2L7aMR0uLhzwxU4yWqieHnpOAoFkaFVQemQMfpuX90L6Jl4Mi2QnIPYGjp82PSd8tD1k07-GRpIy6_Nc76z_asuSV0FiM-PvXraLR3gf6CFXZJ_4Y-m5RktPCRUlEqRXE3NhF67i0-o2eek26sHQdzFm-v40HQmL1xrWxU2MXfZWZCiUZeSNvAGJAXtDBWpKayYG4GgROjgIlR6RGYeKk3ry7dqmRpkGg6fHRHJvuW3pWtZHT5EUyndKEhakGbNP73wxHobstrGrXsie0r_YqFLj80PAP3vVPFymA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=k3fu9VegP8rLh7Y-jfG2Wd8FNtc93dYRPi33wbfp_tKvmSpiK8EK1tq71imm3JflbFmmx1Jg5fMMQYgdlGISFpaxqzF4s4K_WItCq6K5Yq4s-pmPWy7-cDHfR5LdG-cEDpzih69-aafrU0pXF6WhX3KVix1zkOtLDZyGA_BxW1UjXPHZEUvPKpJwyKKAxIupXRfzc_HQ1LvIgwdIuLJOL7-lzpNlFgMNLF6UI0vRCWNmJJKkFu6J3_jfKNHXqjldHKUKEHq6LHIj8vHsUgXONAVN7D05R51rJ-a_KwdTDtd32ATFU-aZtcPFsO0FPcjjFr7vfq7PmSX3vsTfGzVkcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=k3fu9VegP8rLh7Y-jfG2Wd8FNtc93dYRPi33wbfp_tKvmSpiK8EK1tq71imm3JflbFmmx1Jg5fMMQYgdlGISFpaxqzF4s4K_WItCq6K5Yq4s-pmPWy7-cDHfR5LdG-cEDpzih69-aafrU0pXF6WhX3KVix1zkOtLDZyGA_BxW1UjXPHZEUvPKpJwyKKAxIupXRfzc_HQ1LvIgwdIuLJOL7-lzpNlFgMNLF6UI0vRCWNmJJKkFu6J3_jfKNHXqjldHKUKEHq6LHIj8vHsUgXONAVN7D05R51rJ-a_KwdTDtd32ATFU-aZtcPFsO0FPcjjFr7vfq7PmSX3vsTfGzVkcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPRSfRBFcsWdXQ_02a30R38TgNKMK4PBalTpJBDmcgLjOT3xwAXPm-h49n0EleggD-ryJyYy4YoQOgR6Vlxkn6DodOQHzXF5RClPTQrNPivgZ3Z80LiBojJb02wnKGIzLOlnKqhgb8YGZytES3EjPibIxm99TZbeKk7sKrS-A8nrXV35eYwM2zaLbi9CVDZ0ekha7S63gCS1UES8fno7-rDuZRkeWZdG1TNJ0clbxWnHfMJf_SOvRm9BrUgBgEPQI-hTcGWbUfLAHGwEreN7FoABGet_4mQMDWX6WUqsRqpNnSj9NuL8t6dCTGzo9sVv0z-iAnL-vvKwqTd_-wBb0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcVqy8TZQpFaqqmPQx55cZmirNt2UOx3p_2NuNt6Q1ScibE23azKjypi7nab6JJujmSVWpalP3qYGY-zalffGFhPgZnsi_I_IK1n_k83f3DJa4q0brKIplA7QtCXgCEbJj_Ey7jzqMtTV662_M-WXkcJOrMhNV5ecknHvpfVTT9UzqKjzic4L18EhzKQtACfft-dfyM6wNNiS4m6Sg-41SyVjeBicQvN297yyBY01o7rJ0w5H4xFF1ZAjzQM3kAaFP73LkX7LZa-w4C-0eTEQG2QG5f600jE6o3Zdb8cARv3oyZMQai0F4IFClmvFoD06I_oQmQQTjnNn0MDpg3mTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKjD_2RBXdxxq3HCO_2qkoHFrFCOKiRVuw1ikXa_0GQZmQjirz04ZaRzrmnk6JUTB5gw6h-SJENArdj9FRCnl-atvcarTtTI9gqp0_leL4MzfzakQ9ZyuPNDPdctK-WuGrZRv2qXOrGuttyGLF88UI8_n_dbBI1hFIhKQeaeTEMXznAEx_gNFpfvmLyznYaquvriBWJOX_LMNQRJ4gD9gTTQKXbc7ItlK-gu6ELwM4LSa1oXECJQ9ky7VlPQD_IgmqYvn274tIe_g4nS7QZCMMlsviZivtyT8Go9N2UxNNxl4CO1QwbDTohiCtnkRDO1ZdE7q0iXU41oaUa0WBRRHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT62q3oqy_3uE9ilk-la2AY4T0Zy8H6UhgRALni7LNMZS1Q-Lyu8IFt8-CccC5ZiTiCXIxzo63XkuAbnxuleLWowE8k2LdlC91pGROMEDvulEmPIAqqfpKR5NfOLom7blQSKnABjifxApsRPrawyQOeaKNbz8uzxFMkiaHk7OzDXy5yPnbn-EVHzAEPYT-kmYiYI1SjNwS-UrbJ6QYFKi2a1dIEiXouFdByasE5O3mtTtMKrlRGRhU7LwVBEACGga1GP0MQKvGgiHL80vmwyigWqhyWp92fNhSkSQNuRnqZsxusyFrbe0ON-vi0TtYJgH5TFONgZDDtA_G9nad3nEw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=v9SMjwD3hfLjqMkzx-wcHF_RGK5sVilrdMMyZD_kX5E9bgqzlf6IArtFSTLqqFCYTnoSm78uoiLtX0E9bdoa1KWTeZk6QJVyt8u7h9qIafL7KOKBnJ11GdBo7xbgPmyWH1eLJZUbtNWWr-aFvJvxC3VMejmwBB84gjYjAvL_AymeZv0oGtbmLOIKV8To_25orGrQtEIfshL2_GeU9Dc9ctGyqLHu6rs05RoFypwHNx0d9zQdup-zCYwx8enjY1GKYetTSRBqnoPrzFDk9MVuPEqpchWrOzmbwb7n6rEQ9OvFGOMTt2qOh5rPM3ljhwB8A_Pc92RTWJmbd72TlECJrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=v9SMjwD3hfLjqMkzx-wcHF_RGK5sVilrdMMyZD_kX5E9bgqzlf6IArtFSTLqqFCYTnoSm78uoiLtX0E9bdoa1KWTeZk6QJVyt8u7h9qIafL7KOKBnJ11GdBo7xbgPmyWH1eLJZUbtNWWr-aFvJvxC3VMejmwBB84gjYjAvL_AymeZv0oGtbmLOIKV8To_25orGrQtEIfshL2_GeU9Dc9ctGyqLHu6rs05RoFypwHNx0d9zQdup-zCYwx8enjY1GKYetTSRBqnoPrzFDk9MVuPEqpchWrOzmbwb7n6rEQ9OvFGOMTt2qOh5rPM3ljhwB8A_Pc92RTWJmbd72TlECJrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dn9cMWnR-RAiiJyS-o9Fs5OIm0Nrhdealq3ds7EiFhNkRJ_SYuIy0UORfvfzgrMQaCJiVCPOgMX-UJKqfLREm8KM37GfW3L_Nf9S3C0au4bnc9inNr_nGK-3FISL_N_MDTsc-TFzKk82qBP0stqDBW7sdJAEX7A-H_mmJmt07s47OREk-A3Hz36O7juZEbGcFs_vc9DJGkzkMj5JjGx6zHyKmYBFyHnthSxgDAY23BW4YSIq9jM6ALfTnDDlltCs9RMQUhCBpxtTR8tL1rXoIT6E_5yvXBVp8LlDrcMLsnzNMu_PXGyPhVYX3yJoM7Ss6p0mwJhFBeYcBe9u-SkTEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsB_n-_FgOZMGn2Y0RasyrCo3fEt1WmR0wgvgypMMniF2jDgJUtzLBBjkXChrtI9_VPbnixDbTo6tedz7Y4c_TjBogw3CG4O-bFkxMTf6NLzc-YLgsoSUYk9_bFiBUGZbW-GUFDMNdNGfStprfHxFHFZUher55cq_UeIxoQXg6T0Qu13jJNOhqGl0Vr76uawuPP80TyXgZaA0aPShCZuObvfT6loXN11rTkMSwaw-TFIdGo3ZlbhBRrYD7pb10qu8SV7jwk0IHy-7JCdGiJlegOrhPHsI6_J7PEaM4F4X59H99KatIQppYSKIKG_97ZbAwsomF9eut7XGBlrQlOjpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=R57QBNiLth6ZXPIxLDR6iuJKxtBOD91xqtZQJ2JzrE7F6LdFPHylT7lN9yOhSlc2soha03I9PAt6CZa1azHImHPaC4BDdNc__wwf_jsZmoOrYuYXHZCG_jXTpEuVdaqeXwmHEWTyFOq7RV3XRPOCMbyOeJ_ieHs4fjdNco676E-d67w0rKFMkF1r9klwOK307t2EaNPlk2O4rhu_P9NkPMf2ZPYe8PeWrfYLHje0Je2Wx08_OIfxEg6FhKDOeWgHIAnB0Ig42n5aqulevHE4J2NzMqMBZVbLnmP3MlTw7k2qJBNBwaV3YnGqCAMQKiU18yiJF37w0lIUXUsktVLrcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=R57QBNiLth6ZXPIxLDR6iuJKxtBOD91xqtZQJ2JzrE7F6LdFPHylT7lN9yOhSlc2soha03I9PAt6CZa1azHImHPaC4BDdNc__wwf_jsZmoOrYuYXHZCG_jXTpEuVdaqeXwmHEWTyFOq7RV3XRPOCMbyOeJ_ieHs4fjdNco676E-d67w0rKFMkF1r9klwOK307t2EaNPlk2O4rhu_P9NkPMf2ZPYe8PeWrfYLHje0Je2Wx08_OIfxEg6FhKDOeWgHIAnB0Ig42n5aqulevHE4J2NzMqMBZVbLnmP3MlTw7k2qJBNBwaV3YnGqCAMQKiU18yiJF37w0lIUXUsktVLrcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBAdphcC95WYuwxviO9NcJyCA3rutPMTV-KVyWCOPGawrUYdR2qy-3XP_2nHj2cPUnr2r9DpHt0WFBDxW7TOU92_muQ99KsD2l1W9StSXJg0QBp8AvLD_GeGa25IxxPbo2Sdk2ktxkJAxwy4CCFusNuHqu_FfCopk2tzwbHvXbRdRIJaGk7I0ihCNJTITQGxqbsC3h684lRC7dZe7DBPaN9BwlRjY1VRyVr8y0T43HC3JOsKNplgSD1SueT-Z_hwFY4HEUwoSmcDrnrJV6imRS6Psnc6llm5IIHbflHzjr8yXJ5O300of-O3xIzbbQMED2ShJb5fvUXYtyI0LlMjzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=Y_KpCPhLnT33NEH32nbPdt6TxrbyD76Lt9B7Of_cNw6Uip-LVbpYficQNFvGe_Tl7_z82xcX9xG8Uu16BbKP3ksdC4qCMD0_9rrgql54yqKrWyCaFUT_QYYWlMUP98cA8v9JU0rk494ZJDUTeOjJJkdVvqXvdgGS724EmIHFFmwsu89q0rd3C8i6RY8jH-O9IegaYZkF6vjypBs7ZUHY6uj6lMqhxBY15U6DOhQukSYSH_YRZv21J2XcvYb0Xq0X88Z3IKeomIFhskP045wbzzwLeREJHQ3RFpT9dpp-ziOyK7IoQ_Oj-dzalyEnAs3X8IemmtGx9Kf93LrgNvytbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=Y_KpCPhLnT33NEH32nbPdt6TxrbyD76Lt9B7Of_cNw6Uip-LVbpYficQNFvGe_Tl7_z82xcX9xG8Uu16BbKP3ksdC4qCMD0_9rrgql54yqKrWyCaFUT_QYYWlMUP98cA8v9JU0rk494ZJDUTeOjJJkdVvqXvdgGS724EmIHFFmwsu89q0rd3C8i6RY8jH-O9IegaYZkF6vjypBs7ZUHY6uj6lMqhxBY15U6DOhQukSYSH_YRZv21J2XcvYb0Xq0X88Z3IKeomIFhskP045wbzzwLeREJHQ3RFpT9dpp-ziOyK7IoQ_Oj-dzalyEnAs3X8IemmtGx9Kf93LrgNvytbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=OsINEhilLY9fZFeKI3Dlkd3qWQI4UxaQH_77DSD8Sy0YEBQHeU5XE3StAyD7TfNKduyLI6abk6M2kBYeLJP1y7auQRvW2MuszRzKTr4Zt4frVj4RZkhXDLUlayTsMYcDgZKJ_1lTGirBfExYjB_Kb8Oiqeh2lW9vIe7f53FaDWr4C0ZtQ2sqtXGtiCR1JmSw99IViZbhfmXBlRkSvtdikJQ3_RH1MbIIrnLLUZ5C3dT5OJ7T5nMutTkPxHu4UkZslYn6ArNgxa4hV_l_36UpBB95LSpXUfz6oWuPGEqfgeNlxlmH3Ia8FC6OCziJTDcqQap8P_M1gdz9WYhXnYHNpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=OsINEhilLY9fZFeKI3Dlkd3qWQI4UxaQH_77DSD8Sy0YEBQHeU5XE3StAyD7TfNKduyLI6abk6M2kBYeLJP1y7auQRvW2MuszRzKTr4Zt4frVj4RZkhXDLUlayTsMYcDgZKJ_1lTGirBfExYjB_Kb8Oiqeh2lW9vIe7f53FaDWr4C0ZtQ2sqtXGtiCR1JmSw99IViZbhfmXBlRkSvtdikJQ3_RH1MbIIrnLLUZ5C3dT5OJ7T5nMutTkPxHu4UkZslYn6ArNgxa4hV_l_36UpBB95LSpXUfz6oWuPGEqfgeNlxlmH3Ia8FC6OCziJTDcqQap8P_M1gdz9WYhXnYHNpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=mwXDHZbnNOJEfQ9a2SlbKNuHBjmHoLuA-BaTTAM0L9GQCdbQhyqqRfP3h_FqsQ1PB8gDj8uKDHbi8MfOFhr4VEEWzOiZVPuhQNVxM9jrbOJiFRwPk_LRSp4iSalJR1d1pHQv85fexiaPyJd56vjsns8CrZt98rqzUQ1TaZAHwjHwbVY1A0yqiMJmuFJyIqEculmNZVmqgcXJkyN22bO4U1F49DuCvGJMyFoRI7Pq42stosBO1-PX5P20JddcBa6MgPRP3CFaaO8Fn2uxTd1Eo_fklKkhG8-H9dQXC5oqw4keVP9Idv4aJpbHsBZmcj5eBnphImhPCn4x1oxrljQoGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=mwXDHZbnNOJEfQ9a2SlbKNuHBjmHoLuA-BaTTAM0L9GQCdbQhyqqRfP3h_FqsQ1PB8gDj8uKDHbi8MfOFhr4VEEWzOiZVPuhQNVxM9jrbOJiFRwPk_LRSp4iSalJR1d1pHQv85fexiaPyJd56vjsns8CrZt98rqzUQ1TaZAHwjHwbVY1A0yqiMJmuFJyIqEculmNZVmqgcXJkyN22bO4U1F49DuCvGJMyFoRI7Pq42stosBO1-PX5P20JddcBa6MgPRP3CFaaO8Fn2uxTd1Eo_fklKkhG8-H9dQXC5oqw4keVP9Idv4aJpbHsBZmcj5eBnphImhPCn4x1oxrljQoGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=dlXuc8xb_udPafjMhec6PXobc3doKmNr0BmkR3l8ajzza-upOpqBqX5sszPr2g5B1Kj0CvoyPODHFCNgxl9vNd0Dnisb6gQjw8cEjBcQZLnnR0Dz-3FvCjwLmjirvySiY2oIo_a68SpwhrURBrJc-ZazaRN9KnS-l5mmxv73FnGLiUYpH5vkjcg-oVhQ6ytfaLCKn0sT_YqLlfJd3EJtgPUzz_XY6Avvq_sFX68j_0XI4-zhjr0I5-_N75gDDz9S_zAC_60p9xwfRMYYjNOu5lEHGMSfdRHFX2KX5pmDYxBr45tPwtQndWfgdEQuQEZo4M-Dxku6HYW4NUw5vvMpWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=dlXuc8xb_udPafjMhec6PXobc3doKmNr0BmkR3l8ajzza-upOpqBqX5sszPr2g5B1Kj0CvoyPODHFCNgxl9vNd0Dnisb6gQjw8cEjBcQZLnnR0Dz-3FvCjwLmjirvySiY2oIo_a68SpwhrURBrJc-ZazaRN9KnS-l5mmxv73FnGLiUYpH5vkjcg-oVhQ6ytfaLCKn0sT_YqLlfJd3EJtgPUzz_XY6Avvq_sFX68j_0XI4-zhjr0I5-_N75gDDz9S_zAC_60p9xwfRMYYjNOu5lEHGMSfdRHFX2KX5pmDYxBr45tPwtQndWfgdEQuQEZo4M-Dxku6HYW4NUw5vvMpWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=gj53sPhxsszAobVGYT_1Bx8__RKSrHXIyrJujcL-RBlOLTT2X7de-Fnd2ywZYvrJ6BBPY4_VpivryJJ-AQcelb8dEQYF4C8BrTBcZLGMSVDE6x-ri-Evzaukj5QuKh9hLFsLNKDaDgUsplWAZvA0NgV-MQe8xm15cMrVY17h_eFUd3IwBbNleC47tNW1czxOpBylenrmVghsOfDtpTlQ0QjeEQJNgji8KFZSzPM44h2xvbnJ0d1IysrLgcASro9HBwTkTxtO3VkK8LjtWbAD0S8oZneomcfsMahjZFIURCpHzvOTcHVDWVy14yaf1uC06G73u6i2QXHn3tay22yJjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=gj53sPhxsszAobVGYT_1Bx8__RKSrHXIyrJujcL-RBlOLTT2X7de-Fnd2ywZYvrJ6BBPY4_VpivryJJ-AQcelb8dEQYF4C8BrTBcZLGMSVDE6x-ri-Evzaukj5QuKh9hLFsLNKDaDgUsplWAZvA0NgV-MQe8xm15cMrVY17h_eFUd3IwBbNleC47tNW1czxOpBylenrmVghsOfDtpTlQ0QjeEQJNgji8KFZSzPM44h2xvbnJ0d1IysrLgcASro9HBwTkTxtO3VkK8LjtWbAD0S8oZneomcfsMahjZFIURCpHzvOTcHVDWVy14yaf1uC06G73u6i2QXHn3tay22yJjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJtTaBOK56cKzl0dTEI037Cy6xfOw40hV4MCaOOMfPCX3W8QeLS0_aouqMPlSXuHpkdgCXN7tLqZpcH7cQTjmx6KXS-5prUxYykibDdUq-Yq-OWg1nJMWwf5GgYg_3hM1eYn8rpJ17K9odvR79LbgY7rEuXbwQnbFFaxoB0QfaJEM1rpHleFSqNAjh-jpTOnXk-sodILfqo409kiGNb7agbs3yGFx1cPuXXBUrxEFnnQHlKA-O_v4zikZ3IVxHBFXONMEol1cvlo3gbQhYtuyAAT17aLvcGKZDuwje-vCG8pAkCWAjrd53PTSWQn0sTxjmgwk2INDJPDGI6QVLFLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rd2xY2p0V3KbXUDgS6NrW7n1kuB375W1zp_XbLj7v4s-vcpOWqQ64n-Qejlzo09VEblOIzS5YjOACjOByElZaom2gvph7oLW6ovflmydi0DQJ8fW9W7oWtDnpScgbTxe-HHTZ5x_o2dbSdwpPJRph5iNFuxcQnPYzW4maTIDViwM9gIetBoa83tcZFkoVqO-38SnEjRUzkqTVE_KmSjgTUnI-jYEnri8sJUrFmelEiDgPHu2bmP7jWzlDnFiiEyRmAGwFs_orM_xO14dPGBYYQep_VWO7sGYCS131k32fBkZOZr8addOqJepbDMOugI_v4_BFgOYv1BbVGSxT9pZ-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQo9N5wW1JbOsE7C0YVSy-5VaeR1n0WiFQH8Rq8IRgCoc26tac8dZ89AsnFkDfDRsUQIR5y508mIr3Il4ElanebbFCZ8Ag7-mVt2NPRFamHlD66KjzI1b0DGCdBGFKwJpLIliS_u1DiZQDLHd6z8CKwoHXaa8_4i_olnIfC1g0dPdpOAC2Rl2C0fZGnLjrqSEGCFMc18mOkqgTFVPUFZFnrlkIC994RhCZF9RCxsIML52q6TouceXgeWFXQZaKdMcESi2URWKNceNIZguJKozcGLz2IMwAbdYfcOk5aPfd0wDq22_HrreMRNUjISHypUNLCOLEXMxPP6Kut5Wx-OpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOkFSW3mvgDJr6WKG1Dv-e120sf3L2vjuVHx62OtEqz0MvrkNdeRI1CL-EZFPPiaziKOH0Lf_3CkA3wft_UafiFvlYoomGdvF2FYmYgUaslDQE6dqd8jGBqoapjDDdCZSoXYKsnBvmKwUHp3loSI4sEaQkpT76UxLWacOLW6m4yXcibdEZnG6WKjTwPX3CIEolAHgK61yT7j9wbbY7B_LaHB9OpWBfhMxb0x9g3Y-dV44EzxNyVdhfFotpqngTBqo2wxrf4XjlVwuMh_lNrp1I_OmfT0Ii3aSYfzCOvZgt5q3W3R5Jf4iR0sRL-wyuK6Ewqo6D9OnggNTMbuRH6oQw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=F2kTNYtf79TJLQjMHVrEjyCdVWue1LpzwwCePahWLv8R_2qClI87IrXEvoeulKsxoHhTEomaDjr2sIr_Gmfa11RtzDAKpufk8Zv0TykiaoIO6jrgBTKTeL_RqY6EP59FhfYL2lJqYrEDmFDgv61zkjac7rpnaK6Rq5pAaGrX7c-D5lrfqMyCyjzjfIS9uovoyUDxaIo_s3NcZ6Wy82FIw76pWziiC7h_BQBCcQR9LvgX2KcI6GgAEBCEr2BrTQK2Y1N4ukvNLk8h5YcMFAvjWHFrBrcYVWTLckNkqrpDzDYOYOIxZd5b_U50a4Y8yVKwTDWG0LQOGnk5kews6l8oHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=F2kTNYtf79TJLQjMHVrEjyCdVWue1LpzwwCePahWLv8R_2qClI87IrXEvoeulKsxoHhTEomaDjr2sIr_Gmfa11RtzDAKpufk8Zv0TykiaoIO6jrgBTKTeL_RqY6EP59FhfYL2lJqYrEDmFDgv61zkjac7rpnaK6Rq5pAaGrX7c-D5lrfqMyCyjzjfIS9uovoyUDxaIo_s3NcZ6Wy82FIw76pWziiC7h_BQBCcQR9LvgX2KcI6GgAEBCEr2BrTQK2Y1N4ukvNLk8h5YcMFAvjWHFrBrcYVWTLckNkqrpDzDYOYOIxZd5b_U50a4Y8yVKwTDWG0LQOGnk5kews6l8oHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=W5AnckBXZKCAaRY_OxEicV6LdAfD4X6qatOc10wmi5KcBlUZd5PjTw5GnwzF0BVJ_hnn2vwAuz6NzzBZVgpub-jtczBl838rnnUM7rN-s3LyyqJNwKOtu3kXPOnPjNVrw2tUNRV6aawNwf86lEn8ZYady5n1coL2MElCY6FiNY7b-1ZWdouNBY1yBeLmpKd9wQhNcoWC8E80URhQ9z-FyYZpMTEfbz03o0j9j-yWWX9oxkiHH3SVShfp8CQG920UXmOMzVitn2LOxlSAvj-eLNjYvRZFSbSzHvl8OoXd3GuN2Qk9WQFZ5FRJwBteVWMG5qf3VjKYuCPNR1HYzkuFSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=W5AnckBXZKCAaRY_OxEicV6LdAfD4X6qatOc10wmi5KcBlUZd5PjTw5GnwzF0BVJ_hnn2vwAuz6NzzBZVgpub-jtczBl838rnnUM7rN-s3LyyqJNwKOtu3kXPOnPjNVrw2tUNRV6aawNwf86lEn8ZYady5n1coL2MElCY6FiNY7b-1ZWdouNBY1yBeLmpKd9wQhNcoWC8E80URhQ9z-FyYZpMTEfbz03o0j9j-yWWX9oxkiHH3SVShfp8CQG920UXmOMzVitn2LOxlSAvj-eLNjYvRZFSbSzHvl8OoXd3GuN2Qk9WQFZ5FRJwBteVWMG5qf3VjKYuCPNR1HYzkuFSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=Ks0st64K-BmWnNSZsREV0PTXUrKhPnaUP6QDwaaCUMPJAoHmPgomteefPr0NDBjYmP6lyzjpoGmG1LOa4mVS1yUve9vEBBPAh9-P9OAjvS9tAa90Wivl70AJmEr_sYbp7cIkyRn0IuElWAzw8XAaCGekHQzYSQQIrxseXXiEtnFYDMWoDsMpuou6U1JAEhTbCN_SPSMNlNIumxIF6RphM2IfcGTMDOmwKhMKkkAEfOY4PhcuhqEkMDvxuk_0zh-ZBWWjg9Uvs0Da38RJeo3ZQ19E_sLIYoAgC6MYXejYObSPEQJ8sIGoDoAc7xL1lZSDW2ip30eS-hVEc2MAKaQPWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=Ks0st64K-BmWnNSZsREV0PTXUrKhPnaUP6QDwaaCUMPJAoHmPgomteefPr0NDBjYmP6lyzjpoGmG1LOa4mVS1yUve9vEBBPAh9-P9OAjvS9tAa90Wivl70AJmEr_sYbp7cIkyRn0IuElWAzw8XAaCGekHQzYSQQIrxseXXiEtnFYDMWoDsMpuou6U1JAEhTbCN_SPSMNlNIumxIF6RphM2IfcGTMDOmwKhMKkkAEfOY4PhcuhqEkMDvxuk_0zh-ZBWWjg9Uvs0Da38RJeo3ZQ19E_sLIYoAgC6MYXejYObSPEQJ8sIGoDoAc7xL1lZSDW2ip30eS-hVEc2MAKaQPWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6AH7grnCqW9QUDaZSd_bClnWDucdP1klv9B2BdupU33ag_gu81OfumDUftROJfG6-lTqOvs-0MPJJ5GBiUbL1DT-8WhRLQBLbJTO3VgkE1kYREcNX6_qy51FWLs3TPYLxcjgSjK4adPPSyz41PHHcPxIqK6bQ9lQBUGHETiQE5U-yngY2fOeebdRe4lyNsxbbkVyJm7JV0qczCW3ZNQZ6NEi_Yrp4h1ghLQzOzLif4JFNnF906vlfEuS4jyN20jZQHKV0jHs2_8o-_L9lpUB2eIkS1j7gbaN_InvkGoMznK12vlORccJMh67RRcU3rrBcxXX5AUaBVbVi1ZQgaEXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=H4v-0JqbEXAdazfbiBClV8XnOeFsJ0PuBoEg18WSg-FH9YX-CWLehw4GgWLENI_vAMVUySeinVE2zr0EbBS1NcD4zBLAM-OsqKekp3fmnxiJD_6cxZ-6__hCwvGKpZ2gOqS16Po_0UDvdy5No2LzKAnz0aFT3zwQ8WE5yAehawDnP-BOkNQDRPOWI2upyqrRF-bZBdHk_d0XLmd-Ja25GdHegjA03hPCAk0PydMmErX7o0tTFWwLQJ89lWO_EpdZajynbElTeTuY4xX43lFrmQ-M_Em0rPfd_mjg6JungUPGxl04y-pK-MLYXUKmYxNDFMprsBQcOxquHTTon2jm0TxwW9VvBSYvYzU9-WAcBAQE8LWsXC3-JhkcEY5-W7Dt22BocNXZGzv1kL2pq6Tny-Q3sryTotMcFe2B-aljSTV968wnb_Krs7AZBcWSSm6uEGfRcfitVP4amMTpIOmiTikD6e-7HQkkMZlXAc95qn8YdUxXfNy6qjSz2pQnPa3VCbz3RQ34mfVv93lsV2tHpcOFDCtygMwuAUA4k4hqcghYj7M6lXjciv-omconXpl1ezO7bEMy4Jz6HEHjxPL6nDelpC_HzZ05mYdL-FuGyqRZphfjXe75sDfsZDo_86y_d6kK5mgQVls66j7IPVMukAibUgTF1gCp1bQuqn3DOOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=H4v-0JqbEXAdazfbiBClV8XnOeFsJ0PuBoEg18WSg-FH9YX-CWLehw4GgWLENI_vAMVUySeinVE2zr0EbBS1NcD4zBLAM-OsqKekp3fmnxiJD_6cxZ-6__hCwvGKpZ2gOqS16Po_0UDvdy5No2LzKAnz0aFT3zwQ8WE5yAehawDnP-BOkNQDRPOWI2upyqrRF-bZBdHk_d0XLmd-Ja25GdHegjA03hPCAk0PydMmErX7o0tTFWwLQJ89lWO_EpdZajynbElTeTuY4xX43lFrmQ-M_Em0rPfd_mjg6JungUPGxl04y-pK-MLYXUKmYxNDFMprsBQcOxquHTTon2jm0TxwW9VvBSYvYzU9-WAcBAQE8LWsXC3-JhkcEY5-W7Dt22BocNXZGzv1kL2pq6Tny-Q3sryTotMcFe2B-aljSTV968wnb_Krs7AZBcWSSm6uEGfRcfitVP4amMTpIOmiTikD6e-7HQkkMZlXAc95qn8YdUxXfNy6qjSz2pQnPa3VCbz3RQ34mfVv93lsV2tHpcOFDCtygMwuAUA4k4hqcghYj7M6lXjciv-omconXpl1ezO7bEMy4Jz6HEHjxPL6nDelpC_HzZ05mYdL-FuGyqRZphfjXe75sDfsZDo_86y_d6kK5mgQVls66j7IPVMukAibUgTF1gCp1bQuqn3DOOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbv5JtrcdQ-u9OFA7X8yhab-BEB2nicImxkOCsrSSyEE-aPAEMzQtqlF4NIn4GAy1ynJ8uUOUt6W2CO_ol9e3s9AfS2cDHvlnK4GMhI0XdhEZh2pFRb-e1yzkFSmwG4fLG7EvDw-kyC4_jRcJwrr1FHGSP-_R_OENfzyEiKmZIbCMqonUTcWbx9ClHIreCUO5hRNQw1l0P01hNTdDiYBDqMA0Mtr2NSjwafdIKBxigqgKH9noNcbeNjVy3A3Yu652Kp0xT4Q-NdnmZDBu0tIUwB49t0uWxE5aAsJS8oz_lZ64K5iKFEAX-7JjLe12TXvYh5rrQCPopKfh0lhD9ClLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=VjiObgbodJO3ejb1wLYMdYoomc2Ujmc7G5NnMFE0qOwSuXlvsNCoCH9T4m4rpSAJB4QtGhMQ0hBmw4_rdvQ2uiOJYMmzVR87QovSLvIEuAq8str00WOQ6Izu7oYGlRZ2Qo7cgtONkj-kRxFfrCnkno_dZECESU0CvuubM_Ixil9Oct-O1YEkPiX8mx3Nf9pEUwQA3j3lpxML6gtquQb6nF4_XZsGDpvmi2IMv8pawg9saiTtbSIzaJy8v6yHhsbpaDGFfrLHYqEjzN31zqa54oEhFgf_WBmOY79s6XHbBHLiE3Uy4CTZ70F24xZJFO_FpK-qK92TGX8j9BluFhVmuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=VjiObgbodJO3ejb1wLYMdYoomc2Ujmc7G5NnMFE0qOwSuXlvsNCoCH9T4m4rpSAJB4QtGhMQ0hBmw4_rdvQ2uiOJYMmzVR87QovSLvIEuAq8str00WOQ6Izu7oYGlRZ2Qo7cgtONkj-kRxFfrCnkno_dZECESU0CvuubM_Ixil9Oct-O1YEkPiX8mx3Nf9pEUwQA3j3lpxML6gtquQb6nF4_XZsGDpvmi2IMv8pawg9saiTtbSIzaJy8v6yHhsbpaDGFfrLHYqEjzN31zqa54oEhFgf_WBmOY79s6XHbBHLiE3Uy4CTZ70F24xZJFO_FpK-qK92TGX8j9BluFhVmuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d018XqGCiSoYPYOiVU0lZpHSovIW7-8leStkp7buceVcFgem4O5iKfq8hsst0m8PS9l4yAG7B2bkI0g550Ft_FV39eRpPj3sS_1ZJFN-H8QCzi-kCwyeRkcOpi93qTCGKFtRxwO3-U9jyBe_Aauo1MDu2kBf0OnBHD0X9EdEJxfGJftsE5OzibhjI0J5-ZB1XoPoIINETEHFh2FaaYMCw1b-KC1LbjyPqoHLUGSaFxTtT08oRQR-Sq_J2FlISOC8owSQwBW0_ev5Ggsre5kLIvvYJ0CWr7FRVBUtSlfP1Jvb4ne6oraa0vecUd-zdeUJhBQVRWb-8Cw6F_syOZ1bmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnCb2YbN3qcgo7GJWn3ZSwSn-4V5jq89o1ujODbloz_i-SkDe57WJRrRKTxaChgdScBd2aft9Dw2vuk5eIlqgx2VIs75q467OGeKh6aF5lY9qPGMiZ9R9UpgyFqDhvFHMD9_qkHbO_XjmqVmt6P4l9t9cagINZEd18juev7G6q3VH_paPlbae8bA0SbYWanokifDaxulx3UeaWZnM9nHLKn3nXFLbveU2LCVKxbzWwuLH2EdQHvqzB9VMQNKpfV9wJtErxID_BHy9s_89Eo634JRes3ca6E_SmXekWrjeyuKzRZyC5OejEtU01krZurpRvCoNDMmFG9CiPvEsS6BMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TS6UWKmccOo4NqZUX-3mwIj9KSdStWYKpvox63bc7RutCUoMNyagq8gt968XqYcY0S0fniu5b1UbuOFIEzMjyxgyRfxtghrKkOfz8FL9LqOL7Q6lSGirMwZQrhLD8_LgREgJCpPTs15Jcdh4ZKNzqIPzRuMfdrXoPvxDyaKOga2270dh1bQxCm4ac5AObinMg0Uh5Hv3FLknTRCv3do_azzrYqlRnP_0vrkvNsa181xxvh8-0By4vtZlgv9EyCXjJvx8cdwyg3e4VD7Oxo5ptY9jxg4dSwtEauN77Adfjl2B31mf7DcbHqF97q-p2u9ZbfKXDs_489v6z6XAdyQPgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX4WGaslpZUy1YCPiEYNw_3j1MeKpqQ6_3w_p0TRJPqQfhVduAwyuAXlhXfi2GXxiodULeqjc1nPor-Q_cJhAYXCweXBp-pARVPwoqlkeUy0tsrP-71qTVv1qyowBDqRmSLxeoWN3hcH6RfqLaD080gUR3hpTe1qJ19cFsLk1UDmPnCc3HudNP9CzGjZ80rNhd1kBY8w3TAx9Zl--x45K_TG50MRX6DZlHvLN7iozLnBwYweHzLPwOjnsGhFJmFtphSOSH1PehdXS6Hki4tuDuUX1GabQhFXnUVr1km47rWjDbFsoZbg11IWEacmqJgIdqCueDd9zN-dd6A_WsytFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6f4P2s8VAOtPwcDZbWJYEYtomYmByRx45qL2pO6BiwDYPW1duRrXneyKf04YI5x7Pc3VNSPZztEg4C-oN4jimZ57_-C1XpLyggBRdtjEoCzQzfZ0azLeuLZMrLLjJAkVWzTcJoLQl0vUc0zA7qL6jpidekY8RKn5W9Kwf0QTPY5ulzrtn4kgS0gJ0XdgnjSTWcd3lMYAMEFelpt6ON3ocXxRgPRDqHP41j2PnPkmEnCuQehw0lWuKbLqr2OIKcD4TIiBZIcWITynYW54CVzNkPbCwtfqtfKRSar3GtSHWbTAfInjdSoIqMD57ef8IMofg-KAHn4HU-NM7fTKdyozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=aQEa-wVH_lyO1apW_EU9pW7eeO5L2eI8_RMxgePvtQRJuyk78Ey_SrKNgbdK5maWFBfrrmawO6L816f2vbN17NXWMVK1A1SA9TBEouZOXztiAcb3LuQwX6RMqrGSjUoIQjV7C78NbNK_EjDxO9e1csPjjVF6A4cFyHvTdxGxwnvIruI6NcjN3IG1zXCkUYDoeqKxvBMOr2aD_F3hFOy3rkO5EDLc--Ljm-PBMgW6woUz3-dHhsrN7IvTRu2cQ0zN3zuKpNmu-yr-tl2aVt1tRcaO0ObkOD40P37LjXLqJ8UaJChyDGp2Y109NNexSUUetivI3t9k-ruBdQMrWzpZkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=aQEa-wVH_lyO1apW_EU9pW7eeO5L2eI8_RMxgePvtQRJuyk78Ey_SrKNgbdK5maWFBfrrmawO6L816f2vbN17NXWMVK1A1SA9TBEouZOXztiAcb3LuQwX6RMqrGSjUoIQjV7C78NbNK_EjDxO9e1csPjjVF6A4cFyHvTdxGxwnvIruI6NcjN3IG1zXCkUYDoeqKxvBMOr2aD_F3hFOy3rkO5EDLc--Ljm-PBMgW6woUz3-dHhsrN7IvTRu2cQ0zN3zuKpNmu-yr-tl2aVt1tRcaO0ObkOD40P37LjXLqJ8UaJChyDGp2Y109NNexSUUetivI3t9k-ruBdQMrWzpZkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru4aXmlLinkHoFlNbw0t_03ERp6Qf034SryXZ2AXIX8ZcH1mzSGHvOzbR9tTNZDecSvqW54mVnuLQ8M71I83QjqdMbFmk9JsRJExiPHOzyoTFXswwtvLvMmfQe74MXr29XwJkBEnw8JpN9vxPCT5H6HvGfEmIjvX3wZ89dkRVdvQkZryTP5Ssv8eqBK7u3sC7J0MyI7RHSXlgzxK1N25ZwNabtv1rDWpqEBRXXoCIjuYbFtgkpKgW0tAUFq0UEOX0j3gHmp0oPWWBd7YXG816k2zvJ_PKId_UFad0sdolUVpPq_C1p5ysgVA9hXOIOK0zHHnaWbN_9IRarlMUuq8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8XywK3l08PKFYd4bN6nrxHJYKq3tcbYkX3eiH3P4e6wSwwr7hvVuXlOx1yRy60mhR_tTQW_D5wMocGBixwskn-iC4TNlbUvdlizWIJwA4ZhF4tcF2S515gMzsFujeqa5bnNUZY_hYggZ4hD_xZCjiZfaUyrYWuKlH9Pycd_MUrcYuS6gAtrvN6AB5T7GWopXLnnNvSLsEzszTvSWinEfpL-6uhfJw5oJtG0ZEEfqpqyseTAhvry3xDHhUMs2Eq2lpUPMPIvsLSd-k-W4swICsHN7mGaY8VpJ9vSsffb-Mk4GQoK8Vn4dr7JfLAl40EoHWwWTVI-UjLHYQYLZK0YAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4987" target="_blank">📅 10:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=Y3TJU1V1EayHkYKoOSk9-AqXXxmNkEw_pdm-cgDqXdbI1R-Ynw5WtbicCDf2WyuLYFV1qmjdnwuN5xhNTAyim677r1WCRbM-0qRnoZf5SFp_9QPMj21nFuOtz-sAe105W4igHUqhvgxUnmfWnWMRlTNsWkirS-zzuOoIe24ABQbQXjQR80b2bq7Z0o4wGzeX-gT_vsXv93hr1QrWww6dWhSL33NftV5zItprxGt2p8HE80Ij5nbwlsSOE_oWdBWsTDgG5zf7WyQJ2S8HMzlVhp3-LX-XE4mMoImud1c_65IDuL295Q2juc1k7kFHInEq5Vnr4dd-ipsmKIC9QgG_OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=Y3TJU1V1EayHkYKoOSk9-AqXXxmNkEw_pdm-cgDqXdbI1R-Ynw5WtbicCDf2WyuLYFV1qmjdnwuN5xhNTAyim677r1WCRbM-0qRnoZf5SFp_9QPMj21nFuOtz-sAe105W4igHUqhvgxUnmfWnWMRlTNsWkirS-zzuOoIe24ABQbQXjQR80b2bq7Z0o4wGzeX-gT_vsXv93hr1QrWww6dWhSL33NftV5zItprxGt2p8HE80Ij5nbwlsSOE_oWdBWsTDgG5zf7WyQJ2S8HMzlVhp3-LX-XE4mMoImud1c_65IDuL295Q2juc1k7kFHInEq5Vnr4dd-ipsmKIC9QgG_OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=Qa-8CL-tRFMDl6EgbSuoqHT5t89ysxpy34PRd5WzvJnQmC7TymF0Azwb4wCjYv9hjhJQKqimOxhFknouzySHriC7QWCpkVKdgxqfs7fQmrICwsQ5Lwx-jiv8D114GEwV4AHspWDzwYd3_Yl3MchSkYOblB-a8zkbovI88DEduANxoZwq5x74sv0oJGH96ZQzfwi0tlUxKOVUO0ElkERPnFFEEnbcD8IYageN8A2OjfdUfLmS4WBE_--xBR-GAnPt6qCr0WQK6Ju93WbWkYS22eMq7N5wtzWt42OIOlP22JQlkCiVfm8vspLxc26FvUQLg4cNSBTihFpVhPMjWKknlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=Qa-8CL-tRFMDl6EgbSuoqHT5t89ysxpy34PRd5WzvJnQmC7TymF0Azwb4wCjYv9hjhJQKqimOxhFknouzySHriC7QWCpkVKdgxqfs7fQmrICwsQ5Lwx-jiv8D114GEwV4AHspWDzwYd3_Yl3MchSkYOblB-a8zkbovI88DEduANxoZwq5x74sv0oJGH96ZQzfwi0tlUxKOVUO0ElkERPnFFEEnbcD8IYageN8A2OjfdUfLmS4WBE_--xBR-GAnPt6qCr0WQK6Ju93WbWkYS22eMq7N5wtzWt42OIOlP22JQlkCiVfm8vspLxc26FvUQLg4cNSBTihFpVhPMjWKknlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
