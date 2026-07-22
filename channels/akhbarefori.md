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
<img src="https://cdn4.telesco.pe/file/nWmmIbWfzOCvUSXZpld2h2pKB1Y1bN4nXJwkLgXsT2k60RJRIfPEcd70Vtpgx6cDvDnhLq_paLk3jYP-9HXIsnYEM6cm_0qqjj-si2kLhUe1iG10Y0ebltp4RKaQpc_CQjcwZX0ra63uHsp1Sl6lQIFZPkw76i4OZStWY4i78I2DumCql_KLsYTpSI6L56Pf8DwYZU_Ijic_cjEwn477RGs9ZI_pKRc7D3JKcWRAaHVHYMa905J4gEIwpyT5w08mTPzkFWpvOfu8ba8kQTrYznZ5aKMspjQTtrAhxnXciFGz2cv7zEaItqzmRz0WC08GFnFVhXfcoT4hWovI273xkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 15:40:06</div>
<hr>

<div class="tg-post" id="msg-674130">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwfhMQmR57Tu54abztY7tH8mv2KBChYBuBgCeJP2N34QA3bhISOxroEQLvNYRHXGb3m1nozqn3h6yG9cKvA967tg49koHyXGbqoGKr-r8tT-WiWnBvaMA3A9_wPIkTLGe5kX-e6B320sMnktDWp-XPhzR2cQbxD_jd4z_DGowTUnGha3jqs61j-QXdwKzBv-C358Yys4Xsn5J82-skD6qbvRHd2M55EqFM73vpzyyoZUn84OqcltX7hbRbSyz5DSHvBp0DBCwVnFETcTiOKGUNHvMpuEAQ2j2R3qIfKQBT9PsluVoSoLtNjYn6vZgrf6luPSjxuRKwqlyNuaSid38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس مرکز روابط عمومی و اطلاع رسانی وزارت بهداشت:حملات هوایی اخیر آمریکا ۵۹۲ مصدوم و ۵۳ شهید بر جای گذاشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/674130" target="_blank">📅 15:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674129">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
وزارت دفاع عربستان از مردم این کشور خواست از فیلم‌برداری از نقاط آسیب‌دیده خودداری کنند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/674129" target="_blank">📅 15:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674128">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
برخی منابع از شنیده شدن انفجارهایی در شهر الخبر عربستان گزارش می‌دهند/ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/akhbarefori/674128" target="_blank">📅 15:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674127">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
برخی منابع از شنیده شدن صدای انفجار عربستان خبر می‌دهند/ فارس
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/674127" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674126">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
وزارت کشور بحرین: آژیرهای هشدار به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/674126" target="_blank">📅 15:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674124">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
محاصره دریایی یمن علیه عربستان؛ صنعا معادله «محاصره در برابر محاصره» را اجرایی کرد
🔹
نیروهای مسلح یمن با صدور بیانیه‌ای رسمی در پاسخ به محاصره ۱۲ ساله این کشور، از آغاز تحریم و محاصره کامل ناوبری دریایی علیه عربستان سعودی خبر دادند.
🔹
صنعا با تأکید بر آمادگی…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/674124" target="_blank">📅 15:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674123">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
حمله موشکی آمریکا به جزیره لارک
🔹
ساعت ۱۴:۴۸ امروز جزیره لارک هدف حمله موشکی قرار گرفت؛ گزارش‌های محلی حاکی از شنیده شدن صدای انفجاری مهیب است و دستگاه‌های مسئول در حال بررسی ابعاد و خسارات احتمالی این حمله هستند./ تسنیم  #اخبار_هرمزگان در فضای مجازی
👇
…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/674123" target="_blank">📅 15:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674122">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
برخی منابع از شنیده شدن صدای انفجار عربستان خبر می‌دهند/ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/674122" target="_blank">📅 15:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674121">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
خبرنگار مستقر در تنگه‌هرمز: صدای ۳ انفجار در جزیره لارک و سیریک  شنیده شد  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/674121" target="_blank">📅 15:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674119">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ddc3c5467.mp4?token=kh8tSus4dvlpzvKI351GI7BXPWNeNKUrZPv074nuv7s5ap6LnqQVdy8Wzc_7zU0GklBfW-OAWjzbTVSWFup1jUbXKeh4qNV93GXa6iqQrPJO1XvGRWJnlGGKZEpxEyi2XovuobiqO9oQNTreI-HQODwr1v-v9dtZhSmUaou1whbtjDg4Gi9QHx0GVXuLIVYTXP0nvPYjLVnyi1E5f2eWJ3TYXWQXdQvQI1d7tQa4PSEgEMPdkzY6y21zus9ljM1CbHhjPVOiPIW4ItgSL6oXaAi-2tQy1eV5jWhLktiM4Qo5zbqenghlZXnSbd_WK-4DqnYt9vdkzVeO4jdDN_W7Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ddc3c5467.mp4?token=kh8tSus4dvlpzvKI351GI7BXPWNeNKUrZPv074nuv7s5ap6LnqQVdy8Wzc_7zU0GklBfW-OAWjzbTVSWFup1jUbXKeh4qNV93GXa6iqQrPJO1XvGRWJnlGGKZEpxEyi2XovuobiqO9oQNTreI-HQODwr1v-v9dtZhSmUaou1whbtjDg4Gi9QHx0GVXuLIVYTXP0nvPYjLVnyi1E5f2eWJ3TYXWQXdQvQI1d7tQa4PSEgEMPdkzY6y21zus9ljM1CbHhjPVOiPIW4ItgSL6oXaAi-2tQy1eV5jWhLktiM4Qo5zbqenghlZXnSbd_WK-4DqnYt9vdkzVeO4jdDN_W7Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی اوکراین به مرکز توزیع شرکت تجارت الکترونیک وایلدبریز کراسنودار روسیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/674119" target="_blank">📅 15:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674118">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
منابع عربی: صدای انفجار در بحرین به گوش می‌رسد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/674118" target="_blank">📅 15:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674112">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqEZTnNAdUPU8wywHjn18gtDxZHU7C3pE4o8qiUgULTYFkJYuEkUhb_zcXH1Y-AOkOGhHpbo8XOrPbND0uTAfixsmy6-bXkk3Iat1crK5wDs_0uQ1bVor366BYbrqQnR4LXt-8yvR_l_glxSp_bC5KbxWlN9XOnkrs0Lj0XbZrginuBbAWyVAnahLiJZjjmCu37UdLpuk7UtymMGQFv3bcMNLAi0mArKKBdkJJBiK2zgPHpXELfACw4BZqqT8qf7vfkDAjA0K7IPmOHZla89LL6495CADVI4Zz6WjPJJaeLnShlsUekHKYZhwYwQgcyUgX7XmZNlI4m7OoNrawOc0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qf4Xe6Ip5rW6P-IB8O0LUmaGglIIFEM7xJyI4LSGqXbls7ILwwtDc1bN1__ifz0Kh05rMNCg1DUagSaWGg4beVTj8JBL6yzg_DWkWKio9OIFGG3Hsl7VTjmPw6PB7HF4K7xGbOHj4dAMtAi8Yl46oaWn8SWo2fE79kPp5GJwK6zm8nntLqo8lFyqLwPyAkuJ7qaEgZl-64OUfzEiuJxMk78ybRaLceuMgisSL2aQ9FYN0x1rmKpyQefg9cTbkx01gajFt8hlxryEHkJ5IZmK-tKCyNsUSxhxm7rFR65jlgNHG-YmEAeWXWsNTIQ6VDt_cHZPTia8kAQLawU1H4pfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sapby0KbLJJvGEWecR2IbxYkasEA0Tklr3tc6hXBm01qNfqbh8wsUq7UiANFAUJa6CdrZiQlq5F3R9AwWnGMmDTlkyYuXFBQBiHWg9IxHu_cjIoh1fCG0REO1wrOzD1Yxddt1IiC3I4i8hi1ZqONvPzgfqSw1yZFws8IqAA0MHqsv51cl24whBSeEZy9ZDa_u2TTf8bIFqNwdlP4fiSDo8JeHBHnlxhlLMeY7TRMXQf6Oc9zpa6VNJ9ZJLXMW5lEbhiBlUm2tLognZVS5r7x971SlaUhrQEzTDZRhUUJl82Tb7ZfZNbqbz5WhTS1BMyXLN0VklwoYzszc8SBpptMIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOnvPg_za2a1uM7cFzCQ1vrpwnuK_KLbh45e-fgYGvaxe8psgikc-JwHhSo5UIPOFw__QvNkcrtPpqpjbFmTajgg-yWNTk06J9e21GCER-muEsUsKG4xV0B_v5gU9TCPbNoN6rJYPp7Eyy9ljAAdG__zwqaCTQ0WcgxxJ-8YaqT-O8aameKb_ZATLe93jK7BMSuK4grIwQCSO5caPCHh0Pu3bcWO6oW-GD1RDIMkOD467yWAg3ZKXEeZkjKEgGNsTPr-SPJ0VHDf1Wz-HgqPD1g2XkRd5CK_pRCE7AJ49kGKw-4ZYmJdTW4xecWXhQHc0iOBRmWlmn8yCHJm7Na9Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DVyfJHYAGxOHZ9LXHRf7cGkdxTM6ez6LxKopsOMym-pfe68MiVgWSY7SGmgoudFIBBNy5G6LHZVFoi_PoMw_PeRmoIZW36jNcRsYpvnSkSzSXWFtkMdRWli4MHS0FcGBAYjowQgMJIVT446Phn5YJ_fAuaTOXF7Y7ooDqwjkLWvmW7AXG1udpW6FVdDc5wSG2w2bADJdQbyWMfAKn95uN7rVAAw-dQa77eD8FY8pZZrasosKqbOkhhKqRxZ1aiXOSF041rcYiOPYmk8KGcd9xf3i14xLqvLQVQkHCUUSFqHxplokPAQZrFa_tyvppULisY0o3cwgwfkfyi-EocB-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HS5d-c9rpwlyVPpFwI5phc15XaikdmyRVUbKTRh1892Gtp1WT4ktv5A53jwgK3Lzw0Bf68m1nHBiRd49B9-CmcXPz4UgG3dNIQFZJ-gqT9r_v5k6-DhmRrV9k94Edrxqc8cqPyxuGh6NogExd5aTBpxInU1QWE_TCydamtan-vfaHarTMMYQVOMDWDQOiHCqW3JgN2dGGMgZ1SedNzlOY1Yx4mf1vBC_yootwU0hFzEtBwlERJsXOUbFSSuOzTOPoyJaFQ-g7IPT4ySXv4ZYUADqAhpLytfYxCZORxMAPQ8T_H0oH3272IV-JHMgaRj_ymrjUrqhfrF2X4b9ZwHYyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این ترفندهای ساده، نتیجه آشپزی رو از این رو به اون رو کردن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/674112" target="_blank">📅 15:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674111">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
منابع عربی: صدای انفجار در بحرین به گوش می‌رسد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/674111" target="_blank">📅 15:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674110">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2309525546.mp4?token=aFi5OO_aNq1EadgBfyQLSJ3fszjxos1IC12c-JMU7B5tf_JNtyu6fcsUGGnxN010g3sH3sIcqsXaJl3EBEreAXT5zYYBQkY8VfOinH7Dvpen-S-yd8kacBGlM3Qy5dVdK8zQlLbYFAlOfXkGfaZI1ec9O0QdhZkLhX41H16BAfriVuSnyw-nUojkNfpibj4vAJ-Pij367vW3iXrz2bd0IBQ4IOtTMugkC9FVqhqfhWyajp7E3aRa8zsiLi8nhIgfhRk9cqcy3FOTlUhr3wOU4bU0b22UsUdU-6AhRt99BPTpPpxkm8tczTsDQCDLcZTewCHHeKkzRWngzdkZQSRBxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2309525546.mp4?token=aFi5OO_aNq1EadgBfyQLSJ3fszjxos1IC12c-JMU7B5tf_JNtyu6fcsUGGnxN010g3sH3sIcqsXaJl3EBEreAXT5zYYBQkY8VfOinH7Dvpen-S-yd8kacBGlM3Qy5dVdK8zQlLbYFAlOfXkGfaZI1ec9O0QdhZkLhX41H16BAfriVuSnyw-nUojkNfpibj4vAJ-Pij367vW3iXrz2bd0IBQ4IOtTMugkC9FVqhqfhWyajp7E3aRa8zsiLi8nhIgfhRk9cqcy3FOTlUhr3wOU4bU0b22UsUdU-6AhRt99BPTpPpxkm8tczTsDQCDLcZTewCHHeKkzRWngzdkZQSRBxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیروز حناچی، شهردار اسبق تهران: ۳ میلیون نفر در تهران در تاکسی‌های اینترنتی کار می‌کنند
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/674110" target="_blank">📅 15:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674108">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208a49956e.mp4?token=MJqM0hi1BprCqRYszBDECTkC3nwgU9RAI6gO2cyb5xQmyKJiVyz-68lLQDRwj6b6cxft-MM6Hjnoi-8DtvonbTnpV4NT_LiE70ZKaA5Lw4Jg1CsQoPqaBr5CnsWLubFUZiaqHDi3rYKuLmzmRdPOklKLl3c-kTZnoXc97BH5dcj16ILXj0aejygmC_pE_9MfmK71AJbSp3gstjOwr98eNIyQY-LXBNrKbwv3S2ng2Y7d2V_Np45r73iL1CcR2Dpp1fJi_LDew1qoMgVqInTMzijmgGt_F4QOjqTu_-1z3FiJrsYxa1ja5wvt2cWa0pngrEd1CS1Q_JAImSfITjuIXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208a49956e.mp4?token=MJqM0hi1BprCqRYszBDECTkC3nwgU9RAI6gO2cyb5xQmyKJiVyz-68lLQDRwj6b6cxft-MM6Hjnoi-8DtvonbTnpV4NT_LiE70ZKaA5Lw4Jg1CsQoPqaBr5CnsWLubFUZiaqHDi3rYKuLmzmRdPOklKLl3c-kTZnoXc97BH5dcj16ILXj0aejygmC_pE_9MfmK71AJbSp3gstjOwr98eNIyQY-LXBNrKbwv3S2ng2Y7d2V_Np45r73iL1CcR2Dpp1fJi_LDew1qoMgVqInTMzijmgGt_F4QOjqTu_-1z3FiJrsYxa1ja5wvt2cWa0pngrEd1CS1Q_JAImSfITjuIXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عذرخواهی از مردم بابت خاموشی‌های مقطعی/ خاموشی برق منازل برای جلوگیری از بیکاری کارگران صنعت است
⚡️
محمدجعفر قائم‌پناه، معاون اجرایی رئیس‌جمهور: از مردم عزیز عذرخواهی می‌کنم اگر مجبوریم و در تابستان برق شما در برخی ساعات قطع می‌شود چراکه می‌خواهیم کارگری بیکار نشود و کارخانه‌ای تعطیل نشود.
#مدیریت_مصرف
|
#معاون_اجرایی_رئیس‌جمهور
#پویش_۲۵درجه_قرار_همدلی
روابط عمومی شرکت توزیع نیروی برق استان تهران</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/674108" target="_blank">📅 15:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674107">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQo1R7L1cUe8hR2VuBMoFcMI8diRJbbsY800Cs61SrsIvgrTIhvOOTmEexsV-LD1kJa8wVD5OTYPjQW0krgSb0iPJUPRY9HzUuyk2Zm9tO7j9oLe4kiD6k8f_RzNRCQhVsqa2wFtTdEAIi_e2ipG0SL735dLsTDju3xTvA5vvCftNFpeVT7zZRRQJG9LQmegZcJLWsYWyhniWvtPuZToLRL6x76evQZ0e7Oevs0Q5B3UWf8v7xaLbx2s3kZPrf59Od9sV5u3KaVECD0hRTdHPb83xD0lXNJzyxVa5G6KE4ji4-6a2iTjrNSbQKfdRqQgMBnNHToK-L4WcigNxA5DIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت یک بسیجی اهل قشم در حمله نیروهای آمریکایی
🔹
کمیته خادمین شهدای قشم از شهادت «یاسر زحمت‌کش» در پی حملات نظامیان آمریکایی در تاریخ ۳۱ تیرماه خبر داد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/674107" target="_blank">📅 14:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674106">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736cf4867e.mp4?token=InAKJ9r03GYzDxqdTUr4Ptb6INqBQBUyE9iUcW2f-FEczI6knxfRVqOoDXkR9Qqq-rXeqz9oXzvLAR_m88LAKKHKgUMYVFSuJP11ZQ7tNGs4nuLdHIxioAfDOCtyikkvF42XeayVZIqk5olTBJC3L19t149Zlsh_R9aiwmxtHMrEQOI25VS7sCZnOcPBESTEE-HSja9Tt2r_TucrKaOBmxbx1jtDXAh95we14y-dL18ug5-FCbFnCBp4KyCbYAa34psYck-AzjJJImlS5lYjfNQvFF-MgLxZnwdqMmDE3zLFIu8DSxVkG37vvdC19ScCaQ95NqgLZFAep9lVmOUOwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736cf4867e.mp4?token=InAKJ9r03GYzDxqdTUr4Ptb6INqBQBUyE9iUcW2f-FEczI6knxfRVqOoDXkR9Qqq-rXeqz9oXzvLAR_m88LAKKHKgUMYVFSuJP11ZQ7tNGs4nuLdHIxioAfDOCtyikkvF42XeayVZIqk5olTBJC3L19t149Zlsh_R9aiwmxtHMrEQOI25VS7sCZnOcPBESTEE-HSja9Tt2r_TucrKaOBmxbx1jtDXAh95we14y-dL18ug5-FCbFnCBp4KyCbYAa34psYck-AzjJJImlS5lYjfNQvFF-MgLxZnwdqMmDE3zLFIu8DSxVkG37vvdC19ScCaQ95NqgLZFAep9lVmOUOwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار مستقر در تنگه‌هرمز: صدای ۳ انفجار در جزیره لارک و سیریک  شنیده شد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/674106" target="_blank">📅 14:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674105">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
حملهٔ سنگین سپاه به پایگاه‌های آمریکا در اردن
🔹
سپاه: حماسه حضور الهام بخش شما در خیابان می‌رود تا منشأ بیداری بزرگ ملت‌ها گردد و عرصه را بیشتر از همیشه بر مستکبران تنگ کند.
🔹
حملات تجاوزکارانه آمریکا در شب‌های گذشته به بهانه تلافی انفجار کشتی‌های متخلف…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/674105" target="_blank">📅 14:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674104">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ادعای روبیو: ما برای مذاکره با ایران آماده‌ایم
🔹
وزیر امور خارجه آمریکا مدعی شد که خواهان دست‌یابی به یک راهکار و توافق دیپلماتیک با ایران هستیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/674104" target="_blank">📅 14:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674094">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxb6bu58hGJzDU4-nbjnYIQe9MvCuwrN-9ibjSJZCJ7ZXv8MzobRQi3nq-1z0SZcU3myZkpdGpp5ovfkWLTk3gmjUn0dhGpa0UsXhhZvezCt-WjWnF8iALp7-pacxmhxuTrMuK_j9UPEtvGVHfDgcMH87Yck_1B9HJQkI4MdiLMKzofGho_jA_e6s4NtW5ATX57uOWpJ_rhFu_XBQTAfsRkjkAE6ZPbT5E-IOEyOGF6-EXAPFATm0jbJPH5qqyL-BQQF-EbeoPd9zAI2omy03-_4d9kcfpSXdQc-aZPseOEpC5KP2pExmgeqjmLRkUhPmo2dwswh8HIjdLtJ6jhY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3FLgzU6BlUe_iy3L-Jc7l8QTkr9pP92Zs_HKgGZNhJ4TphWv6PuLYOjA6MdqB7VX4OQb-4IOIi0pSBoIRxFj6G73OxJZntzncucWM_BhHcPuNp1KRK1XC4-ZEENKQwk0u2zqNNyI8PrPywLGnDUEP61XPCyXXnyviwHowSkZob-tkvkJJU8yQ3uAMDK26SXsPLOJ4gbbD73TPCzoHouzOJ1ssQEaj7OhMUD371husn2MXOEr2TmWzeM-hk68TQ7_wQ12zfAcCkJKFJkGrBjMlBW2fWoNZao0bWxMcmLvRoT8dQFHfWj_uuhsf6nq09eg6jrbKq5dz0B3UtmEWuY9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smsTfUikVARD_im_iTzdVkXftqHzyHteazfF-alu_AjjTuCQ6GKnC6WwDcVN3ORxmhtlY83-JoIwlBxXYw-7DisHL8ETvuqxd0giUlbWsJeCEStSa_QsaIWkLqlk_yVSuUXQSuVqVG8iGMUFdN4f5O5X0KFMf3vsN_njgOMZzNB2ZyHXhmzqVlYs63Vxc1F6IIBCQZ-ab-aAwnqG6WuzH4TOSpVG_cIXLcScWhQTs3xN3z9lAgl_eWoKshbMRc2y0OAyRBPynPcLqRPvjknOblXjjHJUb2pwarckqf9zbZlyKlFIISP4yBzH3O80ADVnq2gyeiid5EPYg25A3nU2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNgeABFBlU0FHwEYR626O-dllk7HHLA9mzj6_cXGouyscY1IS8ZNGedbgHehjc7LXCX9otjnfjpq-PVyroFlT04hvysJ7_W02osEbYCh1n_jFtq6jXQ_cAs060NsYteX1oe2MLEthflupvj6POKPm3-Ad-trkK5F7lbPFwv0fyuMyUmon9n0m2VsiTbQjSx4zNv1eYeu6CbcWD1OwscbK4jX1evTh4bl2l9AYsI1s1Av2y6_zPoXpisiga3GPJrbb8G8OtqHUCQlTIh3vADCXNwUCzXUENpSeWKXHAihF0qLcbQ_DZtezL9ePFkHHHyZ6r3D6g-08B_BReC2_jtS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQ_XBbQwLPWI-bBM0dxwGSA963tCjavrPi3IyzDHBiF27MKXr2XlHahf2afq46w3E3KrJcSaHFJ7babvPATbOcuBC_fBrxGstzODiUtVBIYG-P5l8h2xlPQUDdWYqfEMh0dj4gbxUnVJluFrVbJvTC8_hlU_1ALr0-lBVH-DzniHim19M3IzjQVzi2jSaLLczJp6MRTtXEQMxi1fhwJPMjlBI0KvCi48oNEuD6rAZ6dqI2a8kHJEl-5nyvNRtBxvjZoYI6kdoWCTV2syF1WJybdwFDnpgXWOu3ZlKtB2gyWH8WUi8KKtoO150WBs2aUQVdKDxzlCiQ2wdYNYqVtPGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3sfsk19Mv07PTg2zwQCsVfUvobF2oPKzV38NXaSxBkG73C5vvX0LXjqhDTl1qUTj3ytehUUWrw6O0FykvWvCOscylzIWPzwF0jlTZLb-5oAAB212CmRFkrRW7U4ZfVyf5HFOO560alUaa8O1h4V38blNVbGrgW0TvEZcPWSsDvbWaMhuRGkb53--XMdpTzK-zOHNIgfuZsdpvEeUC9MNXctu4sFPfe5RLplyTdZ_UOfCkb2dXhoCAUXMIy9XGkPZ6oq42VbuiSRP31G9f9NUuxe5aT4Ss_lrQTnTrRrvYUfmug_9zzK9K1Q3Aj6JnWfbiMwOwdYAinUYrebAUXhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IsMAF8amO23Tkagd8Nd2P-_IK-Ikpjk7ODvVjC4LDFOGDyyf3DIciXpxwCH3vT1XG05uj-Oxs6H-hkYc5CxcB3aOevXqPIvsE1so4rvUhjnqhOSI8QLHLvfVsu-uevp_I3RpJME2AdYACy1UO4jFb7JSMYSnol2UTmyS9nK93twBRslPnabPxAdU6NpnXxHnnCzxtuI3NF9xI1a_OOBCgMrp6_-3aCeKBxyxJF_ogQf0189I7c_OnxuzI-Oae_Y7saekAUpjtRnA6AxLwUroWJLD-mBQMCXGY55-oMuQL7DIoCa3IAFbAwQManK5GHshsebYrhxwVqYxFYRF8JH3YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IbN6Dj01_SB9m2gEn0qh7kJBz_oZvAJnWy402uyxg9TUEbTRk6gziw_yyM0PoZtB__90WG8qylvuEsp2BB9IWzEDv_g6k4lMQ8LaK4Pv4TQpsiXok-vrQIdRoax4t9pyyRE8Y_gIfZCulE8yF0jB-PxZxSgIOIB5dE3-cWH-4h2ceKI3rSw0uMbbyLqtiqlYOvM7q9lt4QjFSFLiK5kUHOmhc0yPGrUcSE9mGmhjVV-NHwugayWDrkBudeSS__G7l4yym4CVXJMIoK7zBer4wLK_MQwlIlT9EKDDuB5KKGMRIDX6p85SMQHjn8hxAEESH-UoY4PMlnUdP8jfQ-eYmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snpdqlhgVABGrPOy4v-eFCVtFAHXCjBxYb42SI9Ko46Ux8TssyAgFDaLs7yiiW_J829u1SxFs312HzZY1VuAqtDWdtzFcp4IYVKDtph_V4f8Zbk5lilohiUG9-va49L9dYB_TPSTkfTxT2bBefXNj_tCD8h0oLd-fEGuB3VlvH9KiiVt8Ei47BSi-N1gRSjk8hWLYfygqCyK4d5b1zEHyeezpL3EPi0tTvcRiwzIfLwk-rQanVkS6cGjleZDeaHdEBaWB5Vj16rGIbvOOgwn5CxZ69BqRRdVZobKANaC2pJ9zDmIxbErHlxSXhABSfTYGbyrMg1CxEDhwJ1mf2WCOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qIozInR0g-eqTbCXI7aI2p332vu9shGU3hBlgUDG6QGFZUw0XkeOznkDEyC5spAE9HamSS0PMhNihK8NslJZRk2EJ8DxiCnlHZ26GrBkPQ1Om4I9pxAEU2gRP5Xtyrn8JPmfK1qC3zl2b-aQeQSg1kzwUGVz5jS8lkb8kgKiBuEFoCiNnC5QkkfyUno_IJjbHcBO6EEqBiP1tq9MxHYw8o6tqElCLZ3mtCNU929C786I_JtQkARYr50UZf2dvYsG3qcPcbrNdm7zzx5Y5Mtf_Oau8DKTK6fFhwTmOnTZic5iDEbfITYY3qTjdHjWbEUkgyLBDsdAqf3JM7oJhBfT0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حذف ترامپ و اینفانتینو از عکس قهرمانی اسپانیا با هوش مصنوعی
🔹
فدراسیون فوتبال اسپانیا با استفاده از هوش مصنوعی، تصویر دونالد ترامپ و اینفانتینو را از عکس دسته‌جمعی قهرمانی حذف کرد که با واکنش و افشاگری کاربران فضای مجازی روبرو شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/674094" target="_blank">📅 14:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674093">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
بقایی: تهدید آمریکا علیه تأسیسات هسته‌ای، نشانه‌ی دشمنی با پیشرفت ایران است
🔹
اسماعیل بقایی، سخنگوی وزارت خارجه، با محکوم کردن تهدیدات آمریکا علیه مراکز هسته‌ای، آن را خلاف حقوق بین‌الملل دانست؛  وی تمرکز واشنگتن بر سایت «کوه کلنگ» را بهانه‌جویی برای تخریب خواند و تأکید کرد ایران در برابر تعرض به امنیت ملی خود با تمام توان می‌ایستد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/674093" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674092">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
۶۰ لیتر سهمیه بنزین امشب واریز می‌شود
🔹
۶۰ لیتر سهمیه بنزین مرداد خودروهای شخصی بدون هیچ‌گونه تغییری، ساعت صفر بامداد پنج شنبه (یکم مردادماه) در کارت‌های هوشمند سوخت شخصی شارژ می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/674092" target="_blank">📅 14:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674091">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3108cde4ff.mp4?token=AyS_EYEpJQtRL3T2VY75TI2NHVcKyX7BfSP0fTiMmMDr3k3BloGAzY6C652G8apw1BC9w-PYLE6u_aZKccVDIuxCn6fMzyfHqzoA628uDD4ZtKUH9iDjMUkhy_ofJ6-KzzjjSGpSFTC8KY9_aH2VVRuNDxsd59Qk6zR_oaGODMvBeGhV0m4OWmez3mzxXsagQCT8ZEdLiCF1dak1lRZUqSgu1BWOxZ9Gz4tZXXXeSgf-hGrPAEKZChUlzQPJCffR3GET3ThOGyfAlYFexYoxdjv9hiufETEbB-kyWvRM2UeySoG1jfUNX5gC4HQbxlRFOGoZs_NOVQ_nZ5tkRrUQKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3108cde4ff.mp4?token=AyS_EYEpJQtRL3T2VY75TI2NHVcKyX7BfSP0fTiMmMDr3k3BloGAzY6C652G8apw1BC9w-PYLE6u_aZKccVDIuxCn6fMzyfHqzoA628uDD4ZtKUH9iDjMUkhy_ofJ6-KzzjjSGpSFTC8KY9_aH2VVRuNDxsd59Qk6zR_oaGODMvBeGhV0m4OWmez3mzxXsagQCT8ZEdLiCF1dak1lRZUqSgu1BWOxZ9Gz4tZXXXeSgf-hGrPAEKZChUlzQPJCffR3GET3ThOGyfAlYFexYoxdjv9hiufETEbB-kyWvRM2UeySoG1jfUNX5gC4HQbxlRFOGoZs_NOVQ_nZ5tkRrUQKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملهٔ سنگین سپاه به پایگاه‌های آمریکا در اردن
🔹
سپاه: حماسه حضور الهام بخش شما در خیابان می‌رود تا منشأ بیداری بزرگ ملت‌ها گردد و عرصه را بیشتر از همیشه بر مستکبران تنگ کند.
🔹
حملات تجاوزکارانه آمریکا در شب‌های گذشته به بهانه تلافی انفجار کشتی‌های متخلف انجام می‌شد.
🔹
شب گذشته هم که با وجود وسوسه خدمه کشتی‌ها، هیچ شناوری جرات آزمون عبور از مسیر غیرقانونی جنوب تنگه را نکرد، و طبعاً انفجاری هم رخ نداد، ارتش کودک‌کش آمریکا خوی تجاوزگری را کنار نگذاشت و حمله هوایی و موشکی به تعدادی از مراکز نظامی و غیرنظامی ما را تکرار کرد و اینک در حال دریافت پاسخ‌های کوبنده است.
🔹
با توکل به خدای متعال، رزمندگان شجاع هوافضای سپاه در پاسخ به تجاوزات دشمن در موج ۲۵ عملیات نصر ۲ با رمز مبارک یا حسن ابن علی (ع) و تقدیم به شهدای مدرسه شجره طیبه میناب، پایگاه‌های آمریکایی در اردن را یک بار دیگر در هم کوبیدند.
🔹
در اولین مرحله پاسخ در حمله موشکی و پهپادی به پایگاه‌های ملک فیصل و پرنس حسن یک سوله آماده سازی اف ۱۵ هدف قرار گرفت و همچنین در حمله به یک سوله آماده‌سازی پهپادها، هشت پهپاد MQ 9 نو و آکبند در بسته‌های خود قبل از آماده‌سازی به طور کامل منهدم گردید و به دو فروند از آنها که در محوطه بودند خسارت سنگین وارد آمد.
🔹
در حمله بعدی به سوله نگهداری بالگردها خسارت اساسی به دو فروند بالگرد سنگین آمریکایی وارد آمد.
🔹
در حمله به یک مرکز اسکان نیروهای متجاوز، تعدادی از آنها کشته و زخمی شدند.
عملیات تنبیه متجاوز ادامه دارد، چرا که اگر متجاوز تنبیه نشود و هزینه سنگینی بابت عهد شکنی و زیر پا گذاشتن توافقات نپردازد، تصور خواهد کرد که هر وقت اراده کند می‌تواند جنگ را از سر گیرد و هر وقت تحت فشار قرار گیرد به آن خاتمه دهد و چرخه جنگ، مذاکره و باز هم جنگ را تکرار کند و سایه جنگ را دائماً روی سر ما نگه دارد.
🔹
تنها راه احیای بازدارندگی و برقراری امنیت پایدار، اجرای فرمان قرآن است که می‌فرماید "و قاتلوهم حتی لا تکونوا فتنه".
🔹
برای دور کردن دائمی سایه جنگ از کشور جز ایستادگی و تحمیل هزینه سنگین به متجاوز راهی نیست اگر این پاسخ‌ها اکتفا نکند و تجاوزات ادامه یابد، آماده عملیات پشیمان‌کننده‌ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/674091" target="_blank">📅 14:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674090">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
آشپزی با چشم بسته روی آنتن زنده شبکه سه!/ مهارت عجیب یک سرآشپز همه را شوکه کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/674090" target="_blank">📅 14:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674089">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سازمان آتش‌نشانی شیراز از مهار کامل آتش‌سوزی مراتع در
ارتفاعات «دروازه قرآن» و «دراک»
خبر داد.
🔹
وزیر خارجه روسیه: تداوم درگیری به نفع آمریکا و ایران نیست.
🔹
پولیتیکو: به دلیل فشارهای اقتصادی و تلفات نظامی، حمایت هواداران ترامپ از جنگ با ایران کاهش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/674089" target="_blank">📅 14:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674088">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43629cc089.mp4?token=uPJ6RCxTnvN1d4aNAWJwIAA8yycQnQO1XPPEnsCT1GJzYY_GHVALlqKAyX5wCn9txewApHLmdLS0L-PPnr2sQZrDE8noXlF2M_hGN697Ex4wgazAVFTNhEbxYNfcyX9a-EXe47zMfFYP1vaVaPqmAIoc1zyM2QyIgp1F3LsYKP2IBxLgXR9lyQVkWe1_0YLKfTtR08mxiZNScWvQqRrKQZrs-1Fqdtm-Skr9F4N9CLQc4KGoX4KweN-OKFuG2Ea2vvsW_YVkuGwHv9azjtEkT86OfZ3-6pfiAi6wzbIkjedcFCqjyLAS_bq3eQO53gaE3ueip47ASSiOohIxvnE8Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43629cc089.mp4?token=uPJ6RCxTnvN1d4aNAWJwIAA8yycQnQO1XPPEnsCT1GJzYY_GHVALlqKAyX5wCn9txewApHLmdLS0L-PPnr2sQZrDE8noXlF2M_hGN697Ex4wgazAVFTNhEbxYNfcyX9a-EXe47zMfFYP1vaVaPqmAIoc1zyM2QyIgp1F3LsYKP2IBxLgXR9lyQVkWe1_0YLKfTtR08mxiZNScWvQqRrKQZrs-1Fqdtm-Skr9F4N9CLQc4KGoX4KweN-OKFuG2Ea2vvsW_YVkuGwHv9azjtEkT86OfZ3-6pfiAi6wzbIkjedcFCqjyLAS_bq3eQO53gaE3ueip47ASSiOohIxvnE8Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیروز حناچی، شهردار اسبق تهران: اگر هاشمی نبود، قطعنامه ۵۹۸ پذیرفته نمی‌شد/ هاشمی رفسنجانی از معدود روحانیونی بودند که پیش از انقلاب، با هزینه شخصی
جهانگردی کرده بودند و به همین دلیل طرح‌هایی مانند مترو را وارد ایران کردند
پیروز حناچی، شهردار اسبق تهران، در
#گفتگو
با خبرفوری:
🔹
در باب جریان‌هایی مانند جبهه پایداری، حدیثی از امام جعفر صادق (ع) داریم؛ ایشان از حضرت امیر (ع) نقل می‌کند که دو طیف کمر مرا شکستند؛ عابدانِ متهتک و جاهلانِ متنسک؛ عابدانی که هتک حرمت می‌کردند و جاهلانی که به قول معروف جانماز آب می‌کشیدند، ولی ریشه می‌زدند.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/674088" target="_blank">📅 14:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674087">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/324cb6ed71.mp4?token=kSb4PpoaP2YyocGmLS4KGRIWxAdDXQ_2jK2FOCCppHmHT2MazZoOM7apri-1ATnIlDGAxUxyVM9UC6cSfyEuABcnGAf2YE2t72xsWP_DAM4_3hvDCDj0wDyzoZ0X29VSCk3hBjt5qxkf_XmBsfDULvMii8A0dT4x0qiIHSU0KKKVtTdwi9FZaW30lWs7cdhsMOrvkHfiFbgxHG9AgQp-0O_SAEBqQLimkXS_QVtLkmx2x9GdA_xqXWn7N_qWiB5P840uLrLil2cQ6KfQvldFoHK6LBuTpPB2FxIl9xcIzgfIuxyfAFfaQto404QUJgsQO1SnC-2gDqU1eZ2oFR7lrWG30lESzTmZucsrYpZ0HdH9WQ90uRpjXDBpKY9jffk-YeE7djT2ijsyYrdK8f2dXBGhUPtoYVRyrEXEnOx1LU5BVzTLVgFod-DBcaX9XXhQnUf65wpnFrzoRAi9H9TkPMzida9t0u_ymBU0I6oglqWjmKC6VfGL10KEj4pMNf-xLwuK5EwDOXmnEMTBXlrXfJvN0jVlx9zlG1Wpp3S7B0_M9sZMDuXweyBgQAJRK_Qi5hE6oFGecsGoAnzk-ATNE41MH24lo4OM1taSt1lXEIV4rNT3_KJo7yeh46nf9lsSxzhlw_p2AxnvT_geuHaKZzB9dOA8bfICx0_UGey5Z1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/324cb6ed71.mp4?token=kSb4PpoaP2YyocGmLS4KGRIWxAdDXQ_2jK2FOCCppHmHT2MazZoOM7apri-1ATnIlDGAxUxyVM9UC6cSfyEuABcnGAf2YE2t72xsWP_DAM4_3hvDCDj0wDyzoZ0X29VSCk3hBjt5qxkf_XmBsfDULvMii8A0dT4x0qiIHSU0KKKVtTdwi9FZaW30lWs7cdhsMOrvkHfiFbgxHG9AgQp-0O_SAEBqQLimkXS_QVtLkmx2x9GdA_xqXWn7N_qWiB5P840uLrLil2cQ6KfQvldFoHK6LBuTpPB2FxIl9xcIzgfIuxyfAFfaQto404QUJgsQO1SnC-2gDqU1eZ2oFR7lrWG30lESzTmZucsrYpZ0HdH9WQ90uRpjXDBpKY9jffk-YeE7djT2ijsyYrdK8f2dXBGhUPtoYVRyrEXEnOx1LU5BVzTLVgFod-DBcaX9XXhQnUf65wpnFrzoRAi9H9TkPMzida9t0u_ymBU0I6oglqWjmKC6VfGL10KEj4pMNf-xLwuK5EwDOXmnEMTBXlrXfJvN0jVlx9zlG1Wpp3S7B0_M9sZMDuXweyBgQAJRK_Qi5hE6oFGecsGoAnzk-ATNE41MH24lo4OM1taSt1lXEIV4rNT3_KJo7yeh46nf9lsSxzhlw_p2AxnvT_geuHaKZzB9dOA8bfICx0_UGey5Z1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت نهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم حدیث ایران‌منش که به دلیل داشتن ۲ فرزند، قصد سقط کردن سومین فرزند ناخواسته خود را داشته اما با اصرار اطرافیان او را نگه می‌دارد ولی بلافاصله بعد از زایمان به بیماری کرونا مبتلا و روح از جسم جدا شده و مدت زیادی را در کما به سر می‌برد و مسائل زیادی را در دنیای برزخی درک می‌کند و در نهایت بخاطر انصراف از سقط و جان بخشی به فرزندش، خداوند جان دوباره به ایشان می‌بخشد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: حدیث ایرانمنش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/674087" target="_blank">📅 14:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674078">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwbFBLTjSJR_oZ42Zl8TglIq1hvHvGfGjqhCkMU2eNwIVg12Y6H09EpfBmzz8xxKtnKAr2FAqVVyn9IdkAeTuvgDhb0kLZ8CuXwzW_XLKu6klMlAMQW4iRyPWwoJrrEx7gvBQnnyPbOhxriKCtUF43XtSQUKUgYf6TVnA5uTURScGLVK0ZT8kRWXM4WpADgy5W0Rv7E19x_xcvPUeHNxjZcM1nCr1E4JXZtGjy7L_hJix3EC_xeXV6Pn4Ao6-io-4eLzC898vT3a_SQk735ygLQFwdSmjPQ7Dq__XdrouVn5Tx4bDgrgT3csgfw1LufdfIrlu3RDy_Fn9UeUcS-kXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLvtLyr4tC-obhO-_48KljUdRkFF0UJD5XyBW6nQiH45ppIiJMbd5gGboBwKUMHOGDjLrowr8sMPQJhPweuDdXh1MiL4oJz_LtRRzDYlddt_Fo1zzxBOdkaGY31tNaMcauUF_Gviv836fWb6UAOUUgxhrNGWHSMnk2aBEZIzoDdnHNGlbdIR6I25m2L3UXyb7v747aCQcnUoubq9pZeesw-YBjpVUpE7KTXqOilfZ9w_pukM3r_2cGZJd2N-0lqJECw5BqDFz6SNoRvDLG0iihLRv9sbK73OFHN_dgr4RgJOMJiANAjbmGsW_DEabl8jny12MJl2oZOxNW5AkiHDjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CKBskwL_xXCw1bqgy4BPkZhXS77dQXu6GOsk56dJBOQYNwmjXNn3z6Ql1Gbl1iYxwV-PPI0nDB168JFS_qw_jocSNpdoe-gJ2g9h23YGc_EKKDkPY4J5BF556ejxCHkpQUh6tUAXY0w8XuVQ55KxF3oVDaVedS7WUxsOEKcoZzztl8GL-mK4H87TYvm4XdeKcUgBDCs1N0n04f9D8UUhrX7R8MS9LQ-Ut14uk1sYRQ1B_QJBWlrjcPSuXDMZsj_V1FbnQGpSRsNYgaxnXmgA3w7TWgM0eXn3sd5Orf2ouNXu0Uvv-UrFD43ejtuY6eTpqAuEV3IX70dPg6nbrNQC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kIFTnn77iMIayr3Eu5meegQ3jdDDjJv3r40FAVLDvfz_1hOqsUjn2S57cvgkTw8GNrO4cmB7tSzY37VwNhnl0ee04QyCgEUTtjQvBn2frlKLq--FdCWhk_R9PQdt-rxK5viCorGfkhJOiJjrwUd2Ej6fizh84s52-qmZZTNxIoMkZiEpaLIDbUWclQ-daI3zBnerTqWL3BWaQG7vOmsYYRoZtT2rP4DRI2EbHKMpv0ANCBy_f9RUqxQfxz5gyS6UBpW_gEucopu9mnIq8XqfIzgBdAKwpNXVmByGtZHoIurVwxRYeW9Mv4SYTWqi2YUKeZh1qUk-8AqAJ9msLLMLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nx9BjE3qAVajS0EPEVsRC-J_5xuPQWkcamnBdA4YX-8jsAz8_T18CTrPyxEba01ozvIUr60pCzJScCjZIEyGeJ316DWfUuNwJ3f3wu4cLqY4t1JKNCPIvzgyNeI9zlQytLzwda8UmppH7E0jg8wbapk24CTsR-usWndND3IwLSY-r1WijTM7UQUyA20-zNp3yEA0rDOxYdoaQZutXhJvx3vfbs0yVkJb5ScFjN13xQI3Nj03RTHDLqpcNgKphZdbjWQ69z5CtI9K_k835GKSfKY0ST_g2XO4Z-nJI0cFJ31vrZ5MKupO2iw2QHCYmR80RYA7B70hjvOPPm5ZmHi5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dO1Vrd8XfVllAKx95iTPtoR7qPZ7Z7M3qWP_pDMEo0gMA95LudfBxt1YSjIHDLF22eVfJBKmUmp8s5OGcrOmf9USCJInakDZ3EUejBOByJFS65K6_TN2hpmqP3RenmTGHtfRW6nZ4axHHb2FJJSBVCyJsz88fTZOknIjO_vwFYyeDYQMHUlLDb5mxL6iapP3weqgHYX7ge8bl9cvzMqY2zWVO1s2NyvHB2M7RR4RF-l0f500XhwfxYvsHTYtL_7_bGCnyoSaVhL5z8_1UU9TLD88RIrlEiv2hVouIIkiJ5CFjuJRBwtw_s2JmY_kDKArqHIQakojm8PId0YoQXsXcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EG3SBGzDFyc-lvIEzc847jqR8f1NS9BAbp0TpsI7YmpMZ-vB3N4niSD1J6Up8aTNTnCJKrOsUEdEVs_e7dR1NSDrwIE7N6V6-JzZi5N1AfATnIOrbRcHB8rO2RGAJYbhzlGeOGAIRy2RIF4YubxS-FEZk7WjWuNRphXNAppSHYrD05dHYr8yqTZJ1i6J4GlF-9BD_1-T8GESH27RUJPMlmpFO0y1YGtXoEWmp7KcTOgsSUMuATIIXfUc2tJJM4oTUAvra1GmLSkXg9VTAA_Wwg8lV_1-Sl9G3NLNrQBi9H533_6KQDuPMcVjqPjmnIBR3eZVPpP19KtsDJSl88iH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBHPiaMqL8QWkCp89NtVM8V5e_FoutRCM38iWZF8y86IVSr2BogH8-oe1GzVxyC1xX9LS8QaOM9c1_-HhvowxQoGAwV2FXjjHi44ffg0U-olhhbeSAoHVMSIWdpL52PNJgUxVXDwHrSCZhFmdRTkUiRxTNSBq4yfHnobSB7nFhLyvR4IJQ8iYOFLSNEKTb_Bxgai4kVH7rsiQhAaKuGTlogFOU0H7Kl0G4zLALgax85lAsfvA1HfSdPH9ovMkCOf6rtkGXo332Wf70OusR1EMFHBBc3H1HA_KMBukYdNa3w71i2FAq9vkA9RpSOS3AyOCw1Qs_KppOKf_3suqXELvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fsvvf9mwsV1rsGCq3Il46S_XNTBo-YY679Vcr0Z182ZWkEhIsv3E8RosRharz8L2iqGFswj5RMscNXgqRVpnezf-ni6iOv_NCclqCfIzll5yG3UIshbUX062h-ZbOr9ytfbER7ER5vl8Ju4ehtMI4F-ZuMFsVY_yGUo5B8-61OvN-ssrPeZ7OBIWP1WJRK_Mz8dKJeWH3ie0xcUGf6iUY9mww1QARBQeyG81ntxg_qzID7ZwZnDFqG2QNzjlAA3wVUu1vRzuTngxRhdC20MchBJVtk46du03Gw3G6fW2Xi21xLrwSBWV72-2X0Tws16tcESJEgJboRKSqZPcvdk22A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جدیدترین مدل‌های آستین که استایل شما را متحول می‌کنند
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/674078" target="_blank">📅 14:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674077">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7e77e148b.mp4?token=VYaOWHQHZIUkyOwB467ua84jGHRZSaL6N0rVsK4ytx0iBZVQxv8X2PSmYnNJkxeEi9bX_xXO-SF65aPGsj4atp5p92X6GU-sTNNNfXAnNK2uo3llViF6GMQyzDKihBvvhCdH2zP5rA3GgTsJAJKQyDi9VJzfLFmyfvcDl61f2279avp8c3cR6VvmxwteDrYEnFhHCJue622N4ZDH3CHnX6yo0ndUcg4M51ccHEm6Bd7V5N9LaCF7Aw_cHxbG6yRD75uWaftcLV2khKGpgpaSSDcHDmHz6ayskuwYQVt6hicsPzOFEhIlIU04MNCnuUa7IVu42zj7LV13S_ZZHKC3PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7e77e148b.mp4?token=VYaOWHQHZIUkyOwB467ua84jGHRZSaL6N0rVsK4ytx0iBZVQxv8X2PSmYnNJkxeEi9bX_xXO-SF65aPGsj4atp5p92X6GU-sTNNNfXAnNK2uo3llViF6GMQyzDKihBvvhCdH2zP5rA3GgTsJAJKQyDi9VJzfLFmyfvcDl61f2279avp8c3cR6VvmxwteDrYEnFhHCJue622N4ZDH3CHnX6yo0ndUcg4M51ccHEm6Bd7V5N9LaCF7Aw_cHxbG6yRD75uWaftcLV2khKGpgpaSSDcHDmHz6ayskuwYQVt6hicsPzOFEhIlIU04MNCnuUa7IVu42zj7LV13S_ZZHKC3PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتحاد مردم در پویش «قرار همدلی» برای پایداری برق نتیجه داد
اکبر حسن‌بکلو، معاون هماهنگی توزیع توانیر، اعلام کرد:
✨
مردم به پویش «قرار همدلی» پیوستند و با کاهش مصرف، بیش از هزار مگاوات کاهش مصرف برق را در روزهای گذشته شاهد بودیم.
این کاهش موجب رفع محدودیت تأمین برق در استان‌های جنوبی شد.
✨
ادامه همراهی مردم می‌تواند به تأمین برق پایدار برای استان‌های جنوبی کمک کند.
#پویش_۲۵درجه_قرار_همدلی
🆔
@tehran_roshan</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/674077" target="_blank">📅 14:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674076">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای العربیه: ترامپ از نخست‌وزیر عراق برای میانجیگری میان ایران و آمریکا کمک خواست  منابع آگاه به العربیه:
🔹
واشنگتن به نخست‌وزیر عراق چراغ سبز داده تا با تکیه بر روابط بغداد با تهران و واشنگتن، در تلاش‌ها برای کاهش تنش و پایان جنگ میان دو طرف نقش‌آفرینی…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/674076" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674075">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uey9SFbLHV8PMqzU7H_dfDgw71yDOK66k7wIzmzy3eu1cYhuaNFiSKRC4tebsBpdxixAYPhOb5yJ0NQFbOzMdz_BBwCdXz-nPjNGSwu6i4-PCiN3lsXUbq-OztK73-XuYXV_bnZA6Zh3nYkY6rS1W2L0iXeMsytfKv9cdoVbBoDLAAmDlIXPidvmerk81B15DeSuMjV8kLZYDhGGqKsq_7kE2AGNv3-_ydlngeg9TtshiZb8keJO3yg2DkNysIF0mdtTJJF1b6UP8KHWim8J7WY1VQtdNqGR28JRYCXk4UxvAnYvvGcpjouOrdMTETmj5Cj-HVzX3qy_vaFFlDNWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه مخاطبان برای ساخت آینده شغلی نسل جوان
🔸
در این نظرسنجی بیش از ۶۹ هزار نفر شرکت کردند که سهم روبیکا ۷۹ درصد، بله حدود ۱۵ درصد و تلگرام ۶ درصد بوده است.
🔸
توصیه حدود ۴۴ درصد شرکت‌کنندگان برای جوانانی که در ابتدای مسیر شغلی هستند، یادگیری یک مهارت تخصصی است؛ حدود ۳۳ درصد هم یادگیری فناوری‌های جدید را پیشنهاد می‌کنند.
🔸
مشاغل آینده بیش از هر زمان دیگری به مهارت‌های تخصصی و تسلط بر فناوری‌های نوین وابسته‌اند و موفقیت شغلی نسل جوان در گرو یادگیری مستمر است.
@amarfact</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/674075" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674074">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa26ad2eb.mp4?token=h436BIrPfhz2ThTdu0RvViedOwyQsC0bH7c53rQCDk6WRXyFbqo3Cj101FqA-GfrpJ63msZACowkkGgHQ5amAKkQylxGiRM2bdiygm0V7tGcEO91h4KBXAH89ej1NfE714ZDCvm744vN1AZMRZAng5bQyCCcnuP8ihuK9kJgxWpboqskeELZD7dafHEI_8OeWc6zU0-kOiLmdVKC8Q91E6Hbcx7KF5oEazg_vrVPiHetTRdeJhzO91XFp9YdaIMCWkTJT3ZzDw3oHIlTKvN26VM6OjCbCOcmiUpKQi9HYi8ehaGSXyrRS3L-9UVTiXUZICKusLzWTxfeb3-T4rPMjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa26ad2eb.mp4?token=h436BIrPfhz2ThTdu0RvViedOwyQsC0bH7c53rQCDk6WRXyFbqo3Cj101FqA-GfrpJ63msZACowkkGgHQ5amAKkQylxGiRM2bdiygm0V7tGcEO91h4KBXAH89ej1NfE714ZDCvm744vN1AZMRZAng5bQyCCcnuP8ihuK9kJgxWpboqskeELZD7dafHEI_8OeWc6zU0-kOiLmdVKC8Q91E6Hbcx7KF5oEazg_vrVPiHetTRdeJhzO91XFp9YdaIMCWkTJT3ZzDw3oHIlTKvN26VM6OjCbCOcmiUpKQi9HYi8ehaGSXyrRS3L-9UVTiXUZICKusLzWTxfeb3-T4rPMjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر نزدیک از مکانی که در کوه ازمر، در استان سلیمانیه در شمال عراق، مورد هدف یک پهپاد قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/674074" target="_blank">📅 13:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674073">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoBOgKj22UblZYwD9t_f5_XDminOdb1VKAUJRo-qsrlqNQm1mdvuD1lJNuikLS9YBhaaOPdRG4SbQAw8kP-PElPvZIM2yiuOMh5-Pu3MPLsx6ZdCzrUFohxqQShiRggBBr9YWtmVbFtyhK0qwT3PtkIGya9upuWsSMmAhUkzmTBED9S8c0poAkyubPPdPTLJP1Y4fwOTJJemlmpGA4WZVjxWH_o0Kpeh00ShGi75pj5SsGxZu5XIz-jxo9tWtvrL-6EKNRQipw9XfuO775iVJVuzs5yFRsZlESLsfIpxmcmJIUj1Ffi1zQg-SxMr1nxfFysg1bGrel6IlCHFmst9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرپرست وزارت دفاع: نوآوری ایرانی معادلات صحنه نبرد را تغییر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/674073" target="_blank">📅 13:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674072">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای روبیو: ما برای مذاکره با ایران آماده‌ایم
🔹
وزیر امور خارجه آمریکا مدعی شد که خواهان دست‌یابی به یک راهکار و توافق دیپلماتیک با ایران هستیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/674072" target="_blank">📅 13:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674071">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
روایت برای اولین بار/ ماجرای نامه اعتراضی پیروز حناچی، شهردار پیشین تهران به رهبر شهید انقلاب
پیروز حناچی، شهردار پیشین تهران در
#گفتگو
با خبرفوری:
🔹
کسانی که دنبال رانت بودند با تصدی من به عنوان شهردار مشکل داشتند. نامه اعتراضی به رهبری نوشتم، عکس‌العملی را که منجر به تایید حکم من به عنوان شهردار شد، نتیجه پیگیری ایشان (رهبر شهید) تلقی میکنم.
🔹
آقای علوی گفت که آقای روحانی به وزیر کشور و وزیر اطلاعات دستور داد که چرا بیخود چیز می‌کنید (سنگ اندازی می‌کنید).
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/674071" target="_blank">📅 13:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674067">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJ_EPmE2qnIs4QbXi-U6lqK3AkqtYKY343rQy82FxOlHCwoVy_8Fi9zk__KNzPiPysCzhgABG3KSCCUikQae3K4AY8Y6nT_3C94JETJmr9dQ9bmGhia7NKqbr7K9RjH65kLhTO0rPptbDa5uO0e8xOiYn9_1L7YXu4-P-zxpw7hoa-dmNFy1EeQzeLsVIgsmJIt8qc4LcNMhrnrLE8RruUYGqp2ayz0L6MWzFDyGn73NvYtCtpoR8WMCX8PQG4L3-9gymO6FhyKauoItKEUGbq6p86F3RBNXvOjlSMkql3oWM4CKWLuN-gwgYjOfYcKtfN6bh4mE7evF5ZaqV-6SRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWq4v9RVevWWkiuQuQkBpjlauTR89FMLfiAuDpjozlrgS2NRvAhJ3Z_bF99gNIo5csaHmC2kJ50fXwmgscMenWE3Va9ZjMJ4Dmotphcb1nIvYky_d0FUbxLAWWCx4ZwhaNF-5jY8TOvZywh-LD0yFp1CXfwBrdvoAB5LXURhgN2AJggYL_V7J4gno6YAKmIIPgHI3zY9kr6nYvIQlyIFeiEh0gERepslTE0KEFaIwKTD2kr9Vl57YIT6wexnCVrSyVqvVNa36kXx-O0JNxiEjiMx2Ac3yTiWDq2wQS72Q2E3CGAVbNJhWEhcOXBq726A2WLkgKNpfAbzVWTogL9C9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDwXRQs_Y4QFtxEbxJPRBd1b87zgcYuNCpeu34cGbZJ_Jve_lsL10jBeHGjP57AgymfvzjHqA42QI5EhnzktV6PTqobnJSC2tvNE9VFFj_Vm9tdzB61H0TjG84GagPOpahqLl0y-pL7PfI6HDLTtYRZVRJ_WhR6nlyX98ZrMXQu6BvIHvGFvvyk0qRUlRWZB4e2XKJ3cMblJQ9ev5aXtgIp0UtZ_zYS4NDl4XTj7ZJMmFFUbeg2QvphiUiMGqDcfqunoriUPhxeFDjUCCNj0SjktHuk1XZI02D9pwe3uX9bOV14SgsYzKVoOf0CdJAPO3ICVvt-rE6MyxFzUxeylYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khqKQmMuIcUoHsph_xWXh1vCA7GDGkcDkTbSzyt8fQ5VLFAN6OMT7m8GNZ-_v1J-N6XknKgVltuHIeg6lK1iSGCb-SWXBxs1lwhpfgNZRKo7yE7d5nR_xEmGh93XUQ47FTNW4y9IYym9Gb4HnfDhs5ZwfvP8NhkWJZ0wZqUO-wz2YKec19TfKyGBErgctLG4RoSwP67J-g8zN99_SLm-Mtl956HpBKvGY8dW4jweVLYAmUS2Pf-NEhTa07BE6pp8O79KfAYn1C4n1VTmM9HVaRS_NDC-MYvr5mn2uxIrnSg5gtGeMK_mOE6pZ38KtnCksDrj96KI-lOuwKWWVCTv4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چگونه در تابستان خوش‌بو باشیم؟
/ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/674067" target="_blank">📅 13:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674066">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhIDzB-2RxGA7uSC6XzFjQmwHnvaLQEdnMEU9DvZmsDeoZezWbP4a7naX9tWmlyFRrJOAGTob06qS_Icl_x5du_OD0uSdfRjtB96CLjqrPvXhhh7V_hWgKeoVevR5pZ7oNxTkcmdsQN9KONWz0AbnTtWs3mxcP-Bc2NGMg7H08ASGwOONw93hKkyTkK6rFR4HDbSO5iACzf0Xj4Wv9RuUfC4lWB-i98YIqXT7chOWyvvdg4SVh7SbQbT6sIQzD7yZX4npzJ1LbmzkbWc5DP0lNX9JrVFNNR5pRAPjeRcngzWIHI0ms9LEIclDcn4DOSISuO1x47os9ykc9WrLpGHHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال استریت ژورنال: توانمندی موشکی ایران همچنان پابرجاست
🔹
در حالی که مقامات آمریکایی می‌گویند قابلیت‌های موشکی ایران به شدت تضعیف شده است، حملات ۲ هفته اخیر ایران، نشان می‌دهد که تهدید همچنان قابل توجه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/674066" target="_blank">📅 13:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674065">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/911c88bf87.mp4?token=EHOHhmvtOn1rK05PBTXZ3drsz6zQq0I8RZM_Gb4i60yi8_Dr-F-g4RhcLLj8F7MEQ6zq2-S9YmoKNESPjJBLpYqqvV2UsW58T980ymg1zSA1gbhRq5Itdrv-z7_haSSJ_dmXFcC_BePTOIpbvIxYuxaRz2i-vl927AWOeh03G7F18v_un2171J4VXibKr31LOVJd9QiBukotBhsaCHe4s8Z6ngRAHv5jjYf8JHrrBIgsvuAZInD15HOpmJF9zff-lydBBwJ2miGBPeeVYszqwLUn9YA08mlX2lEJnLBYoY7AsCc27etNbxPOgtrCC4Ga7JNHulwZFMEUL74ZS_y8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/911c88bf87.mp4?token=EHOHhmvtOn1rK05PBTXZ3drsz6zQq0I8RZM_Gb4i60yi8_Dr-F-g4RhcLLj8F7MEQ6zq2-S9YmoKNESPjJBLpYqqvV2UsW58T980ymg1zSA1gbhRq5Itdrv-z7_haSSJ_dmXFcC_BePTOIpbvIxYuxaRz2i-vl927AWOeh03G7F18v_un2171J4VXibKr31LOVJd9QiBukotBhsaCHe4s8Z6ngRAHv5jjYf8JHrrBIgsvuAZInD15HOpmJF9zff-lydBBwJ2miGBPeeVYszqwLUn9YA08mlX2lEJnLBYoY7AsCc27etNbxPOgtrCC4Ga7JNHulwZFMEUL74ZS_y8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماساژ آسان و مؤثر برای جوانسازی صورت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/674065" target="_blank">📅 13:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674064">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
تکذیب فعالیت پدافند و انفجار بامداد امروز در پاکدشت
سپاه استان تهران:
🔹
گزارش‌های منتشرشده در فضای مجازی دربارهٔ فعالیت سامانه‌های پدافندی و وقوع اصابت در پاکدشت، در بامداد امروز صحت ندارد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/674064" target="_blank">📅 13:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674063">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تردد ریلی ایران به چین ۳ برابر شد
حبیب قاسمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
تردد ریلی ایران به چین سه برابر شده و محدودیت‌های مرزی با ترکیه نیز برطرف شده است که هرچند هزینه حمل در مسیرهای جایگزین بالاتر از مسیر جنوب است.
🔹
دستگاه‌های اقتصادی با محوریت وزارت راه برنامه افزایش سهم کریدورهای جایگزین از ۲۰ به ۶۰ درصد را با هدف کاهش وابستگی به مسیر جنوب دنبال کردند.
@TV_Fori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/674063" target="_blank">📅 13:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674062">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB4D3dvCcEPmeC2o_wijl9lGY67nQQTr5N3JR-v-1eY1d-VQXc2ICH80cGWmJJDsoAFgGXkJvzuo84P0k8l-pjqulT10DjCU63qtohAHl8BCSGxilnoa4Xyc97xQdz6wPoNbIzjuyjtZbYplmp-XkBTshd8nRXjl7h8GpszaEXaAW2lBgDGwNUES9XXR51WjsgcrNDdiY5iEWkFFXGEzcZBOy8H5x_g1NgSJUBtKIfb3t1d4WUkkeJJM71xlpc7QumNHO6R3RCgzKyCs-ovJ4ITBC9xX-OmIo0To11Xi6Cm61KfNwLdzGQmp6dNlr0wBgZL9HCggIloAvLo7drTNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهر تایید سهامداران بر عملكرد سال ۱۴۰۴ بانك ملت
🔹
با برپایی مجمع عمومی عادی سالیانه بانک ملت برای سال مالی منتهی به پایان اسفندماه ۱۴۰۴، عملکرد این بانک بورسی مورد تایید سهامداران قرار گرفت.
🔹
مجمع عمومی عادی سالیانه بانک ملت با حضور بیش از ۶۳.۴۱ درصد از سهامداران و به ریاست مسعود نصر اصفهانی رییس هیأت مدیره و نظارت علیرضا خاتون زاده ابیانه مدیرکل امور بانکی وزارت امور اقتصادی و دارایی و اسماعیل چمنی نماینده شرکت سرمایه گذاری سهام عدالت، منشی گری احمد خیرخواه مدیرکل حقوقی بانک ملت و با حضور نماینده سازمان بورس و اوراق بهادار برپا شد و پس از قرائت گزارش عملکرد هیات مدیره از سوی فرشید فرخ نژاد مدیرعامل بانک ملت و قرائت گزارش حسابرس و بازرس قانونی، سهامداران با رای قاطع صورت های مالی این بانک را تصویب کردند.
🔹
همچنین در این مجمع حسابرس و بازرس قانونی، صورت های مالی بانک ملت را از تمامی جنبه های با اهمیت، منطبق با استانداردهای حسابرسی و مطلوب ارزیابی کرد.
🔹
در این مجمع، تقسیم ۴۶ ریال سود (از محل سود جاری و انباشته) به ازای هر سهم بانک ملت به تصویب سهامداران رسید.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/674062" target="_blank">📅 13:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674061">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AN6PJRBaX4WcYPr3jWOM2_80GxZVAUFxLJPxI78LZgI6rTa4sW0jRN8SlUICQAqqx4D5If-pajnKSkM9y5gHC4aLtx19VUQhBVHVxXo5QgCJro4TdYAJqUI_BVsFjHNEmhzWMyKEo2o3bokLgF9XkZj7u_3GOJFu5BhCPjchO5tKrF8pbytT6imdArEwVp4Sn_-y5CZFR486EFPOylyWcFE62YVyecj55sVJY6QSpWMQ7M_jnlyE02pz5DdwXXndVrKMSy7rQoqMhpJG-Aj52ZBAV9IegPRGDXXZxunGvaejnCKOVHlOtTmRq_4Jmz-Pn9K5JTyt7vEZlnzmdE3R_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک هار مدعی انتقام چندبرابری از ایران شد  ترامپ در پیامی جدید در واکنش به کشته شدن سربازان آمریکایی در حملات ایران مدعی شد:
🔹
هر بار که ایران یک سرباز آمریکایی را به قتل برساند، بهای این عمل را چندین برابر پرداخت خواهد کرد! این دستورالعمل به وزیر جنگ، پیت…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/674061" target="_blank">📅 13:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674060">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTS4Fr4QVul5fmRlZ0XyLkSfo-8YNo3Qm7dPQSTPJ_eaVQ8N7ZEqKYS3NHuLxSsvR6fKRpFglNSzcmoQ-HkWtAiJSlSlyZRplf2KP4oaV3pbFOzWo-4x2EyDGzG-ZbP1IRzYgXyRokRi-4koejfiJU6H9DxRLoIfS49d2vb-_Z9zNhV9oGQf5MNnYtpQG5xRTAWBhU3yF_81JcHoSblpYwYxnWyl6-_A1FeAWRS-X0dS8aaAbScVLUnyxeOYL9yG9QkDr5gfLIRu3XlHmgV02oRhAn1T2HUf2mGC2TgmOjtLbJlNnsRrY77OyLl8Qw9qInpfsN9aypZTS1UoN8IBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۳۱ تیر ۱۴۰۵؛ ساعت ۱۲:۴۰
🔹
دلار امروز ۳۱ تیر با وجود نوسان محدود، همچنان در کانال ۱۹۰ هزار تومان معامله می‌شود و بهای آن در بازار آزاد ۱۹۱ هزار و ۵۰۰ تومان ثبت شده است.
🔹
در همین حال، رشد طلای ۱۸ عیار، این فلز گرانبها را به آستانه ۱۹ میلیون تومان رساند و قیمت سکه بهار آزادی، حدود ۱۸۵ میلیون تومان ثبت شد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/674060" target="_blank">📅 13:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674059">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
تشییع شهدای تازه شناسایی شده مدرسه شجره طیبه میناب  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/674059" target="_blank">📅 13:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674058">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
فارس: دقایقی پیش صدای ۳ انفجار از حوالی سیریک شنیده شد
🔹
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/674058" target="_blank">📅 13:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674057">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
تکلیف امتحانات نهایی روشن شد
🔹
یک منبع آگاه به خبرفوری گفت که طبق جلسه‌ای که با وزیر آموزش و پرورش برگزار شد، تصمیم‌ بر این شد امتحان‌های نهایی به جز در استان‌های درگیر جنگ به تعویق نیفتد.
🔹
در خصوص کنکور هم هنوز تصمیمی گرفته نشده و طبق برنامه قبلی، به قوت خود باقیست‌./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/674057" target="_blank">📅 13:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674056">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h97_HtdEiL2DG8SuSB4Aw9Rcxr49j5E3iCQ67ZvVIwpA8EfRzf0KcQUs3zY2VEZ8R5k9HGPD1F9BB2cHSVOG_zibcM_iBuhGFvWvdnik304EqQF2MgY4T-aqoNFdoYaIAVpioh37H1C-27GhxTBuH80kHckU4TJPSAumX1X99xfQoNJMhL3ZldqyC1TWTgquMnXonprbXDa539hKy1lAE8DCdyF6gwKDW6oFdFZXW0TMqPaj9gwjysRP3q8jX0bcpXhyYyy8H72EZl-lZfMa7xP9lYxpw2WpjhIxzGHKN-j0E_JCtIK6vtfKDj5ZyZWASRHfTGSPTWPvyMCjiJu5Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
♦️
جادوی دمای رنگ: کلید آرامش در خانه
🔹
رعایت استاندارد کلوین(دمای رنگ) در نورپردازی، تأثیر مستقیمی بر سلامت روان دارد. اگر این اصل را نادیده بگیرید، فضای خانه به جای حس آرامش، شبیه به روشنایی سرد و بی‌روحِ مراکز خرید یا نمایشگاه‌ها می‌شود و خواب راحت را از شما می‌گیرد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/674056" target="_blank">📅 12:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674055">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSe-tkMIM9kvS5v10GWVrF36eiidp1qPqRt-FbkNeVx_NbWYe-4UEOSmWGYPLOfc-hnRTDZy3LasfmDogbwc-iZ5eEvmP__9Zjqrca1IIQEOErHTZqLhxhk2lfhL72CxpyJPlju_IvHGuJyeOT4QktyGJSA-NavK_7R0DLc6EbnKAgsFcm6AyYs5vJ3Asjp-k_c_Linzt35zncy1np_ULYvxoWnp51olWk9a35QYz_1b-q3ZUxskLGCIP3nHmn0TmNkMkS5OyBLp7HReo7F01bQI4lU-YkECSTA5hc2mQUhut0filgK1MDymtsa8sdkL84dj8vujUMiUSVMrlkim_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خالق ملودی «پلنگ صورتی» درگذشت
🔹
پلاس جانسون، نوازنده برجسته ساکسوفون جاز آمریکایی که با ملودی ماندگار خود در فیلم کلاسیک «پلنگ صورتی» (۱۹۶۳) جاودانه شد، در ۹۴ سالگی در لس آنجلس درگذشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/674055" target="_blank">📅 12:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674054">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4042d84114.mp4?token=H1DeGYrxhDr6ovaX4uBdKSzdndH86YQBkaocjlVRqoeQF6c3hosvVXJTrCuraZ7M5Zjywcp5lY8wJQEQuKHww8ik17r7GviNuhbGPRtDrtfridK0NZhbFWmPrdIlNxR44Xo1uYuy5qtsnjSN3nk_9Dc2dqUv7Ij4YD9uI4dLXxwYO87BNpMKAnTUxRFXExBYwbVZWVAvdVtob3VIoJId5XCbtxdueU-5xOnEHIdGTMCPxJtzvEVSrG2rL9Kk56hdLv2GQxlanuNXGaVJtft96dbNNunmqg2FqahK6MN16uaVTueDUNENGro36zUyJxvxRkpAKsAarZeQr0oPCqBwsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4042d84114.mp4?token=H1DeGYrxhDr6ovaX4uBdKSzdndH86YQBkaocjlVRqoeQF6c3hosvVXJTrCuraZ7M5Zjywcp5lY8wJQEQuKHww8ik17r7GviNuhbGPRtDrtfridK0NZhbFWmPrdIlNxR44Xo1uYuy5qtsnjSN3nk_9Dc2dqUv7Ij4YD9uI4dLXxwYO87BNpMKAnTUxRFXExBYwbVZWVAvdVtob3VIoJId5XCbtxdueU-5xOnEHIdGTMCPxJtzvEVSrG2rL9Kk56hdLv2GQxlanuNXGaVJtft96dbNNunmqg2FqahK6MN16uaVTueDUNENGro36zUyJxvxRkpAKsAarZeQr0oPCqBwsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیروز حناچی، شهردار پیشین تهران: ای کاش احمدی‌نژاد هیچ کاری نمی‌کرد چون نتیجه‌اش فقط تخریب بود/ احمدی‌نژاد سازمان میراث را به شیراز برد و بسیاری از اسناد این سازمان گم شدند و این سازمان نابود شد/ تخریب باغات در تهران را احمدی‌نژاد آغاز کرد
پیروز حناچی، شهردار پیشین تهران در
#گفتگو
با خبرفوری:
🔹
احمدی‌نژاد خودش را جزو نخبگان امر در حوزه‌های تخصصی می‌دانست، اما به نظرم تخصصی‌ترین موضوعات را به وجه بدی به اجرا درمی‌آورد که دیگر کسی نمی‌توانست به آن دست بزند.
🔹
در نتیجه سیاست عدم تمرکز در زمان احمدی‌نژاد، سازمان میراث را به شیراز بردند و این سازمان منهدم شد طوری که اسناد گم شد؛ اسنادی که برخی از آن نقشه‌هایی با قدمت صدساله بود.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/674054" target="_blank">📅 12:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674052">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f0137ab5.mp4?token=CP2f3zfIkCw_aUFhgsULsubLCxGgN2qkWJYtiwBN61y7U2Ykd9v6Z6jcm0YqJzgCrNfBAaCrFwk5q2N52nezC4-3WxPso7mWeJgxI_jikVHDWLj7AfCZBk_RLZw1Etyddrc1R2_c3O9o3IsmDIdftlSpiLgWIwY6rJttul4pZn1NXYjZuB77Uk5IaqRXiqXPqSgm630w8D6zWpqWSCnK3Sk48zF-8JXBkplnH2X9tRANMhke1mAjPxFe8Fxl01ObNQAsJNswGKTwfF5OmgyaSYxYHiyAbP3yYFdD27u8yhLWd3zy72tSSdwEciUAPvKRBxNTIvYg_AY8QFYQwhuHGqicyqhv7UoqicGgyqE3wKksqq6F1XVKJrFzspHWSaZOnelvZSaaJQGOkYb76lenw-XvMCZ4YYQw91H3CopLwIl6nvZ-_nJeJTkR2_mu0tevaztw_YdYG0XdIkSvp7zFQpPGApWlNzvkGi3S526DIKaBwYKAheT8Tr8v6iqjaIKHw61PdI_HjxpaqyyNx0z1tnbNCjRCp9hnbub4H3oWUKgaDqTf6gcbKDH_qylWeY7VZ1qWueOkZFjxGXTWXaj9_GEy8shWEZRYapp2j_AhHidIgBEubWdBYM0b7kuAXBs8G2PLddgsb0RXpwAqeFTe2j_sPB4_ru7SnxSuXN8B4lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f0137ab5.mp4?token=CP2f3zfIkCw_aUFhgsULsubLCxGgN2qkWJYtiwBN61y7U2Ykd9v6Z6jcm0YqJzgCrNfBAaCrFwk5q2N52nezC4-3WxPso7mWeJgxI_jikVHDWLj7AfCZBk_RLZw1Etyddrc1R2_c3O9o3IsmDIdftlSpiLgWIwY6rJttul4pZn1NXYjZuB77Uk5IaqRXiqXPqSgm630w8D6zWpqWSCnK3Sk48zF-8JXBkplnH2X9tRANMhke1mAjPxFe8Fxl01ObNQAsJNswGKTwfF5OmgyaSYxYHiyAbP3yYFdD27u8yhLWd3zy72tSSdwEciUAPvKRBxNTIvYg_AY8QFYQwhuHGqicyqhv7UoqicGgyqE3wKksqq6F1XVKJrFzspHWSaZOnelvZSaaJQGOkYb76lenw-XvMCZ4YYQw91H3CopLwIl6nvZ-_nJeJTkR2_mu0tevaztw_YdYG0XdIkSvp7zFQpPGApWlNzvkGi3S526DIKaBwYKAheT8Tr8v6iqjaIKHw61PdI_HjxpaqyyNx0z1tnbNCjRCp9hnbub4H3oWUKgaDqTf6gcbKDH_qylWeY7VZ1qWueOkZFjxGXTWXaj9_GEy8shWEZRYapp2j_AhHidIgBEubWdBYM0b7kuAXBs8G2PLddgsb0RXpwAqeFTe2j_sPB4_ru7SnxSuXN8B4lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی یک نظامی آمریکایی در پایگاه آمریکا در اردن هنگام به صدا درآمدن آژیر هشدار حمله موشکی ایران
🔹
سربازان آمریکایی پنج دقیقه وقت دارند در محفظه‌هایی که برای آنها طراحی شده است پناه بگیرند، این پناهگاه‌ها با فاصله از هم طراحی شده تا تعداد تلفات به حداقل برسد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/674052" target="_blank">📅 12:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674050">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e810dcc5f0.mp4?token=GRC0mL8uEo1PPkL0qS_i-99nlZzLiSPuxihbN4bIADhMYPNwAOwcUMqJ6yLN4m13Rn3kNx2pYc89dtTOoMIVgR_9tvl0ng6yu3bI4cly-2qhvl_80f2Z_PGBF-i5a3Dmo2NOzH6W35zUYWUxl0c1zJZpFUrz-2-hoJPvoJ1ZrsVxxon4_dGjwcbrB_CVpCeQPXGffEps75tlsi7469kvZHmBCo0LyyIqTC6XU2i7l5BezbSMWFukV43nv3JwQUoW8aefgk0MdrNO4hTXbVlXOCQfHJw7KbAOaIh1C2kFO9uDrkjmotNCJuzx8x67Rw2vHI6FvwX3hZ9YYIWnPT7ac39Q-RPZQCf5X2UwkgVh_3xR1nUhFFpEn_Vi5a8PX21Dy7tLlHBelSXKEtq2We3x_S_f7DR99ltOKgnV5QXpttFNpL6_eNqzdoU_1jLR25kvFKqFbEM4xxswI2GWu4EpthUyhzu8VwLMFhnS5ezNM9KYPt4NOyxRsNwbjUdVaHGmewheLYJuuh2GcwXQWtGCTJ-15USFmIHjlRCrejYMqDqrAWC56IFPhEBgLshgqIDCjuWTjM4Z4wRA5Iw9FlMh7p7n6QKbVo2p95XIQhOjmwFbxJQH5eZTtWBs9S2aXfxv5QqFijW9LndnCh-klcpZ9BGJs08yrSeBVmTrK0URBR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e810dcc5f0.mp4?token=GRC0mL8uEo1PPkL0qS_i-99nlZzLiSPuxihbN4bIADhMYPNwAOwcUMqJ6yLN4m13Rn3kNx2pYc89dtTOoMIVgR_9tvl0ng6yu3bI4cly-2qhvl_80f2Z_PGBF-i5a3Dmo2NOzH6W35zUYWUxl0c1zJZpFUrz-2-hoJPvoJ1ZrsVxxon4_dGjwcbrB_CVpCeQPXGffEps75tlsi7469kvZHmBCo0LyyIqTC6XU2i7l5BezbSMWFukV43nv3JwQUoW8aefgk0MdrNO4hTXbVlXOCQfHJw7KbAOaIh1C2kFO9uDrkjmotNCJuzx8x67Rw2vHI6FvwX3hZ9YYIWnPT7ac39Q-RPZQCf5X2UwkgVh_3xR1nUhFFpEn_Vi5a8PX21Dy7tLlHBelSXKEtq2We3x_S_f7DR99ltOKgnV5QXpttFNpL6_eNqzdoU_1jLR25kvFKqFbEM4xxswI2GWu4EpthUyhzu8VwLMFhnS5ezNM9KYPt4NOyxRsNwbjUdVaHGmewheLYJuuh2GcwXQWtGCTJ-15USFmIHjlRCrejYMqDqrAWC56IFPhEBgLshgqIDCjuWTjM4Z4wRA5Iw9FlMh7p7n6QKbVo2p95XIQhOjmwFbxJQH5eZTtWBs9S2aXfxv5QqFijW9LndnCh-klcpZ9BGJs08yrSeBVmTrK0URBR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این داروها رو با این مواد غذایی نخورید
‼️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/674050" target="_blank">📅 12:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674049">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfxz0AfojKdLdZ1b_X1KMnaQpEWyvo3J6Gkd7LWVVBkIHeW3Ce74SCAek1BOVDfTKblLnA_b6lb_0WLb7mmjT97iyo_M1Qf9yuDH8HEChNIjrzR5Y5XGddzJ_n2Jln1bBejBpL6VZg-P0oVA9NVJmJE4KQasoYISmP8I1ORhI3RVioD8gUQptEBOdy6BtBOmPKHizXlg1mKR5XPS3sU97kXk3gE3wXFSuW9EbuRANv3C5ExszAXGXNotMWAtb2C5s75jX_dDmHGRQ1Rice7tMUGuobQfYgp-KunbYvESGfH-jVod8umDSMMsdabtv3sGr0FEA_WRflBkHcq0Q-JAgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: ‏ادعای ترامپ درباره درخواست ایران برای مذاکره درست نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/674049" target="_blank">📅 12:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674048">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
سرنگونی یک فروند پهپاد متخاصم در آسمان تهران
🔹
شب گذشته یک فروند پهپاد متخاصم توسط شبکه یکپارچه پدافند هوایی خاتم‌الانبیا در آسمان تهران رهگیری و سرنگون شده است.
🔹
این اقدام در شرایطی صورت گرفت که بامداد امروز، مردم تهران از شنیده‌شدن صدای فعالیت پدافند هوایی در برخی نقاط پایتخت خبر داده بودند./ فارس
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/674048" target="_blank">📅 12:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674046">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07db88e44.mp4?token=D_MfZnd0Mpb1Vq0L7b783Y31VSlSvAVHQyo_HRVQKRcFigGrFZpDUA0LRgHjo-u3qce0ezDD2OuLS7Poeu7G0T_8bBSe0AIDRniWf8LDhJZaQCv21rCsRj9queebAQ5qgw7C-B6Snp50rGX4L0UOEs_c2cm1qFNgvNxNeo8qZWP6pw3F3__d-Md9FRqJieY-okW5xtKjLVzwyUbHD5i3Yi6pvHAWgsLjI-xxxnAEde_6scBOhA3BsLqY0Ird5NUVq7SDCKlwCyi2muViupwHu5Upfbka4kd4KmgocZTJgeIjESQDDTHmbDcrJWKaNLQZ5n1uCZl2aWJl1HspOf44lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07db88e44.mp4?token=D_MfZnd0Mpb1Vq0L7b783Y31VSlSvAVHQyo_HRVQKRcFigGrFZpDUA0LRgHjo-u3qce0ezDD2OuLS7Poeu7G0T_8bBSe0AIDRniWf8LDhJZaQCv21rCsRj9queebAQ5qgw7C-B6Snp50rGX4L0UOEs_c2cm1qFNgvNxNeo8qZWP6pw3F3__d-Md9FRqJieY-okW5xtKjLVzwyUbHD5i3Yi6pvHAWgsLjI-xxxnAEde_6scBOhA3BsLqY0Ird5NUVq7SDCKlwCyi2muViupwHu5Upfbka4kd4KmgocZTJgeIjESQDDTHmbDcrJWKaNLQZ5n1uCZl2aWJl1HspOf44lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
قطعی برق؟ تاریکی دیگه دردسر نیست!
🔦
چراغ شارژی خورشیدی تاشو با طراحی کاربردی، مناسب برای خانه، سفر، کمپینگ و مواقع اضطراری.
✨
ویژگی‌ها:
✅
شارژ با نور خورشید و USB
✅
طراحی تاشو و کم‌جا
✅
نوردهی قوی
✅
مناسب برای قطعی برق، خودرو، ویلا و طبیعت‌گردی
🔥
قیمت قبلی: 1,598,000 تومان
❌
💰
قیمت ویژه: 1,098,000 تومان
✅
⏳
این تخفیف برای مدت محدود فعال است.
🛒
برای مشاهده مشخصات و ثبت سفارش، روی لینک زیر کلیک کنید:
👇
👇
👇
https://memarket24.ir/product/brief/47540/180124/</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/674046" target="_blank">📅 12:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674045">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cv2kTOw8oxRl-pK_g5IIUhBH5Dlfhi_UKJMCNi4b-PdX7z4sCAZ3J7d2MwogRbEiHfVlq9PeR1PcuKLkRqLiR0yqMe0NUr69ZkzRizOmJSDV2ADoE43lWtC6e5NOQZytCSAYnCmWON9NuknScvh2__W7nL5sWm12mtdyQCxAhBY0L9CHN-4keD54atVkAYBif0usECnjXEmo7Tcf-MFM1TIZcKEAPZLkpJkmvWNJeS7npdSb2KL6n36egUoM_RHc_B-R9zp_BJl2cxXxJwyCpoxOq4N4uS0yNYhZjOtwjuRNh4yqR83cJRCIEHaiD57irCr7FJykzWFQqTXehn7BQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جایزه‌ عجیب برای قهرمانان اسپانیا؛ از جام قهرمانی تا کارتن گوجه!
🍅
🔹
گاوی و فابین روییز پس از قهرمانی در جام جهانی، در زادگاهشان سویل طبق سنتی قدیمی، به اندازه وزن بدنشان کارتن گوجه‌فرنگی هدیه گرفتند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/674045" target="_blank">📅 12:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674043">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348d732189.mp4?token=m5qrpbCcvzjlPJmOejeTZh8hv8XUQkHjrb3wZOvP7B9pF5J6Up6t_YUVJeKCGGCUBwHupEuV_grGaqmjvDXh2wqLC4YUX2D6a9ApK_W3OIiq1rISIoYpO9Hv8TlieFZExEkNHb0il5VyIy1qxjP6BOTgsOLJYArwqT-EYI1AnyKUfEycstX9lF2XYvUGtW8xZ1xh69IMpKnPbzeB_FytknYTODqOTZ238TZT7jwG9jlNr4gqyHHuBCdRXhWAdOTaicFrj1y9CsmUdDWfQgkgg3FsEK3vh0-AjXXyPyF2dmSs_UmZDF7lLxktSG6iFiNbIT2nbWwfMUGfVh5OJO8iwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348d732189.mp4?token=m5qrpbCcvzjlPJmOejeTZh8hv8XUQkHjrb3wZOvP7B9pF5J6Up6t_YUVJeKCGGCUBwHupEuV_grGaqmjvDXh2wqLC4YUX2D6a9ApK_W3OIiq1rISIoYpO9Hv8TlieFZExEkNHb0il5VyIy1qxjP6BOTgsOLJYArwqT-EYI1AnyKUfEycstX9lF2XYvUGtW8xZ1xh69IMpKnPbzeB_FytknYTODqOTZ238TZT7jwG9jlNr4gqyHHuBCdRXhWAdOTaicFrj1y9CsmUdDWfQgkgg3FsEK3vh0-AjXXyPyF2dmSs_UmZDF7lLxktSG6iFiNbIT2nbWwfMUGfVh5OJO8iwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: سقوط مشهد در اغتشاشات دی‌ماه پارسال را کاملا تکذیب می‌کنم
🔹
آن شب آقای مومنی، پورجمشیدیان و بنده در وزارت کشور بودیم و مرتب با استاندار خراسان‌رضوی که در استانداری بودند صحبت می‌کردیم.
🔹
بعید می‌دانم آقای عراقچی چنین چیزی را گفته باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/674043" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674041">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pAMuVT5lM5kvjgPcdSpJyu7qhek4RRbi7eNsiv1YDXzr2tiMMUElJk-yBnyHeaA4Tg9ERbSbcoz6n_CZth-uALA6sfjgkULrq1jByySzS91i2ppFtYr76AC9BBinBvkjR_4fESqUaQGARDWoBRPS6_Tr0QA1y3qB2RQF2JKaGVGnHViWN2DQCL3nnCod5oTWwKeeZYAtHqxS_Xza45W_FyQqvLImDk7RQFa_n-dT28bOinMEtve_a-7tZUx7yw_GNIgS-CAfS6TNm-XA9nzcGzCSbObLOMbpkEd-rKIVGJ8vn6zaffo4xbPjNAZUK1S-gAjwNyfsvM89W-TxpvNICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlg80-_Pwf_5eXIsvnSlZ8G5p9G_0oAf1xZZ98VlWacAua77RwQBKg_I25pTaauj3QTR6aoVT0ybKY27XfFWwGSP7FS2qVqsturyGYowQHJYUA7uaYbY8Jv6POXbyDgx5SeSNjWpsOsF1d30o3Hpd2yvOTzZ2ph8Yg4uHnCHYmlFA07KPVoXNcAwHoQf_jpAifjIT-mw9UuUB0MRnykl1G6HJNhga8H95jZhSHMVebChCg5o9ucTnlV9m_LIuUUx5yilztQC82GGoyRe-HylofA72VAJLfnHQ28FeJYHK2i2bPFj-pYssTeS6RbkabmKyf_NeyPB5_7UsvhSMpZcyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویر ماهواره‌ای از انهدام رادار هشدار اولیه آمریکا در پایگاه احمدالجابر کویت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/674041" target="_blank">📅 12:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674040">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd68LO1_6AnNWWidRO1lm39XFNo46GiQF3c_nCy3MUiz5g1XRH-gv5MFbqzBBKdT2VAkLor_4uwDxXqMzYR77VOmKo64hjV-whpoWwnOSFfq0Bc8Z_KrsRnI2JAv6kT4ufU-QIidQgWfB0mEszUB8PHJm_x-ogIyVXFkK5BZQd9PJg-aIprjCCse3sYJ9MMQdSsYdgM-6GulGToRK_BymOa51lTDM0y0oROJ1ROnyApHpVH0anXstDnkBNDVjyktU8-CkBs-MmfCpiao4BU1PCU5T0l_3WLzDxLQ208HvX_Q1ivcFnlVUhHBXiCUXre98t3oxlJUbvR6zQtNCZOO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینستاگرام قابلیت تعویض یا تغییر آهنگ پست‌های قدیمی را فراهم کرد
🔹
اینستاگرام قابلیت جدیدی به نام Replace Audio معرفی کرده که به کاربران اجازه می‌دهد موزیک پست‌های فید و کاروسل‌های منتشرشده را تغییر دهند. با این ویژگی، برای تعویض آهنگ دیگر نیازی به حذف و بارگذاری مجدد پست نیست و تمامی لایک‌ها، کامنت‌ها و آمار تعامل حفظ می‌شوند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/674040" target="_blank">📅 12:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674039">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a25e7a443.mp4?token=i6dCZXmQLX90bgnN5lPg_7R38XxO0df5qjX4tS9bV2FNyJGZRKqWilqrJHQtHBWmwRUpqX-TeEixUPrC7gBCdupAekIcrW6p0NHyHB0bYugKAXOX1J9ank-NHRbO0l_vOarsJXSS_8Nj8YKZn3YIewg0InZe13YxUjBknffrlocq_5fCxrHV2heybxHhaGGFa44qjgxMdQV1ELThN_pVptdJpXYiTuQuxt6NPrpigBXDQmuVPS5EfF0J73_Wk6rjMuf6jxMdyuRnP1ttBLa31nKu6zhETrvGl2WKn8e8EIUpH1SiOXil64talAoGOzy7Nk3jJjVH61WsFwLn1-0LxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a25e7a443.mp4?token=i6dCZXmQLX90bgnN5lPg_7R38XxO0df5qjX4tS9bV2FNyJGZRKqWilqrJHQtHBWmwRUpqX-TeEixUPrC7gBCdupAekIcrW6p0NHyHB0bYugKAXOX1J9ank-NHRbO0l_vOarsJXSS_8Nj8YKZn3YIewg0InZe13YxUjBknffrlocq_5fCxrHV2heybxHhaGGFa44qjgxMdQV1ELThN_pVptdJpXYiTuQuxt6NPrpigBXDQmuVPS5EfF0J73_Wk6rjMuf6jxMdyuRnP1ttBLa31nKu6zhETrvGl2WKn8e8EIUpH1SiOXil64talAoGOzy7Nk3jJjVH61WsFwLn1-0LxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصاویر از کارگاه بمب‌سازی و دستگیری مهدی خانکی
🔹
«مهدی خانکی» عنصر عملیاتی و فعال یکی از گروهک‌های تروریستی؛ صبح امروز به دار مجازات آویخته شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/674039" target="_blank">📅 12:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674038">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91b263bf7.mp4?token=IWoUSBppBWIoU5auMwyp_MdqDsiw7SsAExrWM7ZvnGIJSx1fLnNdSlPKZMRTyXMWYptU7yGLN2zGVlEmgmeZ7FQ0a3SRmLAQOIgdEycZPVk4TBUg73KoVdkfoMyLgOrphfeR35caS8DdR3HtbyYhmbpQrS6FyLfiX8UoxATZjpOjOGma0DBCDf5yp9TPVyFB4eYJL7rKiLifSFGc-2CMG6HFAPbaZdFMJRDwAhg98OUQxvafwwwDD3aQpNoVEV_APjvDqVWNBdrh_RZahmFXmM2Q7B6PihVMe0NIRKW8wyyob9VQhIQtyKvJHeCNGo0iYWkwQdp-FgfNNxr2RtYZMIJoi0tjHkY-6ltFWJmfGlY65FIdcTsyqkEgYj4tlHs15XcHp9kMVdLi2CqdIqgiaJgTt8QAfCQ5ZosbLeS-V2qL2BvZ-Qs4Ci5lu0BDk0ZUVQ3Z3YMZdq4YMyUAo5SpfIrJXwe0gnbRp2tV9rOnwqtZbV3Us3BMSQLLuvlF5UVLa9R-zpZuGvu7QbFzYXY7Vm1TNCBraQxncWUWpqrusX8jXY4Ep107tqVu6iap-2m12PXGQQ6ng1DAmZVV5BPcNcTDHu5FjmvNmmkKGSUNIf5Q3gKmaQvRbzp8KfmcviU9fsBcIOMDboJtKjM3ElHamXb64jg7MNjMEQES-CvCCyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91b263bf7.mp4?token=IWoUSBppBWIoU5auMwyp_MdqDsiw7SsAExrWM7ZvnGIJSx1fLnNdSlPKZMRTyXMWYptU7yGLN2zGVlEmgmeZ7FQ0a3SRmLAQOIgdEycZPVk4TBUg73KoVdkfoMyLgOrphfeR35caS8DdR3HtbyYhmbpQrS6FyLfiX8UoxATZjpOjOGma0DBCDf5yp9TPVyFB4eYJL7rKiLifSFGc-2CMG6HFAPbaZdFMJRDwAhg98OUQxvafwwwDD3aQpNoVEV_APjvDqVWNBdrh_RZahmFXmM2Q7B6PihVMe0NIRKW8wyyob9VQhIQtyKvJHeCNGo0iYWkwQdp-FgfNNxr2RtYZMIJoi0tjHkY-6ltFWJmfGlY65FIdcTsyqkEgYj4tlHs15XcHp9kMVdLi2CqdIqgiaJgTt8QAfCQ5ZosbLeS-V2qL2BvZ-Qs4Ci5lu0BDk0ZUVQ3Z3YMZdq4YMyUAo5SpfIrJXwe0gnbRp2tV9rOnwqtZbV3Us3BMSQLLuvlF5UVLa9R-zpZuGvu7QbFzYXY7Vm1TNCBraQxncWUWpqrusX8jXY4Ep107tqVu6iap-2m12PXGQQ6ng1DAmZVV5BPcNcTDHu5FjmvNmmkKGSUNIf5Q3gKmaQvRbzp8KfmcviU9fsBcIOMDboJtKjM3ElHamXb64jg7MNjMEQES-CvCCyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیروز حناچی: مردم انتخاب کردند در جنگ کنار نظام بمانند و مقابل دشمن ایستادگی کنند
پیروز حناچی، شهردار پیشین تهران در
#گفتگو
با خبرفوری:
🔹
دنیا ایران را به واسطه تاب‌آوری و مقاومتی که از خود نشان داد، تحسین می‌کند.
🔹
قدیم که جوان‌تر بودیم در خاطرم است آمریکا سر ناو خود را به سمت کشوری کج می‌کرد، حکومت ساقط می‌شد.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/674038" target="_blank">📅 12:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674036">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ffb7964c.mp4?token=Guv8nuXNDrVWnOC2XgzYPYmN6f5xhzjfGjQkcNC6MqUBkc7qyOAqQWjGxGLgNhw1Hb6SZUWD6mEfHsZHg0CSAX-hRuoDUsTiCztrAX32OktiwSfU7w-50RVJh_ugIr4yT7luAK9EHFHS0k0hMbZE6_xvX4_QD4c2hyMlX3fhg3WJRD25k5MmvG-b14CL7JXK8zI-N9g1IrgNBUljxT0UqX-Y9s1RPHGv1JQHbSxgeK_K4tyD8ey5XFn8aMYtv_sLjy2iuh4KAD-0xpETx5_hipuadR67c1GNATMEHL6oUnvPiiJKulIW5BAhgfKp6VNAGGg6-ts9rVT1J0RyvlF-jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ffb7964c.mp4?token=Guv8nuXNDrVWnOC2XgzYPYmN6f5xhzjfGjQkcNC6MqUBkc7qyOAqQWjGxGLgNhw1Hb6SZUWD6mEfHsZHg0CSAX-hRuoDUsTiCztrAX32OktiwSfU7w-50RVJh_ugIr4yT7luAK9EHFHS0k0hMbZE6_xvX4_QD4c2hyMlX3fhg3WJRD25k5MmvG-b14CL7JXK8zI-N9g1IrgNBUljxT0UqX-Y9s1RPHGv1JQHbSxgeK_K4tyD8ey5XFn8aMYtv_sLjy2iuh4KAD-0xpETx5_hipuadR67c1GNATMEHL6oUnvPiiJKulIW5BAhgfKp6VNAGGg6-ts9rVT1J0RyvlF-jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور می‌تونیم هورمون‌های شادی رو فعال کنیم؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/674036" target="_blank">📅 12:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674035">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-text">مدیرعامل شرکت توزیع نیروی برق تهران بزرگ در برنامه زنده تلویزیونی تهران ۲۰:
همکاری شهروندان تهرانی در مدیریت مصرف برق کمکی ارزنده در راستای کاهش محدودیت های انرژی هموطنان ما در جنوب کشور در شرایط حساس کنونی است
┄┄┅┅❅❁❅┅┅┄┄
💻
وبسایت اینترنتی توزیع برق پایتخت
www.tbtb.ir
┄┄┅┅❅❁❅┅┅┄┄
🆔️
@tehran_roshan</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/674035" target="_blank">📅 12:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674034">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8d6SjuLqSk1_Viq7RRxvoMDxr3WCUemCIkipVQFzVX4P3Hsj9Uox9lyk29EWyINJz6DW7_G2UhK_mNJrSCbJt4V_sHDCPqodUgMxblwB6UPCGE1K9iurfIT3_UwNvabvJP7N1WVMsI_1uFQ_0vgjgYEQZwdMP3b_WU94vsL8mMPIcUclFeulKJpaIA1e3PByKOVvhPII1Jsh1OyqWuMUUm5jFRta1IeHpHNfGvM0NFnHmWja9BTOXiy3IGPMe-7o9Pt-DfTepNbUOeVQ1th0oNEsJPu3HhRbU6ese2pq4wFSxHOawGsbuzP3V6P1IfvinDsWpGowZhywwIfXYMq_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارلینگ هالند روزانه ۶ وعده غذا و حدود ۶۰۰۰ کالری مصرف می‌کند؛ معادل تقریباً ۲۴ چیزبرگر
🔹
رژیم غذایی او شامل مرغ، پاستا، استیک، ماهی، سبزیجات و عسل است و تا حد امکان از خوراکی‌های شکردار دوری می‌کند.
🔹
جاشوا کینگ، هم‌تیمی سابق هالند: «او مثل یک خرس غذا می‌خورد.»…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/674034" target="_blank">📅 12:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674030">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
فرار هواپیمای صهیونیستی در حمله ایران به بندر عقبه اردن!
🔹
رسانه‌های صهیونیستی گزارش دادند که در پی انفجارهای متوالی لحظاتی پیش در بندر عقبه اردن، یک هواپیمای غیرنظامی رژیم صهیونیستی در پی انجام این حمله از پرواز خود منصرف شده و به فرودگاه بازگشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/674030" target="_blank">📅 11:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674027">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6N4jLLs4E3Ej28cPs5zvLvXwrhnibw_e50ADpFk-dqhpHhB01EV0zPOdxpB-eEtEFkr7co7kvNuGh_SrFbsvtOojzcMtT3RyqbU_7UZX5xYl6GUwfV9EcwjYRaYGW2u2igTr2-WS71gft3yBQctRAyazM0alhSOpPhddqaJ7dQ-VF7mM9Bb40gR65UC3FyxWyyawPmZHAnLxKbRzKU2_w_tIiKNRxr0GrurYqWiFgNRL8950TtFUBc7eKp9TkUl7xA6fmjGw7oDyo-NVSbj_fb1qwuRGUExcCm67qbKbMXCEb7ZD3r1PzMi7fiwhXelabqoFkLIf0gLTGQOwO967g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخستین حلقه ازدواج جهان، که مربوط به ۳۲۶٠ سال پیش است، متعلق به ملكه "ناپیرآسو" همسر "اونتاش ناپریشا" پادشاه ایلام می‌باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/674027" target="_blank">📅 11:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674026">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5ipRCQFfQIOj0SfDdQ2ZOYCjtdvnUsyq05YJx2jSeiGCUVjui0a0PtNnEmR9UhoCDxgLbkvXKPiIVX9Imbu3zXMNbchNtIley9Tnu9aQtxYmhRW-f6cvUsFiH_XGnqt2OYfPoqFBraUu8KyGrBzipEBXxi5LgSFkleTshAtmiG0KgFCwpNV199kqotgSIcTvTBYonaQPwJf0PQqIcWkz0B798C9HK07XVDpha6Wqwu-W1idKmoopGpbP-d6QFGhQasE8-8-GMs887jcdGXILSkAnv2MmcsCl8D42jvzL4QVU-Z7z3liyWwRn7J-y4Um2fYaobgNkUr21Oacd3kbXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوشیدن ۵ فنجان قهوه، دوست یا دشمن قلب؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/674026" target="_blank">📅 11:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674025">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUoOwgbsrymAKEvZLRvcUpY5H8tAojJV2XMygJYm_M1o8LfJsXOAC0OQbUlsWhcsf2uxeJ83iV7vpKtX3rOBWYX6qSxu3UX2pRO3AG91SIN3t5d828JtbbB5vIMCeJFjZMk7kCnwRoZ_VdYTGfwEhtPC2e55wN2AN46oRrzgl8vCHtZqGds4xhdhnD2AZ1YXJW2JgGiOlc1WTb6NvsFjks_vSJgpx45WKtwc71BvHL6UKjwS7JM0E-B-akSv-NEmebtdywonEovHK6UaBgA9GVJlX7xyGHVAzlkZ0i1pC2T9Lc-SfRwJdeo1uH9Z4oZpWKyJg3OcGZJKTGKwbRboLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بانک کشاورزی جایگاه برتر نظام بانکی در حوزه صیانت از مشتریان را کسب کرد
🔻
بانک کشاورزی بر اساس ارزیابی بانک‌ها و مؤسسات اعتباری غیربانکی که توسط بانک مرکزی جمهوری اسلامی ایران انجام شد، جایگاه برتر نظام بانکی در حوزه صیانت از مشتریان را به خود اختصاص داد.
🔻
این رتبه‌بندی در چارچوب مأموریت‌های نظارتی و بر اساس الزامات قانون جدید بانک مرکزی، با هدف سنجش میزان رعایت حقوق مشتریان، ارتقای شفافیت، بهبود تعامل با ذی‌نفعان و تقویت پاسخگویی شبکه بانکی انجام شده است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/674025" target="_blank">📅 11:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674023">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5ff34b00.mp4?token=nFt7sHiFtQL3RY6xzd9NAlCmDTHKBF0OWnCdorgXeobf_DYAhNat30zMCjQg5wijUSM5WR0UQcd5Sdo5jrT-Ini_EZRhjw8K3GNV0LWpccWfscoAjvtcNQGr0njBvL66GgwT7VL5SVAE1ighp43EsmJ9ZkxxN0dnD3CO9rsocBmIZ7EcGFOj0EEyDWtIVlFpCuMX_aZsgwiEUsUDxka5EDtWLL8ioF-EGcba3VR1ECqgsad4MIKRwjDZgADHpscnC12B8SQu7u41hCyGwu5FAI2Xp0LR1gGjyF-_7AnKJ6IP8pJwzijTUq8i_OglUTq_QvRz02W8YNfy9VZyEvkl9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5ff34b00.mp4?token=nFt7sHiFtQL3RY6xzd9NAlCmDTHKBF0OWnCdorgXeobf_DYAhNat30zMCjQg5wijUSM5WR0UQcd5Sdo5jrT-Ini_EZRhjw8K3GNV0LWpccWfscoAjvtcNQGr0njBvL66GgwT7VL5SVAE1ighp43EsmJ9ZkxxN0dnD3CO9rsocBmIZ7EcGFOj0EEyDWtIVlFpCuMX_aZsgwiEUsUDxka5EDtWLL8ioF-EGcba3VR1ECqgsad4MIKRwjDZgADHpscnC12B8SQu7u41hCyGwu5FAI2Xp0LR1gGjyF-_7AnKJ6IP8pJwzijTUq8i_OglUTq_QvRz02W8YNfy9VZyEvkl9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گرمای واقعی جنوب، از دلِ مردمش میاد، نه از آفتابش این روزها یک ملت مهمان مرام و معرفت مردم جنوب‌اند اگر جنوبی به خودت افتخار کن؛ تو پرچم برافراشته مرام و معرفتی #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/674023" target="_blank">📅 11:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674021">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea9b7e62aa.mp4?token=BosjTKGMAkiN2G60JWNzS4mIPNV5ejqkA_IVwJDwbJ7jivacJdkQ2jtc0jqdPeQz61mhydAqSTsA-ZtTNIZWl1pIWf2vJw6zUJeG3qUHJ8asm0vMts-RD4jx1UUAe1WxwmLnyedBYJI7ltjE6aG5l8fn6gQ6CKn3TH-hv7T8h576xDE_oo3UfJrbBgPZadcp51rFkKb_Ok0OWDVTMxWidokePMYT3v6z-SLyAss0CPId1gvqH4j73y-s6SSdVIw4_YeHKeRXpYqSmiGKXjdpDQfVnrCjWjXDjDE9FMrVCU9EGzied3laQGJc2NOo4LFWW_xUkp8qqWkBpcr0rYE18Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea9b7e62aa.mp4?token=BosjTKGMAkiN2G60JWNzS4mIPNV5ejqkA_IVwJDwbJ7jivacJdkQ2jtc0jqdPeQz61mhydAqSTsA-ZtTNIZWl1pIWf2vJw6zUJeG3qUHJ8asm0vMts-RD4jx1UUAe1WxwmLnyedBYJI7ltjE6aG5l8fn6gQ6CKn3TH-hv7T8h576xDE_oo3UfJrbBgPZadcp51rFkKb_Ok0OWDVTMxWidokePMYT3v6z-SLyAss0CPId1gvqH4j73y-s6SSdVIw4_YeHKeRXpYqSmiGKXjdpDQfVnrCjWjXDjDE9FMrVCU9EGzied3laQGJc2NOo4LFWW_xUkp8qqWkBpcr0rYE18Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بی تابی پدر و مادر فرشتگان مینابی از آخرین لحظه‌ای که فرزندان تکه‌تکه خود را در آغوش گرفتند
🔹
از پیکرهای تازه تفحص شده شهدای میناب، ماکان هنوز مفقودالاثر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/674021" target="_blank">📅 11:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674020">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fef08200e3.mp4?token=NPJO7U4ynEgAHy4goMvpGxAO-UFYNZOEEhMo6XkeKWFAeuTg0IPAiHp86GMNmpxjStW_85VL1s7jDPwGNCvEk6FICwkUJDcsb68OKyMr7y1qHyb_d81OnZek7tBORdHY3kh2RHWKkvhi8k55qm-AsqIdbmduPS8BMX-pi-Yg5pisMKmWTVbyi805WKQPbdIAuOIAV3LHmbbi4T7511lfYHSg9pL9HLhEG4R8XH0kGw8ptt26aVhP9payWhMMHyp9naO16BN1sI5-R0MkUvpZtkMmUNH35ZqJXomngGfkCP5b2F6exEuTY62LAF7KhCDEx0VErEJogh1NZG8El9XHIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fef08200e3.mp4?token=NPJO7U4ynEgAHy4goMvpGxAO-UFYNZOEEhMo6XkeKWFAeuTg0IPAiHp86GMNmpxjStW_85VL1s7jDPwGNCvEk6FICwkUJDcsb68OKyMr7y1qHyb_d81OnZek7tBORdHY3kh2RHWKkvhi8k55qm-AsqIdbmduPS8BMX-pi-Yg5pisMKmWTVbyi805WKQPbdIAuOIAV3LHmbbi4T7511lfYHSg9pL9HLhEG4R8XH0kGw8ptt26aVhP9payWhMMHyp9naO16BN1sI5-R0MkUvpZtkMmUNH35ZqJXomngGfkCP5b2F6exEuTY62LAF7KhCDEx0VErEJogh1NZG8El9XHIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر زهرا میردادی و فرزندش علی سالاری از شهدای میناب بعد از چهار ماه تفحص پیدا شد...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/674020" target="_blank">📅 11:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674017">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c0200817.mp4?token=Ut5H4iRzhdV7e8WHhYoq8zKjEO3dEMjDPv54HabvrOvLThDyIX4em1Y0wSLI-GxPqSSlLW9lGxWLFfFDTsyRMDrJn9DU-gpuy6dnoS2DNAW_13NuLxbZpYChOQcrQEXcdkVSiFHDIljgzgHESiMxizTTgzNt8Z5yEoM1IRhNPxuvaqO4Nn5uY5166mO28HcYuSEdVBJn0vTgAtnBhTHTILjeQ_lcGYq8-7csm66ZcUneg8dEFt40yC0ImZ4MX-I-4zBLRb5WqfdO3LXaSJxTWMWt-2NLLmoj8tEcL_ukem4ZwUhm3JHH4850WJpT7pubTHge6bt-nAkmAfZ0ffsN_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c0200817.mp4?token=Ut5H4iRzhdV7e8WHhYoq8zKjEO3dEMjDPv54HabvrOvLThDyIX4em1Y0wSLI-GxPqSSlLW9lGxWLFfFDTsyRMDrJn9DU-gpuy6dnoS2DNAW_13NuLxbZpYChOQcrQEXcdkVSiFHDIljgzgHESiMxizTTgzNt8Z5yEoM1IRhNPxuvaqO4Nn5uY5166mO28HcYuSEdVBJn0vTgAtnBhTHTILjeQ_lcGYq8-7csm66ZcUneg8dEFt40yC0ImZ4MX-I-4zBLRb5WqfdO3LXaSJxTWMWt-2NLLmoj8tEcL_ukem4ZwUhm3JHH4850WJpT7pubTHge6bt-nAkmAfZ0ffsN_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان نام فرزندان «الهام علی‌اف» را می‌داند و تلفنی احوال آنها را می‌پرسد
رئیس تشریفات نهاد ریاست جمهوری:
🔹
صمیمیت پزشکیان در روابط با کشورها خیلی اثرگذار است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/674017" target="_blank">📅 11:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674016">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATjv1HQDSt4Xc7bsPNLc4fVEbtyIjrsNcgvlB29xg-ToyaVWt1VGURIAxIpvgQZSj557GwP1Ip_8IqkIp6c6mB889GP_5ncQ_xbhH_d9_wnz8rGTmTe6I6AUg-FIBhItPLkhRU4SgO1YhK8e0DHqEFawdwhzN28-rT8Ex6y2FiLXSnu-XFFWADeIat2909Je9TWgfGOkgfSm175p-Kwb4p5lc25sy0doIDzlYAm-154sXaRMeBnlIusUOGWGhltYp4D6-0YUO3SS-lRYYaMseGpYRF-AyGLGfTiZjv9tJznH9-QgIcw2QufQ92LhcZymCzSPr7uSuJborqSNZM2tlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده کل ارتش: پای کثیف آمریکا به ایران برسد با هرآنچه داریم با آن‌ها می‌جنگیم
سرلشکر حاتمی:
🔹
دشمن به خاطر بغض و کینه اش از رزمندگان ارتش، هرچه در توان داشت، علیه آنها انجام داد ولی رزمندگان ارتش جمهوری اسلامی ایران راست قامت ایستاده‌اند.
🔹
در قضیه جنوب اصفهان، آمریکایی‌ها تصور می‌کردند اگر پایشان را در ایران بگذارند، از آنان استقبال خواهد شد ولی با تنفر گسترده و ایستادگی وصف‌ناپذیر ملت ایران مواجه شدند.
🔹
با نصرت الهی، قطعا بر مشکلات فائق آمده و دشمن نیز بیش از پیش، در رسیدن به نیات شوم خود، پشیمان خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/674016" target="_blank">📅 11:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674013">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f520b6b90c.mp4?token=vKDWJC0oC4c3pXm7C0QlsdrR_rKj4IlcM_PW9ayX9yx6GK5S6WGrlBemjV9mI7MSbaxu-wUZHPRMMVO-Usp54VzUp6vMYfMtwhK63rVkfpe4Nt78hqilPaPMxcHEzS_wFqfjp6a7DG8qOSSXd_yDKBxqv5dVBuxxWpFvxfexameeDTDsjRhl2CEPPB8Wb2sReyu2CptrYhVODO4x3xd1iwB-X6K1smGopGw3mzGWe4kcxuvI_Vx5FewcpvXBeixTY2ewmpIQPoracCzYGwKF0DXI-uriXNMEvwm2Lo-P4pL-_4rDecz9X5KfR-e4iBMpNpOvA4DdqF3ibvftQcGykg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f520b6b90c.mp4?token=vKDWJC0oC4c3pXm7C0QlsdrR_rKj4IlcM_PW9ayX9yx6GK5S6WGrlBemjV9mI7MSbaxu-wUZHPRMMVO-Usp54VzUp6vMYfMtwhK63rVkfpe4Nt78hqilPaPMxcHEzS_wFqfjp6a7DG8qOSSXd_yDKBxqv5dVBuxxWpFvxfexameeDTDsjRhl2CEPPB8Wb2sReyu2CptrYhVODO4x3xd1iwB-X6K1smGopGw3mzGWe4kcxuvI_Vx5FewcpvXBeixTY2ewmpIQPoracCzYGwKF0DXI-uriXNMEvwm2Lo-P4pL-_4rDecz9X5KfR-e4iBMpNpOvA4DdqF3ibvftQcGykg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع پدیده‌ای نادر در سواحل شیلی
🔹
سواحل شهر «واسکو» در شمال شیلی، بر اثر تلاطم امواج با مواد آلی، پوشیده از کف سفید رنگی شبیه به برف شد. مقامات تأکید کرده‌اند که این پدیده طبیعی هیچ خطری برای سلامت انسان یا محیط‌زیست ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/674013" target="_blank">📅 10:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674011">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: مسائل قانونی و شرعی گواهینامه بانوان حل شده است؛ مقدمات آن در حال انجام است و به زودی شاهد اجرای این قانون خواهیم بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/674011" target="_blank">📅 10:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674010">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ee7eZOpNHOGAmf-ewArdhl3tRlRawkT56uPOXZSLPlepScVypD1wYtW1NlGtyklX54fo7qZ0ZEPA6SMlYpMW-FnEj0A1_s4Q0Es1P804a_Hm3OwiwARc84tJcI7FNZgczWxFmAtk__bePofGdBH3RyEwwRx7OYPNZFtuubWmvh_TsLdaShTDJ1NpGrUI2wIgpyIuMvConS-E7U1WjTe0RZao37H6OCffAVuOEc4hE-HNSqADPTxP2DJrHz52X8R95YZiOXHisDyVJYabTXOJ8dI4rUIYUNQWaz3nIVKNr9Cw_5_fEoa57_wjNKZ9zn0eAibTQaIqPk1D_FnFDfw5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول جام جهانی پس‌از اتمام بازی‌ها
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/674010" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674003">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJx-boLqTNx7N-r4tieVdUIJxzb0u6bolHelPMlzZejbqpfon0PwzLPSrNZunGbMyH5-djl0a5WxzvlR-nrWD6LZwq979LR7vooOcryGsCPjt551DLEOorQdqVPAVlE9ciTUjaE-S4a0YKQUIXQndDIZ1nlRD9eFcFcqG25s3WcBaQ7B3R4H2L5AudwwQJYXQ8SKZ8C0gzqEisdhwGlRkLHQIr5BjeRe9BgzsyPy4BndDYnMz4YCiY7Sr1fGbxnWEZE8Ko92c27HLxsYtJeshdIhK26a_pO2U4SRi6O9BRmuzMe3k1TJNIi1Whlm-bt81kefvVzNdvnU_4reXbrjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GoUSfo_yJ1vaONbHQmhw81LHXc8nwtdxZHoNiYl_AqzhP-sMauP1w1eeeKl3MZPzFvNTqLArD_0zkuPi8S5Ng8d5wl4I0d42zYF-QT9b5REhrSGlfIczYwrKbS9poh9ibYYb7EAyf-xyi5Gtc-HQbZL3H4GPqy9KCJoSZ7YC5grzJVmPKmnZhy05GaIKHum3bai9TFfOjCPc5hOGP-p1fa991-B462KRjGdR-bEpP0YW-ky5POfhS0ebebHrkRqU46Rnm73cFt4e1dBqYPVxKDQR-0JhRq4qVLj7h7vK56YfsuzgcdqgntpRIBH7IQzyQIk1NQaICph3rtSmut4n-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9neQ2wDqF1ZqedxmmBS2pAddBhnzaO4ZCZfh7owBsu0MhlsAgGvnafMN5UPF_c9z1ltjxDfag0gEnIpGsWU0R8pVmS5GOtQl7mw0zw3ebgUDNRb_-fuT8QuV6cXUf372Kb-rmx7yJi0gjqYjaU4n8uhu8CxxHP1KzEkzc0GGNSUXB9ZrQonxCpIJTUboGQ-aAyAcz_pg7NNSKm-BjL4QwgPY1fRSHfnlR48qErem_xe4V-eiaPRCI25896aCEpd0H1pRJfjnsg4Zf8Iw70RHcYXPQhQ6ifZr97mRey7eD2TkQUir_xMfyi5qoRNOaH73xqqXUMHFaXCd77X5YNuNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VbUvLZw37_lQvTvMF0IkJIxcw2VdkIET2piuejik0m1wk6QmrhMNzbflnEmiKg8ranL9r9HLzdUyVjzGKR0hcRz8a_uGJzOWulQa_x6EqM74mJffrhS5n0sx7Co4JnQGDX-xV1YYTLyEV7HeEi-fe2vQtINw2fUpVs5o9w2aT6KMHIS6LA2ExyOTU68Lfe_pWYG0LXCQEvjKdxD2ODkfQivmazFQWdK5CU0HiCE2fr5a9AE6TTnbvTB1VzXBkqrcGyNzpAIL49BbkvJ2hZN_vp2_C97nsK7KGHNE88yQp-54kLKyexeFBuJ-xm4Gf2LsOSOasCnK2PZxsuHK6YGZrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u05A1xhA4zWsXDA_dmEGOtfQpnOHmBalzDVNiBpxUong9PhJ7ftUHSYj_C7WhwGUCVlI3jsl0653V7NdYChum6S_PJcebjuPficK9GfJ_I6QIRoLMgrauvDD7WZISzX_WYyjm80Dw7N5tqU0V1n4w5J5CZ6uT7JKvSY0MZlFi6cIsoURNTXtvvAWzNxf_MbVYRlcPFN0779gC9z3qMc7oo-UxwPOw0yb6dCXmY8AVyQAoPLOqliQu5nfygOpkJy5i6TzZOCU4m7NlIZ0PsXffv9cJ-gZOhsDX__dTYcXBc0N-J-ObggjzXjZH8TTQ9RnjYdQMJeTTKrYpc8BCqqIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HncLOpAcdq6mIMKnL3HFz8Cuzu4XubbIFiyDJmga7yKW7nSdKgdaYqQcovw5vo8RxZRclZdDdEYB7DFyRhFcEw2LAxJ7501XS9r1wjEp0AxZMfmrabvydaPuyvZYKAy9lakveBoNkzDOORrQIByn_J6MNtjtA68u5cChzuOtgdi7cZvc-edqfbKwcVnOEGO3BYtIMUTN8W0cd7d1Mx8iV-Txtz9mNrBenCa659vIdATgfeRKCpi4txEahBL3b8YOq0lJp17xNMNBSwIUlqkuwZWLUU-tj_X-FqhV2DBbU7l6PjHkpPZNfC93zk5kRLmXypWunhOcrMkZhxXZ4azKHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هنر بازیافت خلاقانه؛ تبدیل کفش‌های قدیمی به آثار هنری ماندگار
🔹
این خانم با پیشینه فروش کفش از سال ۲۰۱۹ کفش‌های قدیمی را به گل‌های زیبا تبدیل کرده است.
🔹
نکته برجسته این آثار، حفظ جزئیات، لوگو و بافت کفش برای نمایش هویت اولیه آن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/674003" target="_blank">📅 10:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673999">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9NZA7GWTTlXIhttnhfXN1gZRp1W_v9qhnXNp4frNBfBERa9X8-iij41Ucu61-obc8NfPN6uRjj8IIZyvdSQijukC3la7pXVmwNN5933dbLeGO1n7wFWDwyZmc4gPIwwS294h33WgUjJwgalBUwCgcd3iylB_uFKTTkvEcvu1fC2je2l8S8cAkhu3gP3aa-omm8vI4LxkktXR0yx9vwWi1U0SW8JT7xS5noiZYPCwwe3dvY5FHhHQLpKglrM-nTYdHYql6QUq_VjOReres0Ez1LWjMcRp7KZZK9TgciV64ls-LwBLkWoPVpkx3jUvgFD2iAnTmw_AN_U4sdB-wXVLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فقط تو ده دقیقه و بدون روغن این فیله سوخاری ترد و رژیمی رو‌ درست کن ⁨ مواد لازم:
🔹
نصف‌سینه مرغ
🔹
سیب‌زمینی
🔹
نمک و فلفل
🔹
تخم مرغ ۱عدد
🔹
پودر پانکو  مواد سس:
🔹
جعفری
🔹
پنیر کم‌چرب ۲قاشق غذاخوری
🔹
پرو ماست ۲قاشق غذاخوری
🔹
جعفری
🔹
سس زیرو‌ ۲قاشق غذاخوری #آشپزی
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/673999" target="_blank">📅 10:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673998">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE2j1z4h7s-Lg3jAKNYpfYw3N_w5zZfDTcmFmN4l-oDGNLx_OYad2yMA9OHIR2XdRRNPb7GZS1vl0uIJlJlOBI87uQnwblhwt-yAuPJpmihzx2ou0ykurzQ1QuHFyDVj4ZNQ822mfaDrjfRN4pxhi1xSlfsAgyqMU3IgxYp5iMQLiRc25XIX_c04b_48N6aOOWw2Z0VkGyp1XBm8V7lwH7F5vP5_QiyvYnaWyTQFOL7cx_kB4IL3wx4C2Y2XM4rL8qjVMw4g4dtxpbbyv29d_9YQTmWa3iw0pNABecicXPKWsGgFU__id8uPeG-L1lxCaQZ_VBkXPCRA8wBtQpB0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قابل توجه سهامدارن بورس و صندوق های طلا
🚨
بررسی کامل روند بورس و طلا در کانال زیر
👇
https://t.me/+werraAXV39phMDZk
برای دریافت مشاوره  به ایدی ادمین کانال پیام دهید</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/673998" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673994">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6347d7eaab.mp4?token=cdOSkEDWIHiczLQ7jg_FWmQwvtGTthReGgvVmDQBl1u9DB-aiBPXS_CU8wH4295EfKCFeueFq5H6Zqy_qKhIbKGmiF22H6SNUdllwasM8_VuzBQB_zxKQPUukQJGqMvaWneLCUw7AxdGIQFwU96jrP_TnuD1YbUpI9IwDXJIzTnKbBnmoOa4c1RZePydCo2O2s5mtc0-M9aJF0NzULGVZSJgiG2fCgnGQiiPIZ7PFvF7wlTSVa3L16M-aI-wFg40bLKiHdUZyCkciyiEBOVmgFj0G28YKRtdsaQQBC-2qs8QMnJklHF1Ad7hFiYBPm9LpmCIwh-OSmrOLrQrXgI8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6347d7eaab.mp4?token=cdOSkEDWIHiczLQ7jg_FWmQwvtGTthReGgvVmDQBl1u9DB-aiBPXS_CU8wH4295EfKCFeueFq5H6Zqy_qKhIbKGmiF22H6SNUdllwasM8_VuzBQB_zxKQPUukQJGqMvaWneLCUw7AxdGIQFwU96jrP_TnuD1YbUpI9IwDXJIzTnKbBnmoOa4c1RZePydCo2O2s5mtc0-M9aJF0NzULGVZSJgiG2fCgnGQiiPIZ7PFvF7wlTSVa3L16M-aI-wFg40bLKiHdUZyCkciyiEBOVmgFj0G28YKRtdsaQQBC-2qs8QMnJklHF1Ad7hFiYBPm9LpmCIwh-OSmrOLrQrXgI8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله ارتش رژیم تروریستی آمریکا به چند قایق ماهیگیری به نام قایق‌های تندروی سپاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/673994" target="_blank">📅 09:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673989">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0127444c42.mp4?token=nnQxDZhGnuo7x6xp4yF29QeZGBtthw7Cap2GoE0AMOlA0kggF11s25zavhrFq7ijikDHFRMo4HPh5jC0iIJZlEViGLzkEuonyReYMZ_r30iHLxkucNEu066cFTazs70MsKLOyccZzkmATVb_e4P7aQmgT8EPnGNXyrWW8UE5n23kVn2uuLvdV_cKp2tt_NBfnjnYOlktSw_UlLNEHYjXuMcExiBEZRhQsnxmyVO8ZMVrjuWJ5x7J4lGt3mzm9Nd0YlPGdpekdWBL9ifl5bAoDZ6c2MADFXkzxCv-OQxBEN1TkBQvQhFodj8uWY4GSdbdkYIhL5d29CWJh84qn-olhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0127444c42.mp4?token=nnQxDZhGnuo7x6xp4yF29QeZGBtthw7Cap2GoE0AMOlA0kggF11s25zavhrFq7ijikDHFRMo4HPh5jC0iIJZlEViGLzkEuonyReYMZ_r30iHLxkucNEu066cFTazs70MsKLOyccZzkmATVb_e4P7aQmgT8EPnGNXyrWW8UE5n23kVn2uuLvdV_cKp2tt_NBfnjnYOlktSw_UlLNEHYjXuMcExiBEZRhQsnxmyVO8ZMVrjuWJ5x7J4lGt3mzm9Nd0YlPGdpekdWBL9ifl5bAoDZ6c2MADFXkzxCv-OQxBEN1TkBQvQhFodj8uWY4GSdbdkYIhL5d29CWJh84qn-olhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر هوایی از تشییع پیکرهای فرشتگان میناب
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/673989" target="_blank">📅 09:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673987">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bESu0incjMWeJEbrQX7l4RS9e1omAp6WWFe0p_RHv9x14ryRPdwsulg_b27vpugZjmcCKK69Zztx1ACYd1u7FIed-rLlwnm3_RKsoIPn_uAdvMOmLGElKYzDBtjaGEYeFURJvlsBF3YdhRJ1CrbgvCiJOk8nQ_43Nfg_DAigK4zH-gEYXvvHCgAk3Er0qvorykq_-ug1-o00f0KoKnREuZhkme4-YQkAlgSeap8g2OxIg0xyQa_LX6k7-DoPhhP8iFYF2RuP4JMALGeo5e6COJf-cfwPPlTbViYgH9pdh9LnIuReqPPNIStLLB5YLkoYvXeNTHQyMeRdpepqDhyfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه دردهای بدن؛ هر نقطه درد بدن، نشانه چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/673987" target="_blank">📅 09:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673986">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e92d6bf4.mp4?token=QxxSUlgHQ9xqDWXL21sugK7CKfkahVme3M_9Hhxv7K5YYAGNhaAGgbc4yU8JpSnl3PkC1yFi9DHIfSDfLfDqWMe55B2cS9jLeREwgJhIBLSVb756bQhgGc5N3It0NihmOLIU_MNsNCF9WH5RbWiZHUzLi0UnTOf-yQ096CRm5GvLxCPqXEybNMXUf6EtHFJMqb1pX_m4jHzBIn5ueMgs0C0Pjtb9UU6MrR_wcGnp_6ExrETVz0m4KjsgXKTcbE_6-rtexgBWnEmpmod4u5yQSy-Dj3QEB54A6vSZJf0FtcQY4cm1ikbzlH-ipBxbM2dQhRNfGTIEcXQuHRjFcNaQWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e92d6bf4.mp4?token=QxxSUlgHQ9xqDWXL21sugK7CKfkahVme3M_9Hhxv7K5YYAGNhaAGgbc4yU8JpSnl3PkC1yFi9DHIfSDfLfDqWMe55B2cS9jLeREwgJhIBLSVb756bQhgGc5N3It0NihmOLIU_MNsNCF9WH5RbWiZHUzLi0UnTOf-yQ096CRm5GvLxCPqXEybNMXUf6EtHFJMqb1pX_m4jHzBIn5ueMgs0C0Pjtb9UU6MrR_wcGnp_6ExrETVz0m4KjsgXKTcbE_6-rtexgBWnEmpmod4u5yQSy-Dj3QEB54A6vSZJf0FtcQY4cm1ikbzlH-ipBxbM2dQhRNfGTIEcXQuHRjFcNaQWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
فرزند شما فقط برای امتحان آماده می‌شود یا برای آینده؟
🌟
دبیرستان دخترانه هوشمند مدبّران (بارسا)
🏫
✨
در مدبّران، دانش‌آموزان علاوه بر موفقیت تحصیلی، مهارت‌های زندگی، اعتمادبه‌نفس ، تفکر خلاق و آمادگی برای دنیای آینده را نیز می‌آموزند.
🚨
ثبت‌نام آزمون ورودی آغاز شد
🚀
📩
برای دریافت اطلاعات و ثبت‌نام:
🆔
@modaberanschools_bot
📩
یا عدد
4
را به سامانه پیامکی
3000909030
ارسال کنید.
📲
❗️
آشنایی با روش‌های نوین آموزش و موفقیت تحصیلی
👇
🆔
@barsaschools
📍
تهران</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/673986" target="_blank">📅 09:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673983">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df897bf3a.mp4?token=k-SMSPTaRtHnI1GO9LsyewaBKyD44coZCf5bGGlmaTCVIUwL2npPX0ctg2Y-h__SFVnR5I8Xm9-GyUi6elz6eu1tUYDPrUmVDR-ZrgKyK10ngQXV4zrhEC7AOEMW65k5usgVfhgY9i-cnbuB-n0WW06GWxtstv-zfEFqTF8RiekFjVTooUPgZbM4R4JBF0KgY_IkpaMpgDb3T0_JN1SU6ZYAKAXmPdZNXGOiCDvEQcLVOS7zCYY8AvMldRVm2eUP9cQHcHYt7lSee4Ul441TJ01kl9_WNYIdFTHhM-bMCEn7Tz8kdOvHmHlu7b_nLbJMLiX8a-0b5DuCQbQdzl0WsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df897bf3a.mp4?token=k-SMSPTaRtHnI1GO9LsyewaBKyD44coZCf5bGGlmaTCVIUwL2npPX0ctg2Y-h__SFVnR5I8Xm9-GyUi6elz6eu1tUYDPrUmVDR-ZrgKyK10ngQXV4zrhEC7AOEMW65k5usgVfhgY9i-cnbuB-n0WW06GWxtstv-zfEFqTF8RiekFjVTooUPgZbM4R4JBF0KgY_IkpaMpgDb3T0_JN1SU6ZYAKAXmPdZNXGOiCDvEQcLVOS7zCYY8AvMldRVm2eUP9cQHcHYt7lSee4Ul441TJ01kl9_WNYIdFTHhM-bMCEn7Tz8kdOvHmHlu7b_nLbJMLiX8a-0b5DuCQbQdzl0WsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع شهدای تازه شناسایی شده مدرسه شجره طیبه میناب
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/673983" target="_blank">📅 08:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673980">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b36f8da2bd.mp4?token=LzYW0N9xDMLoq8gp_rYnj6XYEFzTQ8Kw8NWD5u4f-wYNkKowZC8BQdL5dMmeoV-KN1tVUKG32w7Gv9zp5wT3AasDMwOvtgmCk0LlBahp7YeM_0mmXFsgQ2WUifupo3DdGAB1jaHht9DRBLpMjf6EugDuhOWxDKHl-RKiaplianIYfoqcnXlPUQdQRjb-e0J_SZC04Xbdz-hOusY1JC58MX22pzMphf0Hs-ZhOdxGnFSdgPHf2fU29h0aslFqz448VRVasCO0_9wVbDsYO_75GZr23ZqJn1uzpmQTy0afkdEsmPzbjjYOuZSh_DaoOH-P9roWzdkykSrqZyxbIkViiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b36f8da2bd.mp4?token=LzYW0N9xDMLoq8gp_rYnj6XYEFzTQ8Kw8NWD5u4f-wYNkKowZC8BQdL5dMmeoV-KN1tVUKG32w7Gv9zp5wT3AasDMwOvtgmCk0LlBahp7YeM_0mmXFsgQ2WUifupo3DdGAB1jaHht9DRBLpMjf6EugDuhOWxDKHl-RKiaplianIYfoqcnXlPUQdQRjb-e0J_SZC04Xbdz-hOusY1JC58MX22pzMphf0Hs-ZhOdxGnFSdgPHf2fU29h0aslFqz448VRVasCO0_9wVbDsYO_75GZr23ZqJn1uzpmQTy0afkdEsmPzbjjYOuZSh_DaoOH-P9roWzdkykSrqZyxbIkViiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من ایران را دوست دارم چون شعر دارد هنر دارد تاریخ دارد وسوسه ماندن دارد وطن در دل آدمی باید باشد
🤩
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/673980" target="_blank">📅 08:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673979">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d68b609dc.mp4?token=GVL2QDZ5gNT7A-Y1-13EZYLLqXVrfE8o4jjLPC1mMde4Tgv1cYVv3qpVYW-CtbApcRhLyc1BzFQa2hKSad222k3SIHz7awqlQmapeyP_vOnIPGlGA7_GKGpY3XiG8LJO1csKCL_9skVLIKOwVoW6QlM78bPOt9UqpDTcAizvNzXRs1YxV0CMqrfvssWGi3gHOLgZbJxApinNpeCKGsuy2s_qIUKWiwsA7B5oE_bgNixgLvRqf0CiDccC3Ip627v6WZfZFHezRaNr7Yt8w-4qJn6n1GAnU8IPOkFWbNSm9QrT3t4b7erPzmreSmAhOZL5dbFuciUm0DIeKDlsAsogUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d68b609dc.mp4?token=GVL2QDZ5gNT7A-Y1-13EZYLLqXVrfE8o4jjLPC1mMde4Tgv1cYVv3qpVYW-CtbApcRhLyc1BzFQa2hKSad222k3SIHz7awqlQmapeyP_vOnIPGlGA7_GKGpY3XiG8LJO1csKCL_9skVLIKOwVoW6QlM78bPOt9UqpDTcAizvNzXRs1YxV0CMqrfvssWGi3gHOLgZbJxApinNpeCKGsuy2s_qIUKWiwsA7B5oE_bgNixgLvRqf0CiDccC3Ip627v6WZfZFHezRaNr7Yt8w-4qJn6n1GAnU8IPOkFWbNSm9QrT3t4b7erPzmreSmAhOZL5dbFuciUm0DIeKDlsAsogUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب جان ایران
❤️</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/673979" target="_blank">📅 08:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673978">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/388a278e8e.mp4?token=lgm4CmqUXe1Y-pxPEnGiJ6wvpqoTKjMvriLr0WykHJrLjyzPS3ohDTvhlXjn0g8ZrpBVWQ3plYPAjn45rC_XcJfFW-F8Dxa34Y2N77az5xUUlAGIAtJmy2qVs3-zR9O8ftKBne3vBPVJpSOH7ppzpfqAMvJsBMbpgThwx32JI-DDZTv2PaKGHN8N-0q_2pdM6MuWghtXqVv_UKqn3r-g0Ge-N6lG8WTlq1kgD1v80-kfQfEkIE-MiJlIAEXFQqHhlRpEHDjO1_o0S21QGJVCdxEe53RO0_6ePvlHhnzlJEXaecwf8lqDQHiPSOM5GHOlRPNYZzXvo6ZaHgTVtl5WPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/388a278e8e.mp4?token=lgm4CmqUXe1Y-pxPEnGiJ6wvpqoTKjMvriLr0WykHJrLjyzPS3ohDTvhlXjn0g8ZrpBVWQ3plYPAjn45rC_XcJfFW-F8Dxa34Y2N77az5xUUlAGIAtJmy2qVs3-zR9O8ftKBne3vBPVJpSOH7ppzpfqAMvJsBMbpgThwx32JI-DDZTv2PaKGHN8N-0q_2pdM6MuWghtXqVv_UKqn3r-g0Ge-N6lG8WTlq1kgD1v80-kfQfEkIE-MiJlIAEXFQqHhlRpEHDjO1_o0S21QGJVCdxEe53RO0_6ePvlHhnzlJEXaecwf8lqDQHiPSOM5GHOlRPNYZzXvo6ZaHgTVtl5WPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴ حرکت مؤثر برای کاهش درد و خشکی مچ پا #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/673978" target="_blank">📅 08:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673975">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721598e238.mp4?token=hT3iu1DF8u05OCyxljo44CGIHETFtEW1t6kmEkJJ5UDuY7PFHQ0CJeSxoBFGnLiDK_wF-vx7x71nYK9fA0kE2M1RVpKNJJLFCzvBm7eTccPHnz2Vt4LY43JM3wyERIG2HKuOAsD7jPS1taulVlDNJO0yGjnxuQ-RYtsI14KwC3eBWDpxp5zbYGmM2PXS32gIfXSoQJ8irKQKnFHFKUAiyvQckEUnlpct7aVSJLYVXQ__Jl70Ce3qf1jjfAhO8aHEcKwgxPs9tKUj1482OjYc50dP77N77tVVEEQJdzkhVYppZKeo6thAU-_v0pE65zk5iRWZmeY4ZWZcvfKev470yIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721598e238.mp4?token=hT3iu1DF8u05OCyxljo44CGIHETFtEW1t6kmEkJJ5UDuY7PFHQ0CJeSxoBFGnLiDK_wF-vx7x71nYK9fA0kE2M1RVpKNJJLFCzvBm7eTccPHnz2Vt4LY43JM3wyERIG2HKuOAsD7jPS1taulVlDNJO0yGjnxuQ-RYtsI14KwC3eBWDpxp5zbYGmM2PXS32gIfXSoQJ8irKQKnFHFKUAiyvQckEUnlpct7aVSJLYVXQ__Jl70Ce3qf1jjfAhO8aHEcKwgxPs9tKUj1482OjYc50dP77N77tVVEEQJdzkhVYppZKeo6thAU-_v0pE65zk5iRWZmeY4ZWZcvfKev470yIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی پیکرهای تازه تفحص‌ شدۀ شهدای مدرسۀ میناب برای تشییع
🔹
مراسم تشییع و تدفین اعضای پیکر مطهر این شهدا، ساعت ۷:۳۰ امروز در میناب شروع می‌شود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/673975" target="_blank">📅 07:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673974">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
اطلاعیه شماره ۳۹/ زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون در بحرین با چند فروند موشک کروز مورد هجوم قرار گرفت   روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
ملت قهرمان و شجاع ایران اسلامی؛  با توکل به خدای قادر متعال و در هم کوبنده ستمگران، رزمندگان هوافضای…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/673974" target="_blank">📅 07:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673973">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kExtpLglSV1zNJGMOJVxe5v44JNKfgIqYzw2LbOhnphZovd-tiIY-U0n61mcCNnrChZxRCj01D4kK9indi04P1XxyB22mz3Ux8aG3BbhwQomomyoh4ktexMWEcOqFkNUuOIbb1FmdKeFeKozLNAa8qCNar27UsCb-9Gn39YTHnVH9wYlyeBuLXhBOvbD2syNysZaUKy4OWlQsqmYzi_R6LMR4HE_F0_3hP1e9QG_zltGqpmrq2lrKZr6pEhunltPp0RKD5Q5esDjJP37Ek7lJrjRvYoTzxAFHZF8cvyG4Bi_lhuQRaQ9BuSm-CL52pRO6f2aKqHT32eyYbOpw_NFSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۳۱ تیر ماه
۷ صفر ۱۴۴۸
۲۲ جولای ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/673973" target="_blank">📅 07:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673972">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
هواشناسی برای برخی مناطق هشدار سطح نارنجی صادر کرد
سازمان هواشناسی:
🔹
به علت تشدید فعالیت سامانه بارشی هشدار سطح نارنجی در ارتفاعاتِ استانهای زنجان، قزوین، البرز، تهران، سمنان، مازندران، شرق گیلان و غرب گلستان صادر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/673972" target="_blank">📅 07:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673968">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
تایید حمله هوایی ساعتی قبل به نقاطی از استان ایلام
فرماندار آبدانان:
🔹
ساعتی پیش منطقه چوار و آبدانان در استان ایلام مورد تهاجم قرار گرفت، این حمله هیچ تلفات جانی نداشته است.
🔹
همچنین حمله هوایی به منطقه انارک در چوار منجر به آتش سوزی در اراضی منابع طبیعی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/akhbarefori/673968" target="_blank">📅 04:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673967">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
حمله دشمن آمریکایی به بانه در استان کردستان
🔹
بامداد چهارشنبه ۳۱ تیرماه یک نقطه در خارج از محدوده شهری بانه هدف حمله دشمن قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/akhbarefori/673967" target="_blank">📅 04:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673966">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: ترامپ با توافق هسته‌ای ۳۰‌ساله با عربستان موافقت کرده است
🔹
این توافق دسترسی ریاض به برنامه تاسیسات هسته‌ای غیر نظامی و احتمال ساخت تاسیسات غنی‌سازی با مشارکت شرکت های آمریکایی را فراهم می‌کند و همزمان نظارت واشنگتن بر این برنامه را افزایش می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/akhbarefori/673966" target="_blank">📅 04:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673963">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ادعای سنتکام
:
ما یازدهمین شب پیاپی حملات علیه ایران را با موفقیت به پایان رساندیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/akhbarefori/673963" target="_blank">📅 04:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673960">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcrY8LbQrulbdiKPOP4hMQNWqFl8bx-3_BisSWr8FkuM6E1b4RUgKrOXGannc5J_1BYHKteYhG5-jAfrDmJIal99EIvG4UnEaGPgXdWG1Zw57GW9Jdlso4bax2Ru6FRmGWHQRGLHq6F327ZfuEwcDdwQ6Y1z7-0dJbvianPG1O407yhf41FJbp3izJXFtWOEUVT6TShkCOO73b9ilT_ODHpmjP3Qa1MN9Y6mkUZE7H_491tWI8Q08n8fJC0twkuNS5Tzu-98yYS1pFejOyIdufNm4NrBPZCsgc6kqmlRYxCv5QO5dSsGe9E3yAjiFOdKLU9-3hoUwMQ4j--n3GKmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از پلاکاردهای معترضان ضد جنگ علیه ایران در جلسه استماع سنا همزمان با سخنرانی وزیر جنگ آمریکا
🔹
نه به جنگ علیه ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/akhbarefori/673960" target="_blank">📅 04:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673958">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
پدافند تهران دقایقی قبل بار دیگر در شرق و غرب تهران بزرگ فعال شده است و به نظر می‌رسد که پدافند مشغول مقابله با ریزپرنده‌های احتمالی است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/akhbarefori/673958" target="_blank">📅 03:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673957">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
منابع خبری دقایقی قبل، از شنیده‌شدن فعالیت پدافند هوایی در غرب، شرق و شمال شرق تهران خبر دادند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/akhbarefori/673957" target="_blank">📅 03:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673952">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
دقایقی قبل دشمن آمریکایی نقطه‌ای در شهرستان کنگاور استان کرمانشاه را مورد حمله موشکی خود قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/akhbarefori/673952" target="_blank">📅 03:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673951">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd130fc44.mp4?token=UodKWJ1--qy-1yEnArXa--7TqIbmP2PbWn77AYgLBHn_DxROMfaoIDoU8fcOTY4tlT0XXRH0ZNFN_gy7u6H0hLO_c44suhLvmdekQHhIapc3DusUlFY0ezbOgGwvJG3eRKVONhYwgfHDsYu5zQvCHeOShF4OTsPtIsrJgcNTXGfZtqv2WtAK9rBvPjcA6DiIfkeVTygW9zdKXM5othBNvJRM7JhS_TKQCaYk0KIPxeOnP7ioxP30-tHq5lsafJHewUMAL813ZMH272-ZvDLPH13shwkuKesMXcxyOGTkB2wGIcqb-LR_-yWOhULjpZ_lmal5hJ8dL8pyIagED-qCWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd130fc44.mp4?token=UodKWJ1--qy-1yEnArXa--7TqIbmP2PbWn77AYgLBHn_DxROMfaoIDoU8fcOTY4tlT0XXRH0ZNFN_gy7u6H0hLO_c44suhLvmdekQHhIapc3DusUlFY0ezbOgGwvJG3eRKVONhYwgfHDsYu5zQvCHeOShF4OTsPtIsrJgcNTXGfZtqv2WtAK9rBvPjcA6DiIfkeVTygW9zdKXM5othBNvJRM7JhS_TKQCaYk0KIPxeOnP7ioxP30-tHq5lsafJHewUMAL813ZMH272-ZvDLPH13shwkuKesMXcxyOGTkB2wGIcqb-LR_-yWOhULjpZ_lmal5hJ8dL8pyIagED-qCWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعالیت پدافند هوایی در شمال شرق تهران
🔹
دقایقی پیش مردم تهران از شنیده‌شدن فعالیت پدافند هوایی در شرق تهران خبر دادند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/akhbarefori/673951" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673946">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
شنیده‌شدن صدای چند انفجار در تبریز
🔹
دقایقی پیش صدای چند انفجار از حوالی تبریز و از سمت جنوب شهر شنیده شد.
🔹
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/akhbarefori/673946" target="_blank">📅 02:57 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
