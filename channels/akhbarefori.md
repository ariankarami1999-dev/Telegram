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
<img src="https://cdn4.telesco.pe/file/YSt5bCrQaN3c4xKmJwoWVmE6mymrCp_mEVXXt_BwjOlebRcMvRq5PIDPr9s1Rs8NODVopSEPklXmX9T9KZZ5vmBk7nrAdAhDgtcT-lcCO55twE9jJKi8DQoGwJR-fxYcjEeLUazcAYyamj1twUFB0970DwA9lf6pKGJMXwxduToHApuopTTnJ5Lk2gL4q0FZoF7nrYk5Jnv_oJ0qaSLZEk88fZbxWG50_t7zrWUXETrtebXER6quHD0p0L4E_kjWTAerMpkLVbZD_OHnw4qML0GjMs2yFtvdQQf9O_BUi6LaNHfKnbk7i_FXGMGPhDD4IKl1OCnaO_hiHZU2rFeyZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.24M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 15:42:25</div>
<hr>

<div class="tg-post" id="msg-675756">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
حباب سکه آب رفت
🔹
حباب بازار سکه به پایین‌ترین سطوح سال‌های اخیر رسیده است. در حالی که حباب سکه تمام در گذشته تا ۳۰ درصد و برخی قطعات کوچک‌تر حتی تا ۵۰ درصد افزایش یافته بود، اکنون حباب سکه امامی ۲.۰۳ درصد و سکه بهار آزادی تنها ۰.۰۸ درصد است.
🔹
همچنین حباب نیم‌سکه ۴.۷۹ درصد، ربع‌سکه ۱۶.۰۵ درصد، سکه گرمی ۲۳.۲۱ درصد و حباب طلای آب‌شده منفی ۰.۳۲ درصد ثبت شده است. آماری که از کاهش چشمگیر حباب در بازار طلا حکایت دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/akhbarefori/675756" target="_blank">📅 15:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675751">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGyAqHc2iSagp2fncw5WitqOBWzhg8nhXAqVppeIdfrh5OAmUFUwLnDKWj8SWagogzOEtz7AfIg9-zIBPWRVhFaa_xrwKGGT1UIUuMtaVnNWKI-DGuTXZ569xvp17ss2Ad2byvhfsoKbSHimuBo-3TjAvv4xvihmUTHgzLin5-7S6DCqXSNeoD1ROyd3PQmpZBx4HfG6SemRP3z3N2LkElyfzGQtuk-aEJJq6mXiUu8123UYtyydvs4-UudlgROgUT-pxu_iumuiO-vSLhuuCfjM8ZIKLWyPe8DzvjReIPJBpSsovwIJB07qVydrgMAl5mMY02vlot2coJvmx-J9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMltpfAazroHUyscHk8Eth34X4fjpKvPzc_LG-xt-nmbZ17oR38pFhh3xmulW7KZkzYzI8j-EO784l98WTzgai7Xf7uvn5b0VN0dWIpcmwszltvu1lFRLHRUWv-NTJfXwrq4Uv-bxJaHRNKEbSgNVrk8C1iyM-8y1ER7sNWGM-fIttkHIT90H1V_JdQt_V4G6_OdN_i_f6PsgZY92ghQwmukODvKTxfrVJP9-zS-RbH0iZ6TPi2YfgHJDUICsds3y1dH4M6PyXJykJOsScjyKiIczZeK6K5OeoRcGicylWEQ9hOFX_-c9MUKcaspZpBwU2ldJVk40i7m6UOYouUKig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/duQbWk3DHyUWNZK7nR-Tidxj8m1Az-D8UcgqPNrDwqybq7UO4LJqU-QEtihCgw64_wS-bRoZiomsmL1PxZMUEPkyxorxawXZnHIyVJ3-CFJq2tVrNXGsU2PyimLafKxBrxkvK8R3rK_FU6RV0Ct6VLCHkhNo6oS38ze9KUSbfIz-tk5pBuBk-OxS2biD25r_DmnBkSKBmcrAiz8GTsvk0uqftH0vpLwIl60F_njdTelNGvIY59HdMVKOsTjBfIwK2Hil6esSeUewSXdNJsKwGWFqybQLCgrxInoalk1wYjAcYgx7lIXEaEcrxG_mdfGVoWxskUgv229iVhwrnYKIKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ad25p8V8hFCqs1sPYXcB5jSX4OoHpoZ_JvHrriNH5mO2ym7ePTe_qeXfypADPrkEcwV6xWw-wfLkNYKqHhKrFDR6cT6B5JTD7YxFIZ8zBJEcrNW6hHtly_SBXKkmcPzRushibs4AL-3P5sHlaszk7u0Q78aVp3OO68s0CXfEVzF9kfYCP-yAKgLxFosmfDvSr7TXLyQ_CFmmggYRcJJR2OkoQbl9gyNuH-wGpHi75Q85oWpV4fcuOeocpOE6zvU5wqvsi5IEu1VCg7567Sv90kug-GAYO8BSRW_MSqkIw86grn4rrv2wHaf2fZGSECBNMNJsBS2jwEPKPjkcSEPqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIBDwuWAjfk7ya_EzWSYPs5qyFQVh4MvC0cf9MZKgViPT-L9GExJkf7wUpebs9ueGrMXyCzh6cngsg40BEQI_1A79z9NRsRjmRe_khIqhf2d-yAo8l69x0HoyBdm4o4ECDheTK21aEJTsTvzvZdM2pzu2dZSZxFNoGgb3Tu3Q5Rv9VbXwkgLQi93mE01nhkJLghsXUPeZVwaf2nzTH6On7nJOalwwQX7QhdYT9JqonzeBLfVTAq_etQ2nEtOlanLrWzUkDTND8mOKptAIKxbpg47h-qHECiGsIz6tWOYjhwxFRh-EAyToaJ46SzesmmByXZA5Lb7lFRu3TUkbQeudg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قبل از خرید عینک این ۵ مورد رو حتما چک کن
🕶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/akhbarefori/675751" target="_blank">📅 15:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675750">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oa4zmWAZmyJpt3ZGsRgvORdPzdZY91C2gZwLtbYfLST0KKIMgPAHEBU4rjuN61aKLbzAg4JybAYUNDUgvxfyq7R8vOxmySRkfNaYW2hvmtp5VZBIdi9mHrT_Vf9rEoA3YsprGXfxFxDJxPgWuj4I4Jci4cG9DPcKc0h8RRmXppZ8KjxogZ3hgntmTmTLIZOnxIdpPTbRiyUDjiszQDVj6MM1E9d-uUcKLUbBvhkQd5zR0Dd2OQuyOMl7zAPBPslLk1eaTn6TqIpzHTNV1d0yGqnqbyLYsArJrVHCWYfx8Wsl_mkZwXNI29BUyLahzHh8QvPGrPDT8qPxZbImmwm5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتش‌سوزی در کارخانه پالت‌سازی در محمدشهر
🔹
کارخانه تولید پالت در محمدشهر کرج دچار آتش‌سوزی شد.
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/akhbarefori/675750" target="_blank">📅 15:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675749">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBNrJ0fpt7mg73iYwftxFpl_g1_YAkQsmGeeCP_IdYQ88YQYSxjc5fmg624k5r_mA4j5N6zPxiF5PLTUUIk_Sip2No_Jz7tbASQ3K_Y3uoR0gIDPT6eVJuycXrmXb-S_rs38DIiyzsKmY2w5wwELyZgDZ08L7LgQbybkdRsJkWZ25gAYOuHUIjXhB0FDRYKkz8t5-rnPahIbFW5Uz1eJx9YLwzV07A05ZsG5ZZuBHUpH4kjE2WE7tm4tzTpJ_lsAn6mT07VuRu3Djm36DHlVZHAcwfDzvaEN5lVpUnC0fOOt5q5qAawV_q_1tQfe9tuBdVKKswh_vsdjDSIDWKfvcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: رئیس‌جمهوری که فکر می‌کرد چکش بی‌نهایت دارد، حالا به دنبال راه خروج می‌گردد
نیویورک‌تایمز:
🔹
رئیس‌جمهوری که ۵ ماه پیش با وعده «پایان سریع برنامه هسته‌ای» و «سرنگونی دولت ایران» وارد جنگ شد، حالا در دامی گرفتار شده که خودش ساخت.
🔹
ترامپ که زمانی به «مدل ونزوئلا» برای ایران فکر می‌کرد، امروز نه تنها به اهدافش نرسیده، بلکه با واقعیت‌هایی تلخ روبرو شده است.
🔹
دستیاران ترامپ می‌گویند ناامیدی عمیق، رئیس‌جمهور را غیرقابل‌پیش‌بینی‌تر کرده است.
🔹
به نظر می‌رسد ترامپ در دام جنگ ایران گرفتار شده است، حتی با اینکه بزرگترین چکش جهان را در دست دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/akhbarefori/675749" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675748">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1e5b26943.mp4?token=oSeEgrxO5kU3TiT8BAkQRSeSuN_zg6JGcQXiXxTf-hy1TUa8oFxQb7tBJQJJdvOMug6e-i4dxP_m3Em59a7x30feMZWGZRGNKu3wtgAUa6meJw-LW0F_udFNBN4kiDbM7qVDRF4XToZ_lvIh306PBW-qbTx-5NfonkmbbWz8jJRxTpcuYyl-qswemBdgXxsk8gbc2t_nhKbKSwpDOnKbLwjuKKRTENlI4llNcVQVty44Voz-gomGEh-rNXpvuEd3V7zg31zECJ98ft0dz7-U6A0WHhhmnEeRzDhuYw270dh3EWvMkco-aaqnmI0ywrhzNZt_DsdgquxKpzdVVu5fNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1e5b26943.mp4?token=oSeEgrxO5kU3TiT8BAkQRSeSuN_zg6JGcQXiXxTf-hy1TUa8oFxQb7tBJQJJdvOMug6e-i4dxP_m3Em59a7x30feMZWGZRGNKu3wtgAUa6meJw-LW0F_udFNBN4kiDbM7qVDRF4XToZ_lvIh306PBW-qbTx-5NfonkmbbWz8jJRxTpcuYyl-qswemBdgXxsk8gbc2t_nhKbKSwpDOnKbLwjuKKRTENlI4llNcVQVty44Voz-gomGEh-rNXpvuEd3V7zg31zECJ98ft0dz7-U6A0WHhhmnEeRzDhuYw270dh3EWvMkco-aaqnmI0ywrhzNZt_DsdgquxKpzdVVu5fNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از آخرین وضعیت تنگه هرمز و دریای عمان و کشتی‌هایی که در انتظار دریافت مجوز از ایران برای عبور از تنگه هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/675748" target="_blank">📅 15:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675747">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مالکی: ایران به نوعی آمریکا را دور زد
فداحسین مالکی، عضو کمیسیون امنیت ملی مجلس، در
#گفتگو
با خبرفوری:
🔹
ایران به نوعی آمریکا را دور زد و عملیات خود را از حالت بازدارندگی خارج کرد و به حالت هجومی درآورد. این موضوع باعث شد آمریکا دست از عملیات علیه زیرساخت‌ها بردارد.
🔹
حملات سنگین جمهوری اسلامی به پایگاه‌های پشتیبانی و عملیاتی آمریکا در کویت و اردن، علت اصلی عقب‌نشینی آمریکا است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/675747" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675746">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stRbIPCaZ7Gw6QgN4JzCWO5xFFU_KEMkssV7J9kRzfTQOOes4WAqgXAV7QoBwv2W5NrHhxgZbzJyCHhWPAkc-xS4Omu4GO9LfyMn3-xgIQL26rlgyRdFlnT0X5-2_bjLOrMxwLsaUzYqi7m_anCKToP_bsRQltZsglBjwR_5yhoyG-g13oKW8LRVw6pJArD0TD8INhgZZv9Fn7wAo7biJxhiaZapLybPWijnnarPKBhGfp6rMR5HfePppzp5txnmp_kfx5B_3mnWWuIh2nesphmIsqSf1yz3aGr0D2cyZbAGu_WY-BuEbSsVTJI5_NK_DUhpovh2sEzv8mPq0gL6dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منو شناسی؛ نسبت استانداردهای قهوه را بشناس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/675746" target="_blank">📅 15:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675745">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رسپینا مدعی شد؛ هیچ قطعی در سال ۱۴۰۵ از سوی مشترکین گزارش نشده است!
به گفته روابط عمومی شرکت رسپینا، سرویس اینترنت این شرکت در سال ۱۴۰۵ بدون افت سرعت و قطعی در دسترس مشترکین بوده است.
اطلاعات بیشتر:
https://isp.respina.net/LTE-b
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/675745" target="_blank">📅 15:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675744">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسخنگوی شهرداری تهران | عبدالمطهر محمدخانی</strong></div>
<div class="tg-text">ایده‌ای نو که از دل پسماندها بیرون می‌آید
کارخانه‌ای که ضایعات از آن جان می‌گیرند و به محصولات مبلمان شهری تبدیل می‌شود
🔹
محسن قضاتلو مدیرعامل سازمان مدیریت پسماند شهرداری تهران: نیوجرسی، دیوارهای بتنی و فلاور باکس‌هایی که در این کارخانه تولید می‌شود بسیار مقرون به‌صرفه‌ار از بازار است
▪️
عبدالمطهر محمدخانی سخنگوی شهرداری تهران:
در مسیر اصلی خیابان‌های آزادی و انقلاب و در ادامه بزرگراه‌هایی مانند شهید همت از این محصولات استفاده خواهد شد.
🇮🇷
@abdmohammadkhani</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/675744" target="_blank">📅 15:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675743">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رسانه‌های عبری: هواپیمای نتانیاهو پس از رهگیری دو پهپاد در مرز اردن، از یک پایگاه در نقب به مقصد واشنگتن به پرواز درآمد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/675743" target="_blank">📅 15:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675741">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ji5gzVbCR_iNs9vKvD653pal4NmUNEEsmK8-_Cp_Y9s2UpimFqsRgKuxeLyVZ037Y9CDDOOL6q0i_lfvwUXKV52sBfvc-4xkbGGV9S9Yt__cw77AOEwm9XXUIx1RsyJvAOcU54n2kDD2gADQbgO2UVGHBqUuaOWHmRYLdYQRwzih8tn87f6CjRRLEfgpwZvbbm_j8xDtsd45O94KEwx35wC-Ka60-Z0Rn5N9WYLjgsRX9mIln1ggt5lGOGF8aFGe1BgnmFOb7LXSH6MprQoNtzFKKNPcXpYD1ng-TvC9ceV4Zk9D4FKJuMpoUu-lS597e6ktNdGs8JtqsZI8h0Jbvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLwcefV6044Kt6ETPwWYZdbxFL-gjv9_3lS-rnYxWSMLywZ1ayivWyQuJfNrODo7-5jYRJVKKbDYdLInII1C-jeqzxp06XX2PEoEM_LS8DP_zO2_7yQ1ge8f6iwHwEmDK3sbZcg3p9Zzvl0n9d4jpcDsD2QY5nI_-fcCNgpAjfHEtayGjGsnK1VW9SBOS2XDARhfc9pXxdtzKmcMRGNHZ1XIaC4CZL6JVzWdVn4tnEvIsVMADVqfPqeWxirjzC5CbyOcaSerC6dQLYdFKyKhRWM7CW1zSS39w3An7cch4_M2pD6_ZJ1Kg1HrbEDAn1e3NDAhGkMlKTlPQ1XE9CDzIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آتش‌سوزی در تأسیسات نفتی بقیق عربستان
🔹
منابع خبری از آتش‌سوزی گسترده در تأسیسات نفتی بقیق عربستان پس از حملات پهپادی و موشکی خبر دادند./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/675741" target="_blank">📅 14:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675740">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0abee407f.mp4?token=uGXlCCK-3tj8Gqios3_BE1-64H8Z18qtEBkTByklbdxrjga-UXwb4ccV1D3y_HIH6mxQNQ59WJb25aOl8tSAAtZolPMIXdNrtv-yntP_0SCgpD9BhLlUUxcUlBARIk-I5k7IJzF9DQvA7AZ5RhApXTG8BSY6eCi7irauHiXOffQcLd6AxuW19L8zYaMypUf6ezc4RAaznTtUnCkSV7vng5nb16KA02sPfDG7N9M3vrvWnZN2dnA859Fkbg3XYoyOc4i2XjhQpLSCCPwjR99f6kM-P7CH0OcIvOIAWbymR_9EScE3v2jrKC03dVUYO-VZdPLQQhCUpxpCCRLvkfPFGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0abee407f.mp4?token=uGXlCCK-3tj8Gqios3_BE1-64H8Z18qtEBkTByklbdxrjga-UXwb4ccV1D3y_HIH6mxQNQ59WJb25aOl8tSAAtZolPMIXdNrtv-yntP_0SCgpD9BhLlUUxcUlBARIk-I5k7IJzF9DQvA7AZ5RhApXTG8BSY6eCi7irauHiXOffQcLd6AxuW19L8zYaMypUf6ezc4RAaznTtUnCkSV7vng5nb16KA02sPfDG7N9M3vrvWnZN2dnA859Fkbg3XYoyOc4i2XjhQpLSCCPwjR99f6kM-P7CH0OcIvOIAWbymR_9EScE3v2jrKC03dVUYO-VZdPLQQhCUpxpCCRLvkfPFGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای نشان می‌دهند که آتش‌سوزی ناشی از حملات یمن به پالایشگاه جیزان در عربستان، در حال گسترش است و اکنون تقریباً کل پالایشگاه را در بر گرفته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/675740" target="_blank">📅 14:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675739">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
افکار عمومی آمریکا در جنگ ایران علیه ترامپ شد
🔹
در آخرین نظرسنجی سی‌بی‌اس نیوز، آمار بدی برای ترامپ در مورد اقتصاد و ایران وجود دارد.
🔹
یک نظرسنجی جدید سی‌بی‌اس نیوز نشان داد که ۶۵ درصد از آمریکایی‌ها از نحوه مدیریت اقتصاد و ۷۱ درصد از نحوه مدیریت تورم توسط ترامپ ناراضی هستند.
🔹
۶۳ درصد هم فکر می‌کنند که جنگ در ایران برای آمریکا بد پیش می‌رود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/675739" target="_blank">📅 14:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675738">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_IaatnU7Lz__Exvhu1-FL3ywNVwIAgKNg3vG77ywUM3o6KDY9_HT6pyA4SZJg2RXCGpPxjcW62s9TD4kpaGyZsg2nFD2pxuTemCHigI6-Um5-1X0y1oKwf2WAyy9uJHMpsaz6hTzcItIDJHjHWemGxPMmhyQqMKv61WOfyvCDz5PpQYwZMnYC6dixbm2dXGGHfY3aAfCJn249TtpyZJL68NjpuZTp7Jf9x9a4X_9xKsOYOLglFH-O0Fqftuo-_Bl7gRVy0cc0l_FIFEI2rtP4hLI8h0zEznE3WP4zCaoTFzRY-1M3XFQOtwrYUfeKK-c8vDcU3M3OZBIBu_pnePxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
ایران، خانه مشترک همه ماست؛ سرزمینی با فرهنگ‌ها، شهرها و لهجه‌های گوناگون که هرکدام بخشی از هویت آن را شکل داده‌اند. هر اقدام کوچک ما، از حفظ محیط زیست و مصرف بهینه انرژی تا همراهی و همدلی با هموطنان جنوبی‌مان، می‌تواند نشانه‌ای از مسئولیت و عشق به ایران باشد. شما برای ایران چه کاری انجام می‌دهید؟
🔹
همراهان گرامی خبرفوری؛ برای پیوستن به این پویش، یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کنید و با نام و لهجه شهر خودتان بگویید:
«من ... هستم از ... و ایران را دوست دارم، چون ... و به خاطر ایران میخواهم...»
🔸
پیام صوتی خود را با دلیلی که باعث می‌شود ایران را دوست داشته باشید، به آیدی‌های زیر ارسال کنید
👇
#همه_باهم_برای_ایران
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/675738" target="_blank">📅 14:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675737">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
اژه‌ای: ضوابط اضطراری زمان جنگ نباید در شرایط غیرجنگی عادی‌سازی و تداوم یابد.
🔹
فرماندار مهران: در ۱۲ ساعت گذشته ۱۰۷ هزار زائر از مرز مهران تردد داشته‌اند.
🔹
فرمانداری بندرلنگه: احتمال شنیده شدن صدای انفجارهای کنترل شده در این شهرستان وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/675737" target="_blank">📅 14:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675736">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نسخه مردم و نخبگان برای نیمکت تیم ملی/ خداحافظی با قلعه نویی و رفقا یا ادامه فعالیت؟
🔹
گزارش خبرفوری در مورد نتایج تیم ملی و توقف یا ادامه همکاری با کادر فنی فعلی به رهبری امیر قلعه نویی را باهم ببینیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/675736" target="_blank">📅 14:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675735">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6cb7ebfa9.mp4?token=VWHgcNDgpknrGcLeWmjdmNbboydBkkpbBVItEMM6WkjehPw_zQYrrtTnrBnZNTlh0sDVuCRLNC_psCPIPIRp-Ah4rKzUVnO7xbip5QIjh_QZV9f6asqqzk--MvK472wHFehFtCwJgsab3GvcsqvIK8HTTMnytmpmomzELrjW0Z_oEu_Or7mX5utw3EKKZWzpSIvicKki5iENlGUDdxW3P52seIbbLZe8OKvYifd0nxViVNSZdWG17ZGiCzqms0hXZ0NZ24EDYUZ2f845m7mwkUUmyyGgi-qhPJMVTWFc18kcnU6LC6ASJ5zxglnWLZYKAQrea0XJGBMf7RW_Y86itA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6cb7ebfa9.mp4?token=VWHgcNDgpknrGcLeWmjdmNbboydBkkpbBVItEMM6WkjehPw_zQYrrtTnrBnZNTlh0sDVuCRLNC_psCPIPIRp-Ah4rKzUVnO7xbip5QIjh_QZV9f6asqqzk--MvK472wHFehFtCwJgsab3GvcsqvIK8HTTMnytmpmomzELrjW0Z_oEu_Or7mX5utw3EKKZWzpSIvicKki5iENlGUDdxW3P52seIbbLZe8OKvYifd0nxViVNSZdWG17ZGiCzqms0hXZ0NZ24EDYUZ2f845m7mwkUUmyyGgi-qhPJMVTWFc18kcnU6LC6ASJ5zxglnWLZYKAQrea0XJGBMf7RW_Y86itA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود سگ‌های رباتیک به آموزش‌های رزمی ارتش چین
🔹
سگ‌های رباتیک در کنار سربازان چینی در حال آموزش هستند و برای مأموریت‌های رزمی، شناسایی و پشتیبانی به کار گرفته می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/675735" target="_blank">📅 14:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675734">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
صداوسیما: علت حادثه، آتش گرفتن انبار ضایعات پشت هتل استقلال بود
🔹
این حادثه تلفات جانی نداشت فقط ۳ نفر دچار دودزدگی شدند.
🔹
آتش‌سوزی در حال مهار شدن است.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/675734" target="_blank">📅 14:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675733">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
رسانه‌های عبری: هواپیمای نتانیاهو پس از رهگیری دو پهپاد در مرز اردن، از یک پایگاه در نقب به مقصد واشنگتن به پرواز درآمد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/675733" target="_blank">📅 14:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675729">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYiKJDv_I-R5k7xPxDi5HTIiFGLDaHJ49aGsgD31YbnxMsWZ5qlJ_BX9qYdEn1d8u-DrvJVAaoKH3xoPgftUK4DLssOb3_Sc_6-R0oX4R5MwZ4yIIdV7BoRWQls16CktWGR9DRy5S-QpPHrPCfygx5M1_LGwZmO7IQQquqAA-KKiN-L0ap6rGecMUX9DHBOWbFiHgV-e7i1wDgzq015ts1kZQl9CHBdUqqcOVOMahQYgYoXcAY8j9JKbGy17nAofCHFvz3eQ-lP0aCtGqJfOLMqcFnlyAHuuHF1Dzje5mije1FgXrWevUo5C-OY8GmqGddxXimlZnFgJHuaMgxQq8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8_YhiGkNb61BtsdK-e0x-kQrqX62InPJwZuIyZpiCi_P977vlgGLhK9xHE-rYrNb5rHRr3AHFnQYQLFJ3NeD3vZi7P6ICGVPYl5sFYz_-Wf0V3zqc3re55JiMRbpIp_O3FmjoF-piCM0PWF6BeASGUkwBncyEJ4bvQar941kKs4DBBujPYMv0IaC5wjh3zLfwT6LpTaNTJLO9iI2HWCttgQsldOAIvGZYHlZQ5qdmcjXZBY6n6uEG2FRy_JJZY3a1ORDx3jiO9Kein0d8-x2bNdY-_pSVPRG7Mq3PyZTLfoYU_j2rjObQMNdEdlZER7NvtP02o9OxmZqNg7bDRAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSWrXGYWVMTYL_7zj7IUipnAcBy1dSxd1AyPCNy4bh6zdQIVSYsPUAkX3cdBhmcBSMwAEPz4uZFBOeLM8OftBqpizrkTlMKlGnB0MLpyHzp5zP_3wteYBoJxuqqB2_qgURIBm-c8CEAshrSBk7LRDmRUCHxqIEgK2OpZtcbWLfEMkgqDTyk5nVbmU1S7KShdzc9xsPQECtwL8qJmWw36AwmY05ihw4F_oEuHdRt_0GNCnEKTTs_DGogJ8DMjwq3_WQtbBR76BTB0iaKe5-UQBU10406d87xLBTj10dC3r8cHm2w-kWHqB5yc1kIF1p1mkQcz4Ed7mEzVCssIQpvDeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGk4vCxld4G4ProAj8ykksuc3J2ylNjTnSllf_QedRW9swfv3BGknP93bI5IeiEIgbFaW2IfyRQvMufAH3vIvbcWyZ7xn9l3glfNR4UOGt875R_9UV8h4EU-fwRcyoBJKwiuhJ0Nir_jN3pG5OqPHxZiMIsIxV_jJDpxL1vD_6LYEhFpqd6buOKIJYEXzIIB56nfDxCsjBYmGCq9_Btdq1p3fmXk_gy14oEI66x7MFc6EiiPEAjEoEGHwblVUIZPAqi8Pv13aeMtJ8D48dfQUDvDD6zOpo50sohrRRL49NV9uZ5GyUA0kibLxsfag7ohduTAO5ZKR1lNOVz7SEivZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۴نوشیدنی برای کاهش استرس؛ کورتیزول رو پایین بیار
🥤
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/675729" target="_blank">📅 14:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675728">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ادعای‌ رسانه‌های عربی: نتانیاهو به واشنگتن رفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/675728" target="_blank">📅 14:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675727">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
اورژانس تهران: خوشبختانه تا این لحظه هیچ مصدومی به اورژانس گزارش نشده است  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/675727" target="_blank">📅 14:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675726">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgIbKf1flRbBui-Xwv9pOOHxrA2zLvkwJme3CIafaNiLH04kf6HODcIyTstlYEayx35UNqY1-9hGQaiewsGDSbdidYjdz5WDMC-gx8qa5IfLPCVtvXmfXKkAQ62ANcFswL8So8cTjm3ctuhUut1zt-fKMdCNuXAmnc6Na2O5CC40laJqZwnlHRNLrGdCtKWuWHVOeIQNr5rG0waDmHrcfzehJQnMQQ3I__VAV5GW1wLn4ogOqt-KCyR30Fn8O0n6lWOL2N4cw2mYxVFDsRtcJ-kLsHvpAearkfjS0smE5tystnApp0kLenvGOZRZm9dMuaBw7ELjBP4WLrBC-Er40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش ویژه اقساطی KMC Eagle
شرکت واسپاری کرمان موتور
▫️
تحویل فوری
▫️
اقساط ۱۲ و ۲۴ ماهه
▫️
دریافت اطلاعات بیشتر و ثبت نام
02144998204
-8
https://kmc-leasing.com/kmc-eagle-sale
▫️
لینک کانال:
https://t.me/kmc_leasing
#واسپاری_کرمان_موتور
#لیزینگ</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/675726" target="_blank">📅 14:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675725">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
نمایی از ستون‌های دود در پایگاه تروریست‌های تجزیه طلب در کردستان عراق
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/675725" target="_blank">📅 14:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675724">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cca4SuEyB-ce8_Bn5kUf19pqHfsudN5bHU76CKrbsDhhp2kAey8zH5QL1PjPBgKaMnRv---iYFSIkDS4HKIGAhzPwD3NylxJ4bDado-NIRxPxlyANel4ehEyTlecSk0SzD5RkkqqHrYNxVi3lg12TolB3xYcqzhV3OcG051bihKfnekYRFFj7s2Aro2MhOCwhgGtYeUVSDLgdSRk-SR3m5Phe4nc6PJ8ZX0MB1rjTG_S0bZmRebe3XLSlgySm9iG-Qs6IAkP48JasWtoEwkyjxkOJqR6tULhbrFuNQQ6Z72g2TDPNKg2niDCOtckuTthFZX7sOQlXqtb-rRf0mYZ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعویق مبهم سفر نتانیاهو به واشنگتن
🔹
دفتر نخست‌وزیر رژیم صهیونیستی از به تعویق افتادن سفر وی به واشنگتن خبر داد، اما بدون ارائه توضیحی درباره علت این تصمیم، زمان جدیدی برای انجام این سفر اعلام نکرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/675724" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675723">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
افزایش سقف سوخت‌گیری کارت آزاد در ۳ استان مرزی همزمان با اربعین
🔹
سقف هر نوبت سوخت‌گیری با کارت آزاد جایگاه‌ها در استان‌های کردستان، کرمانشاه و خوزستان به‌زودی و در آستانه اربعین از ۱۵ لیتر به ۳۰ لیتر افزایش می‌یابد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/675723" target="_blank">📅 13:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675722">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6457b66f1a.mp4?token=s78lLB67DTgZxHLIdNBKKtHPzCCUp6suDkTfzC6w4g5NFAKrWwcwD_ULQ72fbgBU1O9Cn_S7nxGwPTvxC76VBJqcRIRp13JrJN87iYoNf5yyA6h3QaOS4QbpvswpuPQyi24zAS2reAkUV2KpKncpKnnuaSKLGIFq3AxP1FCOCq2jNIORg0irSpvrWEtMP3013A-4M35xoKASwplJTvKrH2L9sJ2-UMrOFpUQO8XiZA_oHVorX3eFJLxRsf_H2R3Tjkn_M4TeyYmF-ghM-19tHifiJanusmJiZg2Nx94vzjppAb0Xzy-_ARkBQOkewG1hixtBX-beeWyHOkAPz1LwJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6457b66f1a.mp4?token=s78lLB67DTgZxHLIdNBKKtHPzCCUp6suDkTfzC6w4g5NFAKrWwcwD_ULQ72fbgBU1O9Cn_S7nxGwPTvxC76VBJqcRIRp13JrJN87iYoNf5yyA6h3QaOS4QbpvswpuPQyi24zAS2reAkUV2KpKncpKnnuaSKLGIFq3AxP1FCOCq2jNIORg0irSpvrWEtMP3013A-4M35xoKASwplJTvKrH2L9sJ2-UMrOFpUQO8XiZA_oHVorX3eFJLxRsf_H2R3Tjkn_M4TeyYmF-ghM-19tHifiJanusmJiZg2Nx94vzjppAb0Xzy-_ARkBQOkewG1hixtBX-beeWyHOkAPz1LwJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سکته قلبی ربات انسان‌نمای کوالکام روی صحنه!
🔹
ربات انسان‌نمای حاضر در مراسم معرفی پلتفرم رباتیک Dragonwing IQ10 کوالکام در نمایشگاه Computex 2026 هنگام اجرای زنده دچار اختلال شد و پس از از دست دادن تعادل، روی صحنه سقوط کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/675722" target="_blank">📅 13:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675721">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/267bf92a51.mp4?token=Nn7RlTP5cKc7Cfc1eBjH3MJ_eszRLbf2ZXcoqBF3muXB68osEErMtlRp2-b3aukEiiDDLwYFlbvaDTsD13AYJFEstxyamjqx-U3XGD22b788HpPjNTcsRgPF-1yEJDMdDtESZ1jPSzhJ_wOhjKMq8Sz5ltjqwTGU9igvgYN1TMt1Ti-02RRFfHacEGoZC3cy5NBYYRLHcFKPiVFYMaREj4q_qpY1hlq88SXwOmDV9txoS4ZpKm4V3U78o37jIt6SE7ei3hFaxFJjlvuBnrNLrAUf64N3nMog98RmVSk4z5zWip7yzYTT99F_UCB_bhEaT8sVDss1KEppSgowRemuJVF0n3AWCWqxiP3tr4jvLc5uYwkPQJtbw1s-aJltAX6wuDA0HIDqFau94hWS3sx30_gMzUC-uAXv8TjWDaETCZll-i4CPoJlV5bidS0AO9s1N9cgtoiMV3ikyn0HLOEL53MGwJeBQar_QaBQe-NkIGDiQD-zcwCgsx10Qboy_3BJ3KoihmyH15jWdHaR11asJS0r43CJN99EboobjpFjF3PKJtfmqHEGwQYQpBv2jzRyfA9c6Ko62mCqr8xxPzK8uxBZ_47GUhiY2_ndt5CdRRKPoKEXWuEc9FtWoVOnrcl6L9kO24s7wx5F1Ksc1dPgVhOnvGPm4sJ6hn2UUNoZAG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/267bf92a51.mp4?token=Nn7RlTP5cKc7Cfc1eBjH3MJ_eszRLbf2ZXcoqBF3muXB68osEErMtlRp2-b3aukEiiDDLwYFlbvaDTsD13AYJFEstxyamjqx-U3XGD22b788HpPjNTcsRgPF-1yEJDMdDtESZ1jPSzhJ_wOhjKMq8Sz5ltjqwTGU9igvgYN1TMt1Ti-02RRFfHacEGoZC3cy5NBYYRLHcFKPiVFYMaREj4q_qpY1hlq88SXwOmDV9txoS4ZpKm4V3U78o37jIt6SE7ei3hFaxFJjlvuBnrNLrAUf64N3nMog98RmVSk4z5zWip7yzYTT99F_UCB_bhEaT8sVDss1KEppSgowRemuJVF0n3AWCWqxiP3tr4jvLc5uYwkPQJtbw1s-aJltAX6wuDA0HIDqFau94hWS3sx30_gMzUC-uAXv8TjWDaETCZll-i4CPoJlV5bidS0AO9s1N9cgtoiMV3ikyn0HLOEL53MGwJeBQar_QaBQe-NkIGDiQD-zcwCgsx10Qboy_3BJ3KoihmyH15jWdHaR11asJS0r43CJN99EboobjpFjF3PKJtfmqHEGwQYQpBv2jzRyfA9c6Ko62mCqr8xxPzK8uxBZ_47GUhiY2_ndt5CdRRKPoKEXWuEc9FtWoVOnrcl6L9kO24s7wx5F1Ksc1dPgVhOnvGPm4sJ6hn2UUNoZAG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افزایش سرمایه فارس تصویب شد، مجمع فوق العاده به نصاب نرسید
🔹
در مجمع عمومی فوق‌العاده شرکت صنایع پتروشیمی خلیج‌فارس، افزایش ۲۵ هزار میلیاردی فارس به تصویب رسید و کام بیش از ۴۰ میلیون سهامدار این شرکت با سهام جایزه شیرین خواهد شد.
🔹
مجمع عمومی عادی بطور فوق العاده فارس که با دستور انتخاب اعضای حقوقی این شرکت قرار بود برگزار شود اما به دلیل به حد نصاب نرسیدن قانونی به زمان دیگری موکول شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/675721" target="_blank">📅 13:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675720">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NStVrmBuRfXCuo_j8ug1Jb0dqXjpCZoMfl0J-8JayfEdgukUwWr9dKCA4hwvplVsQ1HjeS_yiG7R33dDV4z9UKyu96r2MqZVZkXnwq2LNK04k3WiA94bP8V4p3P5tnzpuQVBBw1joG0tMnKOyPbSDWnYlprKP3upEAguAX1V9jFKPKXeDEfNqmGres7g_hCOvhP2b1evxrYtj6ut561il6UNenuIH2j9WkxXY1SCeFdrzHXIGqogtCOzo8FvINgScKFHlJDo8kDQm0-HHTF5-yYxu2LLloDbS3QivFnHR22Q9sksxsJB7FfjjbZpS2ozAoj9e-uFAbF4gSKtDdGx7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از حضور رهبر معظم انقلاب اسلامی در اربعین سال گذشته
/ فارس‌پلاس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/675720" target="_blank">📅 13:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675719">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس مجلس لبنان: هیچ مسیری جز آتش‌بس و عقب‌نشینی کامل اسرائیل را نمی‌پذیریم.
🔹
فعالیت دریایی در گیلان از امروز تا سه شنبه ممنوع شد.
🔹
انحراف لحظه‌ای هواپیمای تهران–شیراز؛ مسافران در سلامت کامل هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/675719" target="_blank">📅 13:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675718">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
آتش‌سوزی در هتل پارسیان استقلال/ هتل در حال تخلیه است  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/675718" target="_blank">📅 13:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675717">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a22e1cedb.mp4?token=SDux2VquZXotxZRl9eZ7hHn7FPT432W0SvyCL9qKdZxg0nYcMeuVCFJKEa4Ntu_Hv9VL4d_8aBhYOHEkrDIzom6zslK4pyOX0p0aAeqDXbsJ3L8nXdDq5nHGILbmJxWvpBfamPUaH8kZQ_XmqEv1ArJQV7FQu1t4fv6JkGtXJA5B4qSRkODRtOaKbR8x3LReqMGtkpYENVindg0biQ6dFAhqBdkqFTuZw_g3X63ZUYsHDs2eL_HYH2_V8-nQzMVSnMA3UoKmw1uOpr_k02DkrlnjR8UtxLGwQsizXVRwJBR1UIN7w8dV9o--pNP2NHBlpl_Ib3JoDHQMUqfaxC7afA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a22e1cedb.mp4?token=SDux2VquZXotxZRl9eZ7hHn7FPT432W0SvyCL9qKdZxg0nYcMeuVCFJKEa4Ntu_Hv9VL4d_8aBhYOHEkrDIzom6zslK4pyOX0p0aAeqDXbsJ3L8nXdDq5nHGILbmJxWvpBfamPUaH8kZQ_XmqEv1ArJQV7FQu1t4fv6JkGtXJA5B4qSRkODRtOaKbR8x3LReqMGtkpYENVindg0biQ6dFAhqBdkqFTuZw_g3X63ZUYsHDs2eL_HYH2_V8-nQzMVSnMA3UoKmw1uOpr_k02DkrlnjR8UtxLGwQsizXVRwJBR1UIN7w8dV9o--pNP2NHBlpl_Ib3JoDHQMUqfaxC7afA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخی منابع خبری دقایقی پیش از وقوع انفجار در اربیل عراق خبر دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/675717" target="_blank">📅 13:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675716">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbCzlPGUAFt74Cwp2DmYC49prULjq9vr2B6R6WJkLyjzNDzLL0_aCOjw4KMiblFCfuHLcm0ubgldkQFsMUSEsPErh6-HfPkz2YoKkU8XrB-mdlNCeodEc_Wa54g3Ti2uuV77i2M-u7tG-tjnsKysIYTueGcgaj4NUtUWSuMI5EJ1swfHFTzBQ7Ijs6B5rbMW3GNvPA4ygtPZQw19NaMJSQjp49VNhIheeAE2yv3HFgZK2ct_d1EttKCai6CJ1d8bgn7In7ThfH9U-pT24YzuBiyaybLfe9UH5jdkx2PB8mISSiypSF5JnonrgRs1jLYz9uvZQcwzrWulIWXZazDFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت روز طلا در ۵ مرداد ماه
🔹
بازار طلا امروز همچنان در محدوده‌های حساس قیمتی حرکت می‌کند.
🔹
قیمت‌های اعلام‌شده از اپلیکیشن میلی، به‌ عنوان مرجع قیمت معاملاتی طلا استخراج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/675716" target="_blank">📅 13:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675715">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
برخی منابع خبری دقایقی پیش از وقوع انفجار در اربیل عراق خبر دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/675715" target="_blank">📅 13:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675714">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
منابع عربی: شنیده شدن صداهای انفجار در اردن
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/675714" target="_blank">📅 13:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675713">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0151cde69f.mp4?token=fUe036rR6B-NXkZkTiYouq1UCafY6ErVk4swzq2CMbSueHUcKdQ7P3sF9q4Hddi2mc8u9Qt4OKLfSrqM7D_XLtgmnF_6fEMQDtOZK_XPuu13bKqZ2dt7Ji4A3iitTTZnSS1ZfgZKbY_FK2pWwWu0mTx4WG6CV2SHbEvEwbf9YygBt4guhnqUsXl7TFE2EOVCdSZKz_yeeHD5IC-p9uTdiJCy8KeBVWwU6FaZ84pkqLFpvkJCJ9g4B5vjYvu2l1nfH5IENjWvp_eh4inCJZ5bjP3_LPugLn9U7jtMUivy9ieHbfqKO_foZcMS24KpkqQDMseBnrzHtFb2jhrw1Sxs5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0151cde69f.mp4?token=fUe036rR6B-NXkZkTiYouq1UCafY6ErVk4swzq2CMbSueHUcKdQ7P3sF9q4Hddi2mc8u9Qt4OKLfSrqM7D_XLtgmnF_6fEMQDtOZK_XPuu13bKqZ2dt7Ji4A3iitTTZnSS1ZfgZKbY_FK2pWwWu0mTx4WG6CV2SHbEvEwbf9YygBt4guhnqUsXl7TFE2EOVCdSZKz_yeeHD5IC-p9uTdiJCy8KeBVWwU6FaZ84pkqLFpvkJCJ9g4B5vjYvu2l1nfH5IENjWvp_eh4inCJZ5bjP3_LPugLn9U7jtMUivy9ieHbfqKO_foZcMS24KpkqQDMseBnrzHtFb2jhrw1Sxs5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظۀ دستگیری باند سرقت موتورسیکلت
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/675713" target="_blank">📅 13:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675712">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
منابع عربی: شنیده شدن صداهای انفجار در اردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/675712" target="_blank">📅 12:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675711">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521fe5e501.mp4?token=roFqllRbyQwRmcwQjNtiu8eCzd4J-U2oKX9e1hXan3NRlHVsaj9InfGgcS2mdE0mIuujeyb8KLBSnUdt5IJdJTmC1vrr9XSadanlv6FYyXh9joXzAowJ9vufvS4WQUb8C-4BmaH4CIm3RS3IZ-2k3IMxSsHlkNbVi77NzyxRKlmZMumyV54zvak66Dvm2SbDFPHQBQaff7nloutlGcGaxwwKW_guLUIhuwBDztF9lO0DktaK00xgrPrXeyc0Ie5wvzx6JqpvAwpgYKmhABdLST9YsiqzMt7bxbZvmZSALZxiXhIkzP2wTdbEZBrfu3-0M2bIeba0B4ke-s5Sh9Sscw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521fe5e501.mp4?token=roFqllRbyQwRmcwQjNtiu8eCzd4J-U2oKX9e1hXan3NRlHVsaj9InfGgcS2mdE0mIuujeyb8KLBSnUdt5IJdJTmC1vrr9XSadanlv6FYyXh9joXzAowJ9vufvS4WQUb8C-4BmaH4CIm3RS3IZ-2k3IMxSsHlkNbVi77NzyxRKlmZMumyV54zvak66Dvm2SbDFPHQBQaff7nloutlGcGaxwwKW_guLUIhuwBDztF9lO0DktaK00xgrPrXeyc0Ie5wvzx6JqpvAwpgYKmhABdLST9YsiqzMt7bxbZvmZSALZxiXhIkzP2wTdbEZBrfu3-0M2bIeba0B4ke-s5Sh9Sscw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در هتل پارسیان استقلال/ هتل در حال تخلیه است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/675711" target="_blank">📅 12:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675710">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
دفتر نتانیاهو: نخست وزیر رژیم صهیونیستی روز دوشنبه به دعوت ترامپ عازم واشنگتن خواهد شد
🔹
او روز سه‌شنبه در کاخ سفید با دونالد ترامپ، رئیس‌جمهور آمریکا دیدار و در مراسم تشییع لیندسی گراهام شرکت خواهد کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/675710" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675709">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3556924e.mp4?token=Vr8P9Wf2-xfDboh5xQ17YkK_MZ4vC4rtmbCOdJfNJW7ueLX2aMMu5wW0Ub7_ZGWt6eHVG1GeeXwjWgW8HdIb5Dyu-kX-CSFh1rH2t358J6APLLfUu1_c5OXAgBshrUwYoQYcyoB5iM1BC6CA035b2f8FWFgpKL5dwsxz8DWvNBik5sWGTmsCsF02L2dV1CNqImhb9nrjRDUanuiDeZVyQTC5bldZIvmmtZZM17mnr-zYf9jDkfxn_BrrB9IEI8pqPFRlK4PJZX_YD7B3YFBWUjxcBroNKwI8897gb9k_2WPR5Tx-CZSVYzaISlIdTjtC1eZWYC2BhGHRxK_gl1DlhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3556924e.mp4?token=Vr8P9Wf2-xfDboh5xQ17YkK_MZ4vC4rtmbCOdJfNJW7ueLX2aMMu5wW0Ub7_ZGWt6eHVG1GeeXwjWgW8HdIb5Dyu-kX-CSFh1rH2t358J6APLLfUu1_c5OXAgBshrUwYoQYcyoB5iM1BC6CA035b2f8FWFgpKL5dwsxz8DWvNBik5sWGTmsCsF02L2dV1CNqImhb9nrjRDUanuiDeZVyQTC5bldZIvmmtZZM17mnr-zYf9jDkfxn_BrrB9IEI8pqPFRlK4PJZX_YD7B3YFBWUjxcBroNKwI8897gb9k_2WPR5Tx-CZSVYzaISlIdTjtC1eZWYC2BhGHRxK_gl1DlhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات معجزه‌آسای رکابزن آمریکایی از سقوط مرگبار
🔹
رکابزن آمریکایی، در یکی از دلهره‌آورترین لحظات تور دو فرانس ۲۰۲۶ پس از برخورد با گاردریل، تنها چند سانتی‌متر با سقوطی مرگبار در مسیر آلپ دوئز فاصله داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/675709" target="_blank">📅 12:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675708">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMpokTmbQ5KRhgS54cxEi2tF5OKhb3Pg0JEG5n5e8LeLfjdc08bRBGEsMm9fSbu4TObqPZ3IpnZ3CLLnmRMQIAcBbQ0s1DT0LYi9ebXkCEyYEZFCDkdqIGNu86ap9G6ySgApVt0Vaee7p4Y40xUXakHFKiuCbgDrHERcT_2QJEFNM-tWuC3n7ztNPZBmIW4yti2vjgCv2w5Pfuq18bIK-dGitxkpTwS0sDsv3Qwd67QGYv75Uu_xzEOY9LBNCJ_4MnWGx48v1LmVfeN6Mfe66TQ2XcEtk7Q9f0DRWgEc7teS9voNaGFVLggiHiXgfVcQ9bixFKbBC5UYaPJalSIJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در جریان معاملات امروز شاخص کل‌ بورس با رشد ۴۹ هزار و ۷۱۳ واحد در ارتفاع ۵ میلیون و ۵۲ هزار واحدی قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/675708" target="_blank">📅 12:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675707">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
فرمانداری امیدیهٔ خوزستان: درپی انهدام مهمات عمل‌نکرده در شهرستان، احتمال شنیدن صدای انفجار در امروز وجود دارد
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/675707" target="_blank">📅 12:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675706">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/903e392b5f.mp4?token=cC18MH5Hy5ekI9AiSU3gumDq68USHYSaTFjDVaLqvOYwWnsP8cZEldrWg5uMkHEdHoH-Ky65ejwMNJ_IdGNWj0RAy1vDqjReXDopQNrGuij3hYgamxS_bYRCYiqbmEuUf0FhmykCp_oR8T4YoFTqKE3snXW20rBcFaC-U4viBqPA7zOTJETi-VwtnT9HrJl0Lcx2bTvsLGYGBGBxnXFc9DQgGP4Y_9uzuUuRAYbvmhDlXG2qnNH-jufBoNtVpRWkMWpjrGVqvtGDnIy17o-XGnV4J5Sy3YtPZhZtv_gOLTzUtw6Kar4FFXPN7gV0U20lp3kxYIK8-dcyomzcJyYIYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/903e392b5f.mp4?token=cC18MH5Hy5ekI9AiSU3gumDq68USHYSaTFjDVaLqvOYwWnsP8cZEldrWg5uMkHEdHoH-Ky65ejwMNJ_IdGNWj0RAy1vDqjReXDopQNrGuij3hYgamxS_bYRCYiqbmEuUf0FhmykCp_oR8T4YoFTqKE3snXW20rBcFaC-U4viBqPA7zOTJETi-VwtnT9HrJl0Lcx2bTvsLGYGBGBxnXFc9DQgGP4Y_9uzuUuRAYbvmhDlXG2qnNH-jufBoNtVpRWkMWpjrGVqvtGDnIy17o-XGnV4J5Sy3YtPZhZtv_gOLTzUtw6Kar4FFXPN7gV0U20lp3kxYIK8-dcyomzcJyYIYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داخل خانه یک مرد ۷۰ ساله هلندی؛ مردی که ۹ سال با افسردگی زندگی کرد و کسی را به خانه‌اش راه نداد. او تنها برای خرید روزانه از خانه خارج می‌شد تا اینکه هفته گذشته سرانجام درخواست کمک کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/675706" target="_blank">📅 12:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675705">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سلامت نوزاد قربانی تولد در تاریخ رُند؟
🔹
رئیس انجمن متخصصان زنان و زایمان ایران:
همزمان با تاریخ رُند ۱۴۰۵/۵/۵ درخواست سزارین برای تولد در این تاریخ افزایش یافته؛ اقدامی که به گفته پزشکان می‌تواند سلامت مادر و نوزاد را به خطر بیندازد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/675705" target="_blank">📅 12:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675704">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3feb1c9424.mp4?token=jIrkTYhz490MTQU7RaneUonFnbSY_p8EoMKnXPhWkjcTne2OciS-LfBfqTw6Yz2mupWixQqS7q6eUrdN661PIfnuBl5VR1KYxnNvsUzlHjr8GZvMQNLyOsmj0WrG4CxIcX667d7uo5oF43ntjBM3NsJw1LVO8LlesZUXfzV28906Zs46nLO5O515wa4Z6hD7_jX9CoZgjP8VAGS-9OZ7KFktv-CU9zisN_8hrvAvHeqD1YpA53Sql9xSgrLgwqWBVXovcii179Mf9EEveHBQxZ_1F1VOmmxLjy1K-wo7qubveTBFOPs2wlThtkFcoPM7Ke65ob0YLVrJPMkVn_V4HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3feb1c9424.mp4?token=jIrkTYhz490MTQU7RaneUonFnbSY_p8EoMKnXPhWkjcTne2OciS-LfBfqTw6Yz2mupWixQqS7q6eUrdN661PIfnuBl5VR1KYxnNvsUzlHjr8GZvMQNLyOsmj0WrG4CxIcX667d7uo5oF43ntjBM3NsJw1LVO8LlesZUXfzV28906Zs46nLO5O515wa4Z6hD7_jX9CoZgjP8VAGS-9OZ7KFktv-CU9zisN_8hrvAvHeqD1YpA53Sql9xSgrLgwqWBVXovcii179Mf9EEveHBQxZ_1F1VOmmxLjy1K-wo7qubveTBFOPs2wlThtkFcoPM7Ke65ob0YLVrJPMkVn_V4HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این روش ساده، انگور بدون هسته بکارید؛ کشاورزی در خانه
🍇
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/675704" target="_blank">📅 12:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675703">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d875a96f83.mp4?token=rmSDBQnjeL_3Kdjcyk_qaGRZtfSsxC71JCN2FOz7w3HmD_szLWgkk07S4oFgtfLHhkQN1v8k__66q1zbWDFgddYrIcCRVXehNQP1ts0umVLO8_kKEQ3Kwsy_A398SWpRHK_hXTKETlXMHeANLHUcd3LhYg86whpsZvOYoP3Lsq2KlkFUAzZ4GTv8yN1a5eSpCpxrAUq5pnwFymjV8r9lI0dJm3kXSc40QCVfGuFK184n5FLH2IA_A383g_9QPwYV09p8n9-lzEJKgCAISrxIvCLeokrmqJmBJr7p8z8Lt0R1BdmY7Yfl288TXQxDicfj1WO_tWU-7CxA9v20xM0LnIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d875a96f83.mp4?token=rmSDBQnjeL_3Kdjcyk_qaGRZtfSsxC71JCN2FOz7w3HmD_szLWgkk07S4oFgtfLHhkQN1v8k__66q1zbWDFgddYrIcCRVXehNQP1ts0umVLO8_kKEQ3Kwsy_A398SWpRHK_hXTKETlXMHeANLHUcd3LhYg86whpsZvOYoP3Lsq2KlkFUAzZ4GTv8yN1a5eSpCpxrAUq5pnwFymjV8r9lI0dJm3kXSc40QCVfGuFK184n5FLH2IA_A383g_9QPwYV09p8n9-lzEJKgCAISrxIvCLeokrmqJmBJr7p8z8Lt0R1BdmY7Yfl288TXQxDicfj1WO_tWU-7CxA9v20xM0LnIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منبع آبی که سند جنایت جنگی ترامپ است
🔹
تخریب منبع آب روستای کوهستک سیریک، زندگی هزاران نفر را سخت کرده است/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/675703" target="_blank">📅 12:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675701">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
عدم حضور سهام عدالت؛ مجمع هلدینگ خلیج‌فارس را از حد نصاب انداخت
🔹
مجمع عمومی عادی به طور فوق‌العاده شرکت صنایع پتروشیمی خلیج فارس، به دلیل عدم حضور برخی سهامداران عمده از جمله سهام عدالت، به حد نصاب قانونی نرسید و امکان برگزاری آن فراهم نشد.
🔹
بر اساس دیدگاه‌های مطرح‌ شده از سوی برخی ناظران، عدم حضور این سهامدار در شرایطی رخ داد که طی روزهای اخیر، علاوه بر حواشی و فشارهای سیاسی پیرامون مدیریت هلدینگ خلیج فارس، ابهاماتی نیز درباره وضعیت مدیریت و نحوه اعمال حقوق مالکانه شرکت‌های سرمایه‌گذاری استانی سهام عدالت و اختلاف‌نظر میان مراجع و دستگاه‌های مسئول در این خصوص مطرح بوده است. از نگاه این ناظران، این شرایط می‌توانست بر فرآیند تصمیم‌گیری مجمع سایه افکند.
🔹
بر همین اساس، برخی تحلیلگران معتقدند سهام عدالت با پرهیز از حضور در مجمع، ترجیح داد تا زمان رفع ابهامات موجود، شفاف شدن وضعیت مدیریتی و فراهم شدن شرایطی عاری از هرگونه شائبه، از اتخاذ تصمیم درباره ترکیب هیأت‌مدیره خودداری کند؛ تصمیمی که به اعتقاد آنان در راستای صیانت از حقوق تمامی سهامداران، به‌ویژه میلیون‌ها دارنده سهام عدالت و سایر سهامداران خرد، قابل ارزیابی است.
🔹
در این چارچوب، به حد نصاب نرسیدن مجمع را می‌توان نه صرفاً یک اتفاق اجرایی، بلکه نشانه‌ای از تأکید سهامداران عمده بر ضرورت حاکمیت شفافیت، ثبات مدیریتی، رعایت الزامات قانونی و حفظ منافع بلندمدت شرکت و تمامی ذی‌نفعان دانست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/675701" target="_blank">📅 12:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675700">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ec3b00a7.mp4?token=vCofemQPKbZBy0ltA-Y3NB0u8OuDTYYGovzeJobOumOtNNj9Z_iEkLR5s47Bpxpm1ZZFcVllV9dweSvFucOo2K64ZjDjXQF4v3WkAEmjUrYzmOCOob95ZYay2QfgLGBeJKNcr8zE1Eakau_YNpvs96MKFLtaVRMJWl8JPeyYRHMaS9lG76yP1VJRCsHBUTLMl_aZHVMerMne6-64-qqLwuqLiUV9N3CzyVCJidHp62ZitJPzHi8uEUEgdtJPOKWuw4LcpF0Jmb1ObjhCWrlSeZv0J_yivpxzaGuAVAVy-37QzHg9Zb9ZliOkgAg_6VU2KK5-hm0jmGnORQQfft-Qqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ec3b00a7.mp4?token=vCofemQPKbZBy0ltA-Y3NB0u8OuDTYYGovzeJobOumOtNNj9Z_iEkLR5s47Bpxpm1ZZFcVllV9dweSvFucOo2K64ZjDjXQF4v3WkAEmjUrYzmOCOob95ZYay2QfgLGBeJKNcr8zE1Eakau_YNpvs96MKFLtaVRMJWl8JPeyYRHMaS9lG76yP1VJRCsHBUTLMl_aZHVMerMne6-64-qqLwuqLiUV9N3CzyVCJidHp62ZitJPzHi8uEUEgdtJPOKWuw4LcpF0Jmb1ObjhCWrlSeZv0J_yivpxzaGuAVAVy-37QzHg9Zb9ZliOkgAg_6VU2KK5-hm0jmGnORQQfft-Qqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اطرافیان ما بیشتر از چیزی که فکر می‌کنید بر سلامت‌روان‌مون تاثیر دارن #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/675700" target="_blank">📅 12:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675699">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e834c6b9.mp4?token=HGnNYDL11AeUFJBscbjbauyOP33_HiNpuReDmbNENgNTU4fY1pNiIwhoboAe73Pj507WVOLYX5ZroVnM5MPQdrtpvOEmqUEFXH2JACJcsT2Ur-2HIrzvtsrsT2f9J22chcl3KM3vFeh2O7la5HpuE7Ngd4hDgWzBtraWNwf04YvxtBoOjFw9XlZuICdn8EpSwhEYgcXiXvyMq1HX0M1_YdfHRIrkFC5BuY8grioa_waGbm9tA18lm_WcFuQrGLVsfcB7s8gyI2OGJKeW6_Z_kY2FOj8ifHIRgENKuSYvy7QPaJyfdMNjpPByHPxqbSngXkXk5ddP8zp3kP-PW__8kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e834c6b9.mp4?token=HGnNYDL11AeUFJBscbjbauyOP33_HiNpuReDmbNENgNTU4fY1pNiIwhoboAe73Pj507WVOLYX5ZroVnM5MPQdrtpvOEmqUEFXH2JACJcsT2Ur-2HIrzvtsrsT2f9J22chcl3KM3vFeh2O7la5HpuE7Ngd4hDgWzBtraWNwf04YvxtBoOjFw9XlZuICdn8EpSwhEYgcXiXvyMq1HX0M1_YdfHRIrkFC5BuY8grioa_waGbm9tA18lm_WcFuQrGLVsfcB7s8gyI2OGJKeW6_Z_kY2FOj8ifHIRgENKuSYvy7QPaJyfdMNjpPByHPxqbSngXkXk5ddP8zp3kP-PW__8kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
#تماشا_کنید
💎
تسهیلات
طرح کارنو بانک تجارت
ابزاری ویژه برای حمایت از کارکنان شرکت‌ها
🎯
سبدی از خدمات متنوع اعتباری برای نیازهای گوناگون
🔗
تا سقف ۲ میلیارد و ۴۵۰ میلیون تومان تأمین مالی
📌
📞
برای اطلاعات بیشتر به شعب بانک تجارت مراجعه کرده و یا با مرکز ارتباط مشتریان این بانک به شماره ۱۵۵۴ تماس بگیرید.
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/675699" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675695">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f4ecd59a.mp4?token=MpO07SmkIhPlykGZVBblThT2k9VtAhLRqEbmiAopuMgMJ2SXy-REaIIe5DZikj0D1JphGwlMCQix6RX9hxVehDOcdAra7Akm01gpJVv1xj_syqPC1YCdNKizFWkL0ukG2fU4KHsQPOdlRmB9_ColZAa3AXdZYWDHa-CXr0eXmaDGOFlHTXLPVlVhgid7aOr9pbSDRR4Z25eCtojkQmGVHeJqxlvsZnsaqHQK2ZfJT2VO44_H4Kev_UHkwOF8shk5dq30SUUF8udz_Buyx46UhRe3AY-iOxGmnsHwErPe5u0842dB0OB-74thRWl4fmgIKiKvJJY-NXAL69E2XR0yYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f4ecd59a.mp4?token=MpO07SmkIhPlykGZVBblThT2k9VtAhLRqEbmiAopuMgMJ2SXy-REaIIe5DZikj0D1JphGwlMCQix6RX9hxVehDOcdAra7Akm01gpJVv1xj_syqPC1YCdNKizFWkL0ukG2fU4KHsQPOdlRmB9_ColZAa3AXdZYWDHa-CXr0eXmaDGOFlHTXLPVlVhgid7aOr9pbSDRR4Z25eCtojkQmGVHeJqxlvsZnsaqHQK2ZfJT2VO44_H4Kev_UHkwOF8shk5dq30SUUF8udz_Buyx46UhRe3AY-iOxGmnsHwErPe5u0842dB0OB-74thRWl4fmgIKiKvJJY-NXAL69E2XR0yYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدرالحسینی، کارشناس روابط بین‌الملل: تکرار درگیری با ایران می‌تواند شرایط را برای رژیم صهیونیستی بحرانی‌تر کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/675695" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675693">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
بقایی: در حال حاضر هیچ مذاکره‌ای با طرف آمریکایی نداریم
سخنگوی دستگاه دیپلماسی:
🔹
درخواست مذاکره از سوی ایران خبرسازی است. ما همیشه گفته‌ایم هیچگاه از استفاده از ابزار دیپلماسی برای صیانت از منافع ملی فرار نکردیم دیپلماسی را ابزار برای حفاظت از منافع ملی ایران می‌دانیم همزمان به هیچ عنوان هیچ اقدامی را انجام نخواهیم داد که طرف مقابل برداشت ناصحیحی از آن کند.
🔹
میانجی‌ها ممکن است پیام‌هایی را منتقل کنند در خصوص تحولات جاری، ولی در حال حاضر هیچ مذاکره‌ای با طرف آمریکایی نداریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/675693" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675692">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d195aae53.mp4?token=Dqo-CBrsxt7oXQl6CcWieWigbSenBAylUan3LYLiE1BKPsSBbd2g33ncoyL5Gna9qwwk59vUGGy6SD8GlWWt2p0kylxiuOHZ7SnPiddMDkyuQwy7S2-yO1K7-HWRZJI8Y_ZNLe6XtiiQlNJv0pT50RIy5LnwymTJqHp2xCUbtl0c-RCGDU8cw2IgjkkZabARM1HPL0_0g7jlUldx5lhf3Wqsn8MvXvEca6-BWmF5k6i6AYzzE34UXIYMUP5whXXdiAufyoayvVdaNBYk0KOil6p67goelHR1kOqVV9shCt8Dvl6_GTLvSY6Hj7Ej28na_LlYjYNFnnalK5o6em1P7HmyhEMnIkmkQ6SatFeo8AZgeRv9mTPgrQGok_5zjFMqOYIMxV10hDaqXDWPr2aqivXl4QYT4saXRkO3gK2pLkv2bvIe1XaRkYz8OOXH9gZuknOn-CUEJY-4LUPEJ95WCmM4HK3B6ekgtus_HYRS3Opp2L-7_Xq2Knr7K2aCV1HZEpqW67ihujjBvJYpIm3EIuh1Dih9XotLjeSrVwggGyR_UFwKl3D9FiVDGJHoz1zHqtvLH3NamlA8nphmaCBDt5hpaonxPZOOVW0ODCnn9lkBj8XLA-HoH88efGYS-g6HmO87c-KYDVQZMh--uz9L5_ICEFX_Ysl3gyvIhpfMDXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d195aae53.mp4?token=Dqo-CBrsxt7oXQl6CcWieWigbSenBAylUan3LYLiE1BKPsSBbd2g33ncoyL5Gna9qwwk59vUGGy6SD8GlWWt2p0kylxiuOHZ7SnPiddMDkyuQwy7S2-yO1K7-HWRZJI8Y_ZNLe6XtiiQlNJv0pT50RIy5LnwymTJqHp2xCUbtl0c-RCGDU8cw2IgjkkZabARM1HPL0_0g7jlUldx5lhf3Wqsn8MvXvEca6-BWmF5k6i6AYzzE34UXIYMUP5whXXdiAufyoayvVdaNBYk0KOil6p67goelHR1kOqVV9shCt8Dvl6_GTLvSY6Hj7Ej28na_LlYjYNFnnalK5o6em1P7HmyhEMnIkmkQ6SatFeo8AZgeRv9mTPgrQGok_5zjFMqOYIMxV10hDaqXDWPr2aqivXl4QYT4saXRkO3gK2pLkv2bvIe1XaRkYz8OOXH9gZuknOn-CUEJY-4LUPEJ95WCmM4HK3B6ekgtus_HYRS3Opp2L-7_Xq2Knr7K2aCV1HZEpqW67ihujjBvJYpIm3EIuh1Dih9XotLjeSrVwggGyR_UFwKl3D9FiVDGJHoz1zHqtvLH3NamlA8nphmaCBDt5hpaonxPZOOVW0ODCnn9lkBj8XLA-HoH88efGYS-g6HmO87c-KYDVQZMh--uz9L5_ICEFX_Ysl3gyvIhpfMDXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی از حمله آمریکا به شناورهای صیادی کوهستک سیریک
🔹
منبع درآمد بیش از ۱۰۰ خانواده، در آتش حماقت‌های ترامپ سوخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/675692" target="_blank">📅 11:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675690">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f77b10de2.mp4?token=V95oL5Vs-GNNICZBqPCus76tUtylUCM7NBzN3iMCwIBfw4iHipvEeAJFXQrSX2Lrzvc8BP1Cvo1sQ-IyLz5eDmVPxHjNN2hotUbMcBR0aAYAWc67bKeXDuRJ0BTF90E103nkr2DaQnLVXbzUc-d2cZIXorBqLerX5XmBR4tcbU32PrP7ZnVIP3kcSLWD7oI2tM9o9-Cff46HESUibsGfe-5CMFSe21R0V38rf-OqaZiR_ZqsceA-Ny1wDUBi0thI7nrNDWk7Uuqdd7HrefwvMWrn69TJcA3rWUlmunCIbzjRyaM8Fz4-jqu0uqGUdvBrRd6A-mjKHza08PZzqlxodg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f77b10de2.mp4?token=V95oL5Vs-GNNICZBqPCus76tUtylUCM7NBzN3iMCwIBfw4iHipvEeAJFXQrSX2Lrzvc8BP1Cvo1sQ-IyLz5eDmVPxHjNN2hotUbMcBR0aAYAWc67bKeXDuRJ0BTF90E103nkr2DaQnLVXbzUc-d2cZIXorBqLerX5XmBR4tcbU32PrP7ZnVIP3kcSLWD7oI2tM9o9-Cff46HESUibsGfe-5CMFSe21R0V38rf-OqaZiR_ZqsceA-Ny1wDUBi0thI7nrNDWk7Uuqdd7HrefwvMWrn69TJcA3rWUlmunCIbzjRyaM8Fz4-jqu0uqGUdvBrRd6A-mjKHza08PZzqlxodg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرز تهیه یک فرزند مضطرب/ چه رفتارهایی از جانب والدین منجر به ایجاد اضطراب در کودکان می‌شود؟
/ تلویزیون اینترنتی مدار
این برنامه را در آپارات ببینید
👇
▫️
https://aparat.com/v/nalwl41
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/675690" target="_blank">📅 11:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675689">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: فرانسه با پوشش سفارتخانه و به‌بهانهٔ ارتباط با جامعهٔ مدنی در امور داخلی ما دخالت کرده و باید عذرخواهی کند
🔹
شایعه تعطیلی سفارتخانه‌های اروپایی در ایران را به حساب جنگ روانی آمریکا بگذارید که در آن استاد است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/675689" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675688">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2b72f70b.mp4?token=s_JoHQpS7XZyw9-5kx18CmylKyOhvzV6ZnecXPy6SbzUpSejzs-xaqCo-yqmVaLZxW6sKqPcmoVbm_m11XTYEXLr3bMnlnRdm0e8EUfbaQWBV2A3eoQUqcv1SaVzQ8caselp_WxyyFGcxGGe4vijBQlD_X6EEkE37UpE27dm6ne28_TeYdetYdx3m0KoBFQnAyxWz0fNZ4B9Dk48v_u5FQcgEGKzuQJlYVwiAPcttFOKVt_SApMMNj1U1Z0EBWDcWBopYnRTojAVZBVZojZG9vMzJmh6RhpotyvlqtyB3XWYGbiTIX54Vk1h4xx3cMryPt-PlpwNSys-Twj8fov__g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2b72f70b.mp4?token=s_JoHQpS7XZyw9-5kx18CmylKyOhvzV6ZnecXPy6SbzUpSejzs-xaqCo-yqmVaLZxW6sKqPcmoVbm_m11XTYEXLr3bMnlnRdm0e8EUfbaQWBV2A3eoQUqcv1SaVzQ8caselp_WxyyFGcxGGe4vijBQlD_X6EEkE37UpE27dm6ne28_TeYdetYdx3m0KoBFQnAyxWz0fNZ4B9Dk48v_u5FQcgEGKzuQJlYVwiAPcttFOKVt_SApMMNj1U1Z0EBWDcWBopYnRTojAVZBVZojZG9vMzJmh6RhpotyvlqtyB3XWYGbiTIX54Vk1h4xx3cMryPt-PlpwNSys-Twj8fov__g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدرالحسینی، کارشناس روابط بین‌الملل: اگر اروپا در اقدامات آمریکا علیه ایران همراهی کند، جمهوری اسلامی آمادگی پاسخ متقابل را دارد/ تهدیدهای ایران در مورد برخی کشورهای اروپایی معتبر است و توانایی داریم که پاسخ دشمنی آن‌ها را بدهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/675688" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675687">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06c98f25ef.mp4?token=I7C_CbAPVMxEDaRDPPQk28qSGAgeBEN67fXaQ5rMXDsUVVjiiNue42P-BJ91ZpjabrUKTwvLmP_QA3ut0_NGJ_ggr31of3QQy6YtgSWh48at2YvdUcSZsRKVPCJ40cpTX_1FdAJtp9GX0pMjzpV9JtWw7ndAk_GHNoCqF44-u2ao7ByhS7BI39Di_pZHL4wAJmnFY6FVBAhcuOXLT0WEXts1DPKTXdrhup4tqZYicXeqabMSOo7Hy-3rSNoV-hcuuA-t3fVOpGyKnpGfjxlTk4jBCji4ysa64lbps61X0yPRzkCyBm6Lj41YNGopXkUrV3AOHBXftlX1fDl-9AfUxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06c98f25ef.mp4?token=I7C_CbAPVMxEDaRDPPQk28qSGAgeBEN67fXaQ5rMXDsUVVjiiNue42P-BJ91ZpjabrUKTwvLmP_QA3ut0_NGJ_ggr31of3QQy6YtgSWh48at2YvdUcSZsRKVPCJ40cpTX_1FdAJtp9GX0pMjzpV9JtWw7ndAk_GHNoCqF44-u2ao7ByhS7BI39Di_pZHL4wAJmnFY6FVBAhcuOXLT0WEXts1DPKTXdrhup4tqZYicXeqabMSOo7Hy-3rSNoV-hcuuA-t3fVOpGyKnpGfjxlTk4jBCji4ysa64lbps61X0yPRzkCyBm6Lj41YNGopXkUrV3AOHBXftlX1fDl-9AfUxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه خطاب به اتحادیهٔ اروپا: شما که هرازچندگاهی به بهانهٔ حقوق بشر بیانیه‌ای علیه ایران صادر می‌کنید! آیا کودکان میناب ایرانی نبودند؟!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/675687" target="_blank">📅 11:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675686">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/599dbc5f5b.mp4?token=DOI0YCy4i77xyzgaFyp-PMXOvMo7JI_pdChrsLb_FFj9P_mo5T2ttS41TBv5BXsk77pbSVBcLOuPxmiwqxK7bdOgXa671_gWfQOhOvqzEU8OUyiU4KLv1_jDP76l6z0faWIEDvxCrSw6TKLMGBbSekx8K3dCCxRKS4vFc1kVV7x7w6NCDnQxNhR86xxnvGlJlEVfRLYflZr6BThOE2pMZxdMfWGmmQoG4tiihgl-RKSklXMsOG81GfUnl7v2LXjwCfsiPOJNIGltobw4lb_xP6CkWjnxPSOPf6UTi4QMUA7_n7___v0QMfgfByLRMSO6BAotvrbx_pgFV47sSp1vDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/599dbc5f5b.mp4?token=DOI0YCy4i77xyzgaFyp-PMXOvMo7JI_pdChrsLb_FFj9P_mo5T2ttS41TBv5BXsk77pbSVBcLOuPxmiwqxK7bdOgXa671_gWfQOhOvqzEU8OUyiU4KLv1_jDP76l6z0faWIEDvxCrSw6TKLMGBbSekx8K3dCCxRKS4vFc1kVV7x7w6NCDnQxNhR86xxnvGlJlEVfRLYflZr6BThOE2pMZxdMfWGmmQoG4tiihgl-RKSklXMsOG81GfUnl7v2LXjwCfsiPOJNIGltobw4lb_xP6CkWjnxPSOPf6UTi4QMUA7_n7___v0QMfgfByLRMSO6BAotvrbx_pgFV47sSp1vDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجمع عمومی عادی بطور فوق العاده فارس به حد نصاب نرسید
🔹
مجمع عمومی عادی بطور فوق العاده شرکت صنایع پتروشیمی خلیج‌فارس که بنا بود بعد از مجمع عمومی فوق العاده این شرکت برگزار شود به دلیل به حد نصاب نرسیدن به تعویق افتاد.
🔹
به دلیل آنکه کمتر از پنجاه درصد سهامداران در این مجمع شرکت کردند(۴۳.۹ درصد) بر اساس قوانین و ضوابط موجود، این مجمع تشکیل نشد.
🔹
گفتنی است مجمع عمومی فوق العاده فارس از ساعت ۹ تا ۱۰ صبح امروز پنجم مرداد با حضور ۷۸.۸ درصد سهامداران برگزار شده بود.
🔹
زمان جدید این مجمع متعاقبا اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/675686" target="_blank">📅 11:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675683">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91ffff6f6.mp4?token=Kb3pDvpMHK7jLSUscAsNShEq8iNyCcXzs5PVGrWHsMIkpYHMmGsBCU42Fva1l-5Q3yJl7mftzvVOKYe0dp5SbHFTjM4xMsg3wQVwNp_QBAFUMMeTysM1inESezPF1WJr9124WIM5BRvsac3zqc3C-yNWl_AlisloQa62l5ynW1fyhAlB9V0c6uVbGKyZI9w2ehSgdm0VvXEu5E9BOqSu07v51H1mAwzknpZ2BXibM8AmFdKkp_Xm9uoHLRsxp6gRrWnMb23z7kBGccIn0bUYNa_BWOOFYs6oWTGjZZaJwZd85TQqHRkmkuh2LsRkOHJNkfLCWsfGuU0IXwuzZG7nnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91ffff6f6.mp4?token=Kb3pDvpMHK7jLSUscAsNShEq8iNyCcXzs5PVGrWHsMIkpYHMmGsBCU42Fva1l-5Q3yJl7mftzvVOKYe0dp5SbHFTjM4xMsg3wQVwNp_QBAFUMMeTysM1inESezPF1WJr9124WIM5BRvsac3zqc3C-yNWl_AlisloQa62l5ynW1fyhAlB9V0c6uVbGKyZI9w2ehSgdm0VvXEu5E9BOqSu07v51H1mAwzknpZ2BXibM8AmFdKkp_Xm9uoHLRsxp6gRrWnMb23z7kBGccIn0bUYNa_BWOOFYs6oWTGjZZaJwZd85TQqHRkmkuh2LsRkOHJNkfLCWsfGuU0IXwuzZG7nnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه خطاب به اتحادیهٔ اروپا: شما که هرازچندگاهی به بهانهٔ حقوق بشر بیانیه‌ای علیه ایران صادر می‌کنید! آیا کودکان میناب ایرانی نبودند؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/675683" target="_blank">📅 11:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675682">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbb8512399.mp4?token=ClGxzAKEnOvijMYWw2Ztjz9ALgy5twMCb9kaD4ELVuM-Onv29IN32uaSWxV23XakOFZqny6zcmm7VV4vAct5k3eBCoZaDKHJ-3IG9k15T7ZZoMbtIbvgYizDP0LsMbFTo-mzgcYaIBCC5CHU_KeEL82jDavXw-xNHci2zd3gt6whwDevlZSuYlxWYErGuD0cFIT2KYf8dPP20RG4-oNhCNp47iNmp-a4ZhAkYOQr-Ot3RjGhZ4GgKHhs_Z9QQSUNqbJpEhvs95dqSDjgjtejrvAgSH2SNYMHEd3enZ_RFXpj7tcaEf_rQOBH9SADhs5htspiNckUM2EYS-njMR2ytw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbb8512399.mp4?token=ClGxzAKEnOvijMYWw2Ztjz9ALgy5twMCb9kaD4ELVuM-Onv29IN32uaSWxV23XakOFZqny6zcmm7VV4vAct5k3eBCoZaDKHJ-3IG9k15T7ZZoMbtIbvgYizDP0LsMbFTo-mzgcYaIBCC5CHU_KeEL82jDavXw-xNHci2zd3gt6whwDevlZSuYlxWYErGuD0cFIT2KYf8dPP20RG4-oNhCNp47iNmp-a4ZhAkYOQr-Ot3RjGhZ4GgKHhs_Z9QQSUNqbJpEhvs95dqSDjgjtejrvAgSH2SNYMHEd3enZ_RFXpj7tcaEf_rQOBH9SADhs5htspiNckUM2EYS-njMR2ytw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجمع عمومی فوق‌العاده شرکت صنایع پتروشیمی خلیج فارس آغاز شد
🔹
مجمع عمومی فوق‌العاده شرکت صنایع پتروشیمی خلیج فارس امروز دوشنبه ۵ مرداد ۱۴۰۵، با حضور ۷۷.۷ درصد از سهامداران و نمایندگان قانونی آن‌ها در سالن همایش‌های بین‌المللی ارم تهران آغاز شد.
🔹
این مجمع با هدف  قرائت گزارش بازرس قانونی در مورد پیشنهاد افزایش سرمایه هیئت مدیره، اصلاح ماده ۷ اساسنامه مرتبط با میزان سرمایه و تعداد سهام و بازنگری در فعالیت‌های فرعی شرکت برگزار می‌شود.
🔹
لازم به ذکر است که در راستای تسهیل مشارکت سهامداران و طبق ابلاغیه سازمان بورس و اوراق بهادار، امکان شرکت مجازی و طرح سوالات از طریق سامانه «
mymajma.com
» فراهم شده است تا سهامداران بتوانند به صورت برخط در روند تصمیم‌گیری‌های شرکت سهیم باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/675682" target="_blank">📅 10:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675680">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcddfc84d.mp4?token=IIsN9FzXGbxdDZ06urXu-lPOXfkHu8sBfIr9NefZXg5uxSxpPYk5_oDfpEthUzvmz5Rdhb-9Fq1LMP1sRUr3NlzaNjFh-maS-yRoEfnKZVcMQLkE9FWC9uiyH_hFC5knP3MrLVW2GefwuQrgtOQWLVUpXMSsbT_ZfAvGayOpvlUOXc_lo7wxy3v6gv328EtjYRJ5G1jgEomi1Jjqck7RG-KDwoFLd_D3ALfqaNsiKLD1-YiUebpRaIAd-jPhJbf22ppdlDMue79ob09xtpsNTvprb4xwzIBOQlwKRQotZB93QzcXMZMbrT_Af5hGz9XriZf7VnxAzRbApIA-ii8U7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcddfc84d.mp4?token=IIsN9FzXGbxdDZ06urXu-lPOXfkHu8sBfIr9NefZXg5uxSxpPYk5_oDfpEthUzvmz5Rdhb-9Fq1LMP1sRUr3NlzaNjFh-maS-yRoEfnKZVcMQLkE9FWC9uiyH_hFC5knP3MrLVW2GefwuQrgtOQWLVUpXMSsbT_ZfAvGayOpvlUOXc_lo7wxy3v6gv328EtjYRJ5G1jgEomi1Jjqck7RG-KDwoFLd_D3ALfqaNsiKLD1-YiUebpRaIAd-jPhJbf22ppdlDMue79ob09xtpsNTvprb4xwzIBOQlwKRQotZB93QzcXMZMbrT_Af5hGz9XriZf7VnxAzRbApIA-ii8U7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله زنبورها فینال فوتبال را متوقف کرد
🔹
یک اتفاق عجیب و کم‌سابقه، فینال رقابت‌های قهرمانی ایالت باهیا در رده زیر ۲۰ سال برزیل را برای دقایقی متوقف کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/675680" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675679">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4de6a51b.mp4?token=hsYuEGUxZJbFtiodAxJWanDK9fnL1xNxDxBu1knj-nnd_VObGyjGR-Y749WpVCwdhS1Gynus4EJO6HLR55r-v_myPsofSqzbQAC34cHr2jjldluFivyPk9fsmnhh9j92Mn2isFrI_IjcSKg2HLf72dRU_vnhjU_WX1ylJObrHqAuT7Qx8yd4ti2-EkrifX2uYCuv62y5IvaWoaAwecLUOBcfVe2oHUevI8IrJqHXjbRGJhteraUfz80l2Oqb8pLpR-gvTibqt9sFh9N2ZqFV0mnSvz5kWZDM8XDfHZuL0YicJZawZ-Z6Zlx1KmTtVoFZ7oa-R5MONhmhxIcuwWsHSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4de6a51b.mp4?token=hsYuEGUxZJbFtiodAxJWanDK9fnL1xNxDxBu1knj-nnd_VObGyjGR-Y749WpVCwdhS1Gynus4EJO6HLR55r-v_myPsofSqzbQAC34cHr2jjldluFivyPk9fsmnhh9j92Mn2isFrI_IjcSKg2HLf72dRU_vnhjU_WX1ylJObrHqAuT7Qx8yd4ti2-EkrifX2uYCuv62y5IvaWoaAwecLUOBcfVe2oHUevI8IrJqHXjbRGJhteraUfz80l2Oqb8pLpR-gvTibqt9sFh9N2ZqFV0mnSvz5kWZDM8XDfHZuL0YicJZawZ-Z6Zlx1KmTtVoFZ7oa-R5MONhmhxIcuwWsHSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک: رژیم صهیونسیتی از صبح امروز حملات توپخانه‌ای را علیه جنوب لبنان آغاز کرده است/ در این حملات ۵۵ شهرک در جنوب رودخانه لیتانی کاملا از بین‌ رفته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/675679" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675673">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mr6LIolZ_avJmfhdz2BFOPneqDk_lYPx-hKto9q0CXgtVqokOen1PvlpiJgpTeyQxmA7C6YTGmj7DE4CPO5FuC35wWIqLwnJyiXL2RZLiJML1Os2UciLgyr23WqNWvJ0z6Katx2XGnvUXsu_0jwRxsLgD6L9i6unFIcwvot-67MuPhe1qVMb4xExTomvKjP_4SGxGwg1USOKnchy4uL-YoEuCS4naPu-1UFV33hh1kLr24KLXQIoCKg2XtAmx9YOIQQwvvPj0t3AUZO8hT7X0vDgQM8np-hje8sGAynBknRaJ2rDWWvnvYWb64wg9_a0vLMMnASIBISUG-CGOd0E1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bs7N2z9MdFAIfZ3h-j313Nze4OHTmucY36yN6so9ZUK9PMU6cR0vIKsZL6XdNK5RtkV3FnCYP-1tX_a8LSrTvFHlUmLr0J-uKjfo9cd8UwupXJii14qdqmFl9yQw4o3kLSl0d7aywUATBNVlxDG6p8SiWmpQ5ThTnb-p3DG5KUvvHiPUdS1nwq8_D8-Cnj6KSVK0Imc5h7PfPrZDOM6dh7-2MGxChMw7ujktwHPoudNM9wFPbldgS9P1xqQUIC6VIxlhl3ghjJ5WnYWxS3-cbIW50DsXTjCqSQPHP4LD0pmCW_YEOHygGn4FOCtxlNCtMGyLSS67UEBs-uXzHnXl5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tv_3xdsSFZQ79rnvYu7EDuqlqVIwu3rXWXQmmJa3NGbNxR975i8RhWhEQwU7CBarvbhLT-VztaoGSJxHC9PLyXbx6Tc-R_a0y3C7wUz_WJRpfX8EYGbubio0RgFUENKvOGXsqPyCC7igaq5O52djJEhMaYWkD2KEnvFfh_MLMk3GtSBB2wuJ4CSV5yhHGih3q0-6KsaJCAOnBUfQ5OXW-Sen2HRu9Y8Kqy1dMCTjsk1i6j-311mRJ0ZOF0mb0bHjri8A8FjAoItST7iBPeId-APLnHd_2KmsKIplG4HCwSVUudStghBAz9ZSKnKU_E0rZVP-OY31ZByXlirYpFMp9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V12opmBlkYy2xN77g3vJhwDcq3_e-SdYIh5IJi4OdybKcNkI0wG9BAC_0zIbqctqhAAYm4LyLF5h7f3eFy-d_N91xqHe6E1IB2Gibm5sHA2g1PNRdo6AIuer-C8emwUIm9PTHXERO0D7U5R-f76ZevCSVGrTEFmiGxQUAU6vONOhZPGB8PYWvSj_TbD8CzaCju7J_j9MOe_GBRGag_XBGiKYEyMvdQ_BcAwDnCu7tiA6c5JNrVMoHryJ8tXgv2w4fNyhqSdiGsk1W4Icr8Vwgb7bERG-IjeO_C6CH-uue9ISU7G3_rr4-1Qqu8ViLl_ztPqUnhgNkZf3KbgyQY_mhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbiz-4wGXZTYZKwQLjmwe4DjieHjJtqhcN3PMzs-5XpfPtkPn2H4ARF5YJ4AKe9Q2PTLHTlAoKkPTuXBcH6OnpUhZ0cs12ThRgPj9VONSGu_8kJuQZYLMxGC4TzdQ0vvdjugjlGCvX7OSe1qnMhypC4Yn6-LlmBZDhZMgnFIIpDKNwQknMIrhxVIc7VC0yYi_FOdfzM4CrfxVhzkJiirZBnjE4nsgi-pfCAFCDwt2xn5eRaSpUkRf1T77rgTLBAH3khKgI-M07EUYItDXqR6G_MsiOv547pgqU3CrUbZzVrjynSTI6BQlRnxWlO6VEYaojMhD68AH7W092EDuG-mGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KG3QeU6B8N-tdrPZnAQ6j8cgYjJLYHqL5hZH6Fz7V7vzU5Fiw53AgmKh5Ecz4e0biu4j2dNWpCn4wXpAEFA646-BBGIE8n7OJ7dQLeLCXNhYlCIcHQEPAJWv_7iSIEpddxdvGnJWQaONPhKX5T1SWEmpFy-1TB626mJ9rjircTNskR9l41307Iujo-r9kmDHouzMOkNGFZpF7YNrE3kHCIBQZtMBtT9ee7Ytk_iSpG4XUSxu82XlkSv9ClmxiVCr-OOqhbH72Urfo_6oUzHdmHJKnqpmwQZVO_VTRwWd9AfpImVM_oLbcra_CygtXLDe3zuTUAO_EgROF7nuDGR8cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کودکتون روزی چند ساعت باید بخوابه؟ جدول خواب مناسب هر سن رو ببینید
😴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/675673" target="_blank">📅 10:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675672">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a62bcbbf.mp4?token=fxZu0RkjrDSUXI_tsxKH-W6cYwWQO5ptodI3GHNtwITJ7MHZtqIIwUm6xLmWqKp1Qzd0YBZFNVAL3WISZ9FiymtSglHg9B0cmZ3YlPD_XB5p3auZ_GKW8xADESqxO5t_8lRyADeRqleo86eBsm_lzVQCwN0LzC_RSwbs7Vk72-moElrJsy_UzqqoDAPOR54c-YPf8XpBRj0wp-MvngOQCcDK_wUGl8i1QPZJ3sFwiNaLg-hiJVzNJMIOIMeTSzLnuyzj_K8JsgNEkxe-YPBMFGTlYeBffBhIwlXrtK1AUNUcIV7WFnaxDadLinYd80ooSiKfC87AejCuSYLQL7H6sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a62bcbbf.mp4?token=fxZu0RkjrDSUXI_tsxKH-W6cYwWQO5ptodI3GHNtwITJ7MHZtqIIwUm6xLmWqKp1Qzd0YBZFNVAL3WISZ9FiymtSglHg9B0cmZ3YlPD_XB5p3auZ_GKW8xADESqxO5t_8lRyADeRqleo86eBsm_lzVQCwN0LzC_RSwbs7Vk72-moElrJsy_UzqqoDAPOR54c-YPf8XpBRj0wp-MvngOQCcDK_wUGl8i1QPZJ3sFwiNaLg-hiJVzNJMIOIMeTSzLnuyzj_K8JsgNEkxe-YPBMFGTlYeBffBhIwlXrtK1AUNUcIV7WFnaxDadLinYd80ooSiKfC87AejCuSYLQL7H6sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز پذیرش سهامداران برای مجمع عمومی فوق العاده فارس
🔹
از دقایقی پیش پذیرش سهامداران حقوقی و حقیقی برای مجمع عمومی عادی فوق العاده فارس در هتل ارم آغاز شد.
🔹
امروز  در حالی دو مجمع عمومی فوق العاده و عمومی بطور فوق العاده شرکت صنایع پتروشیمی خلیج‌فارس برگزار می‌شود که بیش از ۱۹ میلیون نفر سهامدار این شرکت از سهامداران مستقیم عدالت و سهامداران حقیقی با مراجعه به سامانه «مای مجمع» می‌توانند به صورت آنلاین این دو مجمع را در
این سامانه
مشاهده کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/675672" target="_blank">📅 10:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675671">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miDoy6Xz3nFeWMhr17RK3RmXnLvd8OY928iF5jTOdGhCUx12RXR5pWsfeN7r9q_m66CuGGiFufJHM4T3HmyKWm70yjb-SEZwH5eD85Ep183D4eYVhfQR-o5KMWclN6AyK25TA_rqXgOBsf-l2iMYamSjxIIjfLhtz50N_ZJd85CIRhstPcek8xUb8mTGoQyQDQm9fPF0bQqiIIGG8BDrZzh4WY6Avsn8TbrpaMGtQeg6I-hVzQ08jL8vANI1EZVgo8jJedQIjXzMDx4KgjOCENARinPkt_4_zMAvRJCrO-FkKcGcsNXUtmpmQRQNd0aL0dy6na8-GUiSL7StuRfiww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: اقدام «فرصت‌طلب مستقر در کی‌یف» نمی‌تواند بی‌پاسخ بماند   وزیر امور خارجه:
🔹
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و یک ملوان را شهید کرده است. این اقدامی است که به‌وضوح منشور سازمان ملل را نقض می‌کند و به تحریک اسرائیل انجام شده تا اروپا را به…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/675671" target="_blank">📅 10:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675670">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rcn5AUAZonjOOt0QvjCgHMB0V-Ran9say3DIHC-bzReMvrottOdWLgatgBIhU4qbGdFoC9-Qfc15Wo9Q7Y6FPFSnlCRcjwNE76NIoiwlYcbb7euXSjZIXgL9_Kd4M_6aDlhVEllJ4bhTst3GxgNyUl3CTlawS5CtuhUrxqCUMhd64nzIQUucC_jUROz2QPRg8RZ7YqeCWyvTui52l8bLqvv8aEWqGq-srgTgJ-eH8QxBvNt_qHrB-b2eO1bGbHyn60JP4jxWDnSgju63QVuLIwziP5FldHWBeAnfJV3_xaPfVOMp8BAbUJFeNiz171HXFM58VOJ28jNXPjFju69mzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مادر ایران‌زمین؛ کوه دماوند
نمای دلربای دماوند از دریاچه حوض سلطان قم
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/675670" target="_blank">📅 10:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675668">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab9f096c1f.mp4?token=vpGG6n62_GHPbD3oil46kd4Jb5K0ZBsB5lo1EseQdkhSAo2xtmnuz_bTIUMiTo3Ap2g_KVMJdQXp6quNi3xrjbtF4sFt2i-7bhxW7a1LqJwH8YAcXHX4E0Rlob6r9i5wsyouiX-xkI3HRgd-nsfgf9wJsppvehfXY_ZVXRXXS_LfZuUWL25nE1Hgt3Tq3GN8dhxBlItJALb_ulR4gzx1sDRO9d2RWMpA3ZIGFSgjSdMRkvGaRODrex2NOYDsIbx3c_iue28qoUqfUHZ8Xh3I5vveLNI9Ep0xGl9Gqau206W47ULMNMCjL8E89GfASROl9XMp_-bT9LV4nCyD6bH7Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab9f096c1f.mp4?token=vpGG6n62_GHPbD3oil46kd4Jb5K0ZBsB5lo1EseQdkhSAo2xtmnuz_bTIUMiTo3Ap2g_KVMJdQXp6quNi3xrjbtF4sFt2i-7bhxW7a1LqJwH8YAcXHX4E0Rlob6r9i5wsyouiX-xkI3HRgd-nsfgf9wJsppvehfXY_ZVXRXXS_LfZuUWL25nE1Hgt3Tq3GN8dhxBlItJALb_ulR4gzx1sDRO9d2RWMpA3ZIGFSgjSdMRkvGaRODrex2NOYDsIbx3c_iue28qoUqfUHZ8Xh3I5vveLNI9Ep0xGl9Gqau206W47ULMNMCjL8E89GfASROl9XMp_-bT9LV4nCyD6bH7Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این تارت خوشمزه شکلاتی پایه ثابت همه‌‌ی مهمونی‌هاتون میشه  مواد لازم:
🔹
مواد خمیری
🔹
آرد ۱۸۰ گرم
🔹
پودر قند ۵۰ گرم
🔹
پودر بادام ۲۰ گرم
🔹
کره ۷۰ گرم
🔹
زرد تخم مرغ ۱ عدد
🔹
وانیل ۱ قاشق چایخوری
🔹
مواد فیلینگ
🔹
خامه ۲۰۰ گرم
🔹
شکر ۲ قاشق غذاخوری
🔹
شکلات تلخ ۲۰۰ گرم…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/675668" target="_blank">📅 10:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675667">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
هشدار پلیس فتا؛ پیام مالیات معوقه تله جدید کلاهبرداران
معاون اجتماعی پلس فتا:
🔹
در روزهای اخیر پیام‌هایی در پیام‌رسان‌هایی مانند ایتا، روبیکا و بله به نام سازمان امور مالیاتی کشور برای برخی کاربران ارسال می‌شود که از مخاطب می‌خواهد ظرف مدت کوتاهی روی یک لینک کلیک کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/675667" target="_blank">📅 09:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675663">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7eyQBjEzgy46WW7HJF7g3yEL6UBFBrOgfhpzQbfboj1iiA11Z2OTAsn5fdo4iemB9uo0MCBH6xIj6Ui7-6zUTX5_zH3goUp-hCKyESUTf6smJjHTuHDz-2DUBv8NUHooq9xAJe-yX6DPcvjsOUAFOLQE_MVjHkoy905myx1yqAsch72YGneWIqKcb6FL0vR_aaS321IpEvvYBBr5vXFjp_OeKWnWlur3o4APSY-Ok7N33lK8BduZksxkvY6Hc2TQYZO7eyJbntSUZXL1KSpSFlDL2ndyJD8qY3mJ-T299k4yvXFpqOTqGmAdHnAik-UCxh5KIkT5KOyOvcfOdHVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پنتاگون بی‌سروصدا تلفات جنگ ایران را فاش کرد؛ ۶۴۲ کشته و زخمی
گاردین:
🔹
دولت ترامپ در تلاش است آمار تلفات را کم‌جلوه دهد، اما پنتاگون با به‌روزرسانی خاموش پایگاه داده‌اش، پرده از واقعیت تلخ برداشت. از آغاز جنگ علیه ایران در ۲۸ فوریه، ۱۸ سرباز آمریکایی کشته و ۶۲۴ نفر زخمی شده‌اند.
🔹
دولت می‌خواهد این عملیات را جدا از نام رسمی «خشم حماسی» نشان دهد تا تلفات کم‌تر دیده شود، اما قانونگذاران هر دو حزب این «تفسیر سلیقه‌ای» از قانون اختیارات جنگی را به چالش کشیده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/675663" target="_blank">📅 09:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675662">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVfN5uS5wpos9GXZebulrcscveGaqNxg0BqxreBGcxGSXBS7MkA_N3B6LIVlP-DqzqEblkgFrAAmERpgdpP9l7sWVAcQS8ehcUCAS9jxH9hxrluwRcelNxtpseoesJcstfpi8r5Dffi41k10e-FxkmGiYyJbEE_Txu4JBcBXVxGeQtD7nNDKucScFJO3QKHxyD2b8JrIszEJGWlmTHw80lVC0kF8VZk5O0sLVAFI-Bom3Im5BuxOM5X76snGL125cegAWvKJWp0QYpDQK7xifvqMhsU9NQa8UIXrnUKUAy-zKT99B0WZHqeRYy5f6_DbI_xK7n4J8RhsdrIDe-dHMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار سفارت ایران در لهستان: پاسخ به متجاوزان اوکراینی حق ایران طبق منشور سازمان ملل است
🔹
زلنسکی با الگو قرار دادن رهبران رژیم صهیونیستی که ایالات متحده را به جنگ با ایران کشاندند، رئیس جمهور اوکراین به دنبال کشاندن اروپا و ناتو به جنگ با ایران است.
🔹
او پیش از این از وظایف خود فراتر رفته و نه تنها در امور داخلی ایران دخالت کرده، بلکه در تسلیح برخی از طرف‌های حمله کننده به ایران در طول و پس از جنگ ۴۰ روزه نیز نقش داشته است. واضح است که خویشتن‌داری ایران بی‌پایان نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/675662" target="_blank">📅 09:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675659">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✨
تخفیف  ۵۵٪ ویژه هتل مشهد
در گروه هتل‌های لوکس درویشی
🎁
هر ۴ شب اقامت = ۱ شب رایگان
🏊‍♂️
مجموعه آبی و گیم‌کلاب رایگان
💆‍♂️
ماساژ رایگان اتاق VIP
🚕
ترانسفر 24H فرودگاه و حرم رایگان
⏳
فقط تا ۱۵ مرداد این شرایط باقیست ، همین حالا تماس بگیرید
📞
05138080
‏
🌐
darvishihotel.com</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/675659" target="_blank">📅 09:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675658">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f92c7e73.mp4?token=HL4OIF-4fuxbiAqQ52c_HsyOCN4Ig_OiM9BVV3eQjF2pjauCFJ8-a11Bhp6C_CpTXlKfrGN56S4EKSNflegiNcL5cO_tzgagE5dKrT2Ld85lQ_Dy0-5N7kRqeKjXRwsYbL6o36DUrOE1jjMOw5yMGa5pUglEFQOBbI_I3rcOPujSV7tQ9UOeDaxQyqjeXgBGy_VhuQyYscp3KfxC-_xveSMicJrYlr0mUejBqFapFrYYEWoAHrO2RZr7Wxgac-HBK-yC3wrQeRNYuxoD0OpXj6wmicy27HbsIKwdwRy5qufJpeAnKn1Xq1-b1Bg6erJQG0zfvfo96i3EvR2Uz6pMBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f92c7e73.mp4?token=HL4OIF-4fuxbiAqQ52c_HsyOCN4Ig_OiM9BVV3eQjF2pjauCFJ8-a11Bhp6C_CpTXlKfrGN56S4EKSNflegiNcL5cO_tzgagE5dKrT2Ld85lQ_Dy0-5N7kRqeKjXRwsYbL6o36DUrOE1jjMOw5yMGa5pUglEFQOBbI_I3rcOPujSV7tQ9UOeDaxQyqjeXgBGy_VhuQyYscp3KfxC-_xveSMicJrYlr0mUejBqFapFrYYEWoAHrO2RZr7Wxgac-HBK-yC3wrQeRNYuxoD0OpXj6wmicy27HbsIKwdwRy5qufJpeAnKn1Xq1-b1Bg6erJQG0zfvfo96i3EvR2Uz6pMBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تابلویی مربوط به نقشه ۱۰۰سال پیش کرج
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/675658" target="_blank">📅 09:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675657">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d1f32b62c.mp4?token=YP_YjBoWo5dYq7KMMC8ZJogUDttLRoFTBVc0dzYxM5cUXWiaunhFgkgJDVBhmzAQVFjYHgnB6l-eaa-y6OozmCLW_tl-ekTWuJ2u_2ZEkSecqDExGmsTn7m_6y6pRXm3k8yWD8LboLIHoO9k9x6PNRC99z0_HoRkmvXjHvoYJtoX0B-f4w3WECSg9Lv0VjOOix0sHkknR-lqMdXZ2Zc_3hKNtrQkn4TBWzlTMYnrQYHh829BEKpci2vTZAWSa912X2aDSnHio4kahEcxP1wXiScwNTvtPjQO08mXwALNNc7l2Kqb8BWrYFjttzwwlh3-EewzRpasKxX4VOB-0krioQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d1f32b62c.mp4?token=YP_YjBoWo5dYq7KMMC8ZJogUDttLRoFTBVc0dzYxM5cUXWiaunhFgkgJDVBhmzAQVFjYHgnB6l-eaa-y6OozmCLW_tl-ekTWuJ2u_2ZEkSecqDExGmsTn7m_6y6pRXm3k8yWD8LboLIHoO9k9x6PNRC99z0_HoRkmvXjHvoYJtoX0B-f4w3WECSg9Lv0VjOOix0sHkknR-lqMdXZ2Zc_3hKNtrQkn4TBWzlTMYnrQYHh829BEKpci2vTZAWSa912X2aDSnHio4kahEcxP1wXiScwNTvtPjQO08mXwALNNc7l2Kqb8BWrYFjttzwwlh3-EewzRpasKxX4VOB-0krioQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخریب آشیانه جنگنده‌ها در پایگاه هوایی شاه فیصل اردن‌/ انبار مهمات نیروهای ویژه آمریکا هدف قرار گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/675657" target="_blank">📅 09:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675656">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b5adfbfa.mp4?token=ZgAD5BVtAwXUxvSadeecG8diQXqgw-qHFlrnizffm0rBBI5CecEDdxwdXhC3CkaaXO32ZwJDMPW_M9H7668EEJ9LxR9RJX4QZH9e7Uw2Gt5N3H1hJB3JduTwsuiZxU4O7XfFseUCmRUorFU2yuOKPVuw-xx9rqWU9X-L6rk1KG31FMB0bK_JWrZ-HCTQHMEipr_V1gb1XwQKienXNZIbZAffJaidsxg6M5PE6MGwuPhPIgLbDsatFSbPGt3J_xOQJ059Nrbgb2NvUY8-_xiFrVofKRns463cNFsDZ-s8qCf9hI1xNBB4ZGu9lqN-ziXTTNB1vj_kTQSrxlNBOJj9Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b5adfbfa.mp4?token=ZgAD5BVtAwXUxvSadeecG8diQXqgw-qHFlrnizffm0rBBI5CecEDdxwdXhC3CkaaXO32ZwJDMPW_M9H7668EEJ9LxR9RJX4QZH9e7Uw2Gt5N3H1hJB3JduTwsuiZxU4O7XfFseUCmRUorFU2yuOKPVuw-xx9rqWU9X-L6rk1KG31FMB0bK_JWrZ-HCTQHMEipr_V1gb1XwQKienXNZIbZAffJaidsxg6M5PE6MGwuPhPIgLbDsatFSbPGt3J_xOQJ059Nrbgb2NvUY8-_xiFrVofKRns463cNFsDZ-s8qCf9hI1xNBB4ZGu9lqN-ziXTTNB1vj_kTQSrxlNBOJj9Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار تصاویری جدید از اصابت موشک‌ به مخازن سوخت پایگاه هوایی موفق السلطی در اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/675656" target="_blank">📅 09:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675655">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5137ab1f7.mp4?token=O1NPrRofe7-XP_QrrYK22TTV6jhovBweVgQJkQc-CvjRvilLoYa2_s-yKLKakU9gZzIXwjaZIBSU4eeSm4h7dlBPYqGc3eAbwW7adbO3y1ZDmYbixefpW1YBJnxCptAxZc6YNWsyHoqklskqsU13kDvhI-nhW99T3apEvUkv8QrvJ9mvT9tacJPC6ETHC8vdO6j3nYXtpYWg77JzhKzMeTOenbkge-5A00INGpBb-nYvI89Ny41iM5zkyjw_R3hmuD7QiOvp_mEytZ-Q_92325k90tGt575I8TAQ8JaT1aYg__fd0TBa14NiYNVTkqfwBEIxf_kB9vR7CjYuQWEkqBk3A4jqqXrVIZOJP4_TPsPe1mNl7U3qkjZEsu_ord24la_8k8Y0Ud7uKAxa1THm_-1U1uy__9SlOTLqXHdvS_UT_tu0TlNHVu5C4TJZZmvXLZO2GytmiLX6y4SgyFfCsnD0KFC539UxyqfNwRk0qu1mXSbhhzvER19nyaw7_0hyr_q5XHcE6XpTL1m7HFKv3aby5pQwuzN4vMpUf7xxCzCP8RVqqj0PeLc7y0Gn2b8AWc2FoXCqIhR6EMX_vDlmoXGtQ3rEX-ICdMt-sSMY1aHMWWwaxi2JpWsg00SoiFlikD5v4DbRrzBKlU_VSzUrE9BlDCqRshqb-XJcdXgPJyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5137ab1f7.mp4?token=O1NPrRofe7-XP_QrrYK22TTV6jhovBweVgQJkQc-CvjRvilLoYa2_s-yKLKakU9gZzIXwjaZIBSU4eeSm4h7dlBPYqGc3eAbwW7adbO3y1ZDmYbixefpW1YBJnxCptAxZc6YNWsyHoqklskqsU13kDvhI-nhW99T3apEvUkv8QrvJ9mvT9tacJPC6ETHC8vdO6j3nYXtpYWg77JzhKzMeTOenbkge-5A00INGpBb-nYvI89Ny41iM5zkyjw_R3hmuD7QiOvp_mEytZ-Q_92325k90tGt575I8TAQ8JaT1aYg__fd0TBa14NiYNVTkqfwBEIxf_kB9vR7CjYuQWEkqBk3A4jqqXrVIZOJP4_TPsPe1mNl7U3qkjZEsu_ord24la_8k8Y0Ud7uKAxa1THm_-1U1uy__9SlOTLqXHdvS_UT_tu0TlNHVu5C4TJZZmvXLZO2GytmiLX6y4SgyFfCsnD0KFC539UxyqfNwRk0qu1mXSbhhzvER19nyaw7_0hyr_q5XHcE6XpTL1m7HFKv3aby5pQwuzN4vMpUf7xxCzCP8RVqqj0PeLc7y0Gn2b8AWc2FoXCqIhR6EMX_vDlmoXGtQ3rEX-ICdMt-sSMY1aHMWWwaxi2JpWsg00SoiFlikD5v4DbRrzBKlU_VSzUrE9BlDCqRshqb-XJcdXgPJyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گریه‌های بی امان غلامرضا نیکخواه در کنار پیکر اکبر عبدی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/675655" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675653">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d04916277.mp4?token=vxWvtVqREwo9MhGu7fXIB8J-bcr5C1WFqplBpbzNbvU9qqnMXMFAMfECNtzsNGxl4v6McXacA9MnYNqn9DhIlPyMcv1erZQg0Thaf5th8GyXr_KbQ1bwO5TNhLphnMt9wiYvP4etgL84S3COD91BsW7FeihxbJr0T3P5cPH6ANMmlOmbGF5i8k2KlXGQh9Cf-jgRRsHcTAkCbjgbZrXljCAEBgCvHa4-HtnL2fYcQUPTMYwlrydEkcIktBvJ9cETy00Xqp6HGg-D1nWEbcwnfxNmt_mHRxsKgI1CCayTXZjDqQ8CKy22Ja3sF6gvRn4dxg4t7Bx2x3jF_hQ17NbiIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d04916277.mp4?token=vxWvtVqREwo9MhGu7fXIB8J-bcr5C1WFqplBpbzNbvU9qqnMXMFAMfECNtzsNGxl4v6McXacA9MnYNqn9DhIlPyMcv1erZQg0Thaf5th8GyXr_KbQ1bwO5TNhLphnMt9wiYvP4etgL84S3COD91BsW7FeihxbJr0T3P5cPH6ANMmlOmbGF5i8k2KlXGQh9Cf-jgRRsHcTAkCbjgbZrXljCAEBgCvHa4-HtnL2fYcQUPTMYwlrydEkcIktBvJ9cETy00Xqp6HGg-D1nWEbcwnfxNmt_mHRxsKgI1CCayTXZjDqQ8CKy22Ja3sF6gvRn4dxg4t7Bx2x3jF_hQ17NbiIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آلومینیوم چه کارهایی می‌تونه بکنه؟ چند کاربرد جالب رو از زبون خودش ببین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/675653" target="_blank">📅 08:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675651">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb8b3b13be.mp4?token=AUQlDk3KHZE18p6wZkKqdu6hLXDmqwYWY8Y1_e-Pui329Km1VPqBdpRAFpLcGI_J9X1lK29cXHXPQHLWuZev_b4h_RB7KMFM4JZ_I0A7tQ5xqWB2eI5UynSvkkTaulOHG-8L-rzD-yVcYIVWoGWFEuuz_8tyOcqCg0lrYbhlywQ4YJXZLz1N_Ig3n7fc3mBgkbF4ld7Qgcg3WZPyF0PDS5oLU5YL4FSAsnDVWmlW3HT8tgov_GjrppFCA9-QixmK1xS41GnzY8Q6J8osnwcj2NclzZem4uSAQFCqaW9p0HUbjvirKhXKp1eWg60S-ZCGhkezAAWMfRP2x3b7_YxLYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb8b3b13be.mp4?token=AUQlDk3KHZE18p6wZkKqdu6hLXDmqwYWY8Y1_e-Pui329Km1VPqBdpRAFpLcGI_J9X1lK29cXHXPQHLWuZev_b4h_RB7KMFM4JZ_I0A7tQ5xqWB2eI5UynSvkkTaulOHG-8L-rzD-yVcYIVWoGWFEuuz_8tyOcqCg0lrYbhlywQ4YJXZLz1N_Ig3n7fc3mBgkbF4ld7Qgcg3WZPyF0PDS5oLU5YL4FSAsnDVWmlW3HT8tgov_GjrppFCA9-QixmK1xS41GnzY8Q6J8osnwcj2NclzZem4uSAQFCqaW9p0HUbjvirKhXKp1eWg60S-ZCGhkezAAWMfRP2x3b7_YxLYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قوز، گردی شانه و خمیدگی بدن قرار نیست تا آخر عمر همراهت باشن
🔹
توی این ویدئو چند حرکت ساده اما مؤثر رو نشون دادم که اگر منظم انجامشون بدی، می‌تونی به بهبود پاسچر و فرم بدنت کمک کنی. #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/675651" target="_blank">📅 08:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675648">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvLDnGpZB-vh1ZIkGSQj1UcvIERMdjbRRGnbLnC782UBxnnKisxYsaAdAPe7c10vh0caUOqbCXhLEgetdJjUc1v9vTTJNRcQEfESoUKED38rcKSCGatI4gjteg5R-rUi4hgJ5SZ-AgCcarIcKaV4Xe26MkxUK0xDxMFfrUG4ixfoN1Ur7idNN1iR-RRwM77iD5rC-_ocAAiZIuJz9sk7Utbl0DkNCSzJp5nPOM0gTAt3Ag8KbYvPqNYsfQlqUG3SjOPfUBNOp3ETp1kJ_EUXK9zBO7uaDmoPUoL-zro_NFDtXE-zW8DtxSbdf2wmKIlh7WWTP1fkiJyYqcAl1Z4DjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۵ مرداد ماه
۱۲ صفر ‌‌۱۴۴۸
۲۷ جولای ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/675648" target="_blank">📅 07:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675647">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
پنتاگون: از آغاز جنگ با ایران، ۲۲ نظامی آمریکایی کشته و ۷۶۴ نفر نیز زخمی شده‌اند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/akhbarefori/675647" target="_blank">📅 06:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675641">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NXOuw2YLUJWOI7l9V0-ZW9fUDJ9i50kJ0-n9BhpWyvnnhsvhLSBDhsMy8Qm5-xrF38pYPEH6hYtshCZ0fdmk8Y1wIe2iytBVSOZHqAO1gcYWRNSiCtzNArLrcnbbDNNaccmlNOJeRD46LNklkwI69OHaNBUlT3d7qbNF6yHwWa0V8Bk3w2XSGNyZS9Raw1JFL6WqYYN0uPv_NV50bFNLjrBAjwzrQNyTKdZAsLiu3QXHK96OSFNL4dvMo4NmBQfT5inhaT_WUkQnMnrUAFFX86AxMuMqJhgC9b_oO29ZcHAjDNZS_Wh0wGkl3g9GuWS4es7nGZoxHgKgnfwmqgZbuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKyT6e3Ot79SGV-rmYPG7-woCaJpA9G1T5kwiP9uEuA3ZNBPPesSnaZ1tJkGMQW4-xDVsXs84Qb2KTBDuTgY2kjJSLlfcM6Ztko4u0E7JrjXTtvGrDOEpM76nlP6sbpM-KzSINfcJqZJbrRJRxMlvuiH5IX1IYTGU1lE2CWUiqn_gPivA2qxawFJ_776yR26KtFl5l_DOIscGiKAhXKK83fHCWMsZ4sCDrELU7iByvGYTRE0WDniwBLBknh1Mpg0DbTjocUXeysZ5nkzbMm5wjl3qpsaiXHs_OOMk6sf85zehUWzUwOftd6hPuYFpgGdPZvfG29M5lFcD4G-ICgjrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aBNXUf_5Rw6QNoSant7XKTep69Ank3-urR-BUaXS8A8FjjHPdRZeEyRqYNeuKn0sy9R72U4mibVq7Zm635TDeFN9ZvVXhHwPMHQA8h25ZPNflqipZ-9UEX6ogNL83umig3oO6kvhrRa3VZAGoUof6iwIfDFHOBRmM92yrSrRDt5twMG3X_z-1j3WsPpX7QuCBqOb4ri6L0hyVlLNE9K0T88rmODXGf-wO0MqoA3uXc8ylgzK8AleAuJpE8im1cMA6WZP2qsm6oVm7Gzu-trk3ca5cs5JICN1L5gEo0M55BWdMFlQ5FIcyVjwniS4uwrPoCVCM3Mh1m5rKaVme5ujqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WpDoyUAQVkX-FKvMv9w59AYB9WugCfCOMOfEiUqdAlECpE-jRyW3RsxTAb2426Inu82N_M_ifIqiGEhcuA6-6o6lr0lCxZYhMLQkHu-MR4G2FOnvYu8d2AqjWautUt90LgHi-4YVmPw6EYUgjymzdaN_Uf8jjDeoBtDKxk8V4rk0b6K71SmSWBvwhUTLjSJOfqP2QR-LU3EaH1nEaDHKxmNtTcVj_-JmjEzVmFrUjCjc8SqVr4jVj4kiWaX2hx4oZBWTQ07oQlCSN53eKXzPiNONGjpgrgAxZp3f3bmP4Mv4Q_vMTkGlH4XZtmHCLcw21U7atuwyw78nAHih-VugOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شیطان زرد با کمک هوش مصنوعی به خط مقدم نبرد آمد
🔹
رئیس جمهور آمریکا طی ساعات گذشته پستهای مختلفی با کمک هوش مصنوعی در حساب خود در تروث سوشال منتشر کرده است. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/akhbarefori/675641" target="_blank">📅 03:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675637">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adTuJt0pcmN6-__AourGWOxtcVawo92NfyVtSzbJiQe_0TjXuunpP_hTLBeRTX1ofgzUpZKvIsOgzSpZ9mEurYwA9MsZfIhw2qwJbHKgJJJQdhRT9t1sJXYFi96ZZ82_legky2fJlseFp6it6ZjZ0BHU1kPecYrfJ-kCW8RrN8qotHFAdM2YD391vbdCm7yNfu1E8aXWOh5pSkNXEDQ-jyxvWTLFv-NNcJukVMLny7gN6i84cYr9Ou74-uzT8owtdyCSUNZblxVfFTYOqIVx9BDEh6OkwF6ydl-Cy-FStMv00lv59XfbNsG_l-YAIgyjIZXr5LcEa1CjOncwAluqaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای زائران اربعین
🔹
کدام مرز زمینی برای سفر اربعین شما مناسب‌تر است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/akhbarefori/675637" target="_blank">📅 02:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675636">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b6ca7302.mp4?token=kMVjN6RO98J1Jkbdbqjqwb_dled1imh_2bXTc1SgIgo288QzwrrpORyrIQ4Ih5N7EjrNQbvhERvBpN74i6bxz7-izGv9K39BATu0SqXjHsDP0N-5SlIdcESLHUk8WMlTghNdaceo1dtfODM84C-JbNFFegm260TAYbYhIfVyRjGVFN8RoGUDKiyjR8FRJTD4ly_dIwn-WmGcAltVN0CcO07Ga-NZYqPSonySzhRhIqMxR6R7SCLDVeOvPTYn_zG1DTIYqlBgMH_RvETBArQ1uM4-lBM7vRhWzacstko-Thh-jOjo-AojQ52EwwiB_416ztbw1ORlS_TT5kejixQ7zr_vgYW9SybUB4iFe2-CDkjpH0zIGA-0XxIYtbyX1rAcRg2ao2Tun4fPOq3oyUH7Wkxj6AgyfLjuf6UPFE6htAvHQMOW1zUn43KJBMG6DQTaMxqu0beDOe_OTtouneazcbRkOZAF2FbekQEe6SXP_qnpcmmogmEOrSgg5TVooCWFyBrWyLKXbMp5YfCqt3S-66O0oLLq5wbxzcDfKF-8hAhaBSmmpdKNHxG8_rB2wNthq0nKSBMPs4AYcPOFuNh-c14Md70AFCbSCvO6wZgvRAXIvWGYDp65pU2cZVocfBpD5A_ZXGG0DlmcJoxy9XR12rtRcwYSONF09Lvud2ON53I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b6ca7302.mp4?token=kMVjN6RO98J1Jkbdbqjqwb_dled1imh_2bXTc1SgIgo288QzwrrpORyrIQ4Ih5N7EjrNQbvhERvBpN74i6bxz7-izGv9K39BATu0SqXjHsDP0N-5SlIdcESLHUk8WMlTghNdaceo1dtfODM84C-JbNFFegm260TAYbYhIfVyRjGVFN8RoGUDKiyjR8FRJTD4ly_dIwn-WmGcAltVN0CcO07Ga-NZYqPSonySzhRhIqMxR6R7SCLDVeOvPTYn_zG1DTIYqlBgMH_RvETBArQ1uM4-lBM7vRhWzacstko-Thh-jOjo-AojQ52EwwiB_416ztbw1ORlS_TT5kejixQ7zr_vgYW9SybUB4iFe2-CDkjpH0zIGA-0XxIYtbyX1rAcRg2ao2Tun4fPOq3oyUH7Wkxj6AgyfLjuf6UPFE6htAvHQMOW1zUn43KJBMG6DQTaMxqu0beDOe_OTtouneazcbRkOZAF2FbekQEe6SXP_qnpcmmogmEOrSgg5TVooCWFyBrWyLKXbMp5YfCqt3S-66O0oLLq5wbxzcDfKF-8hAhaBSmmpdKNHxG8_rB2wNthq0nKSBMPs4AYcPOFuNh-c14Md70AFCbSCvO6wZgvRAXIvWGYDp65pU2cZVocfBpD5A_ZXGG0DlmcJoxy9XR12rtRcwYSONF09Lvud2ON53I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحلیلگر لبنانی خطاب به فعال سعودی: آمریکا جز حفاظت از اسرائیل و غارت ثروت شما هدفی ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/akhbarefori/675636" target="_blank">📅 02:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675632">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdac069110.mp4?token=VJ02ir3OVpE9wX0PNbUIOln6y-V6G0P8WcCs99ZEQNPCyacOdtyhmMpbe_IPxNLyqhVsjxb5OuMzZqG93qp4aJNUcEAiH08OQORojLBJPSfZO5jRHqzBwz6Sp_wDcYITGK4eM9LyKkz_ikF2X3V9CrS__Cf9ZaZsXLIBDVApdnx1xh6X4hiGAFwuPp3G-CEAO15ALxQfwiqomQcy9zpHFla3ztrwMG_WTEDlbvL6feV8UBZ5K4WakE5T9n7fU8c25MzDRLzX38IL-OKPYbLhHiD0uPBD00tIZT2SWLERnjxYYvcd4S7Tn236KxJK9vO9Mzeq27UQhhg6XRegZnDYaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdac069110.mp4?token=VJ02ir3OVpE9wX0PNbUIOln6y-V6G0P8WcCs99ZEQNPCyacOdtyhmMpbe_IPxNLyqhVsjxb5OuMzZqG93qp4aJNUcEAiH08OQORojLBJPSfZO5jRHqzBwz6Sp_wDcYITGK4eM9LyKkz_ikF2X3V9CrS__Cf9ZaZsXLIBDVApdnx1xh6X4hiGAFwuPp3G-CEAO15ALxQfwiqomQcy9zpHFla3ztrwMG_WTEDlbvL6feV8UBZ5K4WakE5T9n7fU8c25MzDRLzX38IL-OKPYbLhHiD0uPBD00tIZT2SWLERnjxYYvcd4S7Tn236KxJK9vO9Mzeq27UQhhg6XRegZnDYaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قضیه بی پایان چاله سرویس روغن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/akhbarefori/675632" target="_blank">📅 01:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675631">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujKk9VmQS2Y8IhIafYGnvGLjU1bpre9sK4-Y1c3wmKensp-Q_JygxsH-8aupTkX6iFKGZybFIyK5x4df3xchsaseDCwf9au1OQI9ULnemoSjnyNIRu9zxAcOgt8UQzi8J4YOpM2wiK0M8CgATdSfS6fwnKIfJ1f_nkfWWjenHRTFYF3Sv2NZM6ngcQsWjU7eQzeEEdrLZyEszN3goYOqpvB-Ql1zDb8niSk3z4S3n2VIHPCMmTWDW9sNuGWgPq1goGmwk1rn98kOGqru2wjpl-lqfvtEeh-OkkZq3nSJ9IkjnX_ew7k839dSCV8XaAVCF3Uyb5x8RPjb9mq57mCJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم عزیزی: اوکراین به زودی می‌فهمد ایران اقدامی را بی‌پاسخ نمی‌گذارد
رئیس کمیسیون امنیت ملی مجلس:
🔹
هر حمله‌ای به ایران همیشه هزینه‌ای دارد و این موضوع امروز هم صادق است؛ ایالات متحده و اسرائیل به خوبی از این موضوع آگاه هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/675631" target="_blank">📅 01:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675626">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sp1LAFD0wueyjh_RXQpoX4izmLGy3WIrwnpHhrstImgwmdjjQlUuQVfz26MAzkEPdUU-IRSrHQKRFM7PhdzGa7zwUtruVhgdAEwUtQrZxZIXVB4bIPhl6K3YpFugEQlvHcdWtIarai02XcqDXx-OPS1EZLhtv1si-q0OCL4xjKR8Q4GgGvdXI7LaI57Od_51zXLkz69KivvyKuy-z5Fgif4mjbTqoTTDNKrDAu8D0ZQjGHvQtXYPnh6q1kViyOcdBcgYt60WZBSHlvuUhK_M9Phq36KdExxyIeB09wGuEBK4Yk0tuYFdwLrYzOm_KWXV06wzOk4If19vVmIM2Ry4RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای نشان می‌دهند که آتش‌سوزی ناشی از حملات یمن به پالایشگاه جیزان در عربستان، در حال گسترش است و اکنون تقریباً کل پالایشگاه را در بر گرفته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/675626" target="_blank">📅 00:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675625">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/850e2e6b24.mp4?token=N6GL_lpgKvn3VdDkFRTmrs5Il1q8x4p4d6sh8tgniDozkFC6kjPHjMRMACAivCuoQf1CLMnqrT4bKvlX_qGUkFovj59mKk60EUhd4JpOPOS9a6X_Gh0i99zSe8_GcKVo6fivRIliLXAoN6CTuA8eBcoHU0ZKr_La2rqC2WTj2pOjjUcCd3aT4KQe2VLQ1tOXfc6W9hgdYSESEJTxhV_a9IV2rFfiC39K4veaWcStRoGeNnqGsXsj2YmUSIP6ftjNJjrV8_1_qpf4I1_S1bELkcHaikBOC_Mvo2xx3fhjlCKR_Ou3py-HAJSagM3oYgdHHF34f_QKRMitqcp8-0Kl8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/850e2e6b24.mp4?token=N6GL_lpgKvn3VdDkFRTmrs5Il1q8x4p4d6sh8tgniDozkFC6kjPHjMRMACAivCuoQf1CLMnqrT4bKvlX_qGUkFovj59mKk60EUhd4JpOPOS9a6X_Gh0i99zSe8_GcKVo6fivRIliLXAoN6CTuA8eBcoHU0ZKr_La2rqC2WTj2pOjjUcCd3aT4KQe2VLQ1tOXfc6W9hgdYSESEJTxhV_a9IV2rFfiC39K4veaWcStRoGeNnqGsXsj2YmUSIP6ftjNJjrV8_1_qpf4I1_S1bELkcHaikBOC_Mvo2xx3fhjlCKR_Ou3py-HAJSagM3oYgdHHF34f_QKRMitqcp8-0Kl8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عملکرد تصفیه‌ شدن فاضلاب با استفاده از لخته‌سازها و فیلترپرس‌ها، لجن را در کمتر از یک دقیقه از آب جدا می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/akhbarefori/675625" target="_blank">📅 00:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675622">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si_vqycMFv7tMyfuGbEs0pxgjn8W4BFpOx5z0ANhZa7KCeyxRmvvk7gwy1-loinstpNd0QraaY_JwpMjVGpGYQyXCY0K9J65j34HVzUnj0QJs20L8pNqi4k89d_z2v95AgzASODCq6JehOx0hTisr9OloHvEgfcfBHuARLmEWFWJbSbaEEM8BkALWq-0PU7ykfXm7kVn8t9IKoLLOCXXNStm3bpuJlxgBEgu8d6pCxwzVBZg3UPDJi0hKm2EeDPZeZ2jYp9ZYPgtX8ihGWFLYFtyOZKWhWzXPhNuEl8rjJytrSYcJp3tp31yIND7kKIfZW7Cvc9_em7Ua4IO114j2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخواست دختر اکبر عبدی از مردم برای اقامه نماز شب اول قبر
🔹
المیرا عبدی، فرزند اکبر عبدی، با انتشار پیامی در صفحه اینستاگرام پدرش از مردم قدردانی کرد و خواست برای آرامش روح پدرش، نماز شب اول قبر اقامه کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/akhbarefori/675622" target="_blank">📅 00:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675621">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b348c813e.mp4?token=JmSH7pKTkS0pi8wFn88TfXWqL9Fu36YaLir9_q3Q8I-hrMpkGfdqJATjgHggne-CEWXcRktEF1GP-KbjfTpV1xU2gbTvFBv6YLwk0gxZvYy_e6wYbPKsJHgpOOS4mq-GYFNRvwarDd_JLAGn6SKszW-bkTzyzzM4xISLm1M1AK9o7_w1GBGl_0Y1KZLOa9b7jJ0v_XQE2zvzffr_Ujqv91a03Q8Z1AQh5rsY814FnV4UydN0KFfZ6VgsJSEKvb-GEVbkVRJuVkiAKU90OHxgG70KktFZJLNMqeMVj3YEI0pxvAoW6UEmpDjZwxSdrud3rI0GwIeQmfmmpVKfvEl2eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b348c813e.mp4?token=JmSH7pKTkS0pi8wFn88TfXWqL9Fu36YaLir9_q3Q8I-hrMpkGfdqJATjgHggne-CEWXcRktEF1GP-KbjfTpV1xU2gbTvFBv6YLwk0gxZvYy_e6wYbPKsJHgpOOS4mq-GYFNRvwarDd_JLAGn6SKszW-bkTzyzzM4xISLm1M1AK9o7_w1GBGl_0Y1KZLOa9b7jJ0v_XQE2zvzffr_Ujqv91a03Q8Z1AQh5rsY814FnV4UydN0KFfZ6VgsJSEKvb-GEVbkVRJuVkiAKU90OHxgG70KktFZJLNMqeMVj3YEI0pxvAoW6UEmpDjZwxSdrud3rI0GwIeQmfmmpVKfvEl2eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از یک تصادف در چین که دو طرف حادثه تا رسیدن مأموران، همان‌جا منتظر موندن و در این فاصله سرگرم گوشی‌هاشون شده‌اند، در فضای مجازی پر بازدید شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/akhbarefori/675621" target="_blank">📅 00:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675620">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZgP8mnt6r-1PV_o8e-pP2nw7RD4-B6FT28yPSgVY7lspYyygNYbgxA54keapS7JQ3ewRHV9eQzRiok2TPTmqqoG4vz4Wy1nfYmwZp4GuLTE4f7_KyOMIqekeppZN-IFv_TqAF5lxGiDvycaU24_6LW3D1fsjwHQCE9LOIxIWSg0QYM7iorQ0mdVZff286ErfB-s0HRshtmDLVxyCzTyQdHbtPedl_B2xbvdDqYspqdlBkxL02hhF1jhMOWN8LIfArIOrtG-TK82zfofh4O_NnPotozsXY28_Ef_SCJKjxS9z79abIA7uVrmG5pn0w4MLmWs4zPey8nFal0gzYWzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیطان زرد با کمک هوش مصنوعی به خط مقدم نبرد آمد
🔹
رئیس جمهور آمریکا طی ساعات گذشته پستهای مختلفی با کمک هوش مصنوعی در حساب خود در تروث سوشال منتشر کرده است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/akhbarefori/675620" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675619">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3212f3f8f5.mp4?token=cm6Ew1544AWO9SeisSIR2oAYgco2tzEjd7uYz8v7GqKYDpO5SgW-wzwoFqag3lNA4DlbSF40EltPqU7ThkIIgsuK3exFXISKJ4pvY9LDSSa8dgsB-daL0yK9CR5MX2Hs2lfUGPAeKtk8dmKm6qDZBxxq9yRsIyErTTxtL0Tb2dtJa5gupgW-m3YD6Ri0rbJteVIrgFDe3Q1YmzB3VjL-UWzO0JXc_N1BgOt7YapC0-qZiPTuM-SeQZ7fVUjyZyq49TiukYHVCXFTbVmo_X9OFQPXINUkn9iwmZj04_DcOfAHmoo6tbaPNzGzou_N7EoRBaSoOOlgM28NgvwOkwPBWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3212f3f8f5.mp4?token=cm6Ew1544AWO9SeisSIR2oAYgco2tzEjd7uYz8v7GqKYDpO5SgW-wzwoFqag3lNA4DlbSF40EltPqU7ThkIIgsuK3exFXISKJ4pvY9LDSSa8dgsB-daL0yK9CR5MX2Hs2lfUGPAeKtk8dmKm6qDZBxxq9yRsIyErTTxtL0Tb2dtJa5gupgW-m3YD6Ri0rbJteVIrgFDe3Q1YmzB3VjL-UWzO0JXc_N1BgOt7YapC0-qZiPTuM-SeQZ7fVUjyZyq49TiukYHVCXFTbVmo_X9OFQPXINUkn9iwmZj04_DcOfAHmoo6tbaPNzGzou_N7EoRBaSoOOlgM28NgvwOkwPBWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خادمان عراقی اربعین امسال با سینی‌های موشکی از زائران ایرانی پذیرایی می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/akhbarefori/675619" target="_blank">📅 00:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675618">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e830fb3882.mp4?token=MWFDK9f21sDMevHMhJch3tGk3uCTLYrKaAsLC0rwCIvOAzhYqFKu4hGd04h34R4U-rSFzU_KkyzKXoCb3ucSIIDZbZNX3R4q_z7NBTsUcFIGt14VBBrAuoakJaxgfucHfer_9LvNYrStCk1gnZeXv0GykYCWTQrbfnjasaBjyGKvvm0S3q1FTk6Nrx77z8VJ2usy4qzvKqerR9_iHRnPmoRe3A7wNgxk518GDmXJkTeLqXqdja1l7Y9U7DUN7rE5shUbYoTl7PS5sPB20pHvwp_rATGAu1UeKSKHAmgv-6MyLQZkJ3vY6gD_oErqTqEVrIfqmJe3p6CQ7Tsq5cBEFDHebgUVvtbA39TSH_m71kIi94JrobvJXqh1mnsIB9HWYZWp3krrhsMqSAFXkacX5YvTkqMeQRuu_fxBTO34y1kLIg8Q87Zg3XfnPleUrDHZWPMvMN0JlWQqolRItPahsbH5J54FKOIIYgShnyW394U3D0mnwXx5DeCTZNYGfklm_RzJDmVcgi2hFoKNh446JbDRCjTFGhrCFu0BuobGRk296M1ZesieA7LTzI66SYTTpZ3T56APEkujjB5fDOnOpkUwr6EtEJ4dfech4jrFUAcQism39UX2MtDJTRUpnS-OArp72vZcL6wiWmPEHSfqwxK08pW6LkwuhBPfi-BBOxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e830fb3882.mp4?token=MWFDK9f21sDMevHMhJch3tGk3uCTLYrKaAsLC0rwCIvOAzhYqFKu4hGd04h34R4U-rSFzU_KkyzKXoCb3ucSIIDZbZNX3R4q_z7NBTsUcFIGt14VBBrAuoakJaxgfucHfer_9LvNYrStCk1gnZeXv0GykYCWTQrbfnjasaBjyGKvvm0S3q1FTk6Nrx77z8VJ2usy4qzvKqerR9_iHRnPmoRe3A7wNgxk518GDmXJkTeLqXqdja1l7Y9U7DUN7rE5shUbYoTl7PS5sPB20pHvwp_rATGAu1UeKSKHAmgv-6MyLQZkJ3vY6gD_oErqTqEVrIfqmJe3p6CQ7Tsq5cBEFDHebgUVvtbA39TSH_m71kIi94JrobvJXqh1mnsIB9HWYZWp3krrhsMqSAFXkacX5YvTkqMeQRuu_fxBTO34y1kLIg8Q87Zg3XfnPleUrDHZWPMvMN0JlWQqolRItPahsbH5J54FKOIIYgShnyW394U3D0mnwXx5DeCTZNYGfklm_RzJDmVcgi2hFoKNh446JbDRCjTFGhrCFu0BuobGRk296M1ZesieA7LTzI66SYTTpZ3T56APEkujjB5fDOnOpkUwr6EtEJ4dfech4jrFUAcQism39UX2MtDJTRUpnS-OArp72vZcL6wiWmPEHSfqwxK08pW6LkwuhBPfi-BBOxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیاده‌گویی
جولانی: ما هرگز نباید مجبور باشیم بین جاه‌طلبی‌های اسرائیل و ایران در منطقه یکی را انتخاب کنیم
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/akhbarefori/675618" target="_blank">📅 00:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675617">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toTtHKhU-3EUElbukAZzZ0CgWszrU0WvIpFByaMz6CrV396JjnjXh_V_xZK5n7Op48S7fKPgLbh7clZh83OIOR7GAKpkkNmjJfNq4xr0VfUNFD3de-c5PB0-P6BUg6A6n00beNoRPT42U2wZ4JpZhkfXJNsW2j5YMb4b78txlNfVxuIVdvHOhDGvREngshnNL_J-01-Z3ZvCIofgdI1UfaxKGuMnLNfm2enoulQmY3oZSe1aFgL-II3SZUJ_UOsQ2W0FuBPesIBh-znH7QlFWCRc8Ey3qZrS9nmvNSKzmsPShxnqwFu7K1ejeX84C1xzuvh9TZn_nh9eeF4DDDizJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/675617" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675616">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84cd7cb3c4.mp4?token=KIm62_BGHVNLrizDhHxKK5cDpRQLzG7yT8li7qD1Cj3Lr-2mRr60eImInnEuZEI_avEKp-acKmJ9LA3JcgllY-sRHDesBrXj28rnP_L-8FzrWGFoVQJ17mriIU10SLjKbaqr7xg6pfuGnLpWOoaHy7viotYECzM-dXTD5Upm67VRY_wJSycRg2M-H3Y5rdi23ghdutb6loDC2cvrViJCX-iEWikDGcZUQtrC5NGnngPCdk_5xif0uVVDyQbnKlhnE4J1VA4iyJwahOYEfbWASpLaFWyrN3_PSteS4GC3IIVorWctNY9cPgxugG41wHop_CcwK64sPJH6Bb7-9sYS6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84cd7cb3c4.mp4?token=KIm62_BGHVNLrizDhHxKK5cDpRQLzG7yT8li7qD1Cj3Lr-2mRr60eImInnEuZEI_avEKp-acKmJ9LA3JcgllY-sRHDesBrXj28rnP_L-8FzrWGFoVQJ17mriIU10SLjKbaqr7xg6pfuGnLpWOoaHy7viotYECzM-dXTD5Upm67VRY_wJSycRg2M-H3Y5rdi23ghdutb6loDC2cvrViJCX-iEWikDGcZUQtrC5NGnngPCdk_5xif0uVVDyQbnKlhnE4J1VA4iyJwahOYEfbWASpLaFWyrN3_PSteS4GC3IIVorWctNY9cPgxugG41wHop_CcwK64sPJH6Bb7-9sYS6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در اوایل ماه مارس، لیندسی گراهام پیش‌بینی کرده بود که حکومت ایران ظرف «سه تا چهار هفته» کنترل شهرها را از دست خواهد داد و مشارکت گسترده‌تر کشورهای عربی، «شتابی تقریباً غیرقابل بازگشت» ایجاد خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/akhbarefori/675616" target="_blank">📅 23:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675615">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32d175a29b.mp4?token=OQrq8XEVWeV3RxPWYnYQHfLXoaZRl7eAaC83MkRT8AzyNjZjImZf5YYNfxTqk7YnatxRJly8NlFIcSAX0XJiHiMjVtc1-_geVW9nCCRep4xMWALMJiaITBuKm3QEgNKoBTIthE_6lMMNQZyiQkwa8kFyfZ1YueJSx0xekxsVWaKAjRm0cUJ3GJiAmojiXvqxIn7bOBHrPA_CLRtCqvOjlX9G__947Xxa8k2dL9s0Wt00f_r-kFT5fNFG1UzuXItLEVAgFlbM6cORtPmGKl19tEkVqM9BSd1JcRfQg95Jk0gVk7pQMYY5rbEjRcapwfHFe9ubUwvWqqf91ERhhf6hQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32d175a29b.mp4?token=OQrq8XEVWeV3RxPWYnYQHfLXoaZRl7eAaC83MkRT8AzyNjZjImZf5YYNfxTqk7YnatxRJly8NlFIcSAX0XJiHiMjVtc1-_geVW9nCCRep4xMWALMJiaITBuKm3QEgNKoBTIthE_6lMMNQZyiQkwa8kFyfZ1YueJSx0xekxsVWaKAjRm0cUJ3GJiAmojiXvqxIn7bOBHrPA_CLRtCqvOjlX9G__947Xxa8k2dL9s0Wt00f_r-kFT5fNFG1UzuXItLEVAgFlbM6cORtPmGKl19tEkVqM9BSd1JcRfQg95Jk0gVk7pQMYY5rbEjRcapwfHFe9ubUwvWqqf91ERhhf6hQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست جدید شیطان زرد: دشمن را دچار کابوس کنید - ترامپ ٢٠٢٨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/akhbarefori/675615" target="_blank">📅 23:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675613">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93448d9c96.mp4?token=mpiYBlBFz1oAI3a7ujz-7wrdYBzjpaG9ZvgJDgb5QDM7C0hsTZ6TtvG80JszVZOusZtDYJ9OkM8tV-YSfB-8VKCT5bY_Jz-PLGjh2MStBvr1eJQ8yN8jIwq_bZRdagM1-5hUyBqJdJJPl5mQQbWi3kkVemBXSosilvwB8EEzzTNxDYrraAEYyCDDIWkZaQSBUH-Q30UuwVrznnIW07FLnnGhmWO3uM_tloM8LIPvOrSvHMWQ_Pat9QXz3R0MWgsZCnXRjtKRGWU52iwDozaC5gZzQkuPeZC-3moSpFlRO88jL-PezYQKyQuO6URcXUZPRam6LGRsg5S5VYleMdof6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93448d9c96.mp4?token=mpiYBlBFz1oAI3a7ujz-7wrdYBzjpaG9ZvgJDgb5QDM7C0hsTZ6TtvG80JszVZOusZtDYJ9OkM8tV-YSfB-8VKCT5bY_Jz-PLGjh2MStBvr1eJQ8yN8jIwq_bZRdagM1-5hUyBqJdJJPl5mQQbWi3kkVemBXSosilvwB8EEzzTNxDYrraAEYyCDDIWkZaQSBUH-Q30UuwVrznnIW07FLnnGhmWO3uM_tloM8LIPvOrSvHMWQ_Pat9QXz3R0MWgsZCnXRjtKRGWU52iwDozaC5gZzQkuPeZC-3moSpFlRO88jL-PezYQKyQuO6URcXUZPRam6LGRsg5S5VYleMdof6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
الموت ثبت جهانی شد
🔹
سی‌امین اثر ایران با عنوان «دژ الموت و استحکامات دفاعی وابسته به آن» در فهرست میراث جهانی یونسکو ثبت شد.
#اخبار_قزوین
در فضای مجازی
👇
@akhbarghazvin</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/akhbarefori/675613" target="_blank">📅 23:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675611">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rb8V3CIiFryptBN3JbUNKTFBL0_uR1kBxPA5z__dYNCJmYndgLWTyVjixRHfjRJ9M-8b1tMCy4i55dVpfbnWRtVEWpUx_LM7ijmg9FkNGHNXHwF6q5-adroiJI09-AxDoTuDztx6h1rJry8655KDk_JDm-dmIX9FAUov881Qe1FDzIMV7BNmChwkSaL6L81qaxiz7hP-fUklVD17-fngiiqpMeot-jS7BWYENO88gGIUQSVDiM_CWD6z_59T0lgQGCVtLzZCh1y3Zs9AzgIrI8jo3PpSUgzzhl2BJHcikUuELgALfCsZyWq40qwXOxVPsiMuW7jFGOHWE1BA4GR1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X5hmxNkYoZ4HDF8KPJnKSvHL3-ATp2utTyauaXiRGaVZKSq-sdmNrybCFZ7KxXjwgk31P2u_97xVVqHHLLf-CKHBrx-0u5-xZKOJgiSqL_7H1Qr6WO9v5ueBlYjnho2zNPDfCYDbdyLtdMOJC4vW3RWTsEgxewO_0yheXwWskyLCY9WEsX69-yMCnGlvI0qj1RH1drVopPEbe9eIkXQnPun8T_lClZr4d92rPIJgjkKTULRSyvIBpbcmA6C87UER94ATcsV0HePbumbEdIet63CTOpoD9xMAPxqMX96AbXJtn4F7RL-m9eYsbcnD6iTYf31kjJHHdE0DruunOvSnXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر برای تربیت دینی نوجوان خود چالش دارید، این کتاب را به فرزندانتان هدیه دهید
🔹
«نامه‌های بلوغ» میراث فکری و تربیتی اندیشمند بزرگ، علی صفایی حائری برای همه جوانانی است که در آستانه انتخاب‌های سرنوشت‌ساز زندگی ایستاده‌اند. او با زبانی صمیمی و عمیق، از بحران‌های بلوغ، آزادی، انتخاب، اخلاق، عمل، رضایت الهی و ساختن شخصیت سخن می‌گوید و همچون پدری دلسوز راه درست زندگی کردن را نشان می‌دهد.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/675611" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675610">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c89c9b87c.mp4?token=toeOs7V_SP1Qgs06ndFEMdLezdgSK-lI1LQyNpg2mC9L33C9Zi9RWC3x51ED2SeYxo1XD-t6go53oGYylVYr-NIl__Ipu7gIvjOp1Gk5RC_F01xPx4f-YtGMIAmVUdAsPPusDceau3VpB-2XUK_fh7pmirWxXkrbI5ypn9_gt1kKmt5Zy6pP_DlAG1biFs1Xfa1w9Qt7C3JZawTY2EAuED0BO7RtFApF3KxTmjZ_XyvleQArYRlobQkjtl9zxQ5wX65HNE397BZZ96qBNTNIHLMO5XToXNILAJE87a_EXKy0b0GhOjDD4zMfVFDOyNGiJjOlmxmyPNZqQWyNn8mn7FmbqA3f0RaQDgmKQokrCdmwBzYrRj6zhqQrK5KUVNfaX_6ThiVbcq6DZrGrqUxLMqCvn3ipZz1oe6BKqh_LIsfsOQFKRtiKbxJ7Eqj_M9Jox4wK0lzZpOJZrWivlEJtJVtPOOR-dPxwApztEMbL8WVc3QcuaFuuF8X4hD21NUUDyP3Bh7UNC2HN8I87SqeEB774oFUfT3zaJuqZml_RU1iYQ4czIOJcKTMXFZEJLMv1_GnM-9LzETuFOGX3KAFaRBmYVOqzM6d3U7hJpWUn9tkYnMVBbvcX-bCkrWSb2GifGdGn6jvTQ8yR4jPu-Q152jMFfDCsqW4gAKaQruvVoHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c89c9b87c.mp4?token=toeOs7V_SP1Qgs06ndFEMdLezdgSK-lI1LQyNpg2mC9L33C9Zi9RWC3x51ED2SeYxo1XD-t6go53oGYylVYr-NIl__Ipu7gIvjOp1Gk5RC_F01xPx4f-YtGMIAmVUdAsPPusDceau3VpB-2XUK_fh7pmirWxXkrbI5ypn9_gt1kKmt5Zy6pP_DlAG1biFs1Xfa1w9Qt7C3JZawTY2EAuED0BO7RtFApF3KxTmjZ_XyvleQArYRlobQkjtl9zxQ5wX65HNE397BZZ96qBNTNIHLMO5XToXNILAJE87a_EXKy0b0GhOjDD4zMfVFDOyNGiJjOlmxmyPNZqQWyNn8mn7FmbqA3f0RaQDgmKQokrCdmwBzYrRj6zhqQrK5KUVNfaX_6ThiVbcq6DZrGrqUxLMqCvn3ipZz1oe6BKqh_LIsfsOQFKRtiKbxJ7Eqj_M9Jox4wK0lzZpOJZrWivlEJtJVtPOOR-dPxwApztEMbL8WVc3QcuaFuuF8X4hD21NUUDyP3Bh7UNC2HN8I87SqeEB774oFUfT3zaJuqZml_RU1iYQ4czIOJcKTMXFZEJLMv1_GnM-9LzETuFOGX3KAFaRBmYVOqzM6d3U7hJpWUn9tkYnMVBbvcX-bCkrWSb2GifGdGn6jvTQ8yR4jPu-Q152jMFfDCsqW4gAKaQruvVoHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از آتش‌سوزی‌های گسترده در پالایشگاه آرامکو در عربستان سعودی پس از پاسخ کوبنده یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/akhbarefori/675610" target="_blank">📅 23:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675602">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MPJiC3kIElHZWQyAgMQYqIx52BrHfJVovoeYAp-oVnuK-i2Kh4q016tHpSoSvwKjPORuLuWqXOvLTac9jH5CjnRvUhgQ9Yf9nEKLgoI-MXYretbiw_LnAVd_WH3oi8N2MzBU-pz0bx_S9LfpQYffrF3E42uUxqcqoEu8X_xiFZDPcYGDMKP9yeMWp7y1xKgblhlfx4fZBsF3Sltwqto-rG-UHxlT0jG4ooOTQJUDgcAN8SJ9jClju46s9tXm8kNtxH8mYoY1Tnz7SexBrjtlBLCZP8snZDePTySe2jf-KC1b4U908ZFY6vKisS80yyOI24YwdA2xPl2J85Cx5N4jMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQ2e1W0TmWUTB_QOQ9pNebWuyaW0tlvxNxdYH7hf3SufMXS3X8ipVf_8WHXcxoiD7YnYjBoKK05s0HXR39GA-709sknQxp9-vXNx0NtKZI5sbX1PeYlqXpRkBXyusT_Svs99cQNMUch-_8HlW6pWvmpHkQ1IRZ8Fms7qfQpAtcNnXNjNVIeED1H9yCdtkC1GETZPDGFXNZyp_oIIhfNQfmK58nUfDp-SMGjFB0Yqhc_K0Chn_KwksEdYa8Yw9G3weaGuGnqBI0UN5uRLHryzU7UHLj8tTiLHciSA3-UjUdN97CiG-E9Vu7sODQcqVLuaxkNLdwdhYoXEunXNhKmENg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZxLVfEmfmnlOmWeVIZstBgoStZwbY4bSgVt4E06FtzksEVmYHe0oeAw5hlnlS4L_7Rps86NZWdW3koI5MGmI_ied7gO4KNwaw3DF1dMQU5Kkh8Dm7Zv-q5w_3-XBWG4PeWvZOkeUzDoQhcJXibKSbHFI8lTN4Txcsgma8v27eo18_kOcLvc_L3HQE0X36duAo88u-Iq6jgqzm3-v4_9bdcqJlkX-9HiC1FAhMEoUsCTdRKHTiT6szb4DDdPyBbu4qd-dmBJzhIxrqtVtExh1Ad6cdxefn2JnSOvBy_kbO_nuihnQRxD7AFeeaeAG4tKMx0nWeePbdnDXLnl8R0g6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwWtMdLToGeQ9qV_FSuOf6qEuwJIEwZTwDoGNxeavR0w7PUDCKn-VYiLcIPj9CKy8kqlfu3Rd9XhsfYeiAljFLE-1vmhtB48wNCHDMpAdpkfSjtgR3gMpUggFiIpyk_UOnCrreRuSvnoYc0vk8s-QyWXsmTeliyhDJCvWulFjnlgW2ziuQhrzWn3QlVg8ielYrHqFNU44TG5qCBw4snBW9h1FmWlxA0_4XUN4nOwVubTRcwK2pASYUCFDPt-TBJkqkOrZKtd7kKWoU-A1pRGBj4paLde2kGi8G6p3DPDAZ3EIbXk-AO2ArSgV0gNLQNwXQr0O7cospNXSGiCCnh8wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L21MtjZISGzbG0m5hmGMRs2hPxp9Kzs7csowpbioDX49uav_j34eBDw3t9Zw9fVg8rKKbudU9EVAs93pmo7opguZRArtFLAmP50J88HSJslSgmDDNV9lFlL2oasz9o1_zEzn8vwmRMhT85Fs4SfrgfSjSgCr0OBN74KOmFUEyUKEgP-HCPLp4L38Y7aDKKlupXpxIdnGRDKTxyFCdgLOQpr3Ld0W2BQv_bPBMvLZZ0j_rBY0vdn51Cjx-Bquq_pfmaphZIw6nHxQBMFe94igqB1YkGqt4nIYKfr0dAPWumA30ca4Q0OcsE0k0xhRLVTupRyt1k5eIPYA0P-VFT1lBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f703df7c8.mp4?token=QlhrsrY10Q7nbs9x6kUFWDYgqpDyWazCA9WIRD0ECmjWgj9bJrt4oEulljn1IsBDjcQE1_PDmHVCRwaEmE2R-4wNURE8Eof8uEPKSJYjgN28Jhhf_pkjCNAn3TrohOl9d3q03Q7b_uJ5YKUWXaO3Ll-MUGQUijB9Vg8GGVX49PqjA0v0teEETy5RaS_2QheKE-qTI3ZwzTh65Bjx_uvoNvemSazxVqsqose7rLfgdx4pHDb584MnmatQaix4cUcYdY7xwn6QUj6UDrbqbx3r5Vl6RVarnzbJ6UMFJKS4L4wLJeRDXSRNfN80bmuEySj4MrfSWz5yBFGz8f97dpdVXL6wVqza_LTDYNolniPKKmphjYTYvkyH3wf2ny6Bmrj-6YRSbL5tB3j8z0Rfjp6QWfe0Y5SwU7nwqo1BjXDwyqgeCelbDZt9IqRqWxl3XFZpE7cn9ju3eDn8jdIGRikhk2mUstHHWzkflHpN19xXWB2JBFabesrhKaRVYwhEmWjBjoH-8gVGV4rS1dnkTq4md2cB9MVFXb69JYVDuQqeY-BRsNeNalvevIQ1oKLsRP3h8E-sn105RPuoEdhmb7bfYezkbPiKAr1yZ4JdnNh2gm_5k9FvHHbPh06EsrqmHbFlgwp7gwffMyQQtMvas8Y0pg9ihaLGWO9IL-GXUn_t9Dc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f703df7c8.mp4?token=QlhrsrY10Q7nbs9x6kUFWDYgqpDyWazCA9WIRD0ECmjWgj9bJrt4oEulljn1IsBDjcQE1_PDmHVCRwaEmE2R-4wNURE8Eof8uEPKSJYjgN28Jhhf_pkjCNAn3TrohOl9d3q03Q7b_uJ5YKUWXaO3Ll-MUGQUijB9Vg8GGVX49PqjA0v0teEETy5RaS_2QheKE-qTI3ZwzTh65Bjx_uvoNvemSazxVqsqose7rLfgdx4pHDb584MnmatQaix4cUcYdY7xwn6QUj6UDrbqbx3r5Vl6RVarnzbJ6UMFJKS4L4wLJeRDXSRNfN80bmuEySj4MrfSWz5yBFGz8f97dpdVXL6wVqza_LTDYNolniPKKmphjYTYvkyH3wf2ny6Bmrj-6YRSbL5tB3j8z0Rfjp6QWfe0Y5SwU7nwqo1BjXDwyqgeCelbDZt9IqRqWxl3XFZpE7cn9ju3eDn8jdIGRikhk2mUstHHWzkflHpN19xXWB2JBFabesrhKaRVYwhEmWjBjoH-8gVGV4rS1dnkTq4md2cB9MVFXb69JYVDuQqeY-BRsNeNalvevIQ1oKLsRP3h8E-sn105RPuoEdhmb7bfYezkbPiKAr1yZ4JdnNh2gm_5k9FvHHbPh06EsrqmHbFlgwp7gwffMyQQtMvas8Y0pg9ihaLGWO9IL-GXUn_t9Dc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش تصویری روز دوم حضور شاعران و نویسندگان ایرانی در اربعین به نیابت از رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/akhbarefori/675602" target="_blank">📅 23:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675601">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_dK3AGezak8XH2Ter5t1bDUwHWDogF27xD38zAsK4uK2N2qKcvQbHbdbpC4UAPo3qWODjRcJBkOUZQkazw5afsNBfgk7ooHbbteCBUKq1tAZXRV-sJajvONgtmjc3VWtaIobiVoHUHBUghNzy2hitZp36heKWwkD1_SRKTBdAE5L0lAECTlmUgQC0w9mn9AnE7sqroDYB4jiWWr0W9Ps3qvDYP0pdZvQ794NSi0bb3KJ4sGwbjiAOsCvD1dLMwAVAycYxLUz7YpNNAWhltu2KKcsYbkppYzjoEL9SmXFk2QVb-P8-oy_ZpfQMI4QuBtvZQeX1bBprF-3qPCueTbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سکوت مشکوک و مرموز نتانیاهو در بحبوحه جنگ با آمریکا/ اسرائیل ترسیده یا آماده «جنگ بزرگ» با ایران می شود؟
🔹
اگر اسرائیل وارد جنگ مستقیم با ایران شود، ایران نسبت به فعالیت های این رژیم بیش از پیش حساس می شود و اقدامات اطلاعاتی و جاسوسی موساد سخت‌ می گردد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3233259</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/akhbarefori/675601" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675599">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
حدادعادل: انشالله آقا مجتبی سلامت هستند/ روایتی از شغل و درآمد ایشان پیش از رهبری
👇
khabarfoori.com/fa/tiny/news-3233395
🔹
تصاویر حضور چهره‌ها در مراسم تشییع پیکر اکبر عبدی
👇
khabarfoori.com/fa/tiny/news-3233343
🔹
سکوت مشکوک و مرموز نتانیاهو در بحبوحه جنگ با آمریکا/ اسرائیل ترسیده یا آماده «جنگ بزرگ» با ایران می شود؟
👇
khabarfoori.com/fa/tiny/news-3233259
🔹
عجیب اما واقعی/ فوتبال بازی کردن زن مشهور با شکم برآمده
👇
khabarfoori.com/fa/tiny/news-3233331
🔹
تراستی‌ کیست و چه‌ کسی مسئول فرار آنها با میلیاردها دلار پول بیت‌المال است؟
👇
khabarfoori.com/fa/tiny/news-3233211
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/akhbarefori/675599" target="_blank">📅 23:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675598">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhCQyj1-SkmSDfbR8BFm1xD04cKjJISueZTStOZDz_IXdI1wboHHfqWw9-_QoLE1h6CPM4NGDsYl0e1wegBfNGrR9D6X4Wrn5hVaI1kBspWNCLExZmzoXAQEA9Gyf7LIMcS-drpPs8tSRK2_vIx2R4k62fU7fKhwBnHR1IAe01_Akrq_uyXZ_sfaapptAkgJkl3F8KGds9BvImrN7_RB_kHjO7bRoEheNPUYZ3u0JXHHSQT66c9ULlKiBfMNW4kxYGRGHn5xGCulZKsIpH6sjinPlZIJy_zLBzpG_Nc2caSq_lCbKU-NXwpbHccNANFtejkq6KJLQcW5aXkXjNpqJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر گستاخانه و عجیبی که شیطان زرد منتشر کرد: حمله به خارک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/675598" target="_blank">📅 23:18 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
