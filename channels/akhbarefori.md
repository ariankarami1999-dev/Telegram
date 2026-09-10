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
<img src="https://cdn4.telesco.pe/file/rJD7z0XlXXPABfUIVAiVPexi7Z--2yuzZYrKNh38r-mG_YcikvbgKYYS8hS3ESp0CM5Q3ZVLRmV3iWCKI1lxt1NhKUx_cGQq8QuGOJhmk78eh8QAblExvpFPI2OTBQEmFrpr4dpLrNjbd9w3wbdLfFNTQMcudRPwyZaCH9MyzEdHxNeBVst6cYNbaK27U53zEqy2wI41YWsc4zvhMT-eaXvNUlaPJqCIUNNZ1kwG2U8vtteuyzflKyRoiQ6DUOEnv_apjThdvm-orvoCQgVMn9JxS2P3L-DY5gWJS6yuZ8j0ULyQjBZk3MYrkRuJWvsC9KjAdX1-XnjEArMvjfxsTA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.27M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 22:20:05</div>
<hr>

<div class="tg-post" id="msg-688859">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e56a97930.mp4?token=EJwHTAqM60z4zMS9fUwyn_ZOmUvADfLXDj4aC8mEOmDR_2BcQ8n14z1NXZ6Wks86X6zhtNH4z3F_IHDgtXSX5uH26mWdal0XcdhStQiZe10zCO02AjQm3d6cA3cievZ2D2FCW-eoBeRXo9ezWSN_ZBAD9KMgWTo7kdFRymX07aZRV_Z57r4OWcr1Wak69_FxyxzhTa3SlvUGJ1SdBgzB2Y06pZnxwgNiNhUqVgZMcWGqgDDsBdj2sofAIgHtJYTGUZIx-SVhnUcmHE5l_k4QrRSTHvpwUEyFMfAy8Y9gi-7VMhQwLkGzR8IQf_6TEQ_E8i-l8JA6IO2fueFqN73gTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e56a97930.mp4?token=EJwHTAqM60z4zMS9fUwyn_ZOmUvADfLXDj4aC8mEOmDR_2BcQ8n14z1NXZ6Wks86X6zhtNH4z3F_IHDgtXSX5uH26mWdal0XcdhStQiZe10zCO02AjQm3d6cA3cievZ2D2FCW-eoBeRXo9ezWSN_ZBAD9KMgWTo7kdFRymX07aZRV_Z57r4OWcr1Wak69_FxyxzhTa3SlvUGJ1SdBgzB2Y06pZnxwgNiNhUqVgZMcWGqgDDsBdj2sofAIgHtJYTGUZIx-SVhnUcmHE5l_k4QrRSTHvpwUEyFMfAy8Y9gi-7VMhQwLkGzR8IQf_6TEQ_E8i-l8JA6IO2fueFqN73gTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی دیگر از انفجار در ارتفاعات علی‌الطاهر لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/akhbarefori/688859" target="_blank">📅 22:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688858">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
در پی اقدام ارتش اسرائیل برای انفجار تونل های علی الطاهر، یک زمین لرزه خفیف در لبنان حس شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/akhbarefori/688858" target="_blank">📅 22:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688857">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
وزارت خزانه داری دولت تروریستی آمریکا در ادامه اقدامات خصمانه علیه ایران از اعمال تحریم‌های جدید انچه مرتبط با ایران خوانده، خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/688857" target="_blank">📅 22:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688856">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ارتش اسرائیل اعلام کرد برای از بین بردن زیرساخت‌های تونلی در زیر منطقه «تپه علی طاهر» در جنوب لبنان، بیش از ۱۱۰۰ تُن مواد منفجره به کار گرفته شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/688856" target="_blank">📅 22:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688854">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrUWnZ716Z5dOaE3hSw9jxjAKI8Y_WqHFadWsy7N2FKsC2I9Tpk8YYgrKOPTnnosymOrNUL2fqtK4TKitFoJYPAv6fkIRSO9CO06o2f4TTvPqGn-g0LXToT2EJvDDgA1t1wek_Zpebbpzq3Vks4z0XhJUVqNCIrM3g6ImseUhee9kHX1NJ2rxEDkm6ejWiDXxi3UAM5v3dzLvv4ysLkitXFTTCMdy5YYfbd-rSe-K_eDV21pmMW7lUlHgfhItsSfJPGpyqVh7aZUxvhT7dKlZ1uvbmsQtSzDk7mMmYJGUVIkI2oW4z9fBKrHt83UtxgoyOqMiq3gLF4_N7Q9squD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری / تنگه باب المندب به تسخیر رزمندگان یمن درآمد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/688854" target="_blank">📅 22:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688852">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ارتش اسرائیل اعلام کرد برای از بین بردن زیرساخت‌های تونلی در زیر منطقه «تپه علی طاهر» در جنوب لبنان، بیش از ۱۱۰۰ تُن مواد منفجره به کار گرفته شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/akhbarefori/688852" target="_blank">📅 22:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688851">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
حملات رژیم صهیونیستی به ارتفاعات علی الطاهر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/akhbarefori/688851" target="_blank">📅 22:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688846">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa60631d07.mp4?token=HP6rP2rC1qCYIcbo4YCB_AoFjhOoRP_Q1XRIAZ6FrCvIQzMmXX9FNBMWu5few_DmjL2awwkWWJ8luDhtzf2G8oq3VzrtwrzGZ-KZYVWCENdL_DDePWOcivULVhqM9vuHArpysX6Vb12hbzguYtFPc1xbCw40gIPwDuXRLOSVKXP9TLBKTdHsIRCJbsVYskIGAiHmYatoJ7aGM2UM06Wqx-ryq42eNruEcciK_lLZN33FxNXoSrF6VJAH_RbICJnh7PflLxJ7aL2bysxaYJyQUWK80eCeuJDI1qBS6kzNItlTtbtMwoLAjsBh0_H0fuxKwFIPTLVEKIh3l6AZE2gVHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa60631d07.mp4?token=HP6rP2rC1qCYIcbo4YCB_AoFjhOoRP_Q1XRIAZ6FrCvIQzMmXX9FNBMWu5few_DmjL2awwkWWJ8luDhtzf2G8oq3VzrtwrzGZ-KZYVWCENdL_DDePWOcivULVhqM9vuHArpysX6Vb12hbzguYtFPc1xbCw40gIPwDuXRLOSVKXP9TLBKTdHsIRCJbsVYskIGAiHmYatoJ7aGM2UM06Wqx-ryq42eNruEcciK_lLZN33FxNXoSrF6VJAH_RbICJnh7PflLxJ7aL2bysxaYJyQUWK80eCeuJDI1qBS6kzNItlTtbtMwoLAjsBh0_H0fuxKwFIPTLVEKIh3l6AZE2gVHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات رژیم صهیونیستی به ارتفاعات علی الطاهر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/akhbarefori/688846" target="_blank">📅 22:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688842">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
هر شهر، بخشی از یک روایت ملی‌‌ست...
۹۸ سال کنار ایران
🇮🇷
🔹
کردستان
صدای ایران؛ سرزمینی که باید آن‌ را شنید
و باید آن ‌را دید... در مهربانی مردمی که ریشه در این خاک دارند.
#اعتماد_می‌ماند
#۹۸سال_کنار_ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/688842" target="_blank">📅 21:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688841">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3838521fd3.mp4?token=sHnuYMxvPG1e5n2BiqKjjl6oPmIIxnLG_kTnvirYz1H1RCo_6jSjL8HQdWGbuSnkDf8F4mAJJnl-jKdJEvn7rSKWIX2a-IqeIfT4iwucu_zYRYxkvXIG5TDy978IPZxyC7mpG-f3SzBXix7IyN4fHwO7DijiYdeSg_oguDHP5r4NnYPP1Qico9b88oaIWAycgYIxVVO3Un2l2L7GxybKhRRw5KrE7BcZJlZBQYt_4VsBuxjlakFSp9z4j0G0BFOYGtiPhTJdpPOqMogQY3gfSkXqVUIvh1udKtrlS89hzu28sfbwpebemtHTEUjVsxgAUCBihn65zO7NIh2vUjpcBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3838521fd3.mp4?token=sHnuYMxvPG1e5n2BiqKjjl6oPmIIxnLG_kTnvirYz1H1RCo_6jSjL8HQdWGbuSnkDf8F4mAJJnl-jKdJEvn7rSKWIX2a-IqeIfT4iwucu_zYRYxkvXIG5TDy978IPZxyC7mpG-f3SzBXix7IyN4fHwO7DijiYdeSg_oguDHP5r4NnYPP1Qico9b88oaIWAycgYIxVVO3Un2l2L7GxybKhRRw5KrE7BcZJlZBQYt_4VsBuxjlakFSp9z4j0G0BFOYGtiPhTJdpPOqMogQY3gfSkXqVUIvh1udKtrlS89hzu28sfbwpebemtHTEUjVsxgAUCBihn65zO7NIh2vUjpcBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سازمان رادیو و تلویزیون رژیم صهیونیستی: ارتش اسرائیل امشب تونل‌ها و زیرساخت‌های موجود در ارتفاعات «علی‌الطاهر» در جنوب لبنان را منفجر خواهد کرد/ فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/688841" target="_blank">📅 21:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688840">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
گزافه‌گویی نتانیاهو: ایران بار دیگر تلاش می‌کند تا به سلاح‌های هسته‌ای دست یابد، اما این اتفاق نخواهد افتاد/ نیروهای ما عملیات خود را در تپه علی الطاهر در جنوب لبنان آغاز کرده‌اند #Demon
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/688840" target="_blank">📅 21:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688838">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خبرفوری
pinned «
♦️
خبرفوری / تنگه باب المندب به تسخیر رزمندگان یمن درآمد
📲
🇮🇷
✊
@AkhbareFori
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/688838" target="_blank">📅 21:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688837">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1e7Op67R2r15f_VXGjOOFDGAya2U7Gor8-WhIDwqCkJW-kKhwPznQC4ZXk_AMIeptEAgvs0bEpxfTPSnNPTIxBM5swc5zVw7ABsgRmXNw_bvjpNVKaPKT1kZxbpHzgfF67PPllXIRCkQ_s5RZrEuO6klb7bghtvEfgUhdIIV5-KVRmiUN8SAkpyVnWR4ozfHdN__af-DqINOvJLbgrwPQECSaKTHFC1YAwGkN8LwOGv23KJvzzQth6xdohY4kvQey2qgnwi0B4I6qYfW9PIHC0CVqzkNvqOxrRTwNWwI62hs41IKi7LLAWa7CmRLSwkSpbrufmYKmfN2YR7S7wHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای مجید شاکری، چهره نزدیک به رئیس مجلس: فروش نفت ایران رکورد سال قبل و همچنین کشورهای همسایه را زده است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/688837" target="_blank">📅 21:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688836">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
پزشکیان فردا به هند سفر می‌کند
🔹
رئیس‌جمهور، فردا برای شرکت در هجدهمین نشست سران کشورهای عضو بریکس به دهلی‌نو سفر می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/688836" target="_blank">📅 21:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688835">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
الجزایر روابط با امارات را قطع کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/688835" target="_blank">📅 21:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688834">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
گزافه‌گویی نتانیاهو: ایران بار دیگر تلاش می‌کند تا به سلاح‌های هسته‌ای دست یابد، اما این اتفاق نخواهد افتاد/ نیروهای ما عملیات خود را در تپه علی الطاهر در جنوب لبنان آغاز کرده‌اند
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/688834" target="_blank">📅 21:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688833">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP7K_zD5yVPpgmlP4PKOvKFT84Cm0R4xmV-4yjbFPhRW9to19zoogB-edx4SS3j2xkZudru2YUkdP8ykhunkdikUgx7FqLqIQAWn65J82mQ-0kTEImNVbWNX7TjxO9mKokks7UPHVS36ssPEkMbVg3vuttblY62KSJ16miJwcX1NbGSU6-To73yi247IIP48MU2H72OKihSrIlGfh34BX7ROQUXGVdahSBrb-KXhYnuAci2m1pWObgqTzciOmOPrymNaujo6j3ImP_mGM-rSVbn5kohkMIHWMQ31oO_T_qb1Vj0ro_boJbi0MnFaZ7gVt-5H5oYHnl7599kGoiBQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تایید برنامه جلسه امروز شورای امنیت برای بررسی برنامه هسته ای ایران با وجود مخالفت چین و روسیه
🔹
۱۱ تایید
🔹
۲ مخالف (روسیه و چین)
🔹
۲ ممتنع
🔹
این رای گیری صرفا برای تعیین برنامه امروز شورای امنیت و تایید بررسی برنامه هسته ای ایران صورت گرفت و رای به پیش نویس…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/688833" target="_blank">📅 21:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688832">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49629bf6e5.mp4?token=TmyGFqukrJBosTBCNNIJ8gFNnU419weqVuhz0E6koPAcYSIxIkrr4ek1i7X4uZQffnzFilFY2J6jR35XmzQNDUxwLGVzgua6MsWwBY6T-BW1ABXi6pwSgQ7OlcdwIDxCozIfBdy0wLQ4rZuZG57KwFY2ed4cyh2VZGYSXJTSJFKMY76UBkpiq0-j7o9lRmRICjNXJb8B0hyPvV7iIMczPFyaYzhnmAPgmnnj5MGgHub14fh_1q8BF0NhNIAWSzckYfHISmv5edHfY9TTKfHGNXiuz9SFlO2sDamNAqwV5x-TKBY0ja6KQ_BnS-ei1quIxp91QK_T_SNREV0x1GBJPByM_npHSffdWWKb6yStx9-f68JmnSKlF1oNtKRe8-P7wKXG5DxIl8SrxNgWBGrsEemjfIG9edspUtu_mPuTvMu0qtKaYNE0G0sB3yZMtV2RyUCjq3QoHm1NJ1HNrovqWSfZEXhH3OKR3VF3mrhx_IeuxZmfNM33cPz2NN3-siHhOqbiIBV43HJ2oRi0yFOxk8AAbfF2NwZNB2FFrjnq27OBt2K_CRnO2qhdnR5cYiCeuNpV1ook71VLMDMQwLIsXy415bkKts_tjYO5JhFIexUdCMeLgr6U2TtfLci-PxLSvSvxGTLI2hKMsDcTOjQh-6-AM0_FxGOaDanRZ6O8A88" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49629bf6e5.mp4?token=TmyGFqukrJBosTBCNNIJ8gFNnU419weqVuhz0E6koPAcYSIxIkrr4ek1i7X4uZQffnzFilFY2J6jR35XmzQNDUxwLGVzgua6MsWwBY6T-BW1ABXi6pwSgQ7OlcdwIDxCozIfBdy0wLQ4rZuZG57KwFY2ed4cyh2VZGYSXJTSJFKMY76UBkpiq0-j7o9lRmRICjNXJb8B0hyPvV7iIMczPFyaYzhnmAPgmnnj5MGgHub14fh_1q8BF0NhNIAWSzckYfHISmv5edHfY9TTKfHGNXiuz9SFlO2sDamNAqwV5x-TKBY0ja6KQ_BnS-ei1quIxp91QK_T_SNREV0x1GBJPByM_npHSffdWWKb6yStx9-f68JmnSKlF1oNtKRe8-P7wKXG5DxIl8SrxNgWBGrsEemjfIG9edspUtu_mPuTvMu0qtKaYNE0G0sB3yZMtV2RyUCjq3QoHm1NJ1HNrovqWSfZEXhH3OKR3VF3mrhx_IeuxZmfNM33cPz2NN3-siHhOqbiIBV43HJ2oRi0yFOxk8AAbfF2NwZNB2FFrjnq27OBt2K_CRnO2qhdnR5cYiCeuNpV1ook71VLMDMQwLIsXy415bkKts_tjYO5JhFIexUdCMeLgr6U2TtfLci-PxLSvSvxGTLI2hKMsDcTOjQh-6-AM0_FxGOaDanRZ6O8A88" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش صداوسیما: بهترین برنج را کیلویی ۴۷۰ تا ۵۵۰ هزار تومان بخرید؛ گرانتر نخرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/688832" target="_blank">📅 21:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688831">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7ggwsNu2eN5CK7zZOwcxnFkA16gERCjE3hTw49GdAj03inFKy-OWSzhYcSgDiUUbaWvN9A66m4wabC74IJeJcICodD8PuIFNaE2EJnEiqjvosqpv5vkrtgqGFF82Z699J-cdou1HQB7REjrXPT4MEK4gvJJ3mf-vcNjChs0ERPo9g_OCYI3qjAXjXmhKCW1QX-hN12XGZwfGkM7TnTWOEZDckhz8F-SVPN0N21FvXvwLgJlsryLeMD9g4PDH97kEp0f6yV9ALRtcIdH7J5CurRR723ifU3W-DlZFDu6Sw9GeVTIdgRkHJbSSt4m410_g5QwVf-N0EHFfQiI11aT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تبلیغ سازمان مدیریت بحران کشور در فیلترشکن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/688831" target="_blank">📅 21:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688830">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای رویترز: ریاض از تشدید تنش با انصارالله پرهیز می‌کند و فعلا بیشتر به پشتیبانی لجستیکی، تسلیحاتی و اطلاعاتی بسنده کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/688830" target="_blank">📅 21:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688826">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-PSkUDFfj32rxdMd8FXRfaDB0WwvtBzL9wTHQhy2dedPoSuwDgxo7y3fVRu34xzKHD6mj12OBHB0jqVJ8cXWI5jLniP6J8Ifov0UKKX6nq4iFY3AXHOllB4HQ7GXILCwgGCGVvD4SXjwWDJ67AmIV8YqCE3HJrxJbLWpHrh_Cb8-AI2rLLOWtXQ333LPxqcwikXpYTgtFXmN5jRst3bcUyewzDWGZY8_XTZdUbRE5DG4Dsf4dKughzuuBrRnP1FA37SHNTDbowaw6byIvL1doHQEBky0uwLSQG4Za9Dimbe9Lhqt14z3nySfs6dVsZ1DKApGSIxROHNgl5omxbvGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WA7PgtWoKMCwWOSOUORY4RIOSPQaEUN-gVT2o80rB8ojswBNIlQDZfDeHa5YjWIm0nVeiGbsHPIgOyQXfxazadazhRB0Ab3gh-WTOF6yRTQxzqt0PAESIpetVXisjKDg5VZXGeTCazTp-VuPaCiF6o8pE7VNdPEXMlhOSzQ8LCVjMGxz_8LaxfRmrCi5MxZjtbGa22hEb6TM4fAhEbR8RcIWPjPkTTM2netUc3168Ty954y0j7s8eO6nb0U0vvmutLUtyMJfSek_ktlETKI8tuX2xWByaxJQUI6V0pUNZeK75KPUetLIXAqB5zSHJVTq6XcQKwNXpG2OIWG36JgONw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pX2EICWY2udl72qGFneH__va5sDlD7e96yGS_dac21kGz-P8lSgtTo3AD477A4f79uCHjh-NQdNajE3Vqa_yj-X6cA2q_i6s_DCM7rM3KqtWiBuIr0PbRpzjs6_LFUhWjp8s1Lgwibskf6k78VqJLcFXJEi916OpS-QVTFMH6wTx3dlt_lCdAwACBVMSGB7hBNpsrbX7X_KG_FDm9qGZnw4F6dNa7iMD4QuCkdNxz9irqLW2pL9tSx44TIqS5JL6M3u1VAI3Px752ayTox95EP--HyNqDqs_h8QK1cnueAUWoUZajEwhdADfqI93oVmgvgyhMVgrNqD6RwbxvuEX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/crjOnEKz6FJFacd2zf9xepRQISoOpQBMmSuzZLW31dT6r7pNDMayo_FoktoV_lzu_n9uGhyirInrb-zpmdLsglbE8vyiNmyBk0QIApF91SOCzOPBH2_uKbYB6b-Ym1veAde48JK6Oruioa7ROxLfn86eid9_V9SLQnrOzfMorLapqxSEZ3HX22KLdevuD51SnPVBneOZcNZwn9ESk2JL0RkPILKe8p4-w-U5pvP47yOyGymR0towefh2giLnwerqL1bkvcd8qjY01WSNrgT9GNSVRVYsHx4ChXW5z-wu8Y6ermXDtFC_cm5nqZ82KPBwtuZO1R-Y3sILU3CbORJunQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از پهپاد سرنگون شده سعودی در آسمان یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/688826" target="_blank">📅 21:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688825">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOQbqpG2WxAdexrKOl1i94H0e2xPhIZw4e2lhcd8RBMJuXFn_lvpzkrPBvWTG5gHe8OlwJsptAD4YzFHjw0YegeXspRxwFbui0QU-9XgpwCwlSFQkSro9nfzXHzoJvI-qevQtPBw_m3QOHbnR72tFLUNTP1jQmSy2Cn1ovWI-KOYkm0jEWjybiIjmhqZ_NafqBhFmgIc6qZrr7sqiR3_cpAMKe7IHHUbanh6mGxy3E9bi8eJgSF2Ii2OMHTDKLYdTAMMv9mxq86jQIY-a271n85sLMkubhPuXRauSwe5kJmBZ0IAUd_bfPGct69fasR5h4Rou4pe6VKnP7nN4uyVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ پولپاشی کرد: اگر در انتخابات پیروزی شویم به هر بزرگسال آمریکایی ۵ هزار دلار می‌دهم
🔹
مجری فاکس نیوز: ۵۰۰۰ دلار برای هر شهروند برای هر رای؟ یعنی ۱.۳ تریلیون دلار. رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند.
🔹
ونس: رئیس جمهور…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/688825" target="_blank">📅 20:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688824">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dS40-AEzkPJls86wmy9vDrXRhyMAxw9C0JM5nYZIrWbyuQiOxvaxkNwz1iVjxD9KCDgsGNDj7_lKvvKCYS-App5LhEmKgkCpxHw94a8Xk464k833tQsq-q-L4d-EvO_5d1tOFtJyTB0hPSG31Y1UqQ4CSJbKebJmHRMlLEhCF2BfxZdEhJ3Pxs-fYsxZSwQQVSJcOZATJurlO0NQWM94zLm8GgLOuQLg_BbDYiIwaOHluSLDeKkizzw7oVVKGnMIDev1hjZKvwhI1oZsRuMvJFD8BNdE-rWd8CScGsgwSr8oXVPv3M2k_rJI7u4CW3IHd_LWFQcfvxnTDaumRue7uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسانی از روی نقطهٔ پنالتی استقلال را پیش انداخت
🔹
استقلال ۱ - ۰ پیکان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/688824" target="_blank">📅 20:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688823">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQkgsgiNqyeKtXcs7c32rcyNMBOIlNk8nj1cocoRCfK-cidg08Z7NxU__iWRXoSFJjOgLoixbf950tRdFMs0zNfU-C1Q5vib_GoJKomCgNdRrmy6gEKSD8ytA98f2l_-GeKv2ThoWux0L6kKOByrwciCMz_8PsYcZi11Xwj1wu2bYnUUAYocBB9h1HpwfzcTkM3s78Ks_xxKQK6A1q1FK3HwmckX0WMyT5RdHRoLgA2zXytlpSjtjuLbhJp86HQh425moXOTCxDNS_HxinAvi7gwpe6y5YrTms3rMT833uAL5q9vTlLRE0TshmW2cPFI8680zKZAUpapzADFmuCUEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند ترفند کاربردی اما ساده
🤯
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/688823" target="_blank">📅 20:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688822">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: ایران تولید موشک‌های بالستیک را از سر گرفته است
🔹
به گفته مقام‌های آمریکایی و خاورمیانه‌ای، ایران با استفاده از قطعات ذخیره‌شده، در تأسیسات زیرزمینی مشغول مونتاژ موشک‌های بالستیک است.
🔹
فعالیت‌هایی در چند تأسیسات از جمله مجموعه موشکی خجیر گزارش شده و ایران در حال ایجاد نقاط جدید مونتاژ زیرزمینی نیز هست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/688822" target="_blank">📅 20:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688820">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبرفوری
pinned «
♦️
نیروی دریایی سپاه: یک فروند شناور بدون‌سرنشین (شمپاد)، با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون»، در ورودی تنگه هرمز مورد اصابت قرار گرفت و در اجرای مأموریت خود ناکام ماند
🇮🇷
✊
@AkhbareFori | Link
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/688820" target="_blank">📅 20:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688819">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a73d1b9a6.mp4?token=LjkyrzB2YpcjzLD8LwHK_yhVxrwtjQJp2L-erThJaerevn93xhXZanbnW2G6mbYv13FJJoLGZmswDgo2JTAf1z8MwV0YVHiAEDk9L_tvq8Sp0Bh1ek1DvSCx2ZS-_aOBO4HEH6wkqIoH5vaSvy7s67XcDyGEjwjK0DHmJO4FJnqQRIDds2D0dePxpx91pmAvn-KiSUkRuRvON2xVC7gWNMAtHY92I6sJCwCxWhq4SjfrDF6vQMqXlSb75kys7zWOshIiXHUck4XP0KVzCMUHkIC-EXtGQGv0xVlWmOcLJfu6lln31mBxqy7ni8PB9IsU_Vbt8A36fRqOzEe8vinF0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a73d1b9a6.mp4?token=LjkyrzB2YpcjzLD8LwHK_yhVxrwtjQJp2L-erThJaerevn93xhXZanbnW2G6mbYv13FJJoLGZmswDgo2JTAf1z8MwV0YVHiAEDk9L_tvq8Sp0Bh1ek1DvSCx2ZS-_aOBO4HEH6wkqIoH5vaSvy7s67XcDyGEjwjK0DHmJO4FJnqQRIDds2D0dePxpx91pmAvn-KiSUkRuRvON2xVC7gWNMAtHY92I6sJCwCxWhq4SjfrDF6vQMqXlSb75kys7zWOshIiXHUck4XP0KVzCMUHkIC-EXtGQGv0xVlWmOcLJfu6lln31mBxqy7ni8PB9IsU_Vbt8A36fRqOzEe8vinF0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسانی از روی نقطهٔ پنالتی استقلال را پیش انداخت
🔹
استقلال ۱ - ۰ پیکان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/688819" target="_blank">📅 20:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688818">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ایران به ۹ جنگنده آمریکایی در اردن آسیب وارد کرد/«سی‌بی‌اس» گزارش داد در پی حمله به پایگاه موفق‌السلطی، ۹ هواپیمای نظامی آمریکا هدف قرار گرفته و آسیب دیده‌اند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/688818" target="_blank">📅 20:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688816">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
انهدام Saildrone آمریکایی در تنگه هرمز توسط نیروی دریایی سپاه
🔹
نیروی دریایی سپاه یک فروند شناور سطحی بدون‌سرنشین آمریکایی از نوع Saildrone Explorer را در محدوده تنگه هرمز هدف قرار داده است.
🔹
باید بدانید که Saildrone Explorer یک USV حدوداً ۷ متری و مداومت‌بالاست که برای مأموریت‌های شناسایی، مراقبت و آگاهی محیطی دریایی (MDA) به دوربین‌ها، سامانه‌های ارتباطی و حسگرهای مختلف مجهز می‌شود. این شناور پیش از این در منطقه توسط ناوگان پنجم نیروی دریایی آمریکا و Task Force 59 به‌کار گرفته می‌شد؛ یگانی که مرکز فعالیت آن در بحرین قرار داشت و مأمور توسعه شبکه شناورهای بدون‌سرنشین و هوش مصنوعی نیروی دریایی آمریکا بود.
🔹
پایگاه دریایی آمریکا در بحرین در جریان جنگ هدف حملات ایران قرار گرفت و از رده خارج شد! اکنون Saildrone توسط یگان مستقر در محور خصب عمان استفاده می شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/688816" target="_blank">📅 20:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688814">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cqepock_Rg18rrY2i6aOTguipPuuR1oEszFuiUmZBwXPk804A0DdZ8aiy011Rg09DX1VXNext6l3OBqixfWLnlt9sJlQtszN8_ycAYdBlWD22Fdm-uw_qjYUY1V0rwAUCUP-d4ruGwWLnudOdVY-EYqzHd6QCmS3qS-G7s-aqB3dOKK5CJTErTOJMQfgP3kjm8qbhKEDSBF8If3viov687w9_b2uodaU0orC5WAUTtPzfsBte7RZ2zGLO89hc2Tg4qym-vA_OoVWCDkIxpcA4zPCkBgGyiUdWha1QdCIBPyfDXjsFGrSD8-DM6RO2yPfMOBzIIS-L5K5XkqYzI2Bxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5800849858.mp4?token=kisHjy4nN7_TgPSfLtGgMgjRPVZwQ_tA8aw3yBEBTou_szG6zHGtRDtE8WWtCenPCkvEO6EoZ34wanNxi6nPJB_A-h2I1vz6QyNv3ZXYAhKnOyMUGZ_rugE3RnZUTccfFjEFQ-gEjdqleQZpCxuYxJhsLLlwEV1OiF6MLgGhtYkUfw3XX-Nyq1DrG9AscAENp5aAAuaK_1E-4Wqoe8V3sR-UtnLPV0qU3yCZEVDKdjY_mgZ2PWD73jrFQbzXX1FtyksfSvItAKKjVR8T8Bi_m5ICVvdEPDTLA_C4wDEHpKlGOauQ1iO5vEyCrmTWaQKxK6zDQS24SuJBwzbadUZBKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5800849858.mp4?token=kisHjy4nN7_TgPSfLtGgMgjRPVZwQ_tA8aw3yBEBTou_szG6zHGtRDtE8WWtCenPCkvEO6EoZ34wanNxi6nPJB_A-h2I1vz6QyNv3ZXYAhKnOyMUGZ_rugE3RnZUTccfFjEFQ-gEjdqleQZpCxuYxJhsLLlwEV1OiF6MLgGhtYkUfw3XX-Nyq1DrG9AscAENp5aAAuaK_1E-4Wqoe8V3sR-UtnLPV0qU3yCZEVDKdjY_mgZ2PWD73jrFQbzXX1FtyksfSvItAKKjVR8T8Bi_m5ICVvdEPDTLA_C4wDEHpKlGOauQ1iO5vEyCrmTWaQKxK6zDQS24SuJBwzbadUZBKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروی دریایی سپاه: یک فروند شناور بدون‌سرنشین (شمپاد)، با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون»، در ورودی تنگه هرمز مورد اصابت قرار گرفت و در اجرای مأموریت خود ناکام ماند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/688814" target="_blank">📅 20:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688813">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
نیروی دریایی سپاه: یک فروند شناور بدون‌سرنشین (شمپاد)، با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون»، در ورودی تنگه هرمز مورد اصابت قرار گرفت و در اجرای مأموریت خود ناکام ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/688813" target="_blank">📅 20:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688812">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zn_h7em29E3aqMKckjfoztL_iqstyHmrITyz8x5u4z198bnBFseWLylHqsbBOCz7d5QeZfygWJ66JLthQE_yS3kFNlXEAULxKHJouYZIbw03joa9ef6BhbSXFVVLgKna83J6xguPmT5fPvjj7782n6KfOdpX9nKhaaRubfU5V1b8qT7dy0jlEfzXdDAFUgG2quwP-uqNJ6HBidDnOfqK1p3Hc89tX43sgNhPrGJfwD4YgiiFTIgR4_j_qVTZxzinnwh631hjQWy0MTLnPEdglx8bJNqkJZRI0ltmphSWcYZXE2zTHKi4ktPFohQUxTqIaf4Bey5QBXkD9EELFCKYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: مداخله‌های مالی و یا حتی دروغ‌های خزانه‌داری آمریکا دیگر تاثیری در مهار قیمت نفت ندارد
رئیس مجلس:
🔹
اگر دنبال یک راهنمایی برای آیندهٔ بازار نفت می‌گردید و مقامات اقتصادی دولت آمریکا چیزی نمی‌گویند، بیایید به آینده نگاهی بیندازیم: وزارت خزانه داری برای کنترل قیمت نفت زرادخانهٔ ابزارهای بی‌اثر خودش را (از قبیل دروغ‌پردازی با آکسیوس، مداخله در بازار، آزاد سازی ذخایر و…)خالی خواهد کرد ولی اثری در کاهش قیمت ندارد. این نمودار را ببینید ولی وانمود کنید که نمی‌دانید مرحلهٔ بعدی چیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/688812" target="_blank">📅 20:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688811">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT5GPiCi6RonlURR0g61OPB-MDtQFsDoXNsQAKvfOtZptEfMYabKMWREb1m_A029ntLwUqz-ZO52ww74G-PiAJMaQNaewSEh1DpzGasYNevnjYN73YueJbj0QDeQ2JqAmEExDRkT3JFpnb2HD1cFVUKufjNYc6_zTT6zlheXseQu7Ef4z2XjNAPbl_rV96io5lJLHWM2YQV_78gxHGINBS8G7V8M4rtHMHrzWgdYRvf4QJeYFKzZmJ5inoxkEQ0Sr7SNeJwhOBM5djm6Ta-CRfAtmXCHRRvOTeKHVUOW-b39h60OaPQUr_DBA_AWHVUzlF1XgMRqo9xByHXLM04OMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسکن‌های رایج و کاربردهای آن‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/688811" target="_blank">📅 20:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688810">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
نماینده چین: ایران به تعهدات عدم اشاعه پایبند است؛ ایران عضو ان‌پی‌تی است و از حق استفاده صلح‌آمیز انرژی هسته‌ای برخوردار است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/688810" target="_blank">📅 20:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688809">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">14-2 Ane Manaee (1404-01-30)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/688809" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه چهاردهم؛ بخش دوم
حجت‌الاسلام امینی‌خواه:
🔹
مرز انگیزه‌های دشمنی، از حسادت و رقابت تا جنایت؛ ..و وعده‌ حتمی عذاب الهی برای براندازان! [00:00]
🔹
کشتن ناقه‌ صالح، مصداق سنت الهی در زدنِ ضربه ناگهانی در اوج امنیت و بی خبری! [08:07]
🔹
معکوس شدن نقشه‌های دشمنان از یکسو، تکفیر خطاها و پیروزی مؤمنین از سویی!.. به شرط «ایمان و عمل صالح» [09:40]
🔹
معیار اصلی قرآن در تفکیکِ "حسنات" از "سیـّئات"؛ تناسب با مسیر بندگیست [13:51]
🔹
پذیرش و تبعیت از وحی و ولایت؛ رمز تکفیر سیّئات..و این یعنی «ایمان و عمل صالح» [21:08]
🔹
وحدانیت و نبوت ریشه همه "حقیقت" است، مستقیم یا غیرمستقیم [26:50]
🔹
"نصرت خاص الهی" سهم باورمندان واقعی به "ما نُزِّلَ عَلی محمّد" است، نه مؤمنان نیم‌بند با ایمان ظاهری و سنتی! [30:42]
🔹
راز شکست‌ناپذیری جامعه قرآن باور؛ حذف پندارهای باطل از جان جامعه است و اتصال به حق ناب [35:12]
🔹
«مدرسه تعالی»، تجربه‌ای زنده از نصرت الهی در طوفان بحران‌ها، برای متمسّکین به حق و باورهای مومنانه [40:28]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/688809" target="_blank">📅 20:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688808">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
شعرخوانی جدید میثم مطیعی علیه حسن روحانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/688808" target="_blank">📅 20:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688807">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
روسیه در شورای امنیت: اجازه بازگشت تحریم‌ها علیه ایران را نخواهیم داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/688807" target="_blank">📅 20:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688806">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
وال استریت ژورنال، بلوف ترامپ را رسوا کرد: کاخ سفید نگران مقاومت ایران و طولانی شدن جنگ است
🔹
رئیس‌جمهور روان‌پریش آمریکا، ساعاتی پیش گفته بود: فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام خواهد شد. چون آنها (ایران) دیگر نمی‌توانند دوام بیاورند.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/688806" target="_blank">📅 19:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688805">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/du_VD9qA4NRlzHtzKUGo6uMaQyJ_Y4e1L3osNTeIzd44DPHLgZQb7PlqU3UYzcL9rD7iHHWmEqg_kHjhekGzk13UWLILqk7uDKzdc7zWYutysOw39qF9d59NIVtuO61N_bzriG0ANMmEiEk02o0djxSHb3wbwzR1Y1w_16wzuQs7rKHUc4NXVe9ds1f02sY6Zpt9yyD5xyFAMTaEJ7bDMPWihcCTTd5JS6oMebK92lA1hf3mGGm40pgyig72bXy2TjLA9gta3-hBKuTf08iVnaCok-vDX3xSnx-x4pP-aSlt5_XbBTJowywhsf-p5WVcBfw_llu01F9zenTKiWsxHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جورج گالوی سیاستمدار و مجری بریتانیایی:
«من به تناسخ اعتقاد ندارم، اما اگر باور داشتم، دوست داشتم در زندگی بعدی یک یمنی باشم.»
به توییتر خبرفوری بپیوندید
👇
https://x.com/Akhbare_Fori/status/2098079423224528944</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/688805" target="_blank">📅 19:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688804">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/932929d910.mp4?token=hY5hUbeTce4XwWRzp2ug_laMyi8Y65Kqg2UhN2gvG8WAb40onMdueLk8rnCKeqsxuVTwCNuo2HIBlgO_1dkiqRBIYuuVyTcGLLBEmDdEfqTDRs3uXCD36P9-jpI4RNa4_ZCZ7zk6bHySFzUgxZjJy5SZAWJtQqUJsbaBjpf7c-J5CPLYgedCQXuPypwAtSvQgYEe3ZB_uoI3oCkAZ0dq3Vh3QX3Eavnpoph6T0nY5Uxn5MwIPJE7KrcVRS2WNSB7x49fQuQZ8qLNDX1EHjIeoxFJqTysJY4E5nmutsRZgjUl2BTvuqLDvO-OEhKNzeoFkKX_zVbakwdFD10pURlZJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/932929d910.mp4?token=hY5hUbeTce4XwWRzp2ug_laMyi8Y65Kqg2UhN2gvG8WAb40onMdueLk8rnCKeqsxuVTwCNuo2HIBlgO_1dkiqRBIYuuVyTcGLLBEmDdEfqTDRs3uXCD36P9-jpI4RNa4_ZCZ7zk6bHySFzUgxZjJy5SZAWJtQqUJsbaBjpf7c-J5CPLYgedCQXuPypwAtSvQgYEe3ZB_uoI3oCkAZ0dq3Vh3QX3Eavnpoph6T0nY5Uxn5MwIPJE7KrcVRS2WNSB7x49fQuQZ8qLNDX1EHjIeoxFJqTysJY4E5nmutsRZgjUl2BTvuqLDvO-OEhKNzeoFkKX_zVbakwdFD10pURlZJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گلایه شهروندان وان از پوشش برخی گردشگران ایرانی
🔹
در مصاحبه‌ای پربازدید با شهروندان وان، برخی از آن‌ها از پوشش برخی گردشگران ایرانی ابراز نارضایتی کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/688804" target="_blank">📅 19:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688803">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d1799c58b.mp4?token=EDLALg4vho0FZB3Ofutk6_5SI-pLgCuz0CiLf1-fX7TeaE6lqAGR71bB1Ftfc97yBafGwZbY9hTc788oM6QNx5B0XZLrVbR4N5UjFqkG0PHabM_bp4hizCbCuyu09TmnDrYKPsmqkbwUa767k-kWyyRyMKh6Rg4yDz_ltyvV2j5fbSLZDIS_laOGSmW2TIh5vKJk1VUj0Dvkoj68zaEonoaO8xycJHJZEf5k1D6S4BvBQKI8tzMpEzJhchU6PrqxRxp4z861ja4FgoMsumrM1YbhuAIINv_iSe1MuZ8FHSQilnIFTFJftVFwthRlt8FIvfCWyG6sJj9on-u-R51UtxT9xE8-h90eHmJpbJwIRfPwyT5dSkn8V8XdvN-EflBNf_ou2PnFKbOEIKr1uA4Wu3CFbn-VhokaSwkmMdR95vpWZd3fx8bCdxgr-RdWc-1CjfpeuY1gsyd_w-60nHGQbAuikcSk6Cg5z1AJald-eCzs9RAvgJLKw3k5OZqo_2HxSbOZOOZKQxF3dpgUZ_s4RtufbMNxH9UbqWlV_PUiMhGRdSK5deM7lZHgjdrmKW7h7pmAcV9YO5doluCLeKLXSmr5AgkpHRJYwBUQsrQhyeCb5f7TcMNou4bbAV804W3UUx61O23HsG8TYivTRpfS2m9ruRYVEaHjq4zcusQ8QPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d1799c58b.mp4?token=EDLALg4vho0FZB3Ofutk6_5SI-pLgCuz0CiLf1-fX7TeaE6lqAGR71bB1Ftfc97yBafGwZbY9hTc788oM6QNx5B0XZLrVbR4N5UjFqkG0PHabM_bp4hizCbCuyu09TmnDrYKPsmqkbwUa767k-kWyyRyMKh6Rg4yDz_ltyvV2j5fbSLZDIS_laOGSmW2TIh5vKJk1VUj0Dvkoj68zaEonoaO8xycJHJZEf5k1D6S4BvBQKI8tzMpEzJhchU6PrqxRxp4z861ja4FgoMsumrM1YbhuAIINv_iSe1MuZ8FHSQilnIFTFJftVFwthRlt8FIvfCWyG6sJj9on-u-R51UtxT9xE8-h90eHmJpbJwIRfPwyT5dSkn8V8XdvN-EflBNf_ou2PnFKbOEIKr1uA4Wu3CFbn-VhokaSwkmMdR95vpWZd3fx8bCdxgr-RdWc-1CjfpeuY1gsyd_w-60nHGQbAuikcSk6Cg5z1AJald-eCzs9RAvgJLKw3k5OZqo_2HxSbOZOOZKQxF3dpgUZ_s4RtufbMNxH9UbqWlV_PUiMhGRdSK5deM7lZHgjdrmKW7h7pmAcV9YO5doluCLeKLXSmr5AgkpHRJYwBUQsrQhyeCb5f7TcMNou4bbAV804W3UUx61O23HsG8TYivTRpfS2m9ruRYVEaHjq4zcusQ8QPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین مسابقه اتومبیل‌رانی که ممکنه ببینید…
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/688803" target="_blank">📅 19:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688802">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
بلومبرگ: قطر برای خرید گاز مایع از آمریکا مذاکره می‌کند
🔹
دوحه به‌دلیل محدودیت در تأمین گاز مشتریانش، در حال مذاکره برای قراردادهای بلندمدت خرید LNG از آمریکا است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/688802" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688792">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WRtrh1kXj4oQLCrqFBoGZp4TqOMvLBVcnMEs88KtpyMAhItVAUfKIVhKWLB0rFotSS2Ffe7radqkXDv0Sq0nwkHIHGALpV7aBLMI55pA632SwJMZmWRdon0piXJ4wWfwDEcdXjyEF9fsP9S8xjirFsYCmlWIxuniFvzeqV3OG6nHjFp9nzCXyCzWe_RFIMuaNwcOucADR56rcp3o-ZAwwDwtBCPgLC4n32bOT49qW49OoLq8VIu_GWkJZ0BLrZDkfD64gLzJehwEMwOZFIafmoOFWGUZBgAJ0agdtfs53P6hKXhDYNUZD3ZGCfb5N1AsT6odaMZzugX3nuaDfMjqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMGOg_M-cfqT23sWL0kZdzw508i2sH8LpixbCZ7wMGVh7EMef0hlaxGp2iMTpbLmI4k5z9kaQoaaAFJesSgtzKDs0l7iEAiM0_McdHxdw3fppXy2FnuWlptFsx59qEj1CmIkkcbM2rdbqyR2EZuHlPumB-vl8S9t7fjIejk6nByG0oOZw5DOqMLKkeYge3fxrCwIn5r9owiB0ce_-dsCIKwtAaKM2mrg5e6F8oSfw4oqhOQCPQ-FBKdquBrvKQ4nOzfS9JnmFVCZ_IOfs0dtMFrwZeVblpFx4L29K7YeRNjM1EeJ8K4r65jfK8DCfjKqGD27pMDv0NvzSRinXbKnYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eHqJozsM3ijWx_R6lHd2AhGmXY2Bty21H48PLjo4-wU_MLOb1B8fZuZ9yWDf_txJB4mue-Iy8DLAjFBLRoNVAipHeo6bEgjkuORug-EWFJ2zzFR1V-kmgKUSMb8pLbzi2yaSTVqgsNoulnwDk4x7PDncUv1IjtgI9mFPjQF-kfnTQDuUjFLDQjaaHuJdQcnNzkAMzlGGZfqYECDqqMvvRckn4o-6e_Uvh8G8GD7DdFnf4zrnXNLJB22wYpdMXP-z9M7f_ujsiT5q1liqDhGGSTexdjFvIcW1jP8feDpuf95OXPKlwsX8NDMMLW6lSUDJHZPNhf9hl2c3vfMCIEoMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBSGBVYm3dByG7zU8dHRgmLAx0Yn0ha5uAqNVREG852fqpgo2M-HoJ0mV1-2tsmqiV-qzqVoDjlT2Tsoq12v9AySQqzzUoID3W2ziaLCDbset6tbL6wmhhu-woOkl8wHxnwPouA0PNxs2qjol_tsOaFUVyLXN8rqNVmSKY-rT8b2hmyhDf1ZdCfdcWuPLgqJ64vkx2bcZnNsaQncpf2xW8J76ii3cvY4sMiku_y-PcAL8-jeh_GLFiQE1wfj36_IYMoeuvvnTQK1bCI-L7yE9Q8cG6-00TOK0MTmbSZGwxl_12zeitqJ86TcfmrlNZ3lkKs72Ke9hAtKtSmxjeD1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxoTnqZA0QW1eZ_owFhNxUMiD1EHB6fOcdy0LdLenduzCq-TdklmhcDqftw8YTWDivsnALhsFodEMzCkiM4wEX2Z1YyK6dZtsxrQQda6S53U1nEK77y_uxUdlLB4XQ4sETYCQsKQnWTNr34PbgAXJ9_p2MgVlY_f8XH-jud6Vkc0i3uzT6OawlOyjyV8fR-gXtZb2Gn4FY4ow4o-Q8wNUjpjOqFoCZioilSMEWyf8B3Htt-CbAM7GO831xdViyEsGjhMLDm8mldob8Z2UcI4hgoIdAyYlsnwhHdWPerIs6Vv4WS9OXy3xxSBFCwsYWIJbgvKPdrmZHaVZByY0qfdEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uyz9NsdFQDLZjmxrjDMadu6rYaAUGq2rEb9WEsLerRfgbt8zMxJ-Y2Hk8Wcqfoe-tvgzIBW6aCaaotbFuEynEQvqYb2iJnyTyJjqP10U8SG12TwLD9LgwQMM6r1evaFXBWu3yAywvou-mFpuVX8vkovLyNU7SOVAEjzB0x6UB_aOoQcYiYeSZxgDhLnlGFS7DrDKuI93BgYoMvrOfc8e2MlN58YkqJBFwQdhA6ynxAG7ScHzsijY0dGXu6YvGZMAFMTLuQHkxM6zgZEd-Og25qaDVfONhc7ypyl39rzXqsYcBkDg6Onj5uoU45pxSBBr7fobYNYfxS57GMK5TgFmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRpVXOk_Nem-r07G14isSx_80L-kgH7CPTfoX77jXY2JYUZtTO-5FW0hCvdrTNJ0OBlM_9cXTULpVqToBFdYxYp-ujp3STxjegyXDai8VQd7PbG6XJJ-wJp9YcI7515X91FQsJaBBEppRy68uqG8Ft7gZwrxhH67SafagOwqO3aKKaVX1RJwDpJg3YBZJeCuLI-zaPpHlLiKQGN8CSMIj3-wRP5A9iqymFNXzRUOCJa2BcvSMaxRnxZjtHg-p2DDTT9FL-lN5A0pQMqackbR9YIbA-mbudnqt5UUscSvDMIjewoam462YDJNqkcmNmKGZWQhxe3D1gZP-U7euXq3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gEjf0-KRiCnH5oOmtTjk72K4gDOiTCxHUvY8hlRf_-wq5rc2K8VbYukhSYP8K7tlUUpubv0mbENty8ojZVic3A1iqRwQJnpntxa3chuWTtNm_7H-rrDfFYqgNVgzE5m4AhMdEzhtAS0B3ibY4BI-mEUE16C3LYITdGxS-u09ddlhSPpDqOIB8Gn7aUETVv6JPcXqg_TegSvRvl9hpduNPpf4_-zI4YWXwntaTYALpUsqucL0--XJ8BdgBID08FpYPWocMhJGd17S4RKGdWFU84bEe1TyEJrnMrT_kJgE2zPvpKhs50aRSNXWy7_9uI_fhgpJajmZj6v3eKc1F2vbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMlBj_ciNlcWJDCMXHCmdvTm8HycoRnxhNy9OCCp5J2afogLn1b0TEuNYnlRPXgHSqsv25dmI_YgFXIYsttmKeEqrSF8ovnR0fx0X4UTHNxRNF1Zkj33kdZvKJI242ItAsYqgUrvQcBrJ53YeUTUrzOTVvue3494OIqqhKH3_QYTOBW1coGFCb_CZYPv-i6SBZdSSKYI1HwwyjzDY7PZLMKPf88dhMHm1ZCfvbMNdNfXcVtT_dnLbjqcsFj3IzSbG4Lms-Md1_iq0WWl5fsoDlOa0H-pXVIKeehzpebc1Hi_zQToub225dwsQDUQYULrjG4zK-Z-_aZ-p7n7JzBxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVNzLhqM_IT4gaFSpU05B9iRenM9SQnMt3I8DHqBIuD3WY6mVcMn673cbdmYuLt3VApx2Eon-WM92JLY7oEyZlzu5mK3MwHqa83nqIIAy07Mzdtt2fltqYuT6ROTpEQ9B8_0t1adNI75jqY-ht01C-2QuVe6ejZdDvANgyceCU3sNvaXB3Aur7Ne8cvbz7O8eBwRfU0x8TeMKAgSVfAb_d8dYhMYi9i1fsao0G_nbFZ-Bw2qhCMA1wmsWYFlhi_uE-OwtI1jBY6nq96JGuDz7z7uxKijHaUnU28NkUanZF_rab0EBJPr21o-E9-OmUsvdFYmJHWQ_3j6eWAt-N4cIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
صدای شما از رنجِ مسیر درمان؛ بازتاب   تجربیات شما از گرانی، کمبود  و جست‌وجوی بی‌پایان برای تهیه دارو.
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/688792" target="_blank">📅 19:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688790">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tjv32zKrZJOLMO-0WGaOv-XlBE2lSE4o7yI4wYKOZh54J_emC2s0ZFzAE0VnKwPLzDQj9TYXjnnEG37KKY7uJsrpjoLTxsGW9nK7B9s-Af-yelUDb6D3k9XSUXZPrRMqKAN3wi1E554hDBun7jke1dKC2Bs4TXSjHAWW96DUYRqIXsG_rSnV9cY62vZXj315mKyiDXSr8MgsDB0NFUw9C8-L-qQmgicfus5jEDsFCPNt36OPcHxueLi8dWxpIQVQiDeHQ__hkCjMRCfC-SLqFcm8z3UAnezOtu72HLDdne6rOe3yLBcNOAcoB2tsr7nObemYZBS_Io2tanNR7LMr4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EGsxxc2jotgDCfbDQtR8pct37d3gMShCT5gNEONXQ91eiF-MRO0NgMF7196fanlB9iKZd9g_L7zLkZA5X390ddCoX_O1DQXz-c9oLxHP0UI2o1h1S7LxmL6u76-D2DB0lT9ppk7nB7Xzq8QFC6oytcPPGzJpovhyYGF54rSDtwe9ToKqAVmMhcRBTdtFWySgpUim0E_h93k3biyvWBeFcgk_2H_btG3zjyeSOGG5cHfMG7Em-r2CCGicntPMG1nrZNy0Ah8ljwwMrN7soA8qv0u3XgkE-PrJ7XrDDyMZ28iBKOAQg32tZcaQzXdcH9VYajHcDtjqrIfhD77ht9EOuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کاظمی: محمدباقر خرازی در بازداشت به‌سر می‌برد  سخنگوی قوه قضائیه:
🔹
آقای محمدباقر خرازی با صدور قرار قانونی در بازداشت به‌سر می‌برد.
🔹
پرونده وی هم‌اکنون در دادسرای ویژه روحانیت در مرحله تحقیقات مقدماتی قرار دارد و تاکنون منجر به صدور کیفرخواست یا رای نهایی…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/688790" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688789">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzwLsL8Lq66_87cqae9v_83iIDREGN6uB9701VI29CX1MshpNhK8zG1Ee3B-EcV1XAePvAL0KXAaGcemaOi-qB26qFe4z_mRoh3KEZhbQdVBuFtGu9F3ZiU-qNK7IpkUxQb4_96gFVIM1YrGY-0eqam1YGIamkln3CcXqHqWxJk9FuI_fDHHRsGaBlVjYgP_nErvEz6bD_OqahlMcBk20KWirP3ZsHz8oEe4lg-lCS1b2b5vpBxcafnhOe9jg8xjY-2wHafcwMJTyvkSWLUeBMNNo5_JJ2N_6BLtQJjDFcABpny2IcTHLoNI_xy5S07mcDGHEKFnhbUoPv49YXbSgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ پولپاشی کرد: اگر در انتخابات پیروزی شویم به هر بزرگسال آمریکایی ۵ هزار دلار می‌دهم
🔹
مجری فاکس نیوز: ۵۰۰۰ دلار برای هر شهروند برای هر رای؟ یعنی ۱.۳ تریلیون دلار. رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند.
🔹
ونس: رئیس جمهور…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/688789" target="_blank">📅 19:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688788">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtsD5jAQBtEiAg9YO_x0L1oB4XNKM8zrrPWbRCL8EBwxGTUKEw34zM7w4rKBtdImDDDC_0I-RRvgXtqsL_IbKtHlHT3gb1VbDKBKb2Je5EiPTVO5O-KFHTrYou1Xv74oCq3ypGGCf6lQoScc93sATnA9-Q0BVITTezFSUXSDtCg5KLylyRqmXVssTwaXSNpB3DaURKZ1C_Pa0hfb7M26LHUn8_SJGD91Tdkrft875XFivrZNg1M9NrR-mYDtGjt-M_1yB1P_gSlgDXMlPZuW450NNzBt3aDjnUM8tZ656N-p4uzNwMih0iwZx8BV3p-Co4b137BkoW0QCtnHNxNK5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه الحدث عربستان نیز اعتراف کرد جزیره استراتژیک پریم به کنترل انصارالله درآمده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/688788" target="_blank">📅 19:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
وزارت دفاع: به زودی گوشه‌ای از کوه‌ یخ صنایع دفاعی ایران را می‌بینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/688787" target="_blank">📅 19:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
اسلام‌آباد: اقدام نظامی فوری در واکنش به حملات حوثی‌ها مطرح نیست
پاکستان:
🔹
با وجود پیمان دفاعی با عربستان، فعلاً هیچ اقدام نظامی در واکنش به حملات حوثی‌ها در دستور بحث قرار نگرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/688786" target="_blank">📅 19:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6296a1f0.mp4?token=BSErNBlyqV31GRmeIhnlpe8mQwfFJP4H7DVHBTn7oG1Gr4U3C0cNDhFk09P8-YzlBT-ZNydJySITntzO_kYD_HgPL1kLMbbh0D312XYQ1g2ekkzVSi5UKD-6b1vxL3ifqn_0Dh8jQr_ZKSc3tZa2a_I9eifQ3aARLrGChgMAQ6iuhZXty07GuX20ogiJNB-wetiOAwcPyYVyayG9wbfAVBWFNwRxqmKYGfYMLaerqyFnz0vui9pP55xOwlXpH-QLZ7EtydcOWKZ2UhNArLQCqJKrZBRJYfrInJKRFknjNA4G5Rr9z-sYiW2Auqjh7MDg4LN5nV-Pwx4VOfoSj4T2sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6296a1f0.mp4?token=BSErNBlyqV31GRmeIhnlpe8mQwfFJP4H7DVHBTn7oG1Gr4U3C0cNDhFk09P8-YzlBT-ZNydJySITntzO_kYD_HgPL1kLMbbh0D312XYQ1g2ekkzVSi5UKD-6b1vxL3ifqn_0Dh8jQr_ZKSc3tZa2a_I9eifQ3aARLrGChgMAQ6iuhZXty07GuX20ogiJNB-wetiOAwcPyYVyayG9wbfAVBWFNwRxqmKYGfYMLaerqyFnz0vui9pP55xOwlXpH-QLZ7EtydcOWKZ2UhNArLQCqJKrZBRJYfrInJKRFknjNA4G5Rr9z-sYiW2Auqjh7MDg4LN5nV-Pwx4VOfoSj4T2sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار احمد وحیدی: خدای ما خدای زنده است، خدای غربی ها خدای مرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/688785" target="_blank">📅 19:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga6LVrZmUsWYnL1It2-akUlMTc86P7qKrf7rU2I_U-xynDHL43_riXF8dz6hoCLXG1mO67javcK85-ds0WnWApKqARDdvy0qMNduj44MlOAWDi9CmM81Yhmf6Lxg9gjQmBYsRX_HQO8nkdI0vJCR__MI8nYJd-4mtTSWxufaeDu7VVgCsJgv0CZhC0fQqxliAbsztD5LPtUsy3GM4VDPOntYdnwe1qp1U_i8bzUmtJQzWuNVkZZlUiq-8FhdKDK1YdvdWep6ZpSUejVzPSnyxB2LMkicX9dqpeHJphO8Q-UbWydVNkIjy3y5Y-N0afP-DoXOXfdvVEtE0NPeEklr9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حسین افراسیاب به ۳ سال و ۹ ماه و ۲۰ روز حبس محکوم شد
🔹
حکم بدوی این خواننده رپ، به اتهام داشتن استارلینک و با تشدید مجازات در شرایط جنگ، ۵ سال و یک ماه حبس بود که در رأی نهایی به ۳ سال و ۹ ماه و ۲۰ روز کاهش یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/688784" target="_blank">📅 19:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
تحریف واقعیت توسط نماینده آمریکا برای پوشش شکست تحریم‌ها و تقابل با اراده جهانی  نماینده آمریکا در شورای امنیت:
🔹
امروز باید گزارش ۹۰ روزه از وضعیت هسته‌ای ایران ارائه شود، اما دولت ایران متأسفانه دسترسی‌ها به مناطق هسته‌ای را مسدود کرده است
🔹
روسیه و چین…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/688783" target="_blank">📅 19:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
نماینده چین در شورای امنیت: اسنپ‌بک به پایان رسیده و شاهد غروب برجام هستیم
🔹
تلاش برای بازگرداندن اجباری تحریم‌های سازمان ملل علیه ایران، مانعی جدی در مسیر حل و فصل سیاسی پرونده هسته‌ای این کشور است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/688782" target="_blank">📅 19:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ht5JYUNEJR9K9Bz085JS8I_lJyr79L4EU-2pxreGHmTtB2oCssq0P8tPQy9eTSdkqBkv53OTYB22ZDm2L4pCe1FwTIRw0n5kQam2U47Rk1iGcGcPziwZMfDRgTHHqnEkJ1LArfddINbMIyvFc8ytoia9fuDRJiZueg4ImF38bDYDrsh2z_VEDrxRdr4dypMalEI-d5EZukv4Lg7bp5g9kybUOHrAcDEBoTqg5yNZmJ8lAL8lV891NdKSyBPkwWQqKNGRTLwS_D8cUHhas9Z4jLM7_lPb42E4NFN9fEmMOENBD3cQ_MKAlldOP5bRMc_1WBKHIcpkIbCJIB7cCU2h2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ پولپاشی کرد: اگر در انتخابات پیروزی شویم به هر بزرگسال آمریکایی ۵ هزار دلار می‌دهم
🔹
مجری فاکس نیوز: ۵۰۰۰ دلار برای هر شهروند برای هر رای؟ یعنی ۱.۳ تریلیون دلار. رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند.
🔹
ونس: رئیس جمهور…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/688781" target="_blank">📅 19:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aieqp0Kg97Vi1Ec-8KzTcEUYe3Sb1fcIOyqPEBPZ_10Zcq7ZjX3u5_sXFt3_c6I3IDd-vCNEVl-xnig8w8YXDAIiBQEnYFHg2NmFEAYEx5-WqTz4lZKuDvPzHoikVQz_f6hPKbW0smV0SJSW7nW9kB8TNoTbB3dqn6wXUcLrWDEUeN72bzJ4X6W2oOA6exzb812J0jWIEYrUfPc2QoBaoQYaBAVFEsSN2nOAX98Gt9Vrkmfjt0qZDFFwNyD-lq4QKHy1PTUCgBIAk6kJcGaNcA3SP62oASxV6vNMGna0loTVr_XOyuPWKK5A_jfSKZwh0ky2iUz9zWTJWeVJhKLWIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال استریت ژورنال، بلوف ترامپ را رسوا کرد: کاخ سفید نگران مقاومت ایران و طولانی شدن جنگ است
🔹
رئیس‌جمهور روان‌پریش آمریکا، ساعاتی پیش گفته بود: فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام خواهد شد. چون آنها (ایران) دیگر نمی‌توانند دوام بیاورند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/688780" target="_blank">📅 19:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688778">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBUjtJuDV-ld2lImgUmxIzMSI6RKrbtMSD2QIqdowH_S3u6SyrShLhe0j2MXEHsyvHKVPjtgqoa3dtBm4YedkbXqLDPvMHCY0fLhis6zM8-SqM2QmmAiG3ITVlx0e8bQhWCbbXBR-il_XCP47ETIJBDZs6BKVFnaiNXcoduo9O_xKVv-ziCvrhbbTI7-6LKSoMpYj67CLWdACP1C_7vJ4Gewh5gdjBFUsy95huep3kXQlv7_FfXQM0uWM7fxDSfmUum6-wmZxdbAKYD0vWYmD4k1JwFKYcYh_TB738d_IsQIyTmXSFNK013lVlWopy6gyqCGQfwqbVVyTRtTfWebdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GR0dv3-6nw_BzFadokBjhvaSdcpb2qmha7DC1K6Q6uFXPUVpOtktEit4nzKRFh4ZIC_0AbYzc3JmEhvW3ZFKAjCB-F1Lk2e5fKNiuAdYxGtmy1kZ33LIbIJgjgtuMU5z29TSVu_6tBoxXvCE4FaP_dwAxe5c5BBwdZ2JbFrN0TY3osYCAjiEl_Kon-yOHXVYfkrWX8JkK7KDf3AFwA0Km1_3EANxA8Ot0sOPYH3w_FrwpUClQOIbSBgpv8yS0FTUujGrDb05aESHI3Mu1DHdqVMKSyG50qflUAxv2sdubNaB2if5gDo_FLfBJoheWEc0GWaFvUNh3VZ-B_0pj0x3Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پلی که در جنگ ۴۰ روزه (اتوبان تهران تبریز) توسط آمریکا مورد هدف قرار گرفت، بازسازی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/688778" target="_blank">📅 19:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688777">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a112479587.mp4?token=XfRi60RwoJBluObESLpROMmfYCR5EZ3aeiQbbSzsSvG0VrkgNwsTv7zzyMZ9ItsUO1cpE36VuoZfsajQ46V6k0v2Ai7gr2JPzBbQSqUd3Sou6EEKYmaA93yNqhNXLm427UbipT3WWUF_eGtoSXehFfUrSHUEApvIq-9ze2ZpLGF9P90UZmAba39vzp8JfjzPf-bHLpNXFxbRIjE3OtbARd77I7wYomw8yC570TQ1JCSV4TtGNf_Uwg0EPJVuxK6GqjJS2CHjl0T6yaCMc0H0HlSdShfh8ayi5QDzJQIR9vBGQtSC9CSZRUpHd50dd8u8hyv3OfcqMDw-qt-equMxPk7G_uvpT_zJ7ac7tx8Z6feTwkwhDpaR__gY3gR0R9fdO6IMeco5nwnuh2e1WjsN4fsGW6XhAah68YBapgIVyc47bO_LIb7hpbr29-Su7ell_QaSQb1hmb-S8IT16pOEbMjCw3uC8-0rckhkq7HtV2ts4F1CoOsjtP12yT8Aos_R4qnAuTpGedS1CoDCWl3UzSTeSlRxB-8KdnVd9MKj0Ufl68uQhjYVgpqRENcAG76qaAprXjjuc4TlOqvJz7MwlTdV1d3P4RGpaCls5qbYneNiLOGQckmYByWJK3ZCTcs3pBgtfuXUMSt4k3OydbR90at5YMxfU2Hzw7iJQPKF12A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a112479587.mp4?token=XfRi60RwoJBluObESLpROMmfYCR5EZ3aeiQbbSzsSvG0VrkgNwsTv7zzyMZ9ItsUO1cpE36VuoZfsajQ46V6k0v2Ai7gr2JPzBbQSqUd3Sou6EEKYmaA93yNqhNXLm427UbipT3WWUF_eGtoSXehFfUrSHUEApvIq-9ze2ZpLGF9P90UZmAba39vzp8JfjzPf-bHLpNXFxbRIjE3OtbARd77I7wYomw8yC570TQ1JCSV4TtGNf_Uwg0EPJVuxK6GqjJS2CHjl0T6yaCMc0H0HlSdShfh8ayi5QDzJQIR9vBGQtSC9CSZRUpHd50dd8u8hyv3OfcqMDw-qt-equMxPk7G_uvpT_zJ7ac7tx8Z6feTwkwhDpaR__gY3gR0R9fdO6IMeco5nwnuh2e1WjsN4fsGW6XhAah68YBapgIVyc47bO_LIb7hpbr29-Su7ell_QaSQb1hmb-S8IT16pOEbMjCw3uC8-0rckhkq7HtV2ts4F1CoOsjtP12yT8Aos_R4qnAuTpGedS1CoDCWl3UzSTeSlRxB-8KdnVd9MKj0Ufl68uQhjYVgpqRENcAG76qaAprXjjuc4TlOqvJz7MwlTdV1d3P4RGpaCls5qbYneNiLOGQckmYByWJK3ZCTcs3pBgtfuXUMSt4k3OydbR90at5YMxfU2Hzw7iJQPKF12A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوربین موبایل‌ها روز به روز عجیب‌تر میشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/688777" target="_blank">📅 19:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688776">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⚡️
𝟲𝟬% و %𝟳𝟬 تخفیف تمامی کالاها
در جشنواره پایان تابستان «چرم مَنطِـ»
➕
𝟮 میلیون تومان هدیه خرید حضوری و آنلاین با اسنپ‌پی
با کد: 𝐏𝐀𝐘𝐂𝐖𝐆𝐙𝟓
در تمامی شعب و سایت
👇
🌐
manteofficial.com
با اسنپ‌پی بخر، 𝐁𝐌𝐖 ببر</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/688776" target="_blank">📅 19:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688774">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
روسیه در شورای امنیت: اجازه بازگشت تحریم‌ها علیه ایران را نخواهیم داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/688774" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688773">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
روسیه در شورای امنیت: اجازه بازگشت تحریم‌ها علیه ایران را نخواهیم داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/688773" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688771">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097198224.mp4?token=AVnIz22RucUHIAM0QNJjFhW6kUm7pWJsytfZIPwHZYNJBL3kg7P5HNKp4H0Q07UAPz9AzqFtQg3ysUxj_6VoH3NcQ7FYvtvXpKNXDxf6THP_LYH4RPVD5ifDGruQ3McLFXqY6mNRy8nMiO87AaHeOLwjLB1Tf61p2Z0B6W0-2n2Ya3ccxhENzuaxr7nff0OoPjAjnSJjt3_kL6Bd1muIqV1iBYYoB22RHmq00qUY934o-mMb6Nn_IEyq1AdXKtFtW3uDKIYhy_5L86cg96oAKwrd2PfgBMjgE16RSWDGmZEoFTfazRife-ot5oEc_-LnXuszI-IxJqVjt5GSAFu1cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097198224.mp4?token=AVnIz22RucUHIAM0QNJjFhW6kUm7pWJsytfZIPwHZYNJBL3kg7P5HNKp4H0Q07UAPz9AzqFtQg3ysUxj_6VoH3NcQ7FYvtvXpKNXDxf6THP_LYH4RPVD5ifDGruQ3McLFXqY6mNRy8nMiO87AaHeOLwjLB1Tf61p2Z0B6W0-2n2Ya3ccxhENzuaxr7nff0OoPjAjnSJjt3_kL6Bd1muIqV1iBYYoB22RHmq00qUY934o-mMb6Nn_IEyq1AdXKtFtW3uDKIYhy_5L86cg96oAKwrd2PfgBMjgE16RSWDGmZEoFTfazRife-ot5oEc_-LnXuszI-IxJqVjt5GSAFu1cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحریف واقعیت توسط نماینده آمریکا برای پوشش شکست تحریم‌ها و تقابل با اراده جهانی  نماینده آمریکا در شورای امنیت:
🔹
امروز باید گزارش ۹۰ روزه از وضعیت هسته‌ای ایران ارائه شود، اما دولت ایران متأسفانه دسترسی‌ها به مناطق هسته‌ای را مسدود کرده است
🔹
روسیه و چین…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/688771" target="_blank">📅 18:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688770">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خبر بد برای آقایان؛ خانم‌ها در رانندگی با موتور و ماشین قانون‌مندتر هستند
مهدی قمصریان، مدیر عامل صندوق تامین خسارت‌های بدنی در
#گفتگو
با خبرفوری:
🔹
با توجه به شرایط اقتصادی و اجتماعی، ضریب استفاده از موتورسیکلت توسط خانم‌ها در جامعه افزایش پیدا کرده است.
🔹
باید در نظر گرفت در صورت رانندگی بدون گواهینامه، هیچ حمایتی از راننده مقصر آسیب‌دیده صورت نمی‌گیرد و این موضوع می‌تواند به رشد چشمگیر آمارها منجر شود و رانندگی بدون گواهینامه، خانم‌ها را از برخی حقوق شهروندی از جمله برخورداری از پوشش‌های بیمه‌ای محروم می‌کند.
🔹
به دلیل تعداد بیشتر آقایان، ممکن است تعداد حوادث و خسارت‌های مربوط به رانندگی آن‌ها بیشتر باشد اما بر اساس مشاهدات، خانم‌ها در استفاده از خودرو و موتورسیکلت، قانون‌مندتر رانندگی می‌کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/688770" target="_blank">📅 18:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688769">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
دبیرکل ناتو: مین‌روبی در تنگۀ هرمز به ما مربوط نمی‌شود
🔹
موضوع مین‌روبی در تنگه به قلمروی ناتو مربوط نمی‌شود. البته ما آنچه درحال وقوع است را زیر نظر داریم و کشورهای عضو ناتو از نزدیک با یکدیگر هماهنگ هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/688769" target="_blank">📅 18:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688767">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
بشارت به مردم یمن و غزه؛ باب المندب آزاد شد
🔹
خبرهای اولیه از ورود مجاهدان یمنی به جزیره فوق استراتژیک میون در باب‌المندب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/688767" target="_blank">📅 18:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688766">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A__2GQ-_XjtsPwTqWpzqBOjHbMxB4F_rHKvRzjtvAHmORkT-m9TDS1cajxZ3C7iVbt04uKuDfa8X2I7kKuUb7tVrCRItT7HyBd_0SfwsekLmGPPMKYi74C0LUbOGMkLVD1mQKv3LjQngCIcptMCOD8U36lQVx6JVtThVu0DvDVBbV_FXbrKkXKvYFAP3-2Rqrj1DLgaEKBFmnjaL1X0vlAegtekZqmpfgUY_GHudjBq8ajh84FH96fURt2DA7YdFFGP_lIclkKUF7ceFIARO7wLCL_RJ-AV-USaZs0ERaW6mxQSntesc5hEa5hys5zYfcqVXbmbuhA3-_leuxDh0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدیدترین تصویر از آیت‌الله جنتی که امروز منتشر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/688766" target="_blank">📅 18:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688765">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
برخی منابع رسانه‌ای از حادثه امنیتی جدید در‌ تنگه هرمز و وقوع انفجار خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/688765" target="_blank">📅 18:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688763">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
سکوی تجاوز آمریکا به ایران در جایگاه شاکی / نماینده بحرین: حملات اخیر ایران نشان‌دهنده عدم پایبندی به قوانین بین‌الملل است!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/688763" target="_blank">📅 18:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688762">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
طرح دوباره ادعاهای واهی علیه برنامه صلح‌آمیز هسته‌ای ایران توسط نماینده انگلیس!   نماینده انگلیس در نشست شورای امنیت نماینده انگلستان در شورای امنیت:
🔹
ایران به فعالیت‌های هسته‌ای خود ادامه می‌دهد و از تعهداتش فاصله گرفته
🔹
ایران تنها کشوری است که بدون داشتن…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/688762" target="_blank">📅 18:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688761">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
تایید برنامه جلسه امروز شورای امنیت برای بررسی برنامه هسته ای ایران با وجود مخالفت چین و روسیه
🔹
۱۱ تایید
🔹
۲ مخالف (روسیه و چین)
🔹
۲ ممتنع
🔹
این رای گیری صرفا برای تعیین برنامه امروز شورای امنیت و تایید بررسی برنامه هسته ای ایران صورت گرفت و رای به پیش نویس…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/688761" target="_blank">📅 18:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688760">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f3228749.mp4?token=F0L6ccX6Brnehh_dYr4tlLaoIQbZ5fulnprySqZ7-pQxiY8g-rteVSfb5Qw92-elFzZJVYNurA7fr24paed_1Iw5tlzllPKqXT3P4CKKcXSQRX9CamSUqIfsPtqEm9-xzOKtm0iNBAxX4cOMuyUqRVLwq_oD-ytdJioifUsb4aoCa_fKvGSJiXD-CzNnvhCwdkz054T0yj0A1XBNF4kQM0BZmAllfH5DxLy9Yb6zQVupIqummEeap3i7N3n0s-TBrsaGQ37F62hP16CMNDziaRkyU4ku2KlLYYD_132ZlLAX3nhpW23Uu-ENB0Oywyp_-BTGcn7th0LMjksDGDHWRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f3228749.mp4?token=F0L6ccX6Brnehh_dYr4tlLaoIQbZ5fulnprySqZ7-pQxiY8g-rteVSfb5Qw92-elFzZJVYNurA7fr24paed_1Iw5tlzllPKqXT3P4CKKcXSQRX9CamSUqIfsPtqEm9-xzOKtm0iNBAxX4cOMuyUqRVLwq_oD-ytdJioifUsb4aoCa_fKvGSJiXD-CzNnvhCwdkz054T0yj0A1XBNF4kQM0BZmAllfH5DxLy9Yb6zQVupIqummEeap3i7N3n0s-TBrsaGQ37F62hP16CMNDziaRkyU4ku2KlLYYD_132ZlLAX3nhpW23Uu-ENB0Oywyp_-BTGcn7th0LMjksDGDHWRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترتیب ماه‌های میلادی را یاد بگیر #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/688760" target="_blank">📅 18:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688759">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
تحریف واقعیت توسط نماینده آمریکا برای پوشش شکست تحریم‌ها و تقابل با اراده جهانی  نماینده آمریکا در شورای امنیت:
🔹
امروز باید گزارش ۹۰ روزه از وضعیت هسته‌ای ایران ارائه شود، اما دولت ایران متأسفانه دسترسی‌ها به مناطق هسته‌ای را مسدود کرده است
🔹
روسیه و چین…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/688759" target="_blank">📅 18:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688758">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d4cd9b0a.mp4?token=cG14hY6lcm3cgFdxEuJVX3ERIbnVM9J7N3AJ0Jawp5Tca_fE8k9HaX8xmbpaOAROs_4obEKk2c49Z-AbcvXGxxaQQ7EKzRMwboLqUaYZWkfQZa2k3uv3m0JaYXBOoByrnl6PvfWKqhPIqukxGA5ISLRGEPW6Da5-clU3KuinJBKRviIBTznlqCQb8zwCb2YbdsF5vgw-OWw6kUCrTlZ3DUFtUDKKBxBnMyA-O5bpWx71c96aKiOQKjrRbO99Zp-f2PH6yYymJwgUcbV5uRSXhhfxXffOcWw61c9jaFSgavpOcNp66FSthpUYL0xo3OOM3QhdIl9arSjZqydABShVFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d4cd9b0a.mp4?token=cG14hY6lcm3cgFdxEuJVX3ERIbnVM9J7N3AJ0Jawp5Tca_fE8k9HaX8xmbpaOAROs_4obEKk2c49Z-AbcvXGxxaQQ7EKzRMwboLqUaYZWkfQZa2k3uv3m0JaYXBOoByrnl6PvfWKqhPIqukxGA5ISLRGEPW6Da5-clU3KuinJBKRviIBTznlqCQb8zwCb2YbdsF5vgw-OWw6kUCrTlZ3DUFtUDKKBxBnMyA-O5bpWx71c96aKiOQKjrRbO99Zp-f2PH6yYymJwgUcbV5uRSXhhfxXffOcWw61c9jaFSgavpOcNp66FSthpUYL0xo3OOM3QhdIl9arSjZqydABShVFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر دفاع یمن ترور شد
🔹
منابع یمنی می‌گویند محمد العاطفی، وزیر دفاع دولت نجات ملی، همراه با شماری از فرماندهان انصارالله در حمله هوایی به غرب تعز ترور شد.
🔹
انصارالله هنوز این خبر را تأیید یا تکذیب نکرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/688758" target="_blank">📅 18:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688757">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22e2097cb2.mp4?token=SutpOgL8Q-P83efMsI4OLRlQ-MrH0DXbJbDHjuzDW_4gjnuMr_TfM2E2b18ZBmBED3rZAM0Bp9G7fDTB2QRRZjnk9e94eahOjUkXPcYp6EH_CwphmzHP24vvZTu6HVHRIzH65pXUke7ce9avTIx1r7uMV4RuW5jkm88mqIB4Flr-M1I56r5vah0lV1tYIUmT64ZI08ybo28RXLm0vYf6cjqBpyEv_AQFg-rBob12H9ZuBFAtMi0uC-SHAXCwoYZJEDGaSYeEyccKDb5YJb7IUoNeA6sxos_W08hCQEEFoE4KtKV9FCOdBLNL3vHxEGFYmpyiKl8lz7PYi39vqeftVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22e2097cb2.mp4?token=SutpOgL8Q-P83efMsI4OLRlQ-MrH0DXbJbDHjuzDW_4gjnuMr_TfM2E2b18ZBmBED3rZAM0Bp9G7fDTB2QRRZjnk9e94eahOjUkXPcYp6EH_CwphmzHP24vvZTu6HVHRIzH65pXUke7ce9avTIx1r7uMV4RuW5jkm88mqIB4Flr-M1I56r5vah0lV1tYIUmT64ZI08ybo28RXLm0vYf6cjqBpyEv_AQFg-rBob12H9ZuBFAtMi0uC-SHAXCwoYZJEDGaSYeEyccKDb5YJb7IUoNeA6sxos_W08hCQEEFoE4KtKV9FCOdBLNL3vHxEGFYmpyiKl8lz7PYi39vqeftVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحریف واقعیت توسط نماینده آمریکا برای پوشش شکست تحریم‌ها و تقابل با اراده جهانی
نماینده آمریکا در شورای امنیت:
🔹
امروز باید گزارش ۹۰ روزه از وضعیت هسته‌ای ایران ارائه شود، اما دولت ایران متأسفانه دسترسی‌ها به مناطق هسته‌ای را مسدود کرده است
🔹
روسیه و چین می‌خواهند قطعنامه‌ها را نادیده بگیرند و با وتو کردن آنها از ایران دفاع کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/688757" target="_blank">📅 17:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688756">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
مخالفت قاطع روسیه و چین با تشکیل جلسه شورای امنیت درباره تحریم‌های ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/688756" target="_blank">📅 17:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688755">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
کرملین: اوضاع در منطقه خلیج فارس در حال حاضر مطلوب نیست/ طرفین خویشتن داری کنند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/688755" target="_blank">📅 17:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688754">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4fd80c3cf.mp4?token=rK4fta92g78xKlqRo9f_mUNCOCbhgIT8Nz8E6HiIZ2dxi8vAzy8kj0ab2VSqLwr6Uf-ShWlF1vgiVPfiPCE5rwuT3haNuh5USpmtznZ8FvtOR3IaneDav5Uqg-fzlkmoUg-5KFOYRwgXlqFp5gYjWDiO9A5uHah81vk-gEqtKnaEQ1PQvpNqyK_bvN3rqWTq8NipfbYDcq-TNRxJzSEMOGVtCGL5aFZRGmDW3qX760SY9xdSKeZzDTxr9kVGy9wwB8Jq3LbqqW2Hqpr4lYV6jFuQ1VrNR5FClSVE0YvpDocLTcpOguDOhKUvOcTRvMj1t5lD-JfHyLnCa8fq-ZCSCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4fd80c3cf.mp4?token=rK4fta92g78xKlqRo9f_mUNCOCbhgIT8Nz8E6HiIZ2dxi8vAzy8kj0ab2VSqLwr6Uf-ShWlF1vgiVPfiPCE5rwuT3haNuh5USpmtznZ8FvtOR3IaneDav5Uqg-fzlkmoUg-5KFOYRwgXlqFp5gYjWDiO9A5uHah81vk-gEqtKnaEQ1PQvpNqyK_bvN3rqWTq8NipfbYDcq-TNRxJzSEMOGVtCGL5aFZRGmDW3qX760SY9xdSKeZzDTxr9kVGy9wwB8Jq3LbqqW2Hqpr4lYV6jFuQ1VrNR5FClSVE0YvpDocLTcpOguDOhKUvOcTRvMj1t5lD-JfHyLnCa8fq-ZCSCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربۀ‌ کاری انصارالله جهت افزایش تسلط بر دریای سرخ، جزیرۀ زقر هم آزاد شد  خبرگزاری‌فرانسه به‌نقل از منابع یمنی:
🔹
نیروهای مسلح یمن پس از تسلط بر المخا، جزیره راهبردی زُقر را نیز تحت کنترل گرفتند و در مسیر گسترش نفوذ در سواحل دریای سرخ هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/688754" target="_blank">📅 17:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688753">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6fae3b6a.mp4?token=aR1ApDvjTx56nsIOyPiubjQxKuqL49mKUqWgdj_8e4Pru6nv0-EWNLN0o2zD4WUrBJq8w4xq3120aBF4QLtXHwyckCO9rvOgok3aiDM6_a5nSJYeAiD4n06aGGTE0mSapCSdgxzAqzcM-O_k85qWZw30MAhACGt6CZJx-XAXYeP-5-6MaSwzEWvKLsT3V0mGFkVDJpouCVe59PPGFeN_2ErGC2rXwTqHDXiZN3vcYmCPX1OlJUZ4mrKEEIco6XlPMfnf1DY4lkwvsT_iPLUkr00bEfUneeVIpJrJ7lfSLhSdP7FmZFgvVS276kbfXQJlqdgDwJTN8QWTZ7352GNthw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6fae3b6a.mp4?token=aR1ApDvjTx56nsIOyPiubjQxKuqL49mKUqWgdj_8e4Pru6nv0-EWNLN0o2zD4WUrBJq8w4xq3120aBF4QLtXHwyckCO9rvOgok3aiDM6_a5nSJYeAiD4n06aGGTE0mSapCSdgxzAqzcM-O_k85qWZw30MAhACGt6CZJx-XAXYeP-5-6MaSwzEWvKLsT3V0mGFkVDJpouCVe59PPGFeN_2ErGC2rXwTqHDXiZN3vcYmCPX1OlJUZ4mrKEEIco6XlPMfnf1DY4lkwvsT_iPLUkr00bEfUneeVIpJrJ7lfSLhSdP7FmZFgvVS276kbfXQJlqdgDwJTN8QWTZ7352GNthw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیلاری کلینتون: ترامپ قهرمـان المپیک دروغ‌گویی است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/688753" target="_blank">📅 17:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688751">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R87IaCAv3x-rRTOP3F579zyiDMCEbe_E7nkGMUnbBuuimbsvcfjN7A41QZfRz2pIqDg28_wtpCEo5FwsVuimar6drmf5vWXecSDexI0DAg2lKpxC6KZrOK32vi8t33pMVHjWcWxRAZXeODlBgjkw3FbjUCxHfaiKw4jNEXXjNs_E2znQj1yeWRpngm1lmCZcF1jFIntwy5BH7glJYk-3LtA0w46PqsbFLGfXtnhj3O7kpV54EMNViSl_TO8MhXIOLRD1o-430Uq54K0ZQ1bfdX3Zs2IBegRK_zDVMGVSDSocKr2H-c-7mcusFFR232qBMPaN5HjqbskwaQ9J-xP0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فروپاشی ناگهانی در جبهه جنوب غربی یمن | نفت عربستان در تیررس تحولات ساحلی | چرا عربستان وارد عمل نشد؟
🔹
خطوط نیروهای مورد حمایت عربستان سعودی در جنوب غربی یمن طی شب گذشته و صبح امروز با سرعتی قابل توجه دچار فروپاشی شد؛ رخدادی که معادلات میدانی در امتداد ساحل دریای سرخ را وارد مرحله‌ای تازه کرده است.
گزارش تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3244244</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/688751" target="_blank">📅 17:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688750">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
رزمندگان یمنی دو جزیره دیگر را آزاد کردند
🔹
خبرگزاری رویترز به نقل از منابعی دولت وابسته به ریاض نوشت که ارتش و انصارالله یمن بر دو جزیره «حنیش الکبری» و «حنیش الصغری» در نزدیکی باب‌المندب مسلط شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/688750" target="_blank">📅 17:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688749">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
نفت برنت برای پنجمین‌بار امروز تغییر کرد و به ۱۰۵ دلار رسید!
🔹
بعد از خبر کاهش تولید نفت عربستان در پی حملات یمن، قیمت نفت در کمتر از یکساعت دو درصد افزایش پیدا کرد و هم‌چنان درحال افزایش قیمت است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/688749" target="_blank">📅 17:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688748">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
با دستور عارف، معاونت حقوقی و علمی رئیس‌جمهور مأمور بررسی طرح نفوذ شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/688748" target="_blank">📅 16:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688747">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2367c9e480.mp4?token=E9NuJySRHqo9EDTFR5vl5sHM9nW2PtKdONA8a6-O9ciTDjShOpNek8FU4WI_jMnmC3_wJsFONwi9MTrXfhenSRWwiEy4DWa-LlVRDxS1toKlfV5YFgMeFbpRz5XBSSBn-_sVvDebCATA3UaNE2iAfkif8BUVuaatayGUqhjmpk1KCQhWl61AEicCrrYB4wzaKS00ObUzqjpX-Nvzcz-0oxmdbtHFdGj1tadYWqGESQAvRZ-8IqG8LBmjGa4WIytuJZrIEVHrqYX-qgldSRCHgVDNz22w8aqw1uQRKtFvTe3-7U2Khv0OFexX15mDWRmaXbR_Okp0mNnbVp-aL87LAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2367c9e480.mp4?token=E9NuJySRHqo9EDTFR5vl5sHM9nW2PtKdONA8a6-O9ciTDjShOpNek8FU4WI_jMnmC3_wJsFONwi9MTrXfhenSRWwiEy4DWa-LlVRDxS1toKlfV5YFgMeFbpRz5XBSSBn-_sVvDebCATA3UaNE2iAfkif8BUVuaatayGUqhjmpk1KCQhWl61AEicCrrYB4wzaKS00ObUzqjpX-Nvzcz-0oxmdbtHFdGj1tadYWqGESQAvRZ-8IqG8LBmjGa4WIytuJZrIEVHrqYX-qgldSRCHgVDNz22w8aqw1uQRKtFvTe3-7U2Khv0OFexX15mDWRmaXbR_Okp0mNnbVp-aL87LAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غمگین‌ترین راننده قطار؛ مردی که در متروی بدون راننده چین فقط نظاره‌گر است
🔹
این خط کاملاً خودکار است، اما حضور یک کارمند در کابین توجه کاربران را جلب کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/688747" target="_blank">📅 16:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688745">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73fe73d6bf.mp4?token=INv1mQqkAAsDvsXIoxZZS6PHs1CURF2Hx7oimP2jJdtut2M86TxhYWYvoM9cPXh80Qvav1hB_mYVixv6_XNwyWmj4ustrBq-NjJYWcxvkenHt2QFj8oBzgmGADhG911-yzRpR7EBLb7DqJYlpL42_4gyNgmNwoe41_CeeeAk97Fdp9pFYw5orQIe5WQh3C78eP0MvRz2D4UsO7uCynKjuK_CrP6vh0jpVTXjOV_3V49PrsNZgIOpwvirfRhObFAdUFcjyMF0bOFUBrhGVjfHjccKKqBHGVqOBpr4jIi7tTKvi2Mii1Rk6QNNKSZ4AJNwBU9e6R4IcAs2SqIoA1lZTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73fe73d6bf.mp4?token=INv1mQqkAAsDvsXIoxZZS6PHs1CURF2Hx7oimP2jJdtut2M86TxhYWYvoM9cPXh80Qvav1hB_mYVixv6_XNwyWmj4ustrBq-NjJYWcxvkenHt2QFj8oBzgmGADhG911-yzRpR7EBLb7DqJYlpL42_4gyNgmNwoe41_CeeeAk97Fdp9pFYw5orQIe5WQh3C78eP0MvRz2D4UsO7uCynKjuK_CrP6vh0jpVTXjOV_3V49PrsNZgIOpwvirfRhObFAdUFcjyMF0bOFUBrhGVjfHjccKKqBHGVqOBpr4jIi7tTKvi2Mii1Rk6QNNKSZ4AJNwBU9e6R4IcAs2SqIoA1lZTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربۀ‌ کاری انصارالله جهت افزایش تسلط بر دریای سرخ، جزیرۀ زقر هم آزاد شد  خبرگزاری‌فرانسه به‌نقل از منابع یمنی:
🔹
نیروهای مسلح یمن پس از تسلط بر المخا، جزیره راهبردی زُقر را نیز تحت کنترل گرفتند و در مسیر گسترش نفوذ در سواحل دریای سرخ هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/688745" target="_blank">📅 16:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688744">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ورود گردشگران خارجی به کشور، 90 درصد کاهش یافت
محمدعلی فرخ‌مهر، رئیس اتحادیه هتل‌داران تهران در
#گفتگو
با خبرفوری:
🔹
ضریب اشغال هتل‌های تهران در شرایط فعلی به‌طور میانگین حدود ۳۵ تا ۴۰ درصد است در حالی که در شرایط عادی می‌توانست به حدود ۶۵ تا ۷۰ درصد یا حتی فراتر برسد.
🔹
ورود گردشگران خارجی نسبت به گذشته کاهش قابل توجهی داشته و بدون احتساب کشورهایی مانند عراق و افغانستان، کاهش گردشگران خارجی حدود ۹۰ درصد است.
🔹
با احتساب گردشگران عراقی و افغانستانی، میزان کاهش ورود مهمانان خارجی حدود ۸۰ تا ۸۵ درصد برآورد می‌شود.
🔹
کاهش پروازهای تجاری، محدودیت رفت‌وآمد و شرایط ناشی از جنگ از عوامل اصلی کاهش حضور گردشگران خارجی و افت ضریب اشغال هتل‌ها است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/688744" target="_blank">📅 16:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688743">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfHvheihOxEGoGnuCbdviF4Rj8kQ8X2qnuDNOpRRXeS9U6tF6blHUTDGuXSEt36ck_LzD_QNyW5ayibhNt1vGoq9ePy3tLCwseC7JQtuvJFRvxKLApidqMoYy5v_v3dC0f97JaUKp1llALcICYrMnoPPKSBnIjLHC6W-ueBXltB8Nlt7SYEmbbJ5hB9o5aqpBpBrgGQNn5sz2oT3GGEr5pFfHokFtPvqzGOEaEDoJw_d5ThPNHmuEgvGM0k9kRErxQLAkKqsj_ln1e8lxZ8Ac9C24aiXYV2xNbtVypVuKftftwIxu0Bfd-jShWxwLMXUSXOwPWP2i6d-I9c8FuOR-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بشارت به مردم یمن و غزه؛ باب المندب آزاد شد
🔹
خبرهای اولیه از ورود مجاهدان یمنی به جزیره فوق استراتژیک میون در باب‌المندب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/688743" target="_blank">📅 16:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688742">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a22254fe.mp4?token=KvgX2wkLJBckhq-JgC28ZxBXHyjWGGZx8ZyY4E8rRK8MWRvdLfn-AASrVI7slbbmtzp-f_bycfSShoZIW_oba0jVSU3l79jZqtbO3D_piur0G3FPHmEg1LUgakbdyknkgR_7jPwlZVNSiqfNBzRGeOamKo0lmPoeYoj4j9zGNjy4VH74z5OVfIZIqmHOlKYzw2wv3KagVjESnKJMU8EemZswh_gU3fXJmkPxDh21BM5E7GxqFxEX5RfnglTu2BRRk3dcn3mmjlNGJKBjD0XLgRtpkGT93qG3YDVSIe-9v1WIOpVOd4kIfFlxN7B54w1N1m7VMG3M-adsY6P3t9SR9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a22254fe.mp4?token=KvgX2wkLJBckhq-JgC28ZxBXHyjWGGZx8ZyY4E8rRK8MWRvdLfn-AASrVI7slbbmtzp-f_bycfSShoZIW_oba0jVSU3l79jZqtbO3D_piur0G3FPHmEg1LUgakbdyknkgR_7jPwlZVNSiqfNBzRGeOamKo0lmPoeYoj4j9zGNjy4VH74z5OVfIZIqmHOlKYzw2wv3KagVjESnKJMU8EemZswh_gU3fXJmkPxDh21BM5E7GxqFxEX5RfnglTu2BRRk3dcn3mmjlNGJKBjD0XLgRtpkGT93qG3YDVSIe-9v1WIOpVOd4kIfFlxN7B54w1N1m7VMG3M-adsY6P3t9SR9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: به واسطه نیروی فضایی از فضا می‌توانیم نام مسئولین ایران روی اتیکت کت‌شان را بخوانیم از هزاران مایل دورتر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/688742" target="_blank">📅 16:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688741">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34fa144beb.mp4?token=nyDUqeiF9acfLqxZMBYKpfp5EtLZKT_-SlJITwHDdeUKIVppMjVByonlDmWdbU1u2HiRYphpasasRDHTN8vsW0rfph4e2Edq027IGTMZENbWQqgUjKA5ReQIqsjuaSk4biz-dsPHaKoZ4PMMSig-iDDn7pQKu2lPx3xACkVQUAlOeRZJfw9TK01Fzejqy_WDwWdHmV6HfthSFRckpIbRo6-yN-7xfBUA-Aa_TEaBB_0X-o0ROVXbboSC2oFSQL7n1hbM9yVJUYF_5iaotBfmkege4_xvNHzlEQSrH9H-T5L2tA_lKL0LgtxAEFkCR1KBT8O6rn6sOILuvPdXlzdmVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34fa144beb.mp4?token=nyDUqeiF9acfLqxZMBYKpfp5EtLZKT_-SlJITwHDdeUKIVppMjVByonlDmWdbU1u2HiRYphpasasRDHTN8vsW0rfph4e2Edq027IGTMZENbWQqgUjKA5ReQIqsjuaSk4biz-dsPHaKoZ4PMMSig-iDDn7pQKu2lPx3xACkVQUAlOeRZJfw9TK01Fzejqy_WDwWdHmV6HfthSFRckpIbRo6-yN-7xfBUA-Aa_TEaBB_0X-o0ROVXbboSC2oFSQL7n1hbM9yVJUYF_5iaotBfmkege4_xvNHzlEQSrH9H-T5L2tA_lKL0LgtxAEFkCR1KBT8O6rn6sOILuvPdXlzdmVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چشم شما تنها جایی در بدن شماست که می‌توانید خون خود را در حال جریان ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/688741" target="_blank">📅 16:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688740">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15c3a10b0.mp4?token=V_44MkOVj-Gziv1cIQknjAxHtVM3kdcq7s7kv5GzAOeaY0Yw2qrFyLkbaL4niaqkJ3ukcZSYlLYAmpXAyigMs4IKF2zmaoiXRFJmGogoNokMLNvX15TG1gSzLHdVZr2v3r8IQr-ACwlVY9JLxb9_2V62WXGNtQWO7LvzVWR5GXz8LNqj23fLcAqzH5H97tLlusOcWJR6D4cnlszJLp_VJO1w20ZRj9yVXjYQHgljK5Fu_m_aapgge7F0zQWlxxBWikZV7BllOZbXHpAsvWGg1jhK_WurWgcXvHIWoB2LW2L-3NfwnfVUMArQxtjm69eO8BUxL1icxM1HRjC-WxVPI0yNqt6VNEn26N1Y7FVbiNZKfECSeetWMZraYYLjTeA5_JOcbWb6F8nshijltGA57JpBBMs5UnwlY9bd7G_z_k5u8AnZnoMce9RHWrEmiLzTjcbe5dy85JS1P5NJMk63J-JRBboArPsAE_SujdlP40doMts16C2BhbdOMW1ZHlBnsUJAI0ze7TQqkPnp_Jd2cjcCK4CtLMDbtwANwCYWPTZVzRySAk431ZNcwYi2UNzU-WzaflzeC3Nh0KxuJPthevQLz-92GxSET9lApt-6_yuaQFUL-0UXW_CODB3J0ZWUmSLa9iXhpm2E10n7JWar5V6HWRuF4JosI0_-L_2fS6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15c3a10b0.mp4?token=V_44MkOVj-Gziv1cIQknjAxHtVM3kdcq7s7kv5GzAOeaY0Yw2qrFyLkbaL4niaqkJ3ukcZSYlLYAmpXAyigMs4IKF2zmaoiXRFJmGogoNokMLNvX15TG1gSzLHdVZr2v3r8IQr-ACwlVY9JLxb9_2V62WXGNtQWO7LvzVWR5GXz8LNqj23fLcAqzH5H97tLlusOcWJR6D4cnlszJLp_VJO1w20ZRj9yVXjYQHgljK5Fu_m_aapgge7F0zQWlxxBWikZV7BllOZbXHpAsvWGg1jhK_WurWgcXvHIWoB2LW2L-3NfwnfVUMArQxtjm69eO8BUxL1icxM1HRjC-WxVPI0yNqt6VNEn26N1Y7FVbiNZKfECSeetWMZraYYLjTeA5_JOcbWb6F8nshijltGA57JpBBMs5UnwlY9bd7G_z_k5u8AnZnoMce9RHWrEmiLzTjcbe5dy85JS1P5NJMk63J-JRBboArPsAE_SujdlP40doMts16C2BhbdOMW1ZHlBnsUJAI0ze7TQqkPnp_Jd2cjcCK4CtLMDbtwANwCYWPTZVzRySAk431ZNcwYi2UNzU-WzaflzeC3Nh0KxuJPthevQLz-92GxSET9lApt-6_yuaQFUL-0UXW_CODB3J0ZWUmSLa9iXhpm2E10n7JWar5V6HWRuF4JosI0_-L_2fS6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واقعا چه کسی جهان را اداره می‌کند؟
🔹
واقعیت این است که جهان یک دولت واحد ندارد و هیچ رییس جمهوری وجود ندارد که فرمانده همه کشورهای دنیا باشد؛ پس چه کسی دنیا را اداره می‌کند؟
🔹
در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/688740" target="_blank">📅 16:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688738">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
نفت برنت برای پنجمین‌بار امروز تغییر کرد و به ۱۰۵ دلار رسید!
🔹
بعد از خبر کاهش تولید نفت عربستان در پی حملات یمن، قیمت نفت در کمتر از یکساعت دو درصد افزایش پیدا کرد و هم‌چنان درحال افزایش قیمت است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/688738" target="_blank">📅 16:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688737">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a67ef8c4.mp4?token=jeSRnYTixvCcg6jvu8hOY5m5UGdvtvctqhe2SmUbzpevNdl5TOldB_R8zpPSDE3joEEhV24ejwsOxvqT1XaoZywEXh5tlsUbdwWkQUWiwpVDFxnf3waIfcetUhExlJ2thdnrU4vgLOt2hdIuy-LQJmUcwz3nH_9cZIaeMHNSHupsxRgB--3Td9SphQjxE7xxrEmf5ceEx8WhIuGmQM4fCLtHpp8gahmdFSYziggDX4PfdPwhqh6QjOFmfsI_N4Pquuy4C5N8FilbtykK5hKVBzG6GZgSr2zvU6raG9ZeFI9XKw8m1sMoxElwTg9G7bcr14I6VzyCrw0dYdbl2VZceQ4tJmy8DBOUwJyLvWYm7sCCrZU82aI8_povYexIiFbtLMAph2W_8rynDw8g5-rrjIcqDRkkDzMJrz5og2mxgPj-0l1vZUJDp2yuD8X_EOEWy5SqqImztgV49V5x9C74nj0Fo0qkGQ_3rAwu4T_dEwyTlrjBmkWijF00NhzLgJOTQtLpIJVUIUah1f-DgdpWQmylDlG19b7oiaP8WvbY1ucKQ0aas7CvxmSwhSryAbm9q3VVugYIgiPPAijxC85W3nfOD8u8ayiVEMW34J4q7IkmWnpM1vs_t_Zgfa8gkaxTLYOcoAEBDNVQKXwjDxIX2sp5NX7vNdBIdPmNmByryxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a67ef8c4.mp4?token=jeSRnYTixvCcg6jvu8hOY5m5UGdvtvctqhe2SmUbzpevNdl5TOldB_R8zpPSDE3joEEhV24ejwsOxvqT1XaoZywEXh5tlsUbdwWkQUWiwpVDFxnf3waIfcetUhExlJ2thdnrU4vgLOt2hdIuy-LQJmUcwz3nH_9cZIaeMHNSHupsxRgB--3Td9SphQjxE7xxrEmf5ceEx8WhIuGmQM4fCLtHpp8gahmdFSYziggDX4PfdPwhqh6QjOFmfsI_N4Pquuy4C5N8FilbtykK5hKVBzG6GZgSr2zvU6raG9ZeFI9XKw8m1sMoxElwTg9G7bcr14I6VzyCrw0dYdbl2VZceQ4tJmy8DBOUwJyLvWYm7sCCrZU82aI8_povYexIiFbtLMAph2W_8rynDw8g5-rrjIcqDRkkDzMJrz5og2mxgPj-0l1vZUJDp2yuD8X_EOEWy5SqqImztgV49V5x9C74nj0Fo0qkGQ_3rAwu4T_dEwyTlrjBmkWijF00NhzLgJOTQtLpIJVUIUah1f-DgdpWQmylDlG19b7oiaP8WvbY1ucKQ0aas7CvxmSwhSryAbm9q3VVugYIgiPPAijxC85W3nfOD8u8ayiVEMW34J4q7IkmWnpM1vs_t_Zgfa8gkaxTLYOcoAEBDNVQKXwjDxIX2sp5NX7vNdBIdPmNmByryxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربۀ‌ کاری انصارالله جهت افزایش تسلط بر دریای سرخ، جزیرۀ زقر هم آزاد شد  خبرگزاری‌فرانسه به‌نقل از منابع یمنی:
🔹
نیروهای مسلح یمن پس از تسلط بر المخا، جزیره راهبردی زُقر را نیز تحت کنترل گرفتند و در مسیر گسترش نفوذ در سواحل دریای سرخ هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/688737" target="_blank">📅 16:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688736">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f9275b09d.mp4?token=Kbh1l_b8aeXCbgjmy1LzhchlUSc2EUor4fl5LO2tvkHwh7zon8pSDTe-YmwXJOcfAW0Ru5CxGeUaN7PwvZ2n1V7vvFCPPgkO3E9z31HZNkqQb8ZQsj0BryCEl-mF-NWcWmz9o4Ku2Tyjk2mD-QRmOjgEgiiaglWaLV24Bm6dR5otGxqiAyrdKUZOfLzrA-hw9epv9Nv3g7WFU0Yfz6bJH8RuUz1qHw67wWnCkD2BBCRR3HST61kqU_Mg9IYdLSQrZSsTwGvOVe16oUbwF_LtJ3k14rgd5NTjJKlbzot1RFt7glw0uQ_7jByc2PxwM5CfCUrclWom2nRJ9pbfaRYY3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f9275b09d.mp4?token=Kbh1l_b8aeXCbgjmy1LzhchlUSc2EUor4fl5LO2tvkHwh7zon8pSDTe-YmwXJOcfAW0Ru5CxGeUaN7PwvZ2n1V7vvFCPPgkO3E9z31HZNkqQb8ZQsj0BryCEl-mF-NWcWmz9o4Ku2Tyjk2mD-QRmOjgEgiiaglWaLV24Bm6dR5otGxqiAyrdKUZOfLzrA-hw9epv9Nv3g7WFU0Yfz6bJH8RuUz1qHw67wWnCkD2BBCRR3HST61kqU_Mg9IYdLSQrZSsTwGvOVe16oUbwF_LtJ3k14rgd5NTjJKlbzot1RFt7glw0uQ_7jByc2PxwM5CfCUrclWom2nRJ9pbfaRYY3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر به خرید طلا علاقه داری، این چهار اشتباه رو‌ انجام نده #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/688736" target="_blank">📅 16:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688734">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIavTouox46ofe0pUwle7h22cpgKqWgWjXBrjuJY_tastwmNpl0JFeNAxgdnDeH6LOpB9wUp8YP0aJHM-vOonif49HnYwkZk_Smsc0ngRdUOjYlAxz7OSY_eip3QSCxzE_g3hLGZzzG97_KSn5kj-g46MBWm7D3naHsEvlLOOasz_5-GKrj0E7st4hB2iZBtqIw6mqtIWZxlI8Bc-qrIeuI6PFZLH_sHGQHzdp-HlJ7DO433MLt-CzL0KgjpbXOG9T6QtvUcv91MQPYIQtPRSxkJL-5kBze3n303z9tc0W10LJNhEFmuv81tjBi29TJrPSOaHwiE85S3pw2mZZuNcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خشکی‌های زمین بیشتر در اختیار کدام نوع پوشش‌ها است؟
🔹
بررسی داده‌های سازمان فائو (FAO) از توزیع پوشش سطح خشکی‌های زمین نشان می‌دهد بیابان‌ها و مناطق بایر با ۳۳ درصد و جنگل‌ها با ۳۱ درصد، بیشترین سهم را از مساحت خشکی‌های سیاره زمین به خود اختصاص داده‌اند.
🔹
همچنین مراتع و علفزارها ۲۲ درصد و اراضی کشاورزی ۱۲ درصد از این مساحت را تشکیل می‌دهند؛ در حالی که سهم شهرها و زیرساخت‌ها و همچنین پهنه‌های آبی و تالاب‌ها هرکدام تنها ۱ درصد است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/688734" target="_blank">📅 15:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688733">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ایران به ۹ جنگنده آمریکایی در اردن آسیب وارد کرد/«سی‌بی‌اس» گزارش داد در پی حمله به پایگاه موفق‌السلطی، ۹ هواپیمای نظامی آمریکا هدف قرار گرفته و آسیب دیده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/688733" target="_blank">📅 15:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688732">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEzRi_m6OqoR9KW39IsXAZTM-kkbIfZ4JVcHRfVtxBp5hfiLZF4QpniZFXPX8fNgPY1sy29_R_k0Xb7X0OlgCiKzaaYqm4wSjnNUgCa9ZZ4LGUuYtdoPq16payin2QWyKWCtG1JHckZ3cBy-3mloQmuapdvCID02rOgS7wVFMe_21Ha4ALKfccPC_hD_qtuqpEKDEVUsxCFZLj3hxtE1DGCUSJ8U_65kWku7VQwl38qkKpTYvHH7zlBemffEpHgmMeUKz2toehGXvqEBLl49XJTg2vXlcigq8bZflupBw957ruHBdm0VzMhwHX3lZfZunO19Vr740VB3-rb4-jsDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت خام برنت به ۱۰۲ دلار برای هر بشکه افزایش یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/688732" target="_blank">📅 15:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688731">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
بازار ۱۰۵ هزار میلیارد تومانی فیلترشکن در ایران
🔹
بازار فیلترشکن در ایران به بازاری بزرگ و پرهزینه تبدیل شده است. از هر چهار کاربر ایرانی، یک نفر از فیلترشکن استفاده می‌کند و از هر سه کاربر فیلترشکن، یک نفر برای آن هزینه می‌پردازد.
🔹
در طولانی‌ترین دوره قطعی اینترنت، متوسط هزینه هر گیگابایت فیلترشکن به ۳۹۰ هزار تومان رسید؛ رقمی که در اوج تقاضا حتی تا ۲ میلیون تومان برای هر گیگابایت افزایش یافت.
🔹
دیتاک، اندازه سالانه بازار فیلترشکن در ایران را حدود ۱۰۵ هزار میلیارد تومان برآورد کرده است.
🔹
رقمی که نشان می‌دهد محدودیت دسترسی به اینترنت، علاوه بر تبعات ارتباطی، به یک بازار اقتصادی قابل‌توجه نیز منجر شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/688731" target="_blank">📅 15:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688730">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26efa8e122.mp4?token=aRAqRJvlX_-gQaCZRVIKS1iYzedTyP_rkXO-i_r8l6J2flroh_x2foEtmaEGkKula-j5ZPU0jdh_6uJpfL8AKrEJ2a6EibeQl_VlNrjqjzQg5j84Y9HXAv9hQ4eMliMhCMdgME22-YwFZx7cA2uci9Z7BVZhK8bH7ZUAU6-22gkm1FYO4l5XzijyJRfOSPrX-wrZ_Il8U-ddSMP9zFUtgqMyQab3oWilmiv280w147-M1A1ubc_kAjUZpJRXANDlBwa99HSTBAJQJl5BRd_6AAzXtI7vZiBNbkXzRpOa0oYBHhuU4nkQYA948ZUuqf-72Em-5EgnPyNdwEi7qCHw0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26efa8e122.mp4?token=aRAqRJvlX_-gQaCZRVIKS1iYzedTyP_rkXO-i_r8l6J2flroh_x2foEtmaEGkKula-j5ZPU0jdh_6uJpfL8AKrEJ2a6EibeQl_VlNrjqjzQg5j84Y9HXAv9hQ4eMliMhCMdgME22-YwFZx7cA2uci9Z7BVZhK8bH7ZUAU6-22gkm1FYO4l5XzijyJRfOSPrX-wrZ_Il8U-ddSMP9zFUtgqMyQab3oWilmiv280w147-M1A1ubc_kAjUZpJRXANDlBwa99HSTBAJQJl5BRd_6AAzXtI7vZiBNbkXzRpOa0oYBHhuU4nkQYA948ZUuqf-72Em-5EgnPyNdwEi7qCHw0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتقا آیفون ۱۷ به آیفون ۱۸ پرو همین حالا در هند شروع شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/688730" target="_blank">📅 15:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688728">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
تعرفۀ مکالمه تلفن ثابت به همراه ۴۵ درصد افزایش یافت؛ از ۲۰ شهریور، سقف تعرفۀ مکالمه تلفن ثابت به همراه از ۶۲۵ به ۹۰۶ ریال افزایش می‌یابد./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/688728" target="_blank">📅 15:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688727">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd29b2165.mp4?token=SeS96P-VQcorTkacrWKTlzsGRXbGmFEJWGtXKIjP34DrJ9i2ZnYc3I49Gz1RIi0alMTLqQ0LRajEYP80A36AdzJbjVpy4M_Ti-KUWPO1U53N-sjDcL8cYjq4mxF2wIQOCyQUFT2smRM9ZPBoA35iR3H-ew8EIM7qbjFDYcpk7JhZhuTkgBUWQlyN-Csd_Y_9ef9gUjB7z5z49DN_K8lTK_KFuhri5AiS99-j1h4TYMtKOSK8oJK3srDplMD1_5TQE50NTC1WC4LlGCYFoRB08Fqo78SKOrTK3YbBiAabPXGjvkKoMpJCqPmNB_c-V5bOqRUWb6DeC97H60iOvXoRqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd29b2165.mp4?token=SeS96P-VQcorTkacrWKTlzsGRXbGmFEJWGtXKIjP34DrJ9i2ZnYc3I49Gz1RIi0alMTLqQ0LRajEYP80A36AdzJbjVpy4M_Ti-KUWPO1U53N-sjDcL8cYjq4mxF2wIQOCyQUFT2smRM9ZPBoA35iR3H-ew8EIM7qbjFDYcpk7JhZhuTkgBUWQlyN-Csd_Y_9ef9gUjB7z5z49DN_K8lTK_KFuhri5AiS99-j1h4TYMtKOSK8oJK3srDplMD1_5TQE50NTC1WC4LlGCYFoRB08Fqo78SKOrTK3YbBiAabPXGjvkKoMpJCqPmNB_c-V5bOqRUWb6DeC97H60iOvXoRqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مطمئنم نمی‌دونستی هر رنگ درب بطری آب، معنی متفاوتی داره  #حواست_هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/688727" target="_blank">📅 15:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688726">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e0d0778d.mp4?token=SjZhhVU4PXgqRtn49BUCeDaq0tO61MCGLVNTVLP46MvIdoW2he1Zxe61d93LtO2r2BC4Eb1F5Jc1c_Py44LAKRRTEcoGPlac8MwHp9_oh9EnRezdwrbWLa6E-EMhKEmEyqylgdUsg5KDvklap7ZvQj4PJnK7GpGiMNSbGTz2v1tNVv0tUHee1IRm_LB3kRYRr9eJsU3ptnLqWb4nr4GjOvf9Drg7HXT82b_hcAqDkshHFeNZbb79vV8nsA2L2-9w54O35TBSZG6pcQKfeDZzNI09_ydQRAOm8k_LGknaqgHW-n6f_P4HgidIS1mdKiDIqxzu65WdB-OjMIZzR7365g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e0d0778d.mp4?token=SjZhhVU4PXgqRtn49BUCeDaq0tO61MCGLVNTVLP46MvIdoW2he1Zxe61d93LtO2r2BC4Eb1F5Jc1c_Py44LAKRRTEcoGPlac8MwHp9_oh9EnRezdwrbWLa6E-EMhKEmEyqylgdUsg5KDvklap7ZvQj4PJnK7GpGiMNSbGTz2v1tNVv0tUHee1IRm_LB3kRYRr9eJsU3ptnLqWb4nr4GjOvf9Drg7HXT82b_hcAqDkshHFeNZbb79vV8nsA2L2-9w54O35TBSZG6pcQKfeDZzNI09_ydQRAOm8k_LGknaqgHW-n6f_P4HgidIS1mdKiDIqxzu65WdB-OjMIZzR7365g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشای لغو عملیات ویژۀ آمریکا، در نتیجۀ حملات ایران به پایگاه مهمش در اردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/688726" target="_blank">📅 14:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688725">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7EyKpn1VV3YHyHbP2bNH04_-Y3RpPIs-Xm3D1f6lBD8zU3CUirCo3-5TGtLuwNSwNmWmKj4huftWHZ66DL-DycGLj7ULO3mg9kdA6bIxC4ZSyW2MeuCgUBVP0nZ6UYK0DYLUWIrQHURdW7i6xPvRmqyROSUq_B8qPOl3vwU_PAmo4HjViefVCM9Dm7aZ-u6JcwDclTT_QE2OVoAik-aim_3lUNH00mYlqWX_NOxRQM4nG6u3MabZdZFXMO_pNJ5Ez7rJ2o7CYobhUoX1Z2Pq_kxbE_p0xy6eOCmRgIrCgCZxKLCJkBsEWpyK3Rg5R0UbXOJH4PuBCP1MF1-Ahz6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز   نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/688725" target="_blank">📅 14:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688724">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
جزیره زقر بدست انصارالله یمن فتح شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/688724" target="_blank">📅 14:48 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
