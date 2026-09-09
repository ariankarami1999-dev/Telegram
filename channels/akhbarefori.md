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
<img src="https://cdn4.telesco.pe/file/To_ia5UqGf7zNHbw8l-MZOk3Np1Bl98jyI7iObfbfRug4ogc2JM-7o9Crm9YfqgzhSJiJUZKiDEBI6ukUWPOihpwHnw-EQt6FMRWTgPKFCJLWkae9kmSMhVRP9STiYZtk6ZtwMbVGm_JgqdxEAxyj_E5JZq1LFLs9Y5xFm5RQgVUFTClY9iypR-BXD8xZ_Ku5RN0GBQNodz35XwswwNoo7nSUgaHlSaPShtKM7akCq9g4jWkf4KWUZDN4kqYc2mvDmZhrc1TXeaB9qevninPMRn2d3rC8Ig3uFhZlvp8TCpF0TOfRFunhNrS8w3I4OxqW-3xj_phLAi0uS8lcpN9EA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.3M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 19:06:53</div>
<hr>

<div class="tg-post" id="msg-688540">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
سید حسن خمینی: اگر مردم با یک تصمیم حکومت همدل نباشند، تحت هیچ شرایطی آن تصمیم به سرانجام نمی‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/akhbarefori/688540" target="_blank">📅 18:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688539">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd6461051.mp4?token=rczZbBB2hxA3Mknu0qsutXs7oNjfo7T8DLQsK2joBWo4Pyo6IGg7etT5CeOHtKkC2tunxUJ2oLyMshuMgfHCEIPbEMuXobFSvS9jEfU7xXJfqAQbK6YfcpOXtY53Qt_aVPc-UYyaDLOLkQYLh0_PUqX_4oJZD1nvLaxtrhBICSUB4mO2Gks5fRLEVrSpUtUUcQCevv5rARCKJQnrB3Qh0Zr7rTxglNBL_Q_Rx4gONZD-w1O_LdP_o57KZgEteYe1oPlATovi2Squ1xJvF3eS4GugQI4K7WptW8DawhrQs_yq3V0A8gXQx1HSJV3bwDi-nVdmnGEcysr05G6QFsedYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd6461051.mp4?token=rczZbBB2hxA3Mknu0qsutXs7oNjfo7T8DLQsK2joBWo4Pyo6IGg7etT5CeOHtKkC2tunxUJ2oLyMshuMgfHCEIPbEMuXobFSvS9jEfU7xXJfqAQbK6YfcpOXtY53Qt_aVPc-UYyaDLOLkQYLh0_PUqX_4oJZD1nvLaxtrhBICSUB4mO2Gks5fRLEVrSpUtUUcQCevv5rARCKJQnrB3Qh0Zr7rTxglNBL_Q_Rx4gONZD-w1O_LdP_o57KZgEteYe1oPlATovi2Squ1xJvF3eS4GugQI4K7WptW8DawhrQs_yq3V0A8gXQx1HSJV3bwDi-nVdmnGEcysr05G6QFsedYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوراخ کردن دیوار، نقشه سارق طلافروشی در بیرجند برای سرقت ۳ کیلو طلا
#اخبار_خراسان_جنوبی
در فضای مجازی
👇
@akhbarkhorasanjonubi</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/688539" target="_blank">📅 18:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688538">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeZFEtBoc1Ov0doSTIo8rS0cN19w9Lr5d5p9pNlZf80jlCE9ndBM6SFh1HUUlwtIVDFuUxuNXjT5jEXQTC5sXQlgLGwg6NmtMpXqd2AoAls6MvtEMHpk7cposqgUeNjQ6zn6RymQ1KMoJF9C5VNJvDCYjYRiP8NNedM5Yiwwl74nnrc4bzu_9J5BK_eGTCVcq89bxisKf1bl174dr54GJr3roKjBl2IGaJlIHg0upF5LFVX7zcJItCxEJq5A0PtWeLLCorTjSmOiAl_vL7CH5Qdk8sIeQIb0qqNGZVJuKYpe22XrMHQO5sgOvwDvJhroPwn6tsoQGNaJP2OB0ALjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری سردار آزمون برای ماکان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/688538" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688537">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjNSP3YHgU2W3VjuKKu-5AW2A5pTc_J5EENORTUAxZkhjWgD57PzcFG5P4rJawsjjwq0JMIrgDFVlxdCsW-Ux1jZSVQD8F9Xml3HS0AYq-hGTRG6zT6ZBwIC7gZpnxoww2eidSpibzdnefWWzIQHlOudHjqLv2IJlm9hPjw1ryAx6inZW9mbZstVbA332P0MSu_oIaySbI_w_bdBncNAQ0U1_09bXJok5ysue5yTMf7DAnKiVszkTLoxvmfCkylcLQZaBtuf0EciTbOBRYhudMYxra5ZXLNHZgn2hI0EJO0V__l87f7B_KdSX0k33yPzeu0IHONLxN3bjE-M6PUMIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز   نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/688537" target="_blank">📅 18:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688536">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ab3de9162.mp4?token=ERhNlnHVvfvnlfc2LTF860LNH638WLWYVyJ6S5rlHPW3crRzuQOAvVUZuyg1fXCbeZBJRDynjYE-fBhFnfFCGfgYgzvK-T4VaQ4sprQNNAsxjQf_MAZdf1_anNDNps2h6t10Fr8w63ilv70XdJLpMR6Ch3IvgB92wIWrJkQoZKAs0eLfasG303D9ErthZK8JWbHiKDv3vYzroY0gE1X1XoDB2jof0CGRckgocKJT6Uk0T8brrqwNiH79Fhu3IxZ5yqGqrrQYMeKsYUFyeMJqQaauULqE1Na7nNCV4V2SPbJmMLG63EE-NVN_PfUJ1eCR3Ld-ob_aMGB6jqkOtsycyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ab3de9162.mp4?token=ERhNlnHVvfvnlfc2LTF860LNH638WLWYVyJ6S5rlHPW3crRzuQOAvVUZuyg1fXCbeZBJRDynjYE-fBhFnfFCGfgYgzvK-T4VaQ4sprQNNAsxjQf_MAZdf1_anNDNps2h6t10Fr8w63ilv70XdJLpMR6Ch3IvgB92wIWrJkQoZKAs0eLfasG303D9ErthZK8JWbHiKDv3vYzroY0gE1X1XoDB2jof0CGRckgocKJT6Uk0T8brrqwNiH79Fhu3IxZ5yqGqrrQYMeKsYUFyeMJqQaauULqE1Na7nNCV4V2SPbJmMLG63EE-NVN_PfUJ1eCR3Ld-ob_aMGB6jqkOtsycyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو آیفون ۱۸ پرو لو رفت؛ داینامیک آیلند سه قسمتی می‌شود!
🔹
ویدیوی فاش‌شده از iOS 27: داینامیک آیلند آیفون ۱۸ پرو همزمان سه فعالیت زنده را نمایش می‌دهد و حدود ۲۰ درصد کوچک‌تر می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/688536" target="_blank">📅 18:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688535">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
جزئیات طرح اسقاط موتور سیکلت‌ها و خودروهای فرسوده  مدیر ستاد نوسازی ناوگان و اسقاط خودرو فرسوده
🔹
تسهیلات این طرح از ۴۰۰ میلیون تا ۱.۲ میلیارد تومان با نرخ سود ۴ درصد به متقاضیان پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/688535" target="_blank">📅 18:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688534">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMTjk2KBDFf5mYybxoJtnTb-TGT6ItSDZHa1qRFHADKnvDmh_5FDroSiqqPY94tUW3xLS1KMJTcdB-7exxl5LkI9kbYPAuEG2UsWKHFXMV9Rqnssq7aReu3BGRiUkNhCGqtD2jALHOn6W8h3X4UYxU-HhA72j3AUZbZSol_9OjiKhecdfD2tEkhIksPrJsT3hT5e-2m-d8NCq94jf2XHNDkDh7PPsYXJzA5AkyogEBuRsjgBU5AoZDhZc0miZZudwSkC68Vqy4B3eoGYgAtk86ld5x31cNYH1lzY2_zmpQLeJITRe1jgD7uVcQ36GTozctXD0gP9wlJTRpo7cmGt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت به بیش از ۱۰۱ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/688534" target="_blank">📅 18:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688533">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e66489c4e4.mp4?token=VCD8QIRGUW4CFTaqkh1pkPwvISISYYsxPv5zEpeuxS4PiuM22FAh84SIL6shQvsioWxiZw234tkQGPPatWR7TCpOlEx4itFXsJRknNJuq04t6Wx0OXYzCk6QelIc47d5snSAe_DOf1XpgsSszVNCo6Zl6yTVqH7bp07Q097KaIh-ZtqAN6sYulUH2va9TzwEK_cbFo0FH0h1CLemeOtvaHaWls9wXicvqqdzHwmvJON6nA6wmHaJJLYDnyLtr9PySETuNj8beDdftj8TbHtAKHc5c9doOEFrF957waP4y_gUHFWFBBZ8BEUjNfhF4nzW6e9usOpMLwfRWkPssxf7Nb79_qYscsah7CkLfKdd2N1uHi4xfiPMYdP-ZlRBziQjcRNC-nyT7nVJCHJ34wrogn6JGeuLxG43Xb7tOGaAOhVb-aBrlYBOkHi_fPqZJ8ps0mHlqCN1Uve2mDh_T7NtzZbVz4qav-Je1877ljZ6DyO_xezCDy4nBIWRD-l9IUeQVvAHCo1i6leFv4IRlPRfb09k2IqNXD1DHRnSVAKgy5TQsGybrmsWrKO8DvlQGGLFt6mGDesorb6IHesknkqY_lBJANZCD7zM2jR4Rdrr6vRy789MMb2PS4y-X7TjeLp6o5OsN8XHYSQZO6Jwmfu_dUupzkhDMT2h0bDdM06iU0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e66489c4e4.mp4?token=VCD8QIRGUW4CFTaqkh1pkPwvISISYYsxPv5zEpeuxS4PiuM22FAh84SIL6shQvsioWxiZw234tkQGPPatWR7TCpOlEx4itFXsJRknNJuq04t6Wx0OXYzCk6QelIc47d5snSAe_DOf1XpgsSszVNCo6Zl6yTVqH7bp07Q097KaIh-ZtqAN6sYulUH2va9TzwEK_cbFo0FH0h1CLemeOtvaHaWls9wXicvqqdzHwmvJON6nA6wmHaJJLYDnyLtr9PySETuNj8beDdftj8TbHtAKHc5c9doOEFrF957waP4y_gUHFWFBBZ8BEUjNfhF4nzW6e9usOpMLwfRWkPssxf7Nb79_qYscsah7CkLfKdd2N1uHi4xfiPMYdP-ZlRBziQjcRNC-nyT7nVJCHJ34wrogn6JGeuLxG43Xb7tOGaAOhVb-aBrlYBOkHi_fPqZJ8ps0mHlqCN1Uve2mDh_T7NtzZbVz4qav-Je1877ljZ6DyO_xezCDy4nBIWRD-l9IUeQVvAHCo1i6leFv4IRlPRfb09k2IqNXD1DHRnSVAKgy5TQsGybrmsWrKO8DvlQGGLFt6mGDesorb6IHesknkqY_lBJANZCD7zM2jR4Rdrr6vRy789MMb2PS4y-X7TjeLp6o5OsN8XHYSQZO6Jwmfu_dUupzkhDMT2h0bDdM06iU0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آیا وضعیت درآمدهای نفتی بدتر از سال ۹۸ و ۹۹ است؟
🏛️
رئیس‌کل بانک مرکزی یادآوری می‌کند که کشور
در سال‌های ۹۷ تا ۹۹ شرایطی سخت‌تر از امروز را تجربه کرده است. دوره فشار حداکثری که
صادرات نفت در برخی ماه‌ها نزدیک به صفر
شده بود.
💵
به گفته همتی، مجموع وصولی ارزی دولت در دو سال ۹۸ و ۹۹ تنها
حدود ۲۰ میلیارد دلار
بود؛ اما طبق گفته دستیار ارزی وی
درآمدهای نفتی امروز دست‌کم ۵۰ درصد بیشتر
از آن سال‌ها است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/688533" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688532">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttdkJB3b6pBk8GGqv6ckmbdXZ6hGWL3PHgVahQmFQcDu6gtyqNHAroqeY22t0H1GpaQ43gF7NOF-Ea-UVz_e-aHyQPahSMOiEgzrTEngDUNbloi3dOJ3Y7c545LWEARfnptO7wbewKGAX2-3QLCBLy1JfN1fjXmi4qR0IoMBtCpazQ0LEuNVUap8Qm8-2NaS7gBRwAZb00ZcpUmsbybNVaiT__JMJpb_4qripp8jB_ps6PH00lkU5QgEMgI3-KKDYemagO2S-wLGrk7x_jCwsuEDMceX2yR1lW5AIHTTU3RzocCbRaxWW9F6VTpx2jeEE-maLaeWqv3JES2oZwsAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از سطح مبتدی تا پیشرفته این حروف اضافه در مکالمه انگلیسی به کارتون میاد #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/688532" target="_blank">📅 18:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688531">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
شنیده شدن آژیر هشدار در منطقه خمیس مشیط عربستان سعودی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/688531" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688530">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
نشریه Foreign Affairs: آمریکا نمی‌تواند ایران را خفه کند
🔹
با وجود فشار تحریم‌ها و جنگ، ایران با سازوکارهای دور زدن تحریم و ذخایر بالای شرکت‌ها، همچنان توان حفظ بخشی از تولید و صادرات خود را دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/688530" target="_blank">📅 17:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688529">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ارم‌نیوز: پنتاگون سناریوی استقرار تفنگداران دریایی در جزایر ایران را بررسی می‌کند
🔹
طبق ادعای این رسانه اماراتی، آمریکا احتمال استقرار موقت تفنگداران دریایی در جزایر غیرمسکونی ایران اطراف تنگه هرمز را بررسی می‌کند./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/688529" target="_blank">📅 17:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688528">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd1dc3311a.mp4?token=WWmpbTPujRl2944tMxF49WYg8y1bPfjwUfNGWwrc3AiQLC3GoCqVHApTxzZsMIuKJZPXiNTHXpiWpBUIDjph61wd9tuZx9YJpGX43UhuKGIMOAIQYhO36foh2eX7uLa-q_Gwd1J2dxYwdne-c412p0dUogxGnJuz0c83FxTPXChGOnPBRMmXcJO02IScg_vRpi2zz6Ilk-xkzpahEJvtHUzbpcFaVFx9JzbDpiNb_5BDDD_lG2R0Kg1wNM2g1JlrbI16pJQQ9FLvawz9jfP_5o0ZHSGr3jVUJh5dNROj_2YpD2Qjz3PmIIahkkOje9B9LRz2Ecf80WKCVLM4fRqFcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd1dc3311a.mp4?token=WWmpbTPujRl2944tMxF49WYg8y1bPfjwUfNGWwrc3AiQLC3GoCqVHApTxzZsMIuKJZPXiNTHXpiWpBUIDjph61wd9tuZx9YJpGX43UhuKGIMOAIQYhO36foh2eX7uLa-q_Gwd1J2dxYwdne-c412p0dUogxGnJuz0c83FxTPXChGOnPBRMmXcJO02IScg_vRpi2zz6Ilk-xkzpahEJvtHUzbpcFaVFx9JzbDpiNb_5BDDD_lG2R0Kg1wNM2g1JlrbI16pJQQ9FLvawz9jfP_5o0ZHSGr3jVUJh5dNROj_2YpD2Qjz3PmIIahkkOje9B9LRz2Ecf80WKCVLM4fRqFcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید انقلاب
این روزهای افتخارآفرینی نیروهای مسلح و ایستادگی ملت ایران را پیش‌بینی کرده بودند...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/688528" target="_blank">📅 17:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688527">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c1d39a8e.mp4?token=Kli4746PhG1OsPz3fx85rSpSqqjpLp4cZ4-2reXwQGrEFpIlrxSMz9LI3ICnFF9fGL5qD4kvnh5MntDcmf7lpFM1v0jc3gy3eLpozrfJGObPz1gCMatiBoS_ouasdbtJv1tcdEG5ij7TtTYmA7kei9JbK8_oHqWCkWzk5pNCvtIQwWJq2sjTA7haH72ex8jeN5B7DEXrZHBlCHWu5oQ-dprFeFsT24PMnRcK80PlaXi23EOcBNmB9n_Yc876yavgij3VWZgaihUIc15cC996gmrENDAZkpxteetVwRXS7HevROKM3t5QsovqcoqF6B8zGARC9NCtkWtdq16VFUnzP4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c1d39a8e.mp4?token=Kli4746PhG1OsPz3fx85rSpSqqjpLp4cZ4-2reXwQGrEFpIlrxSMz9LI3ICnFF9fGL5qD4kvnh5MntDcmf7lpFM1v0jc3gy3eLpozrfJGObPz1gCMatiBoS_ouasdbtJv1tcdEG5ij7TtTYmA7kei9JbK8_oHqWCkWzk5pNCvtIQwWJq2sjTA7haH72ex8jeN5B7DEXrZHBlCHWu5oQ-dprFeFsT24PMnRcK80PlaXi23EOcBNmB9n_Yc876yavgij3VWZgaihUIc15cC996gmrENDAZkpxteetVwRXS7HevROKM3t5QsovqcoqF6B8zGARC9NCtkWtdq16VFUnzP4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وال استریت ژورنال: حمله یمن به پالایشگاه جیزان، قیمت نفت را به ۱۰۰ دلار رساند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/688527" target="_blank">📅 17:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688526">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
وزارت نفت عراق: یک کشتی که برای ذخیره نفت کوره استفاده می‌شد، توسط یک منبع ناشناخته در آب‌های سرزمینی ما مورد اصابت قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/688526" target="_blank">📅 17:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688525">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
پاداش جام جهانی برای هیئت‌رئیسه فدراسیون فوتبال گران تمام شد
🔹
سازمان بازرسی بابت پاداش ۲۰ هزار دلاری اعضای هیئت‌رئیسه پس از برد مقابل ولز شکایت کرده و ظاهراً برای برخی مدیران کیفرخواست صادر شده است.
🔹
مهدی تاج، منصور قنبرزاده، احمدرضا براتی، بهرام رضاییان و میرشاد ماجدی این پاداش را دریافت نکرده یا بازگردانده‌اند؛ نام تاج در این کیفرخواست مطرح نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/688525" target="_blank">📅 16:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688524">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای رویترز: در پی حمله به نفتکش «هرکولس استار» در نزدیکی دبی، یک نفر کشته و یک نفر دیگر مفقود شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/688524" target="_blank">📅 16:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688523">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6786c383.mp4?token=FrMOc5YnnrWrW56HGE3xUFyEeSwuNxp1fCcrSleFsEjXveHmhrq7mnsCN1FcXs2QJEMrBDQDYAxbAUb--q_huFenWsE4YQvRHbS3-mAyUXLp1wvDyN1_kC3NETMcW3d2w7-578_zrTPGByKjsozW43heYL4BgwCCoROVbEeub-XhBAhrRwyfRodpkQ2l22w16q5x8b1eHQI-pu3LE7ShoHGG4TSaxXzjOq-eTMIddbCIvYg-njka5fAnzqxrrymoi38Q3ftN8CJNEAyS4jlpPPbmfvgxscjAH8xzxzTVCeBqaqhVnVJrU40GpckFuxdeL4CzB9EZIPUj_j6UVMmAfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6786c383.mp4?token=FrMOc5YnnrWrW56HGE3xUFyEeSwuNxp1fCcrSleFsEjXveHmhrq7mnsCN1FcXs2QJEMrBDQDYAxbAUb--q_huFenWsE4YQvRHbS3-mAyUXLp1wvDyN1_kC3NETMcW3d2w7-578_zrTPGByKjsozW43heYL4BgwCCoROVbEeub-XhBAhrRwyfRodpkQ2l22w16q5x8b1eHQI-pu3LE7ShoHGG4TSaxXzjOq-eTMIddbCIvYg-njka5fAnzqxrrymoi38Q3ftN8CJNEAyS4jlpPPbmfvgxscjAH8xzxzTVCeBqaqhVnVJrU40GpckFuxdeL4CzB9EZIPUj_j6UVMmAfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا دهانه چیکشلوب؛ نقطه پایان عصر دایناسور‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/688523" target="_blank">📅 16:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688522">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
آخرین وضعیت پل ارتباطی لارستان به بندر خمیر بعد از حمله دشمن/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/688522" target="_blank">📅 16:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688521">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
آمریکا در فکر انتقال پایگاه‌هایش به زیر زمین
سی‌ان‌ان:
🔹
آسیب‌پذیری پایگاه‌های آمریکا در برابر حملات موشکی و پهپادی ایران، پنتاگون و نهادهای اطلاعاتی آمریکا را به بررسی تغییر آرایش نظامی در خاورمیانه و حتی انتقال بخشی از تأسیسات به زیر زمین واداشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/688521" target="_blank">📅 16:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688520">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
عذرخواهی رئیس دانشگاه سمنان از دانشجوهای عراقی بابت حمله‌ای که چند روز پیش به خوابگاهشان شده بود
🔹
تعرض و توهین دانشجویان عراقی دانشگاه سمنان به یک خانم تکذیب شد.  #اخبار_سمنان در فضای مجازی
👇
@Akhbar_Semnan</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/688520" target="_blank">📅 16:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688519">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ym0ONy_iJF6PMYO2YcI1Vm3ch6MBPd0YfhXKyPKYGqIOhxUjjCzRzZosHmwGM00ZHHhXtWuDf1K5KFuT4-wykFu4rJkZsfCjKoM3pyGjVfh3_Dbi1UvwWRfCEoegBMuQE4fmvYs2xdqora1OlUQKqRLmkMh5gn-P_vGXO8tNqaxt7Tpoet565ngicgHSxXwK2iNw41kIVHwlNFWeT2sGUR2JA96_6BScPf3K2mcKjEtKdKvptnx4F4tnLGnFl7TlWNdNAWgrXbPDZPZ0RcTngdwjEw2aLiNPBpTq82DUAynNXSMoO2mnRhPCNEQJ0E6YQ7CAXZHy_13ljB8Q2lLCpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای جدید سی‌ان‌ان: تحلیل تصاویر ماهواره‌ای نشان می‌دهد که ساخت‌وساز در سایت هسته‌ای «کوه کلنگ»  در نزدیکی نطنز، که در عمق زمین قرار دارد، افزایش چشمگیری داشته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/688519" target="_blank">📅 16:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688518">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ضربات ایران، آمریکا را به فکر یک طرح پدافندی جدید انداخت
دیفنس نیوز:
🔹
پنتاگون در حال بررسی طرحی برای تبدیل هواپیماهای ترابری و سوخت‌رسان به سکوی پرتاب پهپادهای خودران و مجهز به هوش مصنوعی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/688518" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688517">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c03f1eee0.mp4?token=up787YeheOpfFCC7MBqGSn07X5dhuebsgV0gzyfDO-ZSQWnOyR9vD_ptOTlKY9TkFHLvg2Kk4FNp7chC-h1IHgVek2wV0gVttnuAUVkaF8DySxb9C8nnO3HnnbG4DQGOZEjCukGYFygoCEA7Pk5Pvj3TiReDreUNjK70NF7pBjGJ9H9UbqosybhalqvMuxFl7qq1H4kmMGJ2cALxZ3mDp1ULjZX9ciOyAfKcwfGFOs93k_9WrH6quH-TFb6Z_nNVvgr6esWzjQi1JbptEUdbCd1AJIAQtAYxEZGwg_SsuNpJ8UzMiDEuwAuRhtuNBmJxFHXFUPosn3nLElXOI9R2X1En-rl3PRG1D03PWm4KE2LX9vZOf43FSgrWZbiwSlIT1R9SKeHAS9btgfDdfG574nRXd5F12cdmHSDqfTa8e2pjl-gFH4sJ7HA0wA6aquY0w_leOB5O7qGmWLjvYmztS8L4h_TDv1q3OppW_VhWIBWAmr38ouY-eVHcrrau1k37OmWROn31GFCggeDp6Q85uFIaTeQnI1xaXSXJyvS97HEhpfonZerHr6uKayg9etaWVQOHiNBeTaQkjMaMRZT4G8osZyg1jhcH2VIEFAq69h7bElA4URnYG6UOcQ9E5RVhD5Mbsj6TQbkSqsprbSIrdFnZxOOMAXjvCLmTbuYTJSk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c03f1eee0.mp4?token=up787YeheOpfFCC7MBqGSn07X5dhuebsgV0gzyfDO-ZSQWnOyR9vD_ptOTlKY9TkFHLvg2Kk4FNp7chC-h1IHgVek2wV0gVttnuAUVkaF8DySxb9C8nnO3HnnbG4DQGOZEjCukGYFygoCEA7Pk5Pvj3TiReDreUNjK70NF7pBjGJ9H9UbqosybhalqvMuxFl7qq1H4kmMGJ2cALxZ3mDp1ULjZX9ciOyAfKcwfGFOs93k_9WrH6quH-TFb6Z_nNVvgr6esWzjQi1JbptEUdbCd1AJIAQtAYxEZGwg_SsuNpJ8UzMiDEuwAuRhtuNBmJxFHXFUPosn3nLElXOI9R2X1En-rl3PRG1D03PWm4KE2LX9vZOf43FSgrWZbiwSlIT1R9SKeHAS9btgfDdfG574nRXd5F12cdmHSDqfTa8e2pjl-gFH4sJ7HA0wA6aquY0w_leOB5O7qGmWLjvYmztS8L4h_TDv1q3OppW_VhWIBWAmr38ouY-eVHcrrau1k37OmWROn31GFCggeDp6Q85uFIaTeQnI1xaXSXJyvS97HEhpfonZerHr6uKayg9etaWVQOHiNBeTaQkjMaMRZT4G8osZyg1jhcH2VIEFAq69h7bElA4URnYG6UOcQ9E5RVhD5Mbsj6TQbkSqsprbSIrdFnZxOOMAXjvCLmTbuYTJSk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکسی تمام‌خودران تسلا در تگزاس
🔹
تسلا سرویس «سایبرکب» را در آستین تگزاس راه‌اندازی کرده؛ تاکسی دو نفره‌ای بدون فرمان و پدال که برای رقابت با اوبر و ویمو وارد بازار شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/688517" target="_blank">📅 16:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688516">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
والا: نتانیاهو نگران وضعیت انتخاباتی لیکود است
🔹
طبق نظرسنجی‌های این هفته، لیکود به رهبری نتانیاهو ۲۰ تا ۲۱ کرسی به دست می‌آورد و نتانیاهو از افزایش مخالفت‌ها و درخواست‌ها برای برکناری خود نگران است.
🔹
کنست مجموعا ۱۲۰ کرسی دارد که بین احزاب چپی،عربی و راست‌گرا تقسیم می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/688516" target="_blank">📅 16:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688514">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812edfda29.mp4?token=C-d_TFRzt_zYpESqPR8T3ZPSc6g2trdb-Tn384Nu_winRV3Y8yBJgw7RX39Zk1Q9SvP5slbaEkzUccyI3eE7XcnHcJ1y1Sx1IApULLiatAdMbW41-CO9UicwIOBib2bJuzw2-dRZqeCLe10D53S5FR_VkCP7r-g_UuomhqeIeMOEGkOJHJ7x8ZKqc0gfL_9Yj7zbbIZ0iKnULGp4QwDqRwDCOk--oqjV562BqSgcdXxZ2neTnsEhC3tN6q0HCecHKbpFUCUF0QzvQQT7G9Ny2K4erB-Abv3YXmCsOYAxbRWe7T0eTKHSF4Y73n6X2ioncTFCFE4b-mGvriTzB2HMIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812edfda29.mp4?token=C-d_TFRzt_zYpESqPR8T3ZPSc6g2trdb-Tn384Nu_winRV3Y8yBJgw7RX39Zk1Q9SvP5slbaEkzUccyI3eE7XcnHcJ1y1Sx1IApULLiatAdMbW41-CO9UicwIOBib2bJuzw2-dRZqeCLe10D53S5FR_VkCP7r-g_UuomhqeIeMOEGkOJHJ7x8ZKqc0gfL_9Yj7zbbIZ0iKnULGp4QwDqRwDCOk--oqjV562BqSgcdXxZ2neTnsEhC3tN6q0HCecHKbpFUCUF0QzvQQT7G9Ny2K4erB-Abv3YXmCsOYAxbRWe7T0eTKHSF4Y73n6X2ioncTFCFE4b-mGvriTzB2HMIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر به خرید طلا علاقه داری، این چهار اشتباه رو‌ انجام نده
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/688514" target="_blank">📅 16:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688513">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuyIyoOW7GNcxeIVRLDfY8MYLHvd7uP4W992ICq6mEqRPyKaDmXiuRcBiYWANj_KOhYTTUyqT3GV37MZ0feo4MnZ7IZhT_hafDhmtxrRzjCBVb-IRyieR3PS3y-U80kKhoXQlvnOQQyDmp8BfJjZxQSnSBdRHdqbdDM8tayPBPVSUJVyua2q_GPswoJXfeX8y0udq7Z-_Kd2lNuYLgYG3IAqWYqKUQPAmg5pSdRUCsuoZoeUCLNuxGiD6PqFt3wO6vsh1_pNKfT5jYtiVBJ1ZEJxfjHlhBKnNxHiyaKyyObtlZd2jYatBa4UqEEdIhCQelWq3KvlEv9dVjp7Si3ViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلفات ارتش آمریکا باز هم افزایش یافت
🔸
طبق داده‌های پنتاگون، تلفات نظامی آمریکا در درگیری با ایران به ۸۳۸ نفر رسیده که شامل ۱۸ کشته و ۸۲۰ زخمی است.
🔸
برخی منابع و منتقدان معتقدند تلفات واقعی می‌تواند بسیار بیشتر از رقم اعلامی باشد.
@amarfact</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/688513" target="_blank">📅 16:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688512">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiCAp35Gk8MBw21Rx9bONsHviFK3pt4xMPobzSneDpeATMkvqHdd5oIqwSI2Ngoi54lZtVeCKvv1k8ObBIfqUy2bKd9PzUG59cN8Oo8tR8kya46d2xqJpvz86e_YJb8frY3DKMTxZv6N9FHFSO6Y7a02EzwZISOSE7qB-JV9W5rR9zsCU6zCiJGRrFGK0EeUmwt8Nhn7y4FQjYnQjIaJkAadYr27kCZ1O5FVS0W1umkK-dkQl9emhvbKNxv-u_JwvnZeDJH9qgFMybhH9TuHzh18p8_de2G3vWpJdbCex6yj_1ElFbQBPyNZVvinOC59kymEcmS6tP8UuV8Zzh6_eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☀️
💜
#خنک_ترش_کن
🍦
با محصولات تابستونه سحرخیز یه خوراکی خنک و خوشمزه درست کن، عکس یا ویدئو بگیر و در مسابقه شرکت کن؛ جایزه ببر!
🎁
💚
۱۰٪ تخفیف + حمایت از کودکان محک
👇
شرایط مسابقه
https://zaya.io/d2nr9
🛒
خرید محصولات تابستانه
https://zaya.io/ba5mo
🎁
عضویت در باشگاه مشتریان سحرخیز و دریافت امتیاز ۲ برابر
https://zaya.io/4g7k9</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/688512" target="_blank">📅 16:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688511">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mB8O9A5zpBvgxTJQ6SNB5p-79951kzjOVeJFOm9kIXr76S5W-JIlrnJ6U0CIhP21tuAat0SJaOtHjDp_JtLdoB5Ve4sJopl4pbOV2HrZdI6kMOZAGXp7S4Zh2W-tk7xRwfFUnbr9u2DUl0R59JntcjoV78ysu4KHTvsoh9mTwLlpjhF8XBAJ_NUDA1g1NYgsOyjYTLS_yHBqhq9VAHv8x7kiqjCaHYk-UonTazDIHM3Qztpo23DA8rRjQ8pyYGoyMaQfqDNLS7XpC_PYsEAfxq1EhTD7BYmMCLgtqzhwlA2_e7ci8fpZGbPlV0kBREN7UAxIsgZFt7bMTL9Fa56XVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز   نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/688511" target="_blank">📅 15:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688510">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
عارف: پیش از این با انتخاب وزیر زن مخالفت می‌شد، در حالی که معتقدیم هیچ منع شرعی برای این انتخاب وجود ندارد و زنان ما کارآمدی بیشتری از مردان دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/688510" target="_blank">📅 15:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688509">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/695aaa457c.mp4?token=PJa6bOcXGYqp_WZ75OYU770Yubtxi9gT_qzkP_W6BSQgvjGHVYdAVOeEpE-W-Nh2Ryf8lubX9Souye-VHjLfeS7olRVYUSCTgAjXB5M15v89gr8nJw2FJalUg2vGmZUUNHmNX5WCwp4STTh7QYKxoj3enpE_5b4yPjuHANwBcciiaKV8czNHR06sh8Z9itUpgG8_eqdAIoMPJgyc0zqb8PhxvDWdjEwR9_-E5mJN3hxNjKadKExhXNR69czGKaq7st6UuWfm8uNQLiKO9y-_Zb0Bx0Z6_zKr2L_ICvrTkeavKXrJMjt81bK8fIORDukKqmAkz_Q7BnXcPEbF-lXKng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/695aaa457c.mp4?token=PJa6bOcXGYqp_WZ75OYU770Yubtxi9gT_qzkP_W6BSQgvjGHVYdAVOeEpE-W-Nh2Ryf8lubX9Souye-VHjLfeS7olRVYUSCTgAjXB5M15v89gr8nJw2FJalUg2vGmZUUNHmNX5WCwp4STTh7QYKxoj3enpE_5b4yPjuHANwBcciiaKV8czNHR06sh8Z9itUpgG8_eqdAIoMPJgyc0zqb8PhxvDWdjEwR9_-E5mJN3hxNjKadKExhXNR69czGKaq7st6UuWfm8uNQLiKO9y-_Zb0Bx0Z6_zKr2L_ICvrTkeavKXrJMjt81bK8fIORDukKqmAkz_Q7BnXcPEbF-lXKng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو بعضی از فرودگاه‌های کشورهای همسایه، چمدان‌هایی که توسط مسافران در فرودگاه جا گذاشته شده بودن، حالا وارد یک مزایده بزرگ شدن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/688509" target="_blank">📅 15:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688508">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما اصلی‌ترین علت کم‌تحرکی و پایین بودن سرانه ورزش همگانی در کشور چیست؟</h4>
<ul>
<li>✓ هزینه بالای باشگاه‌ها</li>
<li>✓ کمبود فضاهای ورزشی رایگان</li>
<li>✓ کمبود وقت</li>
<li>✓ عدم فرهنگ‌سازی مناسب</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/688508" target="_blank">📅 15:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688507">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d675398c3c.mp4?token=OrkRfBsVRxmVIRBEY1iXSUzwhyFmgH9nY1MsT5hlyj0kC3vp2Fx-iL3qtfWRc56y449hvslCOa0GxN5wvXBYtaUAZIysR2d1jjNexl56Vj0cVRWq6v008LqrPN8ehcpWy_A2qrcjS6sDE2o4-nBHHqx6iMDSUF6-huSVFkHnPIX-6LGBgIuvWgT5pYxwjKsNMZ-5JAgeyKBZ7jSKp_Hgh4xpSlBfzgr01mJV0-7Tj9ACemHQTptatxFlEKBnYJQYQv5VhfKxqt_LbpPjd9xaMDbFq0V07QVKT40oE-FZ7TLVUmWIiIxBX0GEjnCvOCmKx2s5GIzeQXyH9-PTQCk_yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d675398c3c.mp4?token=OrkRfBsVRxmVIRBEY1iXSUzwhyFmgH9nY1MsT5hlyj0kC3vp2Fx-iL3qtfWRc56y449hvslCOa0GxN5wvXBYtaUAZIysR2d1jjNexl56Vj0cVRWq6v008LqrPN8ehcpWy_A2qrcjS6sDE2o4-nBHHqx6iMDSUF6-huSVFkHnPIX-6LGBgIuvWgT5pYxwjKsNMZ-5JAgeyKBZ7jSKp_Hgh4xpSlBfzgr01mJV0-7Tj9ACemHQTptatxFlEKBnYJQYQv5VhfKxqt_LbpPjd9xaMDbFq0V07QVKT40oE-FZ7TLVUmWIiIxBX0GEjnCvOCmKx2s5GIzeQXyH9-PTQCk_yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عذرخواهی رئیس دانشگاه سمنان از دانشجوهای عراقی بابت حمله‌ای که چند روز پیش به خوابگاهشان شده بود
🔹
تعرض و توهین دانشجویان عراقی دانشگاه سمنان به یک خانم تکذیب شد.
#اخبار_سمنان
در فضای مجازی
👇
@Akhbar_Semnan</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/688507" target="_blank">📅 15:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688506">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhsVWNCPHgJSVLyV3Usp5FXvVizNEnQ24Ndz2na51n3XahfmGOCn2_Ca3c6d9Vc_B1wc1F4DzmTXXOE90Df9olbDloZmzr2nD2K-4H6RE2lG5b9tS4sm2JPWxuQJZsZ-OrBtBzsCZsDPFv2V3a4jUYlvYQAu-2YHGcOHxzf3AtrClbveGyoqTLLChjastETEO14sZpkHkAlpw0sdXuTpqf8xPacEQZEgde35EvnpunUDRsBEWaL0fPxGOM0XlgntPPf5ist5T322TxysmaNZ8PJ47P5XlDHwQI4JfwQ5Mhj8GR7RHSbYfSBB8yNsgd1gvxVjqYXmEI4Aqs3cQbpruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در دل خودکار چه اتفاقی می‌افته که فکرها و کلمات، سر از کاغذ درمیارن؟
🖊️
#حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/688506" target="_blank">📅 15:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688505">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
سی‌ان‌ان به نقل از منابع آگاه: تلاش‌های آمریکا برای تدوین برنامه‌هایی برای حملات قاطع علیه تأسیسات هسته‌ای زیرزمینی ایران ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/688505" target="_blank">📅 15:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688504">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
شروط جدید ایران برای توقف جنگ اعلام شد  سخنگوی سپاه:
🔹
اگر دشمن خواهان پایان این وضعیت است، باید ۱- ضمن توقف کامل جنگ،  ۲- از تهدید مجدد دست بکشد، ۳- ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند،  ۴- محاصرهٔ یمن پایان یابد، ۵- ۲۴ میلیارد دلار دارایی مسدودشدهٔ…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/688504" target="_blank">📅 15:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688503">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرفوری
pinned «
♦️
شروط جدید ایران برای توقف جنگ اعلام شد  سخنگوی سپاه:
🔹
اگر دشمن خواهان پایان این وضعیت است، باید ۱- ضمن توقف کامل جنگ،  ۲- از تهدید مجدد دست بکشد، ۳- ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند،  ۴- محاصرهٔ یمن پایان یابد، ۵- ۲۴ میلیارد دلار دارایی مسدودشدهٔ…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/688503" target="_blank">📅 15:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688502">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
بانک‌ها از SSL خارجی به گواهی داخلی کوچ می‌کنند
🔹
بانک‌های ایرانی به دلیل تحریم‌ها ملزم به مهاجرت از گواهی‌های SSL بین‌المللی به گواهی‌های صادرشده از سوی مرکز ریشه ایران شده‌اند. این تصمیم پس از آن گرفته شد که طی یک ماه گذشته گواهی امنیتی بانک‌ها پی‌درپی لغو و سایت آنها موقتاً از دسترس خارج شد.
🔹
بانک‌ها تاکنون با تغییر صادرکننده گواهی یا انتقال دامنه از دات‌کام به دات‌نت یا دات‌آی آر سرویس خود را دوباره برقرار می‌کردند، اما این راه‌حل گاهی فقط چند روز دوام داشت.
🔹
گواهی داخلی نیز یک چالش دارد؛ مرکز ریشه ایران به‌صورت پیش‌فرض در فهرست مراکز مورد اعتماد مرورگرها و سیستم‌عامل‌های رایج قرار ندارد. این مشکل در اپلیکیشن‌های بانکی قابل حل است، اما در کامپیوترهای شخصی نیازمند راهکاری برای ایجاد زنجیره اعتماد است.
🔹
تغییر مداوم دامنه بانک‌ها نیز می‌تواند تشخیص سایت اصلی را دشوارتر و خطر فیشینگ را بیشتر کند. / پیوست
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/688502" target="_blank">📅 15:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688501">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ارمنستان و ترکیه مقصد جدید ایرانی‌های متقاضی آزمون تافل
مصطفوی، عضو کمیسیون آموزش و تحقیقات مجلس:
🔹
دولت در حال پیگیری رفع هرچه زودتر تحریم‌های ناعادلانه آزمون‌های دولینگو و تافل است.
🔹
وزارت علوم پیگیری خواهد کرد تا کسانی که نمی‌توانند در آزمون خارج کشور شرکت کنند، پول خود را پس بگیرند./ جریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/688501" target="_blank">📅 15:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688499">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
سخنگوی سپاه: دشمن ۲ هدف از ما بزند، به ۲۰ هدف حمله می‌کنیم  سپاه:
🔹
هر کشتی که از منطقه ممنوعه تنگه هرمز عبور کند تحریم می‌شود.
🔹
منطقهٔ تحریمی تقریبا از سمت چابهار شروع و تا بخشی‌از دریای عمان و دریای عرب ادامه دارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/688499" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688496">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6l8n2x9EnubjJJF4gEukc1Io8qXeVgDTtbyh-pt9XM5tDon_UJ_PTwaRRRI_U3Ff0ja-j3bxkcJ00NkX2s02TZyGmKVFEiU09rZWJio8vs5gIJ08hrZuULLb0GCV3q6p-zSUNUMJz6pks4RMaOEjqrq4C_4vmjbo_E5ySGBtnqXVgfdOZ6dO2BOPO8o7Br0bC59XblhiL6Obc6DuGLGA1ieA3nSrHrZ1EtbQIuNGEIB4sw7qJx8fLiGzabtG_oC3PDFrGsBWJADhp6g7Nke2lfHS9C7055QFvUZS_-Qs2uOFZdB9wNVUMgOlPC84houaNvnDrH-cVJHLd9LB1LNxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acea70049e.mp4?token=l6sQ_7obf8QtWxokd2lQPYjM3pd-ZD5qJ3pxUD9fdYJiOlC8hArXB0DYkw5uw5ds6mC6NjEgydmmOEHfjO-LpwxuI_A7PGmfwpWXNqoPnBIe2PCytSyDl9peP_USbU7t4eJU8gneKipcCaN_IvuN8UJroEojQnwQaDOxwmuATVdCsv6VdxCdsjFM9meDdUNRrZvCe1XlZZOdUlbw01_dDTT4QsYEyvRVAkbrkiYRMFuaE_20nUQ7AzDlzIxjZZBC5_OCs_mslNPZ7pgpRyjyPKA0aht5VY3rrliEM59cURLn0h-pDQLuYN3hm4rWTCLybeRNYPqasnV5Vil-Gy9xyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acea70049e.mp4?token=l6sQ_7obf8QtWxokd2lQPYjM3pd-ZD5qJ3pxUD9fdYJiOlC8hArXB0DYkw5uw5ds6mC6NjEgydmmOEHfjO-LpwxuI_A7PGmfwpWXNqoPnBIe2PCytSyDl9peP_USbU7t4eJU8gneKipcCaN_IvuN8UJroEojQnwQaDOxwmuATVdCsv6VdxCdsjFM9meDdUNRrZvCe1XlZZOdUlbw01_dDTT4QsYEyvRVAkbrkiYRMFuaE_20nUQ7AzDlzIxjZZBC5_OCs_mslNPZ7pgpRyjyPKA0aht5VY3rrliEM59cURLn0h-pDQLuYN3hm4rWTCLybeRNYPqasnV5Vil-Gy9xyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👕
از یک تیشرت ساده تا یک کسب‌وکار خانگی
🔹
کمپین #چرخ_زندگی تلاش می‌کنیم کسب‌وکارهایی را معرفی کنیم که با سرمایه کم، امکان شروع دارند و می‌توانند به تقویت اقتصاد خانواده‌ها، به‌خصوص برای بانوان، کمک کنند.
🔹
این بار سراغ چاپ طرح روی تیشرت رفتیم؛ ایده‌ای ساده…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/688496" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688495">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
الجزیره به نقل از متن پیش‌نویس قطعنامه آمریکا و اروپا: ایران همچنان به تعهدات هسته‌ای خود پایبند نیست و باید درباره مواد هسته‌ای و دسترسی به تأسیسات، فوراً شفاف‌سازی کند. این پیش‌نویس همچنین خواستار ورود جدی و بدون پیش‌شرط تهران به مذاکرات برای حل دیپلماتیک این موضوع شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/688495" target="_blank">📅 14:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688494">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
واریز یارانه دو میلیون تومانی به حساب کالابرگ مشمولان طرح کارت امید مادران
معاون رفاه وزارت تعاون کار و رفاه اجتماعی:
🔹
این یارانه حمایتی شامل ۳۳۴ هزار مادر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/688494" target="_blank">📅 14:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688493">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سخنگوی سپاه: دشمن ۲ هدف از ما بزند، به ۲۰ هدف حمله می‌کنیم
سپاه:
🔹
هر کشتی که از منطقه ممنوعه تنگه هرمز عبور کند تحریم می‌شود.
🔹
منطقهٔ تحریمی تقریبا از سمت چابهار شروع و تا بخشی‌از دریای عمان و دریای عرب ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/688493" target="_blank">📅 14:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688492">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436ad5c5e5.mp4?token=aXcGPkBmmJFxW3SkHTR8mHPrUPKFA9zEEi5M2w1WOhdD8yIQG2n45l7F_q9tpvNiodPLgvpP474_1Fkj5nyTr9Oz4uwoq857_CqRuYx-Hu-vJt4kJYhuDhoAxbaiGLWMeR3ixS7xrZhZOUpWsCjwNyMvavZhBcVBre8Eif1cNX8rCJdf2n5rkU0q4WFUNaIBSy10GOunMRrMOHxqqfg7Pa_tXOzNYBU3R_MOJp2w-7unqotv3gzDutLuZPSPyVIcjkid8fGay2asu5bYZBn-_fEj524isLFmBDlS24iMSzlD8VnsVWMZg3hX9CfHpwyZqn-Ip54tyxKu-O3IlGQ-ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436ad5c5e5.mp4?token=aXcGPkBmmJFxW3SkHTR8mHPrUPKFA9zEEi5M2w1WOhdD8yIQG2n45l7F_q9tpvNiodPLgvpP474_1Fkj5nyTr9Oz4uwoq857_CqRuYx-Hu-vJt4kJYhuDhoAxbaiGLWMeR3ixS7xrZhZOUpWsCjwNyMvavZhBcVBre8Eif1cNX8rCJdf2n5rkU0q4WFUNaIBSy10GOunMRrMOHxqqfg7Pa_tXOzNYBU3R_MOJp2w-7unqotv3gzDutLuZPSPyVIcjkid8fGay2asu5bYZBn-_fEj524isLFmBDlS24iMSzlD8VnsVWMZg3hX9CfHpwyZqn-Ip54tyxKu-O3IlGQ-ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حداد عادل: به‌دلیل شرایط جنگ، فعلا نمی‌توانیم آن‌طور که باید وارد مساله حجاب شویم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/688492" target="_blank">📅 14:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688491">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e08049b3.mp4?token=ChSkHMu_uEkW4DYEZYJABIdTwwt3O7cEE8Wsfr90MuG4FexLAWojiJOyu4_VKT59uSXUAmr07tKGBudhAkDPXhKV28CdWtsxNONJ_WHeOUIksTWXS6OYlNE8eBgxANQCsEmaq9V5Ni3Azf3sK4W5_TX22UpuAUZt6Tn7wiytDhfYlK3GKp728U7JvFmeXlXdfkUrPnzOvivMax7OuDKZr418LLaDZmiic_1QDxtAsg8o93rhKIpoBXLXU879K0oqjL4vhw_yymZTOey821cOG3tuB5Qw-mbc6_gaotDwGAdqBmF51p9ah5GhfhZVpTDoXsma8z509tyoi5qZkxlz_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e08049b3.mp4?token=ChSkHMu_uEkW4DYEZYJABIdTwwt3O7cEE8Wsfr90MuG4FexLAWojiJOyu4_VKT59uSXUAmr07tKGBudhAkDPXhKV28CdWtsxNONJ_WHeOUIksTWXS6OYlNE8eBgxANQCsEmaq9V5Ni3Azf3sK4W5_TX22UpuAUZt6Tn7wiytDhfYlK3GKp728U7JvFmeXlXdfkUrPnzOvivMax7OuDKZr418LLaDZmiic_1QDxtAsg8o93rhKIpoBXLXU879K0oqjL4vhw_yymZTOey821cOG3tuB5Qw-mbc6_gaotDwGAdqBmF51p9ah5GhfhZVpTDoXsma8z509tyoi5qZkxlz_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برداشت ۶۰۰ همتی دولت از منابع صندوق توسعه‌ملی
داوود منظور، رئیس‌سابق سازمان برنامه و بودجه:
🔹
رشد نقدینگی و ناترازی در دولت زمینه‌ساز بروز تورم در کشور شده است که دولت به کمک فروش اوراق و همچنین برداشت از صندوق توسعه ملی به‌دنبال مدیریت این وضعیت است./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/688491" target="_blank">📅 14:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688489">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sO8v0MDF3QkxaMcows-Y7zT3YbbsAny3yx2geRpNvwYzWcx_AjLDQ4qI_jLfYz-6TVrkHIi8VVjKf7hUc_-zjqKuv54SgHedwbYLJZIB0-psQW0UNVmSlbYnKp_hNrb5FPxaIAxuBD24L8-I-IwL4hDiX07nl1B6vESc1flyGLSY4X6164k77XLWh2JgamiKglVsJzxtR-ABW0r_tRmTcfuLxAlJvI7L6BOhMHGNeCA38sRbVJNOOF9x5NMESAVnW9J6DDGjyJIil5mkwCpXWtuhKd-NKL2A-_XHDt6ZrortJFMEZNXxN8RIpoQAlOLmR9gUHX3E-GWJx_YCA0lMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UL_8PnXZc5uOE96hW5nMbCUsvvngNMmgGUfocg82f20x6UPIwmHEwu10bDSKn4_2cUHf_A-VcdATjWY7sUHLowvgELFP7ZuPb_3egt77_0lYgdorpih1o0deMcXABTX8cccVpE5ShOyqpD76k5zUZaW04ypOpf7zBA3tw7WocgWaN6Ppt8iUJK3gR2R1VPp953OojIA-TASpib3Qx24U8ZF4PQdWZ_T_Cw9DmRylx1RnUmK06lL2vHmvpP8VSJcE01dsyiQM-NyTloFExu1MqwfNzW_tucDHVvkIGEB9qyJ3XcV5ox71ImE7NcN9ciUxzUrpKvILorAydplc8f6SLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این هوش‌مصنوعی مثل یک‌خواهر بزرگ‌تر راهنماییت می‌کنه کدوم لباس‌هاتو ست کنی، چه لباسی بخری و کجا چی بپوشی
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/688489" target="_blank">📅 14:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688488">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d5b369d9.mp4?token=OBS8Mc2fdgykqVzrA8c4T4NgxbXxFOf89HTN2DPHV_6JXufkWp1K82G38eUw69hirA-q1V-1_PRfJCjaUfJYi_91IdnaNLRU9Ob2z8OSzoDnJLeyLVcfuK879Elkdj7fvNjXlx5DgHfIhzLaqcqh6ikrzOZ-ISFmcsjq4J1yuLauY0csdnIqjmZEgmReiO_djNoNjwn3pq7IPIMesBy-P1MraQTO7Q-61cRl8GhU3af89737pmTXutIM4vyxYXIhluQURm2MEOIx-hRyxHiA9ZMR6Ahl2Gu8JUxBrfDt6kkXMFtV-eWTl2hIays_hphnt_ZTvY2g9Bj1bmWOGeA5CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d5b369d9.mp4?token=OBS8Mc2fdgykqVzrA8c4T4NgxbXxFOf89HTN2DPHV_6JXufkWp1K82G38eUw69hirA-q1V-1_PRfJCjaUfJYi_91IdnaNLRU9Ob2z8OSzoDnJLeyLVcfuK879Elkdj7fvNjXlx5DgHfIhzLaqcqh6ikrzOZ-ISFmcsjq4J1yuLauY0csdnIqjmZEgmReiO_djNoNjwn3pq7IPIMesBy-P1MraQTO7Q-61cRl8GhU3af89737pmTXutIM4vyxYXIhluQURm2MEOIx-hRyxHiA9ZMR6Ahl2Gu8JUxBrfDt6kkXMFtV-eWTl2hIays_hphnt_ZTvY2g9Bj1bmWOGeA5CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎉
فروش فصل پاییز شروع شد
🎉
جا نمونی !
🛑
مغازه‌دارا و فروشنده‌های پوشاک، مشتریات منتظرن...
*
✨
مدل‌های ترند و پرفروش
💰
قیمت عمده واقعی
🚛
ارسال سریع به سراسر کشور
📦
خرید مستقیم و بدون واسطه*
اگه دنبال سود بیشتر و جنس پرفروش هستی،
همین الان وارد کانال شو و لیست مدل هارو ببین
👇
🔥
تولید و پخش نیکلین (منگو سابق)
https://t.me/nikleinn
https://t.me/nikleinn</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/688488" target="_blank">📅 14:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688483">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPpkSPIhE8bMVj7W5GGJAgHjcMvqs53ZURGiE-H9eb-yVkELHpAxbXWOsLI16sHcFgwBq_QuWdGiGLjcSQeglQuH_XGHJI5GD7l_WlvBRR7RKoBSb_eaTBX_KvwhdHcEKcNDyb__fuQyHFkZwBwNPwZ4xa_Nss5Mi1vHfrp1BPDXp4nCYvBnfKU68Dp6p_oYwwLHjlEmNVPfClYwp88zPvDIMWGOtAtisUsWQNmALztzY_Z-9xEOxp9NZfQ0hvDsx9azxYPdmCiy6dOIPtInlr9Fl9TS4OT5jeHZ84IR-F5Mbk1jMyAYJTp0M9koTYaRFKKlw-_5jF-kR33IgkuXFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MhRzfWrVMoF4FQzZFMBr5_adkwwsD790Aq21FB8GI5f5a9MflfZYxo5f2j1TKq3bYYq604eYsBiqVKzeUHE2kwFZ-Bnm_l2M67gz617EhwwVRkCh6ugvW3gQBluKoTRWU8I3tuOXIwM1pVEKNsN42xovDLhsrUcJ7Q2P_oCR4HEIhbCrorR5DlLIk95D_6EaJOczCzZoXZrz4eIzYQORMz8oSiq5mGhk0tT_QkmZsclPKeqxrKbP25arYQcKmVU78K-qKgdAKHQFCQHombFDnYkNzsho6OnatK109BjktY5aO1I3K4hcHPH7yxmAnAYNLblTH_ShEP3_m1nzIuHDtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBWRN32vSSWYImvAa9Q2Q4_3vQvX78EeaSyaEiqGXFl6sHZAHH-pzs2s-dwz2TTLZroAArVQlgGU1KW696p7LWJu1tJ-O34C1c2Jm2ZJaGW9GcuqS9wLrr8uC1v9Oqv9G7Uvi10jBGEUwpwMCH2ygJO1byzS9vUzpQwlbjxqiIgu0889ZGrEn1zNMEgEIBt9JSLSFffzdtPqOBQAHwV1AiDXdcfadiOSIw-qtLG7FqT-ypDiDDIDDcAirSTGRKbzuIQNC_1oT9AXY6rIbpb6EtNgM2ep9fDBrFN5L607_cz-NVnHfa5vE5bqPrrctP5M9H3tc4SsO2En52_1KHZ42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7GLaYOMAGJiM1pECX3FLSp809FdoK_BpPLdGPIjb1QnvpUcnH7F8bne_JE5bbH7bOFNhBcsyngbngvrPN_cv9jUqb42Htjnb7e2aFIk3RDhlYMrlTiR-aiv2_nQUgty8AD8HaHZbBZF6nZCtvfpGiCbcgm2I8mH9Sa-OTg60iG7dFeFQCLUu1t2YZLgKVmAsNCTA8OPR9W9d_1L-ak2fS2C0anHNVAvSE6BFGqjAyClqdbXzcNPXoGwBStgR7hhCWdfLdT4E8DftCWQYOMACq8Z6OYHlfzwXHOMhukIOkH287JTKDyCO_xFNcoWhge9LzOQGhSU-KZJFAEo5osT3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/usJMakPppxisIHpAsdC-bFwltodHjiPSzEH4Nj8d_AbcDPNsgfCkrOIv519KSUhFqu53ljPqDGEJLezXnqAOWlNuR7qtkCURdgpL4nicye-m9F8rKIo-R45T6J2Ffyof55XYGEF91MoLSnH1WukEr6MO7YWwFXSiizo37xKXJRNhfxeEVDfB2pL2vhMTvO3aFkvPykqDNQoyDdtNd04xfB9JYBzCMCcK214iwUI1qw67N7fF8T1D6dE8CSjwp_lvEgiy482PWF3hMlr6jqQwrxDY_Xk9mymtWYs-CrtTQUFVOVB2-ujleRude_n12EaIDhemWFPzjbeizRZC7Hkx1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
تجربیات شما از گرانی، کمبود  و جست‌وجوی بی‌پایان برای تهیه دارو.
🔸
در چند خط  روایت خود را همراه با نام، شهر و نام دارو برای ما ارسال کنید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/688483" target="_blank">📅 13:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688482">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szYH8O_kXsmRkvNQ9EOKatD8kuhjQsUBZ-bWt20WTFs8_QRLBNIkkVcCy3bibYaHa7wUiLr8gam9L-9BywZmBctn0XByEFk158wBUNmXJPIhVEWCs0rESRp3MhkFl5-ls_9JGevg_2mUpcJCIyZqQ1VPUBa3SW13-yt_UVCCeOe-NrGuNdvVuYJITSq9pQKySbMULSbJqq7BZY_eDeTSdhjJAte3lJibtTF3aCRP9X0m2NVP7FHG7Gfkw-JWr4VcUjIyOf-_3nSZFxg-Y1OLFZ9FSYi_fwhSRRIemK193UrlEiMjJWipHGZ9THWVYs4hisZcsT2zjDhKuQugijtcRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگه خریدار آپارتمان پیش‌فروشی هستی این حقوق رو از دست نده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/688482" target="_blank">📅 13:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688481">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ir_z5ixsZJjI3YMZCwiMbeUsfnXPRGjThKlrGimpjskhb7SEWBj71MPe6u6OwcjdI0_NkJZrW5vKbea351rGFZFPT3uAuN1LLgxdYwmmgS2pprI_JENr5Zo09lLNEGG-9iRwrDQiSmmqVwl21GhUBR9CDFQvet0UCbTcGgHK4QmtuJS75tDv5VxySEl4Lo_GwpiVFVFA0MwRirfLQgvaky_XbmxlsEMSkNpfeRwc7N6ZS1pcMaosZNmTV-qGzpYfTo79Vz8FnR1eeIdGfOrsRhi7j0DvAFVaPtHRMgbqevJAoAwyYwTcqDAbOJiSBFLFc6BLFzZD9SGycJUzPWgCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره تعرض ارتش تروریستی آمریکا به شناورهای ایرانی و پاسخ دفاعی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/688481" target="_blank">📅 13:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688479">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64eb224b0d.mp4?token=h2iv_xSxNe0wOEc5d-ajNfaGQF_zfrigzNFKcMe7hEue55b0WnzeF55PHZD1t84uWnY9WyNq1mZHZMyk8P5_6ps-6lJlb7lom5jBiuYwU-q7Eyg0zSsQsElxIXx1wAQXD5JSjkG5mZ2L6YK4BG09jN2bZyNZ5Inob9Z9coqb7GlYvK6vYmt8_4wJCCFctlQdtMHIlZ8C33lbLIRuYFYcJRjSvErSOdRODHig6BaFI059CevUvc8RCy1de_A8lKE4-5RdYSuI0mcr6andu-reP1rsezUTdvI8uhTKg1s2gav_AjBMfgUxaMYfjYEmigoIH7FCTnQPDnVWT3YixHgtxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64eb224b0d.mp4?token=h2iv_xSxNe0wOEc5d-ajNfaGQF_zfrigzNFKcMe7hEue55b0WnzeF55PHZD1t84uWnY9WyNq1mZHZMyk8P5_6ps-6lJlb7lom5jBiuYwU-q7Eyg0zSsQsElxIXx1wAQXD5JSjkG5mZ2L6YK4BG09jN2bZyNZ5Inob9Z9coqb7GlYvK6vYmt8_4wJCCFctlQdtMHIlZ8C33lbLIRuYFYcJRjSvErSOdRODHig6BaFI059CevUvc8RCy1de_A8lKE4-5RdYSuI0mcr6andu-reP1rsezUTdvI8uhTKg1s2gav_AjBMfgUxaMYfjYEmigoIH7FCTnQPDnVWT3YixHgtxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دعوای پنگوئن‌ها با میانجیگری کارکنان باغ‌وحش پایان یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/688479" target="_blank">📅 13:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688478">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعا شد که ۴.۵ میلیون دانش‌آموز هوش مصنوعی را آموزش دیدند
احسان عظیمی‌راد، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
از سال ۱۴۰۳ آموزش‌های مرتبط با هوش مصنوعی برای دانش‌آموزان و معلمان آغاز شده و طبق گزارش‌های ارائه‌شده حدود ۴ تا ۴.۵ میلیون دانش‌آموز با این فناوری آشنا شده‌اند هرچند این به معنای تسلط کامل آنها بر هوش مصنوعی نیست.
🔹
حدود یک میلیون دانش‌آموز و ۲۰۰ هزار معلم نیز در برنامه‌های آموزشی مرتبط با هوش مصنوعی هدف‌گذاری شده‌اند و در بخش معلمان این آموزش‌ها آغاز شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/688478" target="_blank">📅 13:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688477">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjOJ4voUSDfQG01LleCeAyNZhR3aTdBMvbtRLdyMCBTCzlu3hRb33SJojK0yMNou4CH5BdYZR_H-N1XDOZ1GjyWg1Gt-4aTNpQ_6j5EGnFhd42D2EsAHELdHpX7TJaMG_BXQGpTsQ4pKmMsNp-FhxfgJ15UZRomXZPmBf6r7bOmdv52sudF4hFdMBeYA6apm7xC2yJf_b7lijSVkRnd4pU7OIpUG6SsndL0FGnFPB06PNrjVfh-FgUjbD_LKTMb2Kyye06mjsBrX__-w0y7ngPN_0kvFEciBFyMmIBnrClhe3S7N-bFsTw4rEYkfAu-VRcq9FsUhp4O2X4wBlnuaFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موشک‌های رهگیر آمریکایی به‌شدت ناکارآمد از آب درآمده‌اند
ویل شرایور، تحلیلگرآمریکایی:
🔹
مسئله فقط کمبود ذخایر نیست؛ واقعیت این است که موشک‌های رهگیر آمریکایی PAC-3، تاد (THAAD) و SM-3 همگی در عمل به ‌شدت ناکارآمد از آب درآمده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/688477" target="_blank">📅 13:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688476">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp8XKuYSI0lIwAljZH2cy-BYLfNRd7ipKBp_6CvRN-37r3prgBu6dKAb1X5IHZudkiU7WdXJif73kMTH836Bei29e7jcXXh04SQ8Gmp5dwSYFXvDqHs9PX6KBdV3QMiyf7LiwfX-i_mkREKj9AysptCGd1aA4BFXK6JIY0rKVRZIKDUDDoO-D8HHPUMYkchLfPJyOjz6HiVgVJT3ej8rNzoZK3C__nGcBdn58R6MFPBbe6PP7g_7l_M1PpFihahjr5QaQLS4d6r5dT7ntBpRhsazH9heB66uVjetUncCrz-5fDmMTjo3iebMiRnXUhekBAp0CCHNziAe31pUQSYfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
والیبال قهرمانی آسیا/ عبور بلندقامتان ایران از سد دیوار چین با طعم صدرنشینی
🔹
ایران ۳ - ۱ چین
🇮🇷
۲۵ | ۲۳ | ۲۵ | ۲۵
🇨🇳
۲۳ | ۲۵ | ۲۲ | ۲۳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/688476" target="_blank">📅 13:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688475">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a639b5f41.mp4?token=YVekwghIT5jZsjDAyqTaD4-j7_u8QVN6Or8qjnsHstIHujQtcYSY2QUShRpJRc0ULX6iXjZ_lLKuQporcgi2nMLyFrDdx1x_1qQ7eiV-U4aAsESXH2yux_O30kz1YDz4Gp_kY8_6c5tDt6hqcw6MpKSd2lFIOrR33ObpLl-grop_922X58kDypb5xEofTHCBXUz0kS1lqGnhsl_cPq1S0A0KdgCZcitgNfyp8XlqYDde5P8CqVk8_FQD5kQzdzvOEoKZ3uOWA90-N1uD4N4twEml5ztsbhpgMfgvluNmmALzxM46-yBGcREkl2M45yF9K9_87AlUIyH7YpQu3KOyqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a639b5f41.mp4?token=YVekwghIT5jZsjDAyqTaD4-j7_u8QVN6Or8qjnsHstIHujQtcYSY2QUShRpJRc0ULX6iXjZ_lLKuQporcgi2nMLyFrDdx1x_1qQ7eiV-U4aAsESXH2yux_O30kz1YDz4Gp_kY8_6c5tDt6hqcw6MpKSd2lFIOrR33ObpLl-grop_922X58kDypb5xEofTHCBXUz0kS1lqGnhsl_cPq1S0A0KdgCZcitgNfyp8XlqYDde5P8CqVk8_FQD5kQzdzvOEoKZ3uOWA90-N1uD4N4twEml5ztsbhpgMfgvluNmmALzxM46-yBGcREkl2M45yF9K9_87AlUIyH7YpQu3KOyqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عباسی معاون وزیر راه و شهرسازی دولت سیزدهم: آقای رئیس‌جمهور! مگه نمی‌گید هرکی می‌تونه کار کنه بیاد؟ من می‌تونم کجا بیام؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/688475" target="_blank">📅 13:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688474">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
«پروسیجرال» کنترل ذهنی پروازها نیست؛ یک اصطلاح تخصصی در ناوبری هوایی و روشی استاندارد برای ارائه خدمات کنترل ترافیک هوایی است
🔹
مرتضی دهقان، معاون وزیر راه و شهرسازی و مدیرعامل شرکت فرودگاه‌ها و ناوبری هوایی، با تأکید بر این موضوع گفت: کنترل پروازها در فضای کشور بر اساس تلفیقی از دستورالعمل‌ها، فرایندها و تجهیزات انجام می‌شود و همه تجهیزات نیز محدود به رادار نیست.
🔹
عبور شرکت‌های هواپیمایی خارجی از آسمان ایران نیز نشان می‌دهد که این شرکت‌ها به دریافت خدمات ایمن و استاندارد کنترل ترافیک هوایی در فضای کشور اطمینان دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/688474" target="_blank">📅 13:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688473">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
بستری کودکان زیر ۷ سال همچنان رایگان است/ رئیس مرکز طبی کودکان: در تمامی بیمارستان‌های دولتی درمان بستری کودکان زیر ۷ سال که کد ملی داشته و ایرانی باشند رایگان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/688473" target="_blank">📅 13:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688468">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa042eba94.mp4?token=HpJkr9n9yj4tF7tlzNYszwHrBlwkTTyGBfWU53gOGR0WX1ccfEWrrkMHcOYqMRcFCdwVOSZAxyg6NJcr7meu-DdlljkjWFa0fqexyYRgWsZmmc2MFiNPINLxh6z7ibfuQ49CcFFrm_1MedC1KrdBrlZvyLG-k5y4v4Gn9Lm8WrLoXt2x-dEbmwzPsaGQIpxYSryFDVtZDDr_psUAA4t6BpqpzPc37_fMjg9Rw_18L_6pjBqTSEgHc0pOLwXc_ZV10bFQHIDnvoghfCpRWZLB4N8fSgvlBxdtjlGJwBsywPcy2QWilRciL-jcZjAQgk__fCeZRT9JAJQkqwEptInxhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa042eba94.mp4?token=HpJkr9n9yj4tF7tlzNYszwHrBlwkTTyGBfWU53gOGR0WX1ccfEWrrkMHcOYqMRcFCdwVOSZAxyg6NJcr7meu-DdlljkjWFa0fqexyYRgWsZmmc2MFiNPINLxh6z7ibfuQ49CcFFrm_1MedC1KrdBrlZvyLG-k5y4v4Gn9Lm8WrLoXt2x-dEbmwzPsaGQIpxYSryFDVtZDDr_psUAA4t6BpqpzPc37_fMjg9Rw_18L_6pjBqTSEgHc0pOLwXc_ZV10bFQHIDnvoghfCpRWZLB4N8fSgvlBxdtjlGJwBsywPcy2QWilRciL-jcZjAQgk__fCeZRT9JAJQkqwEptInxhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منظور: ردیف‌های متفرقه در بودجه ۱۱۰۰ هزار میلیارد تومان است!
رئیس سابق سازمان برنامه و بودجه:
🔹
دولت باید سراغ ردیف‌های متفرقه که با رقم ۱۱۰۰ همتی، ۲۵ درصد کل بودجه را تشکیل می‌دهد و بخش سایر هزینه‌ها در بودجه دستگاه‌ها برود و از این مسیر هزینه‌ها را کاهش دهد./ تلویزیون‌اینترنتی‌مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/688468" target="_blank">📅 12:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688467">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
سازمان عملیات دریایی انگلیس از وقوع یک حادثه دریایی در شمال خلیج فارس و دریای عمان خبر داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/688467" target="_blank">📅 12:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688466">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfcff78997.mp4?token=sGmcIACNGrcOl7fGeMEQXYoNXlHFCkT0kBTE7AxQ5QzhQE3H3aXJmpD8fezF9PlkdIrept0aGXZjtiR0RagYFLYw3bKaVRMfcTA1lRhIbvdgze-NLJr7OaDiycIhVTbeEISxgmM7mH9Hu6W57qH1yzRgCmik25-Tb7tT2LycRzAfnheuNBqnoUSDCUoQVcZx4wLdwJlYChwMxOJmzmEY8C8AQzQsWKTHwdVdpmba_LYhylHrnWMbQQ8WPbbGLqtfA3bxeWTWtEVun5vPO6HTRodRwd2pMYq_SfzsWaRanqSkGnlkwMZ25aV_Rmy-3WSJqPJvYbgVVUaJ8pT-o46vQjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfcff78997.mp4?token=sGmcIACNGrcOl7fGeMEQXYoNXlHFCkT0kBTE7AxQ5QzhQE3H3aXJmpD8fezF9PlkdIrept0aGXZjtiR0RagYFLYw3bKaVRMfcTA1lRhIbvdgze-NLJr7OaDiycIhVTbeEISxgmM7mH9Hu6W57qH1yzRgCmik25-Tb7tT2LycRzAfnheuNBqnoUSDCUoQVcZx4wLdwJlYChwMxOJmzmEY8C8AQzQsWKTHwdVdpmba_LYhylHrnWMbQQ8WPbbGLqtfA3bxeWTWtEVun5vPO6HTRodRwd2pMYq_SfzsWaRanqSkGnlkwMZ25aV_Rmy-3WSJqPJvYbgVVUaJ8pT-o46vQjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدن دنیا از چشم یک موشک که از جو خارج می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/688466" target="_blank">📅 12:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688465">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hV57od2U2gohUp4BhThRb1t5dooTZppKjCC17j0SXXx3yxiSR9QZ660oAg7bwCdTv43kUvo-H5JpfsHb3JfYShZbpVQ1AR2KbgOHpEIQVPosanHVvRT03VUWbAAN7Ogq9a0tqoqv1VkaHieX4ocYR1e89Z8f_-FrJWyakGEVCVgLOIBnK3PkNhFVqZd8TjqZI506uk_wRl7BFN4QI4bnpCvlYXr8JKGE7Nmt727ipdmlBlSIh9mWjd1ITG4GXcIR7Ot1Kbt2JoGCAr9Wl4_49sJu-W7wa2alDsbqQnBYvknzVqSp-HO4zElIt8eW-j-SkwsP0TXND1c4G850gVGDtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
پک ویژه «عاشقی»؛ نجوای کربلا در کنارت…
کربلا، همیشه در قلب ماست. اما گاهی دلمان بیش از هر زمان دیگری هوای آن سکوتِ پرمعنا و نجوای آرامش‌بخش را می‌کند. پک ویژه «عاشقی» از مجموعه «قرار»، مجموعه‌ای از چهار یادگار متبرک است که برای یک دلِ بی‌قرار گردآوری شده تا گوشه‌ای از آن فضای معنوی را به خانه شما بیاورد.
این پک شامل اقلام زیر است:
📖
زیارت عاشورا
🌹
عطر متبرک حرم سیدالشهدا (ع) حجم ۲۰ میل
🧱
مهر تربت خالص کربلا
📿
تسبیح تربت خالص کربلا
💰
قیمت اصلی:
۱,۴۶۴,۰۰۰ تومان
✨
قیمت ویژه با تخفیف:
۱,۲۱۴,۰۰۰ تومان
📩
جهت ثبت سفارش این هدیه ارزشمند:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/688465" target="_blank">📅 12:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688464">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/688464" target="_blank">📅 12:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688462">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
تجربه واقعی از پلتفرم‌های انلاین/ خالی فروشی یا تحویل فیزیکی؟
🔹
پلتفرم‌‌های فروش آنلاین طلا این روزها متهم به خالی‌فروشی هستند و مردم برای خرید از این سایت ها دچار تردید شدند.
🔹
چالش خرید از این پلتفرم‌ها چقدر می‌تواند قابل اعتماد باشد و آیا پس از خرید رنگ طلا را خواهیم دید؟! یک خبرنگار این چالش را انجام داده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/688462" target="_blank">📅 12:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688461">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعایی درباره بدهی دولت به واردکنندگان کالا
داوود لپه‌چی، رئیس انجمن حبوبات کشور در
#گفتگو
با خبرفوری:
🔹
بزرگترین مشکل فعلی بدهی ۴ میلیارد یورویی دولت به واردکنندگان کالاهای اساسی است که حدود ۱۸ ماه است پرداخت نشده و بسیاری از واردکنندگان با ورشکستگی و مشکلات بانکی مواجه شده‌اند.
🔹
واردکنندگان حبوبات کالاها را با قیمت مصوب وزارت جهاد تأمین و به سامانه‌های مربوطه عرضه کرده‌اند، اما با وجود گذشت ۱۸ ماه، هنوز ارز تعهدی خود را دریافت نکرده‌اند و این موضوع چرخه تأمین کالاهای اساسی را با خطر جدی مواجه کرده است.
🔹
با وجود بسته بودن مسیرهای جنوبی در جنگ ۴۰ روزه و شرایط نیمه‌جنگی واردات حبوبات از طریق مرزهای شمالی غربی و دریای خزر انجام شده و خوشبختانه هیچ کمبودی در بازار نداریم و پیش‌بینی می‌شود تا پایان سال نیز مشکلی در تأمین حبوبات وجود نداشته باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/688461" target="_blank">📅 12:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688458">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
سازمان عملیات دریایی انگلیس از وقوع یک حادثه دریایی در شمال خلیج فارس و دریای عمان خبر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/688458" target="_blank">📅 12:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688454">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYVnkAFbi3Q9vJkxTph8cbl9a3TFJctGjPxtYSVqVeFirh_vOHBnIaPf7PlnVNDN19183gOvXVgdT8lsDGT9uzIhEiFcFOmiSSnypUPZrn3vlfKbo2pAFAOH20vv5cSwpPwKyUOkO9pbiRlwca1A7Zy8U-jWJSJcoiMzIofJ59DT-VttPAW1QvR6UW3swX1w-CCNm_2ERpaea7QdLmKrRgZl1fW027P927jaaQuYcpwMFLdcTowAjQgYI0Hp-Mu89v16hzjZdLP9Ly5GkMwy9jkoH9dk3O94g3Ij76xT0ZE2JU5KuEQ-7c7Fc4sBFke055m6lgeVGpBh0iPhyKcnZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clBM5AKnN38R9tPiH6qT0ADJdrW0M0nP-x_mqtvbAuXoSzQAAw8VoVOz3a2UV0YFmOmndDWYwAFKm68mD2GOlXJl8MFbnDMFxaq93yrcAa2BF6eoRQ6XsZ_eVrNg5jkgWwMq3P9s_EAEeyR_GRnArWOz7MmZgWAsEBRlJsG7LwidFF8S_hKKz_kqHZp-56aWtX2-fHNyxBNOHzzHFVpkqz0uTLu_0meWrfwSz0U_u8imu_GvQMQI8K_VzmkjLgNxDpGludLoEKCI8nA-mWDCdPJYB517wrDGPT4lhALgTFU_Uz2sfYsOj6GDjteRwAll_3P_uzL9z05L6vmcbsDQlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11174a77dd.mp4?token=ZJ_c2EABDXcaQi_vrgeIpyEeqUtiZZGTnPumE0ZjXTTKH8xBHhV22LuvA1reIc1sJioL50oB5O__XS8n8u_exWW35utoP6qFA6BbeRnlONrtFckr5cXiIBUPX0KPdG5PmglIVP8wkR9az3-dfDTyBzdAv_CTylFTr0GI4ZCzRc84t113wj37ohLa2gAKdS7C7UpDxRVe_xZyCWRR6iq_LIrfPeTFOvwtrxjitIdwKnl5lG4Mf1BiVpbFfkM5CSJFt9VznFUynJFXJ4l1FRaSNZO63IJgDYysVTSm1Ac7N4KKGN-ko_5BAvz-SQQb6kUDwGaxlk40P2ZiWObbcPqa2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11174a77dd.mp4?token=ZJ_c2EABDXcaQi_vrgeIpyEeqUtiZZGTnPumE0ZjXTTKH8xBHhV22LuvA1reIc1sJioL50oB5O__XS8n8u_exWW35utoP6qFA6BbeRnlONrtFckr5cXiIBUPX0KPdG5PmglIVP8wkR9az3-dfDTyBzdAv_CTylFTr0GI4ZCzRc84t113wj37ohLa2gAKdS7C7UpDxRVe_xZyCWRR6iq_LIrfPeTFOvwtrxjitIdwKnl5lG4Mf1BiVpbFfkM5CSJFt9VznFUynJFXJ4l1FRaSNZO63IJgDYysVTSm1Ac7N4KKGN-ko_5BAvz-SQQb6kUDwGaxlk40P2ZiWObbcPqa2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجمع معترضان مقابل سفارت آمریکا در سئول علیه جنگ با ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/688454" target="_blank">📅 12:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688453">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/846952efbc.mp4?token=sfUyMYOJIcEH4DKRKyMMeVDpNBA_3UviFFxmV1sQ_XzwaWMG7MIrUyw9gheZjxWLHw_LLqxB9jSX22KyVCwwuHx2dII98NJuPKvvO6eaVt5baGz9ykzNinyhD-iIglElMdiurs9_cSIIoVN6c6eb5uP7TxbROgwRxJc5fP1zmBVIW1hkvm0I1Y5PKQ6sqB2LspCU-J3RtRyPqicGXoKdUhQK2NshjFKlwzzIzFRaIseo7PlXHDHGvC8RC8iSFRsperNm4X5IB27qhPTlDibjXVVRunUYEKFK4-9Ez0UKsNPLmYW_hDGcM-dmwPmHnyXlb9Dspwg2UL4lUiS50qfsqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/846952efbc.mp4?token=sfUyMYOJIcEH4DKRKyMMeVDpNBA_3UviFFxmV1sQ_XzwaWMG7MIrUyw9gheZjxWLHw_LLqxB9jSX22KyVCwwuHx2dII98NJuPKvvO6eaVt5baGz9ykzNinyhD-iIglElMdiurs9_cSIIoVN6c6eb5uP7TxbROgwRxJc5fP1zmBVIW1hkvm0I1Y5PKQ6sqB2LspCU-J3RtRyPqicGXoKdUhQK2NshjFKlwzzIzFRaIseo7PlXHDHGvC8RC8iSFRsperNm4X5IB27qhPTlDibjXVVRunUYEKFK4-9Ez0UKsNPLmYW_hDGcM-dmwPmHnyXlb9Dspwg2UL4lUiS50qfsqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهندسیِ عجیب فراری؛ پیچیده‌ترین پکیج آیرودینامیکی تاریخ
🏎️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/688453" target="_blank">📅 12:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688452">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/570e8110a3.mp4?token=Vo5Rd4VJCCH7vnu-zrAYS6fIWDCbi2z0WQbM0b9J4RYoMX_v0j1jQvPh69Yx4h_q5VC4q1tI40j7mOz56YRnl9p_qDm5DcdUqoWgjmsB8Kau-s_0oxXjnESf16zj2MbkyAYpTgVdPbaxP3jSV6woG0yBCsO2x9SsAJxSOjQgAtKCLlcp7BVmtN4EzeHi93Uk6R2NLSb-_SQyMgQ6IcvAbx90GwPfc2EpzSAZH3Qmy_ihJZnXCvrCYL30Fn-8YczdJ2krYhAtYPzIWriod1a3bKZhyAO7plETdnEFOAcoJqB4MmJmCvydBfjfsm1uDlqpC7O8x6kpd-AZbYGMsaHK9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/570e8110a3.mp4?token=Vo5Rd4VJCCH7vnu-zrAYS6fIWDCbi2z0WQbM0b9J4RYoMX_v0j1jQvPh69Yx4h_q5VC4q1tI40j7mOz56YRnl9p_qDm5DcdUqoWgjmsB8Kau-s_0oxXjnESf16zj2MbkyAYpTgVdPbaxP3jSV6woG0yBCsO2x9SsAJxSOjQgAtKCLlcp7BVmtN4EzeHi93Uk6R2NLSb-_SQyMgQ6IcvAbx90GwPfc2EpzSAZH3Qmy_ihJZnXCvrCYL30Fn-8YczdJ2krYhAtYPzIWriod1a3bKZhyAO7plETdnEFOAcoJqB4MmJmCvydBfjfsm1uDlqpC7O8x6kpd-AZbYGMsaHK9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💡
چراغ قوه ۸ کاره  LED TORCH
💳
868 هزار تومان
🏠
پرداخت درب منزل
❇️
۳ روز ضمانت تست و تعویض
خرید سریع:
http://istgaharzoni.sabzgostarr.ir/FastCart/smscart/5872</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/688452" target="_blank">📅 12:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688451">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f90226e0.mp4?token=ux03rHkWfXEi9I2YhyYljM0GaiU9zad2B3B0rjhX2w4CInulGei4FrIncAEH7zlsZT7PDyw4GKJq3WBD7UeNfgbIDpco0guSgH60v2Quo-ed0JA_-rvYG5ZLuqGg8iKqQK5ZNaT42SovoYxmXwbteA8M5bjCy8AphxCHovtZDHw08PUr57gPpBXgHrkU-s3ndCHlUlzTDY3eC9K_qLN1PtPol3i1kSXiSjfp9j9UC6hM4GoVYzdmRx3Uk7m81Y_XMeVR7AUUIzWIlXYauotYrcZas_k6XF9cRHNUQdTEPQiZZyZZscSUUGUNvDJm2_pl4G5O8Y4h3sqohlwCZvA-mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f90226e0.mp4?token=ux03rHkWfXEi9I2YhyYljM0GaiU9zad2B3B0rjhX2w4CInulGei4FrIncAEH7zlsZT7PDyw4GKJq3WBD7UeNfgbIDpco0guSgH60v2Quo-ed0JA_-rvYG5ZLuqGg8iKqQK5ZNaT42SovoYxmXwbteA8M5bjCy8AphxCHovtZDHw08PUr57gPpBXgHrkU-s3ndCHlUlzTDY3eC9K_qLN1PtPol3i1kSXiSjfp9j9UC6hM4GoVYzdmRx3Uk7m81Y_XMeVR7AUUIzWIlXYauotYrcZas_k6XF9cRHNUQdTEPQiZZyZZscSUUGUNvDJm2_pl4G5O8Y4h3sqohlwCZvA-mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری عاملان شرارت در محدوده فرشته
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/688451" target="_blank">📅 12:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688449">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda33b8b4a.mp4?token=FAGk2RN3ehq0u9uDzK3WNzhFnCoTKqYX5XKfGci3Mm0Xj3GBiQb9lIgtpxDToqxEsNGiaE2rYNvaaf4119yqWKl3cXlJcmkAWM2zFjcuoOq7OFQx8YQIV-TQgwIJ6tWBcMStrru9MUxlheoc4CDR5PoMHS6z0h3jD1HRCImsvntRKxoBZ_5GiUXB5p9Pw-rm5aIi2qVdH4Nhw9wCaePEAkcOHXHvmhsoktRESFZyIxvMYD1XHxqwH5YjZDpziamscNiOPq4GOsm2oMW8t5kX5GoFU6sintOj8L1BViLFANf8l6u3rq2Skjug9ggDw_dOpwse9NiQ8lJR2Bw6zYlecA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda33b8b4a.mp4?token=FAGk2RN3ehq0u9uDzK3WNzhFnCoTKqYX5XKfGci3Mm0Xj3GBiQb9lIgtpxDToqxEsNGiaE2rYNvaaf4119yqWKl3cXlJcmkAWM2zFjcuoOq7OFQx8YQIV-TQgwIJ6tWBcMStrru9MUxlheoc4CDR5PoMHS6z0h3jD1HRCImsvntRKxoBZ_5GiUXB5p9Pw-rm5aIi2qVdH4Nhw9wCaePEAkcOHXHvmhsoktRESFZyIxvMYD1XHxqwH5YjZDpziamscNiOPq4GOsm2oMW8t5kX5GoFU6sintOj8L1BViLFANf8l6u3rq2Skjug9ggDw_dOpwse9NiQ8lJR2Bw6zYlecA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوستی‌های زنانه سمی‌تر از دوستی‌های مردانه‌ان؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/688449" target="_blank">📅 12:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688448">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbpkdZzYs_BB2JlQ25onRWYZV2gw7sfdHJr3jX5QhOAxJh8i3e7uywUfpRYdIJvsWwrIMDIqWQkkgxL8fgeYxguoKR_5emdfS5Ie0hG5MXZidbx_OOgoFgpqkZc7ecoGxkpWJVVEzhqWtrl5QbwbAQNZV3GmgJcBp23fPztzbs8s06WpkAOTpZozKAdAHxn6du4k7ZWR4mWXg15DBYPhEGsWanJgB0M7vA6juxolqz6T4jNdQ1zebiHYAp6Hc7Vhm95ipV65aVoSTISsq2cD3waVmucH6KIJOxGAd2ubAKaKfdteYlKoKzk2N9b74qoaMUwbW7FSz_ZiY6NcKquPcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیش از ۳۰ موشک فقط برای [حمله به] اردن. این یعنی ذخایر موشکی ایران وضعیت خیلی خوبی دارند
هشدار تحلیلگر مسائل سیاسی و ژئوپلیتیک به رژیم صهیونیستی:
🔹
اسرائیل، اگر دیوانه‌بازی دربیاوری، یادت باشد که فقط ۶ تأسیسات آب‌شیرین‌کن، ۱۳ نیروگاه و ۲ پالایشگاه نفت داری؛ و من حتی درباره دیمونا هم چیزی نمی‌گویم.
🔹
نمایش را تحسین کن. ایران دیشب منظره زیبایی به ما ارائه داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/688448" target="_blank">📅 12:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688445">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر کمیسیون امنیت: بر تحرکات آمریکا، تسلط اطلاعاتی کامل داریم
بهنام سعیدی، دبیر کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
عملیات‌هایی که نیروهای مسلح جمهوری اسلامی ایران انجام می‌دهند نشان‌دهنده تسلط کامل اطلاعاتی بر تحرکات آمریکا است و هر تحرکی که آمریکایی‌ها انجام دهند، توسط نیروهای مسلح رصد شده و به آن‌ها پاسخ کوبنده داده می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/688445" target="_blank">📅 11:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688444">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f69956aa.mp4?token=MIuBzlnxSMZXQZn9z9gjYNaw35ODwC9qiUO7J9EZSvTiovDkC0-pyBOXbyVJ81T6qJpVTrvanZq6IlY0bNclE5CkajX6dTNkKoFYyj3LicaCln9ItfBJfQNPpPhNKgMeg0gkMVZWHEeb9l3dp9OcVOMtkXq3B0NTHpbr-CwVH9MX6sOeVXx1dHKKMb6PvL7QrmrWWlNtCecjEoDpMTzasaBXahw3Dl9wmsIsL3Gx8ADkT9s5j83y4c-Dv1V40p3dSM0h2vC-MnXuQF4t6tVFrB9ai8FBwD7pZoPL8H9BqHTC7wjNAuI4LuSA0yYJ2QrRrWvVw50W4gDgrAtCGIsBsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f69956aa.mp4?token=MIuBzlnxSMZXQZn9z9gjYNaw35ODwC9qiUO7J9EZSvTiovDkC0-pyBOXbyVJ81T6qJpVTrvanZq6IlY0bNclE5CkajX6dTNkKoFYyj3LicaCln9ItfBJfQNPpPhNKgMeg0gkMVZWHEeb9l3dp9OcVOMtkXq3B0NTHpbr-CwVH9MX6sOeVXx1dHKKMb6PvL7QrmrWWlNtCecjEoDpMTzasaBXahw3Dl9wmsIsL3Gx8ADkT9s5j83y4c-Dv1V40p3dSM0h2vC-MnXuQF4t6tVFrB9ai8FBwD7pZoPL8H9BqHTC7wjNAuI4LuSA0yYJ2QrRrWvVw50W4gDgrAtCGIsBsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظهٔ انفجار تانکر سوخت در سنندج  #اخبار_کردستان در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/688444" target="_blank">📅 11:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688440">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdluRrOsoPw-8hThBbd3ILiVfqNhkbEb1akWyo9xhsAL8ExzoNZdimMHDvu5wuGYvsfgX2KxO5CnjoNNDKG5L9K4raEHdb4NQ8jpRExsSI-BF50I4D-Lvvl5mKKM_Eo5PHfMr9VNxwNQbvXKXtVWmIEIBI2nHA-cJZcRbBEM-XIcG3GarrbMxZCMg0HZXFSxgYvLo0CX0N6l3buvTY9kgyy8uqvXIiF4FUZHpCUTqgNM4Ol6LtS-6odFcIr8VHcd9ErlkXULwRZXzY33fXSm3f81U2dlfRYDaA7r6NI5nCoaCgPXbWTB7paj3eVY8d1c-B3xpQAwkqWbigUcE9SDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lWa71v0DTqUnrFLx25rmVpvfGdgTwcWkGoHTyjH9lsg5w8JHMSm_Hcomt-0B9q66L486mUvxjddy4exUfpZ1ZnNHb9fCtoKS4kvicoLnx5o8pnPJGPUrxzSaSWs61Hu_ZmzrruWwoaWReDcg_fzSSw1vSLNDDp0oXc3-lXuSkGYCKbO3sUQej8ddOh1LsNdb2ykPTp70JpPpEGortWtp7hUgudRm0OwJiVRhiabm8dHelzxX4oy-M3CAFkT4fBRYOFQ4zBbEO8U1AhwbzknBky6BcKtIN6-2Rf0zf3uyHoR-QAMeV_g5MUv5vKWen2e_xSeg9J9O599qkrecYQo7tQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اولین گوشی تاشو اپل با نام آیفون Duo و قیمت ۲ هزار دلار معرفی می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/688440" target="_blank">📅 11:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688437">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
تا یک‌سال خبری از برق یارانه‌ای نیست
مدیرعامل توانیر:
🔹
برق دارندگان استخراج رمزارز غیرمجاز تا یک‌سال با تعرفه واقعی محاسبه می‌شود. مردم پیش از نقل‌وانتقال واحدها، وضعیت برق آن‌ها را استعلام کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/688437" target="_blank">📅 11:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688436">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/661fabb507.mp4?token=v7gM5sM7-ObZl7E2R1rXD60nWg29KyqId5WAqoxoTqMt3jGrcIqNTrFUrLUOtnlcbt9emQFadkf0stcIfRjXBuodxrt-lDpe-7OOxP0diwU4fw-NO5yTlGKwPD4anI1OyfUtDcUoAJDROoZpTKmONl3LcWtOfSRAUCTcg8f-VTCSm7AW2_p59aYW1sKUKi8KH8_OgTF_eWhfBZFXaDReqKPStfEJTynJUKbqB8TarB3Olup_saH_OVYzstmrbwIYJqC3thzS-aWQ8ZjfHk3ZV19sfi_hGutMUuryOAtFxaR4mV1nWouSUSOyc6368Plu38bZvdy0qa3PJuvRKCyxDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/661fabb507.mp4?token=v7gM5sM7-ObZl7E2R1rXD60nWg29KyqId5WAqoxoTqMt3jGrcIqNTrFUrLUOtnlcbt9emQFadkf0stcIfRjXBuodxrt-lDpe-7OOxP0diwU4fw-NO5yTlGKwPD4anI1OyfUtDcUoAJDROoZpTKmONl3LcWtOfSRAUCTcg8f-VTCSm7AW2_p59aYW1sKUKi8KH8_OgTF_eWhfBZFXaDReqKPStfEJTynJUKbqB8TarB3Olup_saH_OVYzstmrbwIYJqC3thzS-aWQ8ZjfHk3ZV19sfi_hGutMUuryOAtFxaR4mV1nWouSUSOyc6368Plu38bZvdy0qa3PJuvRKCyxDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با یک ترفند ساده، تخم‌مرغ آب‌پز را به صبحانه‌ای بامزه برای بچه‌ها تبدیل کنید
🐣
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/688436" target="_blank">📅 11:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688435">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/688435" target="_blank">📅 11:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688433">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyTzzsdUw9IqxX2qxVCjzWfR5zb9DUoeTVk2EV04_Uq8QbayGRA1VzKmCEeHd9ty39jkH3C3Q03Mm6UojcW3bpCqey2P0eI6BnFVzcXysqiGysShaIp6FgJWKtTR2RxPyhRL01UsZMnjrVl5nLaQKI91syUbqZ3jHTSBDTK12SB_r74lniO4AwBwvLSmQv51LakG4WqNFPmqUMiymOSiC5I6wpFSH5HD37VXYPQllSCfCwc3qOmuq0VAgL6C6HBuSicAau-dSNu-q574Jv1I3e_FVomVLlyvlP8tVUyht-njntcDjcnvnB9LTYok52gywwcxdjNdMcJgNXWX69r_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۱۰۰ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/688433" target="_blank">📅 10:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688431">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxeAFVcj5d1Gaf4zaY47AEiyqqowis19HWsWB-UmPeQFFe7pbks-doE77kove_7iuAaaqso6a3HPn9ycNNfNL46ZLPtlKlrYZ3pPKpjXXiMinv2QII5FNY41P5jjNqM3OYb1Bnx4VV4mCIvGrbet3dXPGPVrFVucmuIIER29s8HgKIoveQesCk1w2C0vK2yFVF9MdG54S7E_Vvvb9zoiLDI_5W3x_xJ9OIHczzk3Niof-8dYSlprQ7pQaJCvnCOf6O9NU4kaAbIEjDPTT1hfvconbGUvgm94Rl7TQJNMqe7xMtoxML2bF1RzlZUP3b3TVTuaY5CEgfGQC2MGwaC-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حجم قابل‌توجه زباله و پلاستیک برجای‌ مانده پس از سیلاب در میدان خزر
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/688431" target="_blank">📅 10:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688429">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6bfbf89.mp4?token=mlg4oj6yqySyUUU4vYBGlEAbbRSl7sqzZLnj9jp3wI5dYOsOdBpj3TsEsNvxy_USCAwLXbshT-s5RSSRMAkdLS3lQMad6nygzag2tijzLpaJ4lLYqK8qv39cE2Vu2x5Y2-3GToIZr0BXYu2VWEEYV_VQPsXnbaT-25Bx4TwZfaC4ozt9aCCgT3QPgID-EKiD8zpMwGPRzomWwgNdVVc89LLTSELQpIumiP4bWHAbVa8NHPc75PUCbVGdo6cnRuNShtHRcK1DrYzHdfq4dXmezZ0nJQNsjFEaZFi125FU6Ux91SLvLL283n7aMx-hUaqjmIF8OIdLwid-rIex1jY-VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6bfbf89.mp4?token=mlg4oj6yqySyUUU4vYBGlEAbbRSl7sqzZLnj9jp3wI5dYOsOdBpj3TsEsNvxy_USCAwLXbshT-s5RSSRMAkdLS3lQMad6nygzag2tijzLpaJ4lLYqK8qv39cE2Vu2x5Y2-3GToIZr0BXYu2VWEEYV_VQPsXnbaT-25Bx4TwZfaC4ozt9aCCgT3QPgID-EKiD8zpMwGPRzomWwgNdVVc89LLTSELQpIumiP4bWHAbVa8NHPc75PUCbVGdo6cnRuNShtHRcK1DrYzHdfq4dXmezZ0nJQNsjFEaZFi125FU6Ux91SLvLL283n7aMx-hUaqjmIF8OIdLwid-rIex1jY-VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شارژ فوق‌سریع BYD در سرمای ۳۰- درجه؛ فقط در ۱۲ دقیقه!
🔹
بی‌وای‌دی اعلام کرده خودروهای برقی این شرکت در دمای منفی ۳۰ درجه سانتی‌گراد، با فناوری شارژ فوق‌سریع، تنها در ۱۲ دقیقه از ۲۰ به ۹۷ درصد شارژ می‌رسند؛ عملکردی که به گفته این شرکت، تنها حدود ۳ دقیقه با زمان شارژ در دمای معمولی اختلاف دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/688429" target="_blank">📅 10:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688426">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
برخی منابع از وقوع انفجارهایی در خميس مشيط عربستان خبر می‌دهند
🔹
خمیس مشیط محل استقرار پایگاه هوایی مهم ملک خالد است که یکی از بزرگ‌ترین پایگاه‌های نظامی و هوایی ارتش عربستان سعودی به شمار می‌رود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/688426" target="_blank">📅 10:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688425">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f806d658d1.mp4?token=HPiAVoKPXr909GWPkVp_sMh31E6bKdYw-wFmiuynB7CmmY9IQOOHgOZIpi-yN2laO8aThv--cWayTGVX0M14hrCoRwgM8HsMZijVc8sQVStkvO8j6BvNOKitdJnSt7YSd21ur3P-uIKrHfBr0PsCWWHMKWCmKychbDW7gVvhoNdfp3yR_W6_CAlKfhJ6rC3Sfa9GkMfC2XSJlM52wFV6hFhhZdSUHn_lH8eEhuBjFzLpwW2OQmG_XYofSSPkIeCixBR6qYrpQQsS6wfJ-oILkWhhBxSR2rcW9F31qTZhjjubeLGZFAEGgIha2A3nX3AuihbSv73K50sh1S8trlyeUlg2vdH7SF-3GRupFz5fk_CeA6LhPf2Fua2Vm3Wawl1JRmCVy-0MQOs9PIcXEc3ve2Z-mUyPwGRK8129IWUZ7TgFn1kiB7nRuuPaVC2bqygODNFFp41b9HzY8VDw8yrRuP2pRnKYregyXbnL0InS7Q2EpkE7dcwZsAncV5cP6QteTTiurrUzQ252cpZLZ3C_QungNfO8fP9HGUOHFaBoXzy65ZbmwGFr4jXD8cusgMVGyXZbpmwpeW2eEDMQuwbGymckfiwK7pCB7CptmFvBfjmdi7DyWnQyxEt1B35cK1BaS9yszUZG0xOG6x1Qa2Yl7KR9EqwQzo2xAUct5fGjkPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f806d658d1.mp4?token=HPiAVoKPXr909GWPkVp_sMh31E6bKdYw-wFmiuynB7CmmY9IQOOHgOZIpi-yN2laO8aThv--cWayTGVX0M14hrCoRwgM8HsMZijVc8sQVStkvO8j6BvNOKitdJnSt7YSd21ur3P-uIKrHfBr0PsCWWHMKWCmKychbDW7gVvhoNdfp3yR_W6_CAlKfhJ6rC3Sfa9GkMfC2XSJlM52wFV6hFhhZdSUHn_lH8eEhuBjFzLpwW2OQmG_XYofSSPkIeCixBR6qYrpQQsS6wfJ-oILkWhhBxSR2rcW9F31qTZhjjubeLGZFAEGgIha2A3nX3AuihbSv73K50sh1S8trlyeUlg2vdH7SF-3GRupFz5fk_CeA6LhPf2Fua2Vm3Wawl1JRmCVy-0MQOs9PIcXEc3ve2Z-mUyPwGRK8129IWUZ7TgFn1kiB7nRuuPaVC2bqygODNFFp41b9HzY8VDw8yrRuP2pRnKYregyXbnL0InS7Q2EpkE7dcwZsAncV5cP6QteTTiurrUzQ252cpZLZ3C_QungNfO8fP9HGUOHFaBoXzy65ZbmwGFr4jXD8cusgMVGyXZbpmwpeW2eEDMQuwbGymckfiwK7pCB7CptmFvBfjmdi7DyWnQyxEt1B35cK1BaS9yszUZG0xOG6x1Qa2Yl7KR9EqwQzo2xAUct5fGjkPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرصت آشپزی کردن نداری و یک غذای اقتصادی می‌خوای؟ پس این رسپی رو ببین  مواد‌لازم:
🔹
سینه مرغ یک عدد
🔹
سیب زمینی یک عدد
🔹
هویچ دو عدد
🔹
پیاز یک عدد
🔹
شوید #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/688425" target="_blank">📅 10:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688424">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
وام اشتغال‌زایی ۲ میلیاردی برای جوانان بیکار  مدیرکل طرح‌های ملی وزارت ورزش:
🔹
جوانان ۱۸ تا ۴۰ ساله دارای ایده در حوزۀ تولید و خدمات، برای وام با سود ۱۵ درصد می‌توانند از طریق پنجره‌ واحد دولت الکترونیک ثبت‌نام کنند. شرط دریافت تسهیلات، تأمین ۲۰ درصد آورده…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/688424" target="_blank">📅 10:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688421">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukMHrb1iGvrp6p1slHTb6xoFlVfZ6u6atSKUvZQ4k7NZHNpQlvVWFoVxIrdELkmi51nxJNzAj9omT9GfM64cZfenV73MMn_neiDA_ufBzk-UyuDffdVY9IpAUMN0tT24p51YlltFZrAS0M9brJ3ttPCu5NlKhcII-Ehl-yuWb5gTMjJPFhlaQbB0ikrfPXxt3j-oKDPc4Lqj3lMmN6GAbHB7vdWQNppa5hfcXCJcclxi-1ooKpSJL6ZW07Y23dBXeDvWA9tFkXPNn9hnTxMjf_5yMBIWTP3smxC0zI_nWQQBrU1LH8yZrKIQ2ZC9m11QuvKP-iVAiL1Pn8IvlT4WaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RO73WUWPnfGPs3rnXJUYehsRgf-AlNz6t9ElT4RrrFkFbJT90JPl1GKnzybDlNxovOZ6NV2OE8FCCiqQKa2pyxhqrYG13u6FM7Ekx8YWOMBk1V7bNxqb4yyOrxJe8FPRP024sxn46zBPP9tjFkwROLRL19HVHwH8DNNYeLy_dfwGJmg0FReW5e7D2IAxquG8EgSFSYDQ6zO7Kzwec9t_t7wAe_BFhVTCG7isSQjYF07Jg81Qbwiaa2ObGaAGzLIkXrbBtvAC5sCgePYvwRG-IzpsU_fFCyyyd4qjm2iIun2hnPfNCaz_MIJkoiU4UGLJCVuTEeV522pEgqqu_N6tLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SrFDIjyFHDmBr3lyRnb5dOB04fmKgIwSTDH-AIKVSFmYDHAdeNaT7SToUh8DFqrIo2uVvMvG-ZPWkfH0sSAO8taNumNeuV4hl9jv99k0Mt-QPM3wT6WNR5nzkVsFiQNZRNWRao41xsElAsRUN6q7GDYjBUj-9wG7bGJ9Tgqytz-fGXggSUspRIyBILSuZP686cbZJ_Lsd_yRc-3X0GB5-jylQgu2l4Lrk4mep5QH96Ad-hdsysprdSt7BpzB18o7TXYY5VYBGUAE_XNtvXCWZYEfNbJ21O7_GWF69jvi49jp0JFOu3r6XoC9U434HYLFP6-rjA-mf6J9kH3NwE35GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری زیبا از رعدوبرق در رشت
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/688421" target="_blank">📅 10:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688420">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJv7c_S5S9iGZQk77LzblkvBTyrzgk4Btda-X0jbGGPECWRZT5de1ZmrvsR5jWNYdj0I-BWOlDvMo6FhKBZp252N5YKTlyYyvVOmTnzMU4rBTG8ywoK3h_Rqu5HKiHeAy8VzGM9H5frKlsH2BxRbH8tIH7FNj0WfSMzbjKXnZd5TEeqITeiLaTZ4McJe6LgJfFPBRqlByyodKpfFvCQc35AkMSaBuNX1qW8YN-VSV__UKVbdEw9LOpzrY9yvNhDXScSIPL8mjs4K45Lb6kwu9vd1RNe9BD4JQRM3R_nBT7H3Vshn7OQFJMP-2y8vHHakUjupWnegJK4WgTkR_S8ZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خارک؛ رشد سودآوری زیر سایه جنگ
عملکرد سه‌ماهه پتروشیمی خارک در بهار ۱۴۰۵، از بهبود معنادار شاخص‌های عملیاتی و مالی شرکت حکایت دارد.
🔹
۱۵۰ هزار تن تولید
و
۱۸۱ هزار تن فروش
🔹
رشد
۱۸۰ درصدی درآمد عملیاتی
و رسیدن آن به حدود
۱۴ همت
🔹
افزایش
۱۰.۴ درصدی فروش ارزی
از ۹۶ به
۱۰۶ میلیون دلار
🔹
جهش
۱۱۱۱ درصدی سود خالص
؛ از ۴۸۴ میلیارد تومان در بهار ۱۴۰۴ به
۵.۸ همت
در بهار ۱۴۰۵
اهمیت این ارقام زمانی بیشتر می‌شود که عملکرد شرکت در بستر محدودیت‌های عملیاتی، لجستیکی و شرایط جنگی ارزیابی شود. شاخص کلیدی این دوره صرفاً افزایش تولید یا فروش نیست؛
این عملکرد، نشان‌دهنده توانمندی پتروشیمی خارک در حفظ و تقویت بازار و درآمد ارزی است؛ عملکردی که با مدیریت کمیل پورضیایی و تیم مدیریتی شرکت، مسیر مثبتی را طی کرده است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/688420" target="_blank">📅 10:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688419">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
تعطیلی کنسولگری انگلیس در اسرائیل
🔹
رژیم صهیونیستی در واکنش به اقدام انگلیس در ممنوعیت واردات کالاهای تولید شده در شهرک‌های صهیونیست‌نشین، کنسولگری این کشور را در قدس اشغالی تعطیل کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/688419" target="_blank">📅 10:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688418">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
وام اشتغال‌زایی ۲ میلیاردی برای جوانان بیکار
مدیرکل طرح‌های ملی وزارت ورزش:
🔹
جوانان ۱۸ تا ۴۰ ساله دارای ایده در حوزۀ تولید و خدمات، برای وام با سود ۱۵ درصد می‌توانند از طریق پنجره‌ واحد دولت الکترونیک ثبت‌نام کنند. شرط دریافت تسهیلات، تأمین ۲۰ درصد آورده (نقدی یا غیرنقدی) نزد صندوق کارآفرینی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/688418" target="_blank">📅 09:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688417">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p25IdV4NHdNSDSVMWKG5wcq2ovRtX6z87tsMj-1mnHGtaIb1Uw5cq0gsC68IMsZ_4Dq-qe4Ls8nrBGP30GdI_NiviTXayNgEvNIOzg5Xrc71uKk7jlizD93TmD0GIR-ZNP6MrD-pT3-ZudOsNMDSs2UuYfx1qb8ZkrmdEGlMG4VF9TyK1vdXZ63KV0GRSk4SOKs9ggwxD7OnUVG8WrL-Cq2J7x1lgvW2DhGpm-v5khJ-InC9tc5I8PhKoCtHBVXJFQIG9_Ww7XCFHplaaZ8cle_8mIs9bjlobyy4O48alWJHuJv4mRp1tWVezxbcj1HM-JKHnnr_Zo31OGOQcp6Zkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سناتور آمریکایی به اظهارات ترامپ که به‌جای «جنگ» از واژه «عملیات نظامی» درباره ایران استفاده کرده بود
چاک شوکر، سناتور آمریکایی:
🔹
آن‌ها می‌توانند دروغ بگویند و هر نامی که می‌خواهند بر آن بگذارند، اما مردم آمریکا حقیقت را می‌دانند؛ ترامپ ما را گرفتار «جنگی» بی‌پایان کرد که موجب جهش قیمت‌ها در داخل کشور شده و هم‌زمان جان نیروهای نظامی ما را در خارج به خطر انداخته است. ما باید فوراً به این جنگ پایان دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/688417" target="_blank">📅 09:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688416">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvugT9NMW0f1svxse8VbwRL2kT79IJ0SqXRBq2nWLBy3FeXE2qu3dbpIvW19MFTR1i26T_xyDTDbaHbR3DEjujDtFt7fBiqzFMOkVZQNGI9qvRhYM5f_BR-2hY1RvbvoAnPdGDIuDb2QGbsl6mEAcfNW-pqDZ4rorGCTIgJW2Y4g04jPdlgxJiR1cqNHrPleKPLuO0HeXzA9eHJeL0YFlgQZhedwTKk_zVJ6cOZ-Y2JoUHXHMFS5mWoCY8Aomyia_4wvwzpYcAMHhtD49q4GQcR7TjrDopYLuNHOryOysBFttxQl92egdI7CekWM4QKb4PlOryAz7kDyfwbcIyB52Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پس از مدت ها سانسور؛ انتشار تصاویری از اصابت موشک‌های ایرانی به پالایشگاه «حیفا»
🔹
ارتش رژیم صهیونیستی بامداد چهارشنبه اجازه داد بعد از نزدیک به ۱۴ ماه، تصاویر اصابت دو موشک بالستیک ایرانی به پالایشگاه حیفا در تاریخ ۱۶ ژوئن ۲۰۲۵، در جریان جنگ ۱۲ روزه، منتشر…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/688416" target="_blank">📅 09:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688415">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8dfff2991.mp4?token=Xm-diJ2niPTA6bxTupGWJfagOaE2HS4GjWmVVRZrHHQaHlMsbkYeubXrmyPVmwWTufSNGZm3IEJhwRHgwo57CzBQacPcMuH5WH3ihaAFPPeNXYks0pjJh0avFHyyIgvG1c7ab5A7RDPatKJbxPogvZnvuLesxElzDaazVP3urxCuAUxzh9W7zsrhev-3oQ1iLF4ylToz4AI1e2q5VT1899s6dQYVLWfvSr0V3kCkRVph3y7C4lsQ8obsu-TFKASw7G6Lv_5PKV4HdjP6VAtKXQOUgRyT-EmDl0p58yJkXckQuqT7cwQpKtDBdFKiwtL9tNu27tUFXJ3t_FbsPSqFeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8dfff2991.mp4?token=Xm-diJ2niPTA6bxTupGWJfagOaE2HS4GjWmVVRZrHHQaHlMsbkYeubXrmyPVmwWTufSNGZm3IEJhwRHgwo57CzBQacPcMuH5WH3ihaAFPPeNXYks0pjJh0avFHyyIgvG1c7ab5A7RDPatKJbxPogvZnvuLesxElzDaazVP3urxCuAUxzh9W7zsrhev-3oQ1iLF4ylToz4AI1e2q5VT1899s6dQYVLWfvSr0V3kCkRVph3y7C4lsQ8obsu-TFKASw7G6Lv_5PKV4HdjP6VAtKXQOUgRyT-EmDl0p58yJkXckQuqT7cwQpKtDBdFKiwtL9tNu27tUFXJ3t_FbsPSqFeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خسارات گسترده طوفان دیشب در ساری
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/688415" target="_blank">📅 09:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688414">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDkksBcO3_bJZQmZC6X91Wlw4ouIQjhqibk5gmOoU3R0NU5SHNlfBLrb5wyrkfywB8sYxytws37jtihXcWpyz9J5aNCtTZ6OwoN00_A6joe65hjBRmLLX47EWJLVmwDcp2tVzGsTA0BWMnYfoMqWltrD9QXeVypghR9NGO9Si38sXj1D-r2Tg9OhWFftuBSB3G_dzRTSr7r49siG1IT1jQUmuibJ9Xh3Q8ZcaFSn6w6NgaVamf53Qn2hqqKPHX7ht54KJqHICV0ZIGnRf6XYwqTalFybFEt6mCJEdiU0xLOh1ZH47HbH3Ow5_19n6Qmzn3TAR8RT9Few5g9KJdgcxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر گاز اروپا در سطح پایین؛ آلمان و هلند در وضعیت نامناسب‌تری قرار دارند
🔹
ذخایر گاز اتحادیه اروپا حدود ۶۷ درصد پر است؛ در حالی که سطح ذخایر آلمان حدود ۵۴ درصد و هلند حدود ۵۰ درصد گزارش شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/688414" target="_blank">📅 09:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688413">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
دلیل رسمی کم شدن سرعت اینترنت ایران در ساعات اخیر اعلام شد  معاون وزیر ارتباطات:
🔹
کندی اینترنت ناشی از قطعی فیبرنوری در ارمنستان است و تیم‌های فنی در حال پیگیری و رفع این مشکل هستند./ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/688413" target="_blank">📅 09:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688412">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04d06ea70.mp4?token=I3AzIN-PaLJ9zLZUflwMHJlojMRdlVEMMJatSro2ENs8vIL8Q62RCi6ewe-rAtPim_-MJTbrn5tZdBWcFyF-192TG_qcU4BKY-yZJatrEX8-y1KXiHMRMmKx2zsEMVzD1njFxnr7g56TeMUrYtbZw5Dm5OvLC0Ud7KBEoG2xKDYrt1HXyAgXS1LZa9Tw5zElaxmSJ8v8ibiGdFY-8ubs-Gh4ZCtJyWUPqLSiKfgxzV_AXY6uNDgKTLKEFzbe_EksMe3ucMmmQlpzo1aZwzl_0U6bO5h7GlRCVBlWUmS2cKCGe_VHNpukyd7CsoTy-Kkiacm0Yc7EEhLDJinnCDAB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04d06ea70.mp4?token=I3AzIN-PaLJ9zLZUflwMHJlojMRdlVEMMJatSro2ENs8vIL8Q62RCi6ewe-rAtPim_-MJTbrn5tZdBWcFyF-192TG_qcU4BKY-yZJatrEX8-y1KXiHMRMmKx2zsEMVzD1njFxnr7g56TeMUrYtbZw5Dm5OvLC0Ud7KBEoG2xKDYrt1HXyAgXS1LZa9Tw5zElaxmSJ8v8ibiGdFY-8ubs-Gh4ZCtJyWUPqLSiKfgxzV_AXY6uNDgKTLKEFzbe_EksMe3ucMmmQlpzo1aZwzl_0U6bO5h7GlRCVBlWUmS2cKCGe_VHNpukyd7CsoTy-Kkiacm0Yc7EEhLDJinnCDAB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۵ گیاه آرام‌بخش برای خوابی عمیق؛خداحافظی با غلت‌زدن و افکار مزاحم قبل خواب
🌿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/688412" target="_blank">📅 09:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688410">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D1kbtydwfrXDHerANuOoMfLWlIzmbIQVsrg1O-vQo2-kkaad68V-y7z0hoUVO2ZGJp-v6SeBHkDqntj4hsfY8nHIWUTbXBgrdF4GlSHC2UH5yQaQ31_gVbKL0hlY5V4KLXxXDa3cSlfOgZv0bs_VPy0mT7ayjLJIIHFjnNbvkPbAKe7-79hHKLK40jMba-DkKQ7WsqiwOXP-fWKBhk07mYUPiaTamRSK7nPi5_Nej_wGzBeM42kWTDd7BKqwA_3haw_bOO9eCRtk6NudAjrbWOVe49big3DB8jqHqO28WZjsqNC7ZSCjDW57OjJz8UCX3Xv3o2oMhUvBp-HeMZG5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Khd06CzRVBCSfkr9t61InV4ca6OOb663g9IvIkqwDkCl1O2g6viYy3153z0c5DBKK76FvMFoVOUayL04Nw4yRXy-ncSDfY41eVzzYSIYFCaOOUAKd0wiPN11jI2qCMOnDPrjW2Q2fs0S3feIvNY_u_5dJVjEPIXTPgL1C1MHhvYqcdvlAv-WJAERStkbRrITlPxeb_xC61zmqaYp9Wz_XNmDxUk0BEudxpwGBpblisCYVWJfiQ25a-dLCltzJ_tuETJ1o6WQFnyMCvjQVmP8X8kCBSkfgVuQCjrBeKK6C5VVXEGwL9qurltdcDqxkx6CxceNdlIu8iGEoeh_nbWS5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ارزش صادرات فرش دست‌باف ایران
🔹
بررسی آمارهای گمرک از روند ۳۳ ساله صادرات فرش دست‌باف ایران نشان می‌دهد ارزش صادرات آن از اوج ۲ میلیارد و ۱۱۲ میلیون دلار در سال ۱۳۷۳، با افت مداوم به ۵۰ میلیون دلار در سال ۱۴۰۵ رسیده است.
🔹
این افول شدید سبب شده تا سهم ایران از کل بازار جهانی صادرات فرش دست‌باف به ۷.۹ درصد کاهش یابد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/688410" target="_blank">📅 09:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688409">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bddd4d825.mp4?token=Xp8ya1JJxGEJCFMpATXEpOxJbc9kZPlRIng45uJxHl8df9D4Ho8KKXtRe0AImYKOLXzzQeMLS9K9ww32RCIQjhjdKr-w-3YNZgwSqEbAYOxDSuqAELNix9V0cVhv8o226eeqC-fNrp0qp5vV3JebwFS3z_S6Y0oCbsiaG2AdltryCffOMxwlIbCXSeHf4hIWij9Jzs85Isi22XhvruKhtz7_vnt3nIqifhK6zWp1F5TSYyIX9CZJZWF_mDs9MSZBsFiEPrx_24cNJySbCXH8PeV-2EtWLXIxI5EoCqjfUZa7Y-GXQhZTIPhIFH1mORvMQ7B85yA_HEX0Rtnwd78vYnOQT999STXv4DcRzfpD-nfJBa62fIXlNdB3-ExIJipvAHD8hgX-ncmd_O9qx_fw4Qsi_5UHC8lFf7tncW3U2JpbMcIKABn3sSZd4NIDsELVW9IjfORuqYJiTq1eGXmHTT4A47N6f84RJuVEteCFD88rWSPey3If-7q90AXFxEa-a17h7Eg4LniaJ-gB3FBSkfVS_SE9GSpJCU1-D3eEQW43elFxGDdtiMS9RsUEv7aNvWwHwiGuagzzWaSE_FoZBWwYPhwh9UT3Sfvj7ZymcpCwWnYiqCWchOWuhlSi9xMAHwaEhhIZHUiXhtptDXs8M8HRw-V3j1RiGK1FE3aMGRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bddd4d825.mp4?token=Xp8ya1JJxGEJCFMpATXEpOxJbc9kZPlRIng45uJxHl8df9D4Ho8KKXtRe0AImYKOLXzzQeMLS9K9ww32RCIQjhjdKr-w-3YNZgwSqEbAYOxDSuqAELNix9V0cVhv8o226eeqC-fNrp0qp5vV3JebwFS3z_S6Y0oCbsiaG2AdltryCffOMxwlIbCXSeHf4hIWij9Jzs85Isi22XhvruKhtz7_vnt3nIqifhK6zWp1F5TSYyIX9CZJZWF_mDs9MSZBsFiEPrx_24cNJySbCXH8PeV-2EtWLXIxI5EoCqjfUZa7Y-GXQhZTIPhIFH1mORvMQ7B85yA_HEX0Rtnwd78vYnOQT999STXv4DcRzfpD-nfJBa62fIXlNdB3-ExIJipvAHD8hgX-ncmd_O9qx_fw4Qsi_5UHC8lFf7tncW3U2JpbMcIKABn3sSZd4NIDsELVW9IjfORuqYJiTq1eGXmHTT4A47N6f84RJuVEteCFD88rWSPey3If-7q90AXFxEa-a17h7Eg4LniaJ-gB3FBSkfVS_SE9GSpJCU1-D3eEQW43elFxGDdtiMS9RsUEv7aNvWwHwiGuagzzWaSE_FoZBWwYPhwh9UT3Sfvj7ZymcpCwWnYiqCWchOWuhlSi9xMAHwaEhhIZHUiXhtptDXs8M8HRw-V3j1RiGK1FE3aMGRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شور و هیجان توریست آمریکایی برای ثبت اولین تصاویر از بازی رنگ‌ها در مسجد صورتی شیراز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/688409" target="_blank">📅 08:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688405">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
سی‌ان‌ان: آمریکایی‌ها ۱۰۰ میلیارد دلار هزینه اضافی انرژی را به دلیل جنگ علیه ایران، متحمل شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/688405" target="_blank">📅 08:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688403">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2382c06d2d.mp4?token=o8Cw_TAQMhF3-b3K-qeMf70kLeT3mtSuS2RJd2jNal17GfnFLCKmYFaYLMROhqisBx8Zy5KIg2OVJrxntx2BGNYG_DKY39qX_5CMAHK2gCWjs62LSm5cloF0OQp7BMd89SB7Ulo_dFro3L3sXrJ1-jUWSYkYZMKv4681HVK7ZD-II1JvpIjvFCeaZ0VPoh1TqOhVszjhMNPE9_OTIz71RocRk2mu5AzuRU7tEdgPEjYnwk5mFnczvgxFGIemGQOheIM1NOZMnMmPJ49zVvkM3cZFS0lQ38Qini4m4ULRYdRtJdHEx2w5x_aND-O1nV9Chg3gAyn281_eU7PT3oLGkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2382c06d2d.mp4?token=o8Cw_TAQMhF3-b3K-qeMf70kLeT3mtSuS2RJd2jNal17GfnFLCKmYFaYLMROhqisBx8Zy5KIg2OVJrxntx2BGNYG_DKY39qX_5CMAHK2gCWjs62LSm5cloF0OQp7BMd89SB7Ulo_dFro3L3sXrJ1-jUWSYkYZMKv4681HVK7ZD-II1JvpIjvFCeaZ0VPoh1TqOhVszjhMNPE9_OTIz71RocRk2mu5AzuRU7tEdgPEjYnwk5mFnczvgxFGIemGQOheIM1NOZMnMmPJ49zVvkM3cZFS0lQ38Qini4m4ULRYdRtJdHEx2w5x_aND-O1nV9Chg3gAyn281_eU7PT3oLGkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انیمیشن لگویی ایرانی، از غنیمت گرفتن زیردریایی هوشمند آمریکایی در تنگۀ هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/688403" target="_blank">📅 08:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688401">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPXwtffDKkZ10gkzR65Vq-84C3EhetLCtPrdBMHjl260-BHqiwDaCE8oYVGYy7Xyd4N-Ed1p4DhC7BgQeDD5Bnhyxll0UJ5GVOl5ZGxQ4lzdnKzlBzc7gEPu9ZsMGVsMLA-JwrRHcCAqM-WP1PVmcVLnTHs_Xgd1Al4C2x5NrBOUba9hMDAZU9oUOr0Sl3CpPrCgKA1ppBv2-wxCxHD4O-ezPfnbUJVTTUPr-VLYqK73jx2jALwk-G4UvGJR5BWClvjAVQ2I1jDnL43pvhiJnDzVLFN-DGrD-pN0-zlqUx3wZ5IwQSr05uedj_ZuYmbcdBnaSK97jbfcEH8Ko_Qu3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۱۸ شهریور ماه
۲۷ ربیع‌الأول ۱۴۴۸
۹ سپتامبر ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/688401" target="_blank">📅 08:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688398">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21fc856401.mp4?token=ICRV_tSu0h8YjkNFGCg3XEY2zxXGJlR-tBwZ3olMQ52d2L330Lr2bWY4c1W9tuRo4INGRhQ6N0AI6so6WQOjDZm6ddXOPSdda88LUMXMOiqNejZNxBY5lmg7lW1EijOTdV1Ukg0UEaKcpyOemLUw9jEPd6p-uNGrTRVbdfNyMIByTvTZLZBar-5wVWXgbWK0FZVHyD05HWDmYHXlMMiIiCXTZwnVze9fuUQYEplkIuf9axrMA-SMNAYc--QqWA-rfeGxWMnOiX0Q6wYuC29MnxjZmHK1LInkazaIZIU3KaGY2qnWuhHtOOz9CedH3HAFCLZvks2184rLhHnv8ZRl4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21fc856401.mp4?token=ICRV_tSu0h8YjkNFGCg3XEY2zxXGJlR-tBwZ3olMQ52d2L330Lr2bWY4c1W9tuRo4INGRhQ6N0AI6so6WQOjDZm6ddXOPSdda88LUMXMOiqNejZNxBY5lmg7lW1EijOTdV1Ukg0UEaKcpyOemLUw9jEPd6p-uNGrTRVbdfNyMIByTvTZLZBar-5wVWXgbWK0FZVHyD05HWDmYHXlMMiIiCXTZwnVze9fuUQYEplkIuf9axrMA-SMNAYc--QqWA-rfeGxWMnOiX0Q6wYuC29MnxjZmHK1LInkazaIZIU3KaGY2qnWuhHtOOz9CedH3HAFCLZvks2184rLhHnv8ZRl4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سپاه پاسداران انقلاب اسلامی: ۲ فروند شناور آمریکایی، ۸ نفتکش و ۱۰ فروند کشتی متخلف مورد هدف قرار گرفتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/akhbarefori/688398" target="_blank">📅 06:16 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
