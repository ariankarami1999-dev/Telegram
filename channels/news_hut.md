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
<img src="https://cdn4.telesco.pe/file/ohJkvxcbBl1svpoh22ptzIfbPgMl0XMzaWEmrgsnZJpNTCho_HFgis0_dxAbh3Y2ik5ra_6q4R82w0G5X_lEXfsI6FBzaDDr-iWzY98DJLGisDiRf60yITCO8Y23QuXs07LIvJNJAhJArDVCpDaUtvHmk3xm-IUlIMU6dv5z2Bj6lTU59IOBsdUAQgEpIZabcT234PBD4LTbLb0Kr5lQTqNS169P_I_l8enRSHcgAOfKXvIAHjbYmXeVVyor4C25gJhOrbN7m177UJIN8TcIgIMTu7Lcn52Nefzy8412r1EZdgBPLdI2UKl_zfvwkULqxea8V3CUxtKjJNwF7BZd6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 222K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 21:45:51</div>
<hr>

<div class="tg-post" id="msg-66522">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f005383e.mp4?token=rhRrvQ-QZuDNg71Kwz4oABbt8EdPy5pe9KaN1TORpzBrpt9YcQfAr9b8rexpndyjHYJZEc0MU0iug_nfSwDhsSShX6RUpT12AF2TTctoWQ3c1PTKtjLbbtnneNPvZZyWhknji8_kT3GYdd2nrAn-dszg-FfJVpkA0N9vuCMStzLhHVdhAKZYYIHgBVU9fap-PQ4FNxdpHkviyiWbo8WXsnEguMJYS_FyZhJm3KIeElHrJxZmoPjkQ8VUnMiSun_wD7V6pY-lxePDXPX62vhiqeUCY1Ix5PWeoOPzidCF6aQIEyIO_LmpBfSE90jc3WOgMGQBt7xf0UFBwetlCkWZsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f005383e.mp4?token=rhRrvQ-QZuDNg71Kwz4oABbt8EdPy5pe9KaN1TORpzBrpt9YcQfAr9b8rexpndyjHYJZEc0MU0iug_nfSwDhsSShX6RUpT12AF2TTctoWQ3c1PTKtjLbbtnneNPvZZyWhknji8_kT3GYdd2nrAn-dszg-FfJVpkA0N9vuCMStzLhHVdhAKZYYIHgBVU9fap-PQ4FNxdpHkviyiWbo8WXsnEguMJYS_FyZhJm3KIeElHrJxZmoPjkQ8VUnMiSun_wD7V6pY-lxePDXPX62vhiqeUCY1Ix5PWeoOPzidCF6aQIEyIO_LmpBfSE90jc3WOgMGQBt7xf0UFBwetlCkWZsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره اسرائیل:
من از تصمیم ترامپ برای پایان دادن به توافق ایران دفاع کرده‌ام و اغلب متوجه شده‌ام که استدلال‌ها این است که «اسرائیل فکر نمی‌کند این خوب است، بنابراین بد است.»
واکنش من این است: نظرات اسرائیل مهم است، اما اساساً آنها از هم جدا هستند
@News_Hut</div>
<div class="tg-footer">👁️ 313 · <a href="https://t.me/news_hut/66522" target="_blank">📅 21:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66521">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=oo_ocYEUJD0vHZRZtomHvmYWhx5cqpJiOV9TKnL6qwU8vHTMzsus8N4erCMD3rRvZ9x1TonEP95XZ47nGQPDA7fPYhgrUGp-bv7WrZUQE75zuIu5EbezKs4juo55DIGc0J1aCqZGym-VnBAz0-TJwxSGwx7NMiWjTs4cRwt8FbCNedOKppkhvkUyvAT_HTHZftV2zWD25BqbbvczjDrmo4wkapEXfnKolSf1DdJXZrNPmUiZ6ykk9QcCYWr_TUpjluZNJuqXTcidOk94AG3IZv3LDuAUd90ITvbxZMkUrKO8uXEW7RHaYTUqUBzb-86cVeJgLXluoYlGEG4kgHF_nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=oo_ocYEUJD0vHZRZtomHvmYWhx5cqpJiOV9TKnL6qwU8vHTMzsus8N4erCMD3rRvZ9x1TonEP95XZ47nGQPDA7fPYhgrUGp-bv7WrZUQE75zuIu5EbezKs4juo55DIGc0J1aCqZGym-VnBAz0-TJwxSGwx7NMiWjTs4cRwt8FbCNedOKppkhvkUyvAT_HTHZftV2zWD25BqbbvczjDrmo4wkapEXfnKolSf1DdJXZrNPmUiZ6ykk9QcCYWr_TUpjluZNJuqXTcidOk94AG3IZv3LDuAUd90ITvbxZMkUrKO8uXEW7RHaYTUqUBzb-86cVeJgLXluoYlGEG4kgHF_nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره اسرائیل:
اسرائیل شریک خوبی است، همانطور که بریتانیا یا فرانسه شرکای خوبی هستند.
این بدان معنا نیست که ما همیشه منافع همسو خواهیم داشت
@News_Hut</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/news_hut/66521" target="_blank">📅 21:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66520">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=o5f05IBHt0hKL6QxHLqwQCAT4hclO6s7D0nwa122S0_AVMxA_sKQxDz-L6n9xT8BhWFcwEnbzpiHZXsOyzjPAd7xcBjvT1KfT1coHpDAdrehskoExMMPSZpCmNIzHlnNVYSMF4B5jGVA_KjTm7261Kb979lMuirYEaef-na-uIbFjs5GCIf6SO7fS8IX007We1QBkbpe2Tun_beqtl4T9WpmPSI9BigkD1ysDk9FMhJxis2sXQhYcQNU-DKymk0InWdAh2v4E8jZjT9tvkGvvsEagSpMsa6aGematt8c1tq0Q8O8X5G65c9rTeW098W-8QghmUq24c7eCz_rTcJjvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=o5f05IBHt0hKL6QxHLqwQCAT4hclO6s7D0nwa122S0_AVMxA_sKQxDz-L6n9xT8BhWFcwEnbzpiHZXsOyzjPAd7xcBjvT1KfT1coHpDAdrehskoExMMPSZpCmNIzHlnNVYSMF4B5jGVA_KjTm7261Kb979lMuirYEaef-na-uIbFjs5GCIf6SO7fS8IX007We1QBkbpe2Tun_beqtl4T9WpmPSI9BigkD1ysDk9FMhJxis2sXQhYcQNU-DKymk0InWdAh2v4E8jZjT9tvkGvvsEagSpMsa6aGematt8c1tq0Q8O8X5G65c9rTeW098W-8QghmUq24c7eCz_rTcJjvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره ایران:
باز کردن تنگه هرمز دلیل کاهش قیمت نفت از اوج ۱۲۶ دلار به حدود ۷۵ دلار در امروز است.
و همچنین به همین دلیل است که قیمت بنزین، اکنون که ما صحبت می‌کنیم، برای اولین بار از ماه مارس، با وجود افزایش به میانگین حدود ۴.۶۰ دلار، به زیر ۴ دلار رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/news_hut/66520" target="_blank">📅 21:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66519">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q751ZHJaVnZ9QlYe2kZGRIbNSBRhxJrq5Ej1NbU0VsqEls_cF-WKuu_Jmp-yEuFXeUu65aCYJptz8yf2U4Uc1Lbstl3R4pKCZ_s1QnaZ-ACPWLksyHLk61axGK5AtiFcXZQLguYBC8eCsaYZ3hz-i5zGPjw8M7_F981812LJilDy9fwWVA7ZLL8jT64wC22-6JIa19EpAR2qhoyS33Ei0Rkvojv5KeOaxD69LHGZ-F1SKZR-X039sP90Z273EOiCgoZYcbWzJOi7maUCpWZorEd0Fovkf1SXz6Xe5ULmKB3B_Lotu0MiTbe42SWTnqQfOB9187AQ9E1g9OJ8RKOeqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هیئت قطری رفته سوئیس ولی ایران و آمریکا نرفتن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/news_hut/66519" target="_blank">📅 21:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66518">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pB9jbM1WbD2lFuw4E6Mj_LO_zJJRHbvqgKeaCxu-awioBhUDJGMyPey-p15SgAhg7bKxaM5AnFzQjWesTmYeq8AAsXwunPJR90G-0L6XwXGiEN-O0Fi-0X7HL4iYFdmC2QZfGY8H7BqKG0WA2JPga9uQoWmSpw1jFRRn1VZfTWEk4dTcTL6Ugd96irhL3Puv5MBOu6BN64ENNPe_-iEjkUO0MJTwmTB7Qy8oCXT1slFoZ1t6FFEF-IM_WnW380xeXgz2zd3ZojMIjuOoYtsD8AKKmRERd_mKKQPbOe8T8kkv59m8E09ZJFCnTmVKXbk9bkDtOi5oQsaGgM75Xvibtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌پست:
آمریکا ادعای «مزخرف» مبنی بر اینکه امارات متحده عربی - یا هر کشور دیگری - دارایی‌های مسدود شده ایران را آزاد کرده است، رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/news_hut/66518" target="_blank">📅 21:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66517">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4VamswQSOglcfWTa3CUiVyxNNyxmxkHwr8UUZ94QfLXCMUpiE9w9oruNJ-ZwQdBHppsvkIDLzGbZ1HslCeL-F3Zf_o9_xpRna5o9pGtsQ3D4H-QNCS91HwN0d-ha6oVAvMqXRtmBeJgEdA2fA85Cjk1s4W3A036qB9v0UTPcxVi1KDdFlRPPhvMdESDUC1ftIVo1rb2oaFW7ITpN-a4ad0rN9VSuI4hSh8XIckTFGn2o_XtDiLwQAagqg1X8RlUQXpgzHXOk4tt7AG6pdRWVFyV-altiQ_y7xp4R9NPIEnpz4uoCuSnJu44ObssLi6-O_6ep-G1C1dIm8JZzteR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌های اطلاعاتی ایالات متحده به دولت ترامپ هشدار دادند که نتانیاهو احتمالاً اقداماتی انجام خواهد داد که می‌تواند توافق صلح جدید ایالات متحده و ایران را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/news_hut/66517" target="_blank">📅 20:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66516">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=pswvFv6J4uqxZiXLAslHA5tALG_dB_kdecdJSojNjdqPkxyBo68Ys57T_PhoiTdQknF0RwCTcVxc3SEMcAXCRgOaEBVYq6LCCD09NJ6vgFsl6L7IMnw4wZj2LHtRmtjfI_3Fxiu8XnEos3b-YfUMVeZ5GNBk13uy_o3TStveIP8ijWqX8JXFNHxfDApCrgTAmtY-PbWcXbV8cWdLgkGk4FGSdjNr5JN9tqlCMuYQ1tZrhhliR5OQB493s7zePLuRUMPMPgHh3TO1t4Y65VBMduA0xoJUizZEDzl0Z0L9rB5tzDeLFPEwO09X0QZadw_KVjujE0QXeSaRb7EzwFmQ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=pswvFv6J4uqxZiXLAslHA5tALG_dB_kdecdJSojNjdqPkxyBo68Ys57T_PhoiTdQknF0RwCTcVxc3SEMcAXCRgOaEBVYq6LCCD09NJ6vgFsl6L7IMnw4wZj2LHtRmtjfI_3Fxiu8XnEos3b-YfUMVeZ5GNBk13uy_o3TStveIP8ijWqX8JXFNHxfDApCrgTAmtY-PbWcXbV8cWdLgkGk4FGSdjNr5JN9tqlCMuYQ1tZrhhliR5OQB493s7zePLuRUMPMPgHh3TO1t4Y65VBMduA0xoJUizZEDzl0Z0L9rB5tzDeLFPEwO09X0QZadw_KVjujE0QXeSaRb7EzwFmQ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم، دبیر کل حزب‌الله:
امروز در لبنان، ما با خطرناک‌ترین مرحله تاریخ خود و بزرگترین توطئه مشترک آمریکایی، اسرائیلی و بین‌المللی روبرو هستیم که آینده کشور و فرزندانمان را تهدید می‌کند.
هدف اصلی این طرح، ریشه‌کن کردن و حذف کامل مقاومت و پایگاه مردمی آن در لبنان است.
دشمنان برای دستیابی به این هدف، ابتدا جنگی جنایتکارانه و بی‌حد و حصر را آغاز کردند و با کشتار غیرنظامیان و تخریب گسترده، مقاومت را به زانو درآوردند.
در گام بعدی، ایالات متحده و رژیم صهیونیستی پس از مشاهده تغییرات در معادلات منطقه‌ای پس از تحولات سوریه، توافقات قبلی را نقض کردند تا موازنه قدرت را به نفع خود تغییر دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/news_hut/66516" target="_blank">📅 20:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66515">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=pWsMSRNpixzPkVhr1fqOnOD7p_REz1VUsUgx5-IpW1xTIYOX0GR26Ml7mPqry7jhwWS8rM3iVLPwW9JrKOvrYCnANR5HORyd4xmPhO3nBdYp2NU8JPSbxnx7PbMUpFJN97HPoFqFE5LpFA4Y6_JInNqGLfrl1DNOCpTWpCPCPOpaevoexHg5YoZKFsiXq_4W0ZqNnFEe8SLKXpmH4AeCGEt7xTwx1h7puNUfEESolQAhRfTtOuMa4-ZR4RGO6cwmvvOckUhJ6MLJJ-QDhNqjRMeb7q-HXIScKbQYarnHvP9wjnhJQOa4agb6d04Ze8Xz24k3A1Ldo-dls_e5sNQ8oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=pWsMSRNpixzPkVhr1fqOnOD7p_REz1VUsUgx5-IpW1xTIYOX0GR26Ml7mPqry7jhwWS8rM3iVLPwW9JrKOvrYCnANR5HORyd4xmPhO3nBdYp2NU8JPSbxnx7PbMUpFJN97HPoFqFE5LpFA4Y6_JInNqGLfrl1DNOCpTWpCPCPOpaevoexHg5YoZKFsiXq_4W0ZqNnFEe8SLKXpmH4AeCGEt7xTwx1h7puNUfEESolQAhRfTtOuMa4-ZR4RGO6cwmvvOckUhJ6MLJJ-QDhNqjRMeb7q-HXIScKbQYarnHvP9wjnhJQOa4agb6d04Ze8Xz24k3A1Ldo-dls_e5sNQ8oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
پروژه نابودی حزب‌الله شکست خورده است، نقشه‌های اسرائیل به بن‌بست رسیده است و پیروزی نهایی، یعنی اخراج کامل و قطعی اشغالگران از هر وجب از خاک لبنان اجتناب‌ناپذیر است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/66515" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66514">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66514" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/66514" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66513">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/66513" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66512">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
نعیم قاسم، دبیرکل حزب‌الله لبنان:«تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
حزب‌الله خلع سلاح نخواهد شد. این سلاح‌ها برای مقابله با اسرائیل هستند.ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
«ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/66512" target="_blank">📅 19:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66511">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN_ghPHCScaUhPduIgxmi7xH6sLzf3EPsidTDgP61ievoUb1HBeKyz0B8uIn-uoI7-yAty0OSj6HT0rlYp6xNpSoR4j4rUHXJwtDSBo3Xls6J-gYnrPjGuFWdT5w299cvcvIs1UPdEjdMUO4ZZN5gPSVyVzbKFVzgqHr33Q5EZh2YApmex0CuE9DaCJUX9cpZeI10t8Cvt56j2rpsB91YitakIb0skieW0XhHIAGVpV6RgxqRnI568sehW8lJwi08lc7RIeUfGZcjwkv9CyRvrpDSTSAdAiCDwMVA1pKgqh5ag3i52Ue-Q2TjAaOYb1Zjjick1wM-roqRAc5BnQgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اتاق جنگ اسرائیل:
رژیم تروریستی ایران از نیروی نیابتی خود، حزب‌الله، برای حمله به اسرائیل استفاده می‌کند، به این امید که بتواند وقتی اسرائیل پاسخ می‌دهد، اسرائیل را به خاطر از مسیر خارج کردن مذاکرات سرزنش کند.
ایالات متحده باید به حمایت از حق اسرائیل برای دفاع از خود در برابر رژیم نسل‌کش ایران و نیروهای نیابتی آن ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/66511" target="_blank">📅 19:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66510">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=Mb20T0uqPXDfqVz5-fye3UCzxZ2njVwhFI0zLUXsxk4hb6mwGMTjEFaa2lt8HXrb8HKjm0bfzAbZ3nQQGUtIt9ySFlAqSKNqmEoeIZiUgYLCTvAzdofBcjdk419btM99a2egeRQr4W-LOeYHz7uynqIjk6407FmWxuNny4xoERjfcSiK4YOX7nrHTbIGov5XKS43QVWpeHQhgFGuAQ29c6Bx6usqEGgHtcm1fXNq2TwGLlcT_fAN4XV9SOLo0e7nCZVG7fCVahKXyYX3tnRqpXZSgo0AQp-vJqw_wwdIKXyS4E7mgVtEC8o4xwLafry_lSfe-gKmunT9tGS2EMS42A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=Mb20T0uqPXDfqVz5-fye3UCzxZ2njVwhFI0zLUXsxk4hb6mwGMTjEFaa2lt8HXrb8HKjm0bfzAbZ3nQQGUtIt9ySFlAqSKNqmEoeIZiUgYLCTvAzdofBcjdk419btM99a2egeRQr4W-LOeYHz7uynqIjk6407FmWxuNny4xoERjfcSiK4YOX7nrHTbIGov5XKS43QVWpeHQhgFGuAQ29c6Bx6usqEGgHtcm1fXNq2TwGLlcT_fAN4XV9SOLo0e7nCZVG7fCVahKXyYX3tnRqpXZSgo0AQp-vJqw_wwdIKXyS4E7mgVtEC8o4xwLafry_lSfe-gKmunT9tGS2EMS42A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
«هر مشکلی در خاورمیانه مستقیماً به ایران برمی‌گردد. حزب‌الله؟ ایران. شبه‌نظامیان شیعه که عراق را نابود و تهدید می‌کنند؟ ایران. حماس؟ ایران. حوثی‌ها؟ ایران. اسد که در سوریه مردم را قتل عام می‌کند؟ ایران. این رژیم هزاران هزار نفر را کشته است.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/66510" target="_blank">📅 19:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66509">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak-uId66iN2xxp0L5tlad5apiQkboWY-P-qji-7U_iWkaKvSI68dBFIY98y9DoPZAfUmLZ4wy2eeZeAxYSwakfEKesv7AG74Ic2I34U0fZ9P-Lz4zGE4BDxU9R-Djb7gda2Ejvka1tHA99ZGFaVg20dVtbmfrFJrmSBrCY4kFlZfoAB9bIqxfCaJiK_UynUBc2IGK1-uodBMOGeNDyZ3ZphcsweF4zjn-jGKg7ygKLcojJXdC4lWj9_kDzbBVZ8P-KIfDRv_VbE2BxiUdh6oPA5gTstaP-jT0QnIgE4hB9klzuAVBjsAdwlJoz5fon92dukicvcws2_hPV4_EMC1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسرائیل هیوم به ترامپ:
می‌تونستی بزرگ‌ترین رئیس‌جمهور تاریخ باشی، اما شکست خوردی
شما به منافع جهان متمدن ضربه زدی و ممکنه به‌عنوان رئیس‌جمهوری در یادها بمانی که باعث تحقیر آمریکا شد
به اسرائیل خیانت کردی و حالا تمام تحقیرهایی که قبلا باهاش روبه‌رو بودی، کاملا موجه به نظر می‌رسد
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/66509" target="_blank">📅 18:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66508">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ:
ما از روی استیصال پای میز مذاکره نرفته ایم.این ایران بود که از سر استیصال آمد. کارشان تمام شده است!
ما این دوره ۶۰ روزه را تا آخر پیش می‌بریم. آن‌ها هیچ پولی دریافت نخواهند کرد؛ حتی یک سنت هم نه!
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/66508" target="_blank">📅 18:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66507">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=v9Rykgkj1E6U8L-_UioBcsx86O_1libQv8AAFuhHfIEnMtmLmhC23H3P1CRSuy8XLciAjG3gKJLYCwURScH_hw18nu-2ChuUy4URhLSwx8dlgI5vtKooYWdvHKytsgcf6Vx6rMLp9HqHtvFCI-iVzQ7OJCzQRI-RFECFcSHLHCh-jBzhWb0yuOVPMLVY43mUibzgjbs1EuvzlfQsp1KIx5xkHm7N6WyDTwXC0P39g8Px2xFyfiRh93lxguOLTkcexvW-qqIY_-zNBjWmhfcz29cxgtnPPpS_1NUZk5kXghsiNKzMjHOTCQfDuxkgvoHWXIAjzA5Xd7H7oitKp_u-gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=v9Rykgkj1E6U8L-_UioBcsx86O_1libQv8AAFuhHfIEnMtmLmhC23H3P1CRSuy8XLciAjG3gKJLYCwURScH_hw18nu-2ChuUy4URhLSwx8dlgI5vtKooYWdvHKytsgcf6Vx6rMLp9HqHtvFCI-iVzQ7OJCzQRI-RFECFcSHLHCh-jBzhWb0yuOVPMLVY43mUibzgjbs1EuvzlfQsp1KIx5xkHm7N6WyDTwXC0P39g8Px2xFyfiRh93lxguOLTkcexvW-qqIY_-zNBjWmhfcz29cxgtnPPpS_1NUZk5kXghsiNKzMjHOTCQfDuxkgvoHWXIAjzA5Xd7H7oitKp_u-gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
همانطور که دستور دادم، ارتش اسرائیل با قدرت به ۱۵۰ هدف حزب‌الله در لبنان حمله کرد و ده‌ها تروریست را از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66507" target="_blank">📅 18:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66506">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">Live Tennis</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/66506" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66505">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=YoeyvmIF4KyMeth-KlrcPOSOC9qB_AyY07ieHLYi9k4Z-T7VASrctArWG-dAwps9M53fD51dZPSarGkEdG52RL8FFd8CMYB_a1fGaMMBXejZrYTqCIXaLxsnHR5tm7GnOV95qPcTPdRiNZbLR9tgmM5pwMxaDctobQA2JtqM4I1F5lef7X0I9itXsFeLQ_10yOMpNzDCbKjRhY3Y50n2IHk949qq0NIgAXCCHX0MQF344ae0E-wbSf5dDVgEDsSyFTl-Jicly1kVYB0eU3s2OsSUlxkTuglO-CmnO4D8vpQGwJELrh9ilmX42CZjZoB8XD44tLsTBfbdWFm0gqOIbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=YoeyvmIF4KyMeth-KlrcPOSOC9qB_AyY07ieHLYi9k4Z-T7VASrctArWG-dAwps9M53fD51dZPSarGkEdG52RL8FFd8CMYB_a1fGaMMBXejZrYTqCIXaLxsnHR5tm7GnOV95qPcTPdRiNZbLR9tgmM5pwMxaDctobQA2JtqM4I1F5lef7X0I9itXsFeLQ_10yOMpNzDCbKjRhY3Y50n2IHk949qq0NIgAXCCHX0MQF344ae0E-wbSf5dDVgEDsSyFTl-Jicly1kVYB0eU3s2OsSUlxkTuglO-CmnO4D8vpQGwJELrh9ilmX42CZjZoB8XD44tLsTBfbdWFm0gqOIbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محکم تر بززززن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/66505" target="_blank">📅 18:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66504">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=SSnkbtL0Sb-YZ2q6sgKX2PfkYi5GBnP9PAwM0sBbkfIEphY0L8gPBDCfnpXZf3LO21T-AXyJO6ezLV_TBHF9fWmIXFm9zYdRemEjeptXKcU4VgAvn9dbNpdUrCyDtHbiUdEDllKyywuIWMJhWyiGN9BuGoybu24dIpJ1be-9ecyyCAsFw-obYLldt5_1TIGpvqgBkA_YM_L2UL_tllhSBtPX4n7l65BhPDIAeERgg9iV2iHUCmUctTCiO5k5ipKnrpxdXES4fFrhHGhJCVthQepIoFoekzXCFMKyi4uV5ypiBTqXfAboEUsYtbBatSWfRqMMIdW6-sPe0Kt4bNJ1JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=SSnkbtL0Sb-YZ2q6sgKX2PfkYi5GBnP9PAwM0sBbkfIEphY0L8gPBDCfnpXZf3LO21T-AXyJO6ezLV_TBHF9fWmIXFm9zYdRemEjeptXKcU4VgAvn9dbNpdUrCyDtHbiUdEDllKyywuIWMJhWyiGN9BuGoybu24dIpJ1be-9ecyyCAsFw-obYLldt5_1TIGpvqgBkA_YM_L2UL_tllhSBtPX4n7l65BhPDIAeERgg9iV2iHUCmUctTCiO5k5ipKnrpxdXES4fFrhHGhJCVthQepIoFoekzXCFMKyi4uV5ypiBTqXfAboEUsYtbBatSWfRqMMIdW6-sPe0Kt4bNJ1JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از لحظه سوخت‌گیری جت های جنگنده F16در حین انجام عملیات گشت زنی بر فراز خاورمیانه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66504" target="_blank">📅 17:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66503">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=By-X3l2s_714Hyg1jLRJNhEK1W9nmZBOGJ3hOtMnP2Rcl0mWOaT95I4XysghdZLeyf6ODFXEkCxrTLxtfdvTo3kFPUbZr2GFHyrVv9qYJL5LGxx_i_spQpxzZ-8MQf6lnzXeeAM_UHD5tk4gIZr4wHSonbPv_qGKClaichVTWKcxMXaPbxAfmE-97HCWZb-vfSDzI1tYL8stxULollMhiE6KGC3E6f5WNdx0PTuL7QQo0JrHG2tusBvMCeq0d86vp-QocGR54mX2SSYCkh5TwkMEe4e4iQ7CbfL89i8cbx5rGYyZvrrFoL9anWDihg_F--A8OSd25HflviukQI_AZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=By-X3l2s_714Hyg1jLRJNhEK1W9nmZBOGJ3hOtMnP2Rcl0mWOaT95I4XysghdZLeyf6ODFXEkCxrTLxtfdvTo3kFPUbZr2GFHyrVv9qYJL5LGxx_i_spQpxzZ-8MQf6lnzXeeAM_UHD5tk4gIZr4wHSonbPv_qGKClaichVTWKcxMXaPbxAfmE-97HCWZb-vfSDzI1tYL8stxULollMhiE6KGC3E6f5WNdx0PTuL7QQo0JrHG2tusBvMCeq0d86vp-QocGR54mX2SSYCkh5TwkMEe4e4iQ7CbfL89i8cbx5rGYyZvrrFoL9anWDihg_F--A8OSd25HflviukQI_AZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد از نشست G7 پشت سر جرجیا ملونی نخست وزیر ایتالیا گفته:
این زن همش التماس میکرد باهاش عکس بگیرم. حالا جرجیا در جوابش گفته:دروغه، شوکه شده‌‌م. نمی‌دونم چرا ترامپ با متحدانش این‌طور رفتار می‌کنه؟
ولی یک چیز رو به خاطر داشته باش: من و ایتالیا هرگز التماس نمی‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66503" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66502">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
منطقه امنیتی در جنوب لبنان ۱۰ کیلومتر امتداد دارد و ما به تقویت نیروهای خود در آنجا ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66501">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMRD-t6PBfy7eytlQbbinwERlnBn8nZgo8mdP0zxWMKEbxlkWYBsmBtxEKxD54DPUxri1PzXMf4IR_3mqeyXNTePBMycdrYQRgWzNwDvsSxLLBlxi-o9F0s3_iGWd34xXbprpR9o2ZfHOnJQ18boaDZ-VfLsCpMHJjTko_Or5jIMRzsVzGWx4269eY3H_f2PPsMAbfkPSLhaE27IDrYxBkN6kvqIQphvBMaL70y5f0Mg6rCZis-JuW2WG8S2TPAeXJihKcay9xFTd0DjJw9FirKAwThISaS_w8Ax6vd3mMYETUonLlpUFgmIqhd1bwfVjta3hlcUBChnjUtqyayA1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و حزب‌الله به توافق آتش‌بس جدیدی دست یافته‌اند. حزب‌الله از توقف بمباران اسرائیل و پایبندی به توافق‌های آتش‌بس قبلی خودداری کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66501" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66500">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxweJoc7pnH1g5r-5om4cwKmhniY6Uv3YjN6yqLTV3gR696-rFvYWjGiLtD-3LQRCHYJAgn3PCEkykrOH0fQweyQqyb1eURMriRk1cWYEXxTrpkq9jsHatAKCHk1Mi7RDHQidIqdzZIdoI3UHucaYiDGA9dVimPC693vmTNbQHdf6PF9hyjEMZgwX4N1lJUNFh09YC1ULXu2ZZG6iRyV8rP171WOhevJv4OoYPBodbBgfC3qG9rcytGpudud2Wx4Bh08Em87ccbI8JMP_Z9sQoEpLIqC0H33OqQBjU0t6XzjtUjTp5vHjSIVu0cTB0FQG4TAo5ZSYf9mWfXa7QPAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک مقام ارشد آمریکایی به من گفت: اسرائیل و حزب‌الله بر سر آتش‌بس مجدد از ساعت ۴ بعد از ظهر به وقت اسرائیل توافق کرده‌اند. این توافق جدید با میانجیگری آمریکا و قطر پس از مذاکرات با اسرائیل و ایران حاصل شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66500" target="_blank">📅 16:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66499">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eii3Y-fa_VmtsNkpFOXmBuM8mEUWs9N7B0S_E4thJeZ_10tAuM5maZIyl8PU9ELiC4_Wfo7AmrlXl0RjM7GAMT7K-3MSbMaPvrUeTSrIzVaM1SxeEp3a_7Iu9Gaeqk4CDjyNZU2O0z043OWfY830d8z403_7prJDT8wkIVn8itaYiD7EB8P96_JOSjwtj_0BZYf7W0v9P0b8X7XdqVXF9woFkEn1Wb7mKFjlxxKsNIXAYTHVNvgI1C767qZhPyQu9AggHhcnjO-oDgvY0NL1JVHBdvuwWPkJe3J8F_9YIyxMxmXH4qNWi2IKFxBUaJ6DdV_0mBsHF1_uDIr_-pl_hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما از روی ناچاری ملاقات نکردیم، ایران این کار را کرد. آنها کارشان تمام است! ما 60 روز را بازی خواهیم کرد. آنها نه پولی می‌گیرند، نه ده سنت!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66499" target="_blank">📅 16:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66498">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECXuZOVxCW1Yaat6htAQNo9MjlERNgFrtfU1ZFgicGtX0W_nvS7vpwBCvVtB27jaLWoKBgCXShWY3PNTcRhMLUboTtwVP2cuHbzXv-Ips50RibgdGy58i85Xe_lN95VgDunsHJkmfG0QLzDZc2VwpknkJDrd1fw9BS4UyWz0UczRJYpokg7NVv6AGoNj_z12FLd9akKOr4LJunFrj5-5rM-JVSlHqFnt_lbe_J4K-zK_qh3TJkiJnpPSIcW_GdMQCM2DzR3aYJ7AxmX3COWDVSXu6Yo7DqFLsED-CohjQo2XNfp7OO-Ep1g4W2DZ432H5ih5cNW8l7YrVE-3t99FNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
این جنگ ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات پدافند هوایی، نه رادار، و تقریباً هیچ چیز دیگری. با این حال، دموکرات‌ها می‌گویند ایران اکنون نسبت به چهار ماه پیش وضعیت بهتری دارد.
می‌توانید تصور کنید که کسی چنین حرفی بزند و از آن جان سالم به در ببرد؟ بعضی‌ها واقعاً تا چه حد می‌توانند احمق باشند؟
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66498" target="_blank">📅 16:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66497">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
‏اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا مسئول حملات اسرائیل به لبنان است. جمهوری اسلامی همه تدابیر لازم را برای صیانت از منافع، امنیت و حقوق خود و متحدانش اتخاذ می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66497" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66496">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXn3S1slJUkjN1nUQxIl_a4ei5ekUsnVC1Px_gvlOtZ83htimbt3GjYDEYOfsIirzvK-0hXEEn0hhTJK85lRPWD2-vZ7U8Cip11Olf7-lysjtQ3Ge4HpiWiefNIIguoSa-BSIj4KrlL9tGqvvs7UMpMW5w16aS8m9xWrSbTcCH2vqBbZ2oQ-ZVZINMJDZChfK9xpw5d6XrPe2DM6N1aRmZEnHg6HjtPcCf47DDGjZoLPlUDFKtMJRZLlk5m_x1eBSkNxvJIPxKHWcN7cVX9TtejNxGPu3L-gBMQiV_Y41GBZtapJQJRGzTC-HxhTLu6Y6CbtQwvncoFDIhF5sfNCKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اینفوگرافی خدمات فعال‌شده پس از رفع اختلال فنی</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66496" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66495">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=d8CteydmpcTPYqg0lPLkVhq5i4Z4W9Kz71FSiCyg1kTXXvPPQuDBtJS5Rwrr_qNmmQ9OEzji58VuweTNX0Gp_DPvXPh1GjHcTAYWcRpw3ybCC1-sUtD-KKoLHeU1lxCzLfVJdBM2aL0PuvqwWUYTK-YNb2W9lSQfFQ70iF7kHSTRhyZS_JtGtvvQu6kIrhAOKaLj4yuV1xW_tFL_pE3zc_iawe4JnSe4jJ_K0uDJzVaG22kbHm1X09oQe0VnkCVuQgTjWG1yiyihx8d56XHn9FwnNFN6t4zKAg0cEahqanepga7q5gVYvdez1ySXNvFolTrtm92ivhCK4c0VvQjcvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=d8CteydmpcTPYqg0lPLkVhq5i4Z4W9Kz71FSiCyg1kTXXvPPQuDBtJS5Rwrr_qNmmQ9OEzji58VuweTNX0Gp_DPvXPh1GjHcTAYWcRpw3ybCC1-sUtD-KKoLHeU1lxCzLfVJdBM2aL0PuvqwWUYTK-YNb2W9lSQfFQ70iF7kHSTRhyZS_JtGtvvQu6kIrhAOKaLj4yuV1xW_tFL_pE3zc_iawe4JnSe4jJ_K0uDJzVaG22kbHm1X09oQe0VnkCVuQgTjWG1yiyihx8d56XHn9FwnNFN6t4zKAg0cEahqanepga7q5gVYvdez1ySXNvFolTrtm92ivhCK4c0VvQjcvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران شهر نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66495" target="_blank">📅 15:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66494">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=bRSo0VrTI8_HKg6jMWq0B8XyUQGApQUcHuX6lV7Gy04_KR2zx8BeUxpt2jrNEMAP5nVhWqwdPXQ7wvw0cgMTv7FUXaZWFl0nzRDS67iGZ9Ajb-3yDpgRHhzH2FTxYPAoqgTMgBhWLi13CEwzwQztGp5mPxcDWnSNyZ3WGMaOAlIp_tH3Lrp6uE1AePSTnc1hzAN22RQPqJq-awnjVhiZ4SpJz3mQ7KJ82R76EdHxKyeivafayfhDuRckaz2WEBxXF2yWkNCq8rKqDx27YQh0cbnbpPL-sp3neaotOyaHDIKYhiGiw-Ix_esQYBcYs9troU9O4_DCJDTCtJJ-M-ca7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=bRSo0VrTI8_HKg6jMWq0B8XyUQGApQUcHuX6lV7Gy04_KR2zx8BeUxpt2jrNEMAP5nVhWqwdPXQ7wvw0cgMTv7FUXaZWFl0nzRDS67iGZ9Ajb-3yDpgRHhzH2FTxYPAoqgTMgBhWLi13CEwzwQztGp5mPxcDWnSNyZ3WGMaOAlIp_tH3Lrp6uE1AePSTnc1hzAN22RQPqJq-awnjVhiZ4SpJz3mQ7KJ82R76EdHxKyeivafayfhDuRckaz2WEBxXF2yWkNCq8rKqDx27YQh0cbnbpPL-sp3neaotOyaHDIKYhiGiw-Ix_esQYBcYs9troU9O4_DCJDTCtJJ-M-ca7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیا می‌توانید جلوی حملهٔ اسرائیل به لبنان را بگیرید؟
ترامپ: «بله. آن‌ها احترام زیادی برای من قائل هستند و هر چه بگویم انجام می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66494" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66493">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66493" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66493" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66492">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS2Kh5Xengf6MSG09GggYGDaIdLMT-CprxpsugsVICc-f36tueEm0NII2iBw40xP4qkVrzObtgYZQwC3C25zqvQQuGLM-TVhzsNqCT5p3cpUpIzcgQJu43zHI2MZsHBpox5QhuIfgT6GD9uF16htyUzOdseg3xteID9KkcWQxTmZ9XrdIgU_iYHgGqqU8yRnjiOWEyK-1FViW7AvDb9kEpm_9spWhiR9EdZ3oSlAuhzm1RH0R5LyIP3QzCk4Tbs8TZ-iUL2vmgX3cAwuuMEY_sLw89mNysI29CZK1M7DX-TKz2UrgpvWBKovl-iSteB-eKKYI1CaSo64Fi6naTAa-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66492" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66491">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUtTHPCXzgDKFClzap6awfBgD8Zi8yZuDY95Zb-UB3GVfMkr3rh1P5mhnWevSxCEbwEHhfvkj1mk3U5Jd2_i3ArbyeQlhxbzxZQAnnYMGz0b4NeEsLN80O2595UEBZxe-4-qjGHtBEbmDBoBej4K9G4OsL3HqnI4hktCUQ3d9tTp-9Oqq-KM92QGhLTVkVNzolrtwIXmBE8yopjcEtoPStGsp0dsfsruw5zs_S-QpBxEP0M34GCYYBjXgB4OuKd8AfDiI7cTGCIR6S4Z2sXDTQOEg_m3lY0b3SpWo61spy1A7TeapGvrO-WuJie0_-xJhpjQHN58gNeIJ96mA72mlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به فارسی؛نخست وزیر نتانیاهو:
پس از حمله جنایتکارانه حزب‌الله که نقض آشکار آتش‌بس است، دیشب به ارتش اسرائیل دستور دادم که با قدرت به حزب‌الله حمله کند.
ارتش اسرائیل به بیش از ۸۰ هدف تروریستی حمله کرد و ده‌ها تروریست را از بین برد. متعاقباً، ارتش اسرائیل امروز صبح به مقر حزب‌الله در بقاع حمله کرد.
امروز صبح با وزیر دفاع و رئیس ستاد کل، ارزیابی وضعیت را انجام دادم.
دستور من واضح است: اسرائیل حمله به سربازان یا خاک ما را تحمل نخواهد کرد و بهای بسیار سنگینی را برای این حملات از حزب‌الله خواهد گرفت.
ارتش اسرائیل برای خنثی کردن هرگونه تهدیدی علیه نیروها و خاک ما اقدام خواهد کرد.
همانطور که به صراحت تاکید کردم: اسرائیل تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان باقی خواهد ماند تا از شهرهای شمالی محافظت کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66491" target="_blank">📅 15:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66490">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=FR7m8BSn0QPmkNwWuxITPGlBXhsyW_VO4JunfiPfmqFmZ4WlrpMIiCzLSiXVcoA3skU10ikceCFYfxTW_W8B_DnDaFuP2s3kWBgUUv2n3vNSCfJFKGrIJV1Kwex39BqAXxzjwuOd4XqQbp1s0FilrbZI4rOsRPghFT-DtX0fi1LRs2zAXsieklzgKg7O5rqZqNIKvGeev01OyEgW36NmeFpduFN7zJTr8CwuU5aYEDURehGNmvO07NtNQZ7tbqvs8-zcAuu5D_V3zlSyK5Jw46M4RUsWrdVozqcaZSSZM6pVfU074b0fEzrP7ULDlMUh6NCDIxfMIF1LC3-Z0btb2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=FR7m8BSn0QPmkNwWuxITPGlBXhsyW_VO4JunfiPfmqFmZ4WlrpMIiCzLSiXVcoA3skU10ikceCFYfxTW_W8B_DnDaFuP2s3kWBgUUv2n3vNSCfJFKGrIJV1Kwex39BqAXxzjwuOd4XqQbp1s0FilrbZI4rOsRPghFT-DtX0fi1LRs2zAXsieklzgKg7O5rqZqNIKvGeev01OyEgW36NmeFpduFN7zJTr8CwuU5aYEDURehGNmvO07NtNQZ7tbqvs8-zcAuu5D_V3zlSyK5Jw46M4RUsWrdVozqcaZSSZM6pVfU074b0fEzrP7ULDlMUh6NCDIxfMIF1LC3-Z0btb2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.  @News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66490" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66489">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=FG4c6JEaVa99XCgC0Y4uDF30dhd3-uW2jX2Ds2gXUKEI-IVWaOgCMGs6PKcWmJsz-339iM2_1YyC8jNbDQJNp3lSCCrz8sRgCwFEzpsOrvIwSX-Di2ykQB76aFPVNiPoX8_absa74Un4FXzHlHRGFAG6llpyCmQxTLe_FSF2CCQQ5Pfel_twlwDoGTHC7i-OI0Z_fo4fRO3pstMoCzlu44lkKbgjeOPR5stTLauOrPEZ4HevNvrgd9qFbMyhZXLG7qCNmAtag2R8UcojlV4KvkjrblkS4gAF81DkzylFnI9fBp6_TV5-m4VLaaSozrZW2xcCNlpA_RvFpdjk_E6w5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=FG4c6JEaVa99XCgC0Y4uDF30dhd3-uW2jX2Ds2gXUKEI-IVWaOgCMGs6PKcWmJsz-339iM2_1YyC8jNbDQJNp3lSCCrz8sRgCwFEzpsOrvIwSX-Di2ykQB76aFPVNiPoX8_absa74Un4FXzHlHRGFAG6llpyCmQxTLe_FSF2CCQQ5Pfel_twlwDoGTHC7i-OI0Z_fo4fRO3pstMoCzlu44lkKbgjeOPR5stTLauOrPEZ4HevNvrgd9qFbMyhZXLG7qCNmAtag2R8UcojlV4KvkjrblkS4gAF81DkzylFnI9fBp6_TV5-m4VLaaSozrZW2xcCNlpA_RvFpdjk_E6w5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66489" target="_blank">📅 15:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66488">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=fTf0RYRyb0b-0E3p552dst6vMNhrQsGJK46AD8YfFsDl3AO9dYivr4vcUiLV-5JFzxqPkFV91nXO81VRsdX3nbfVr12MWTp3voR3tNzcTrfjXlY3WQ4O81H6RY3IlI4PkyCy7IVFg6ZeC7c-L5ifp66xrJW8xErZbkjwI3pFrVWlKHmlEVLoESnvUaVAve7AgD7EMR6z2rkqeVbZLhrbl6NcZosYn4aP7f26GCzdlTEJTxvxVYiDUbzgsOWpGDrCfyIxH6F-WYDIKfe9CL0LfWK7syIgereJ-vS13QbMSPm1EchzehtPQbjmJnPiWUdC7sshostlYWh2hegrsAGeIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=fTf0RYRyb0b-0E3p552dst6vMNhrQsGJK46AD8YfFsDl3AO9dYivr4vcUiLV-5JFzxqPkFV91nXO81VRsdX3nbfVr12MWTp3voR3tNzcTrfjXlY3WQ4O81H6RY3IlI4PkyCy7IVFg6ZeC7c-L5ifp66xrJW8xErZbkjwI3pFrVWlKHmlEVLoESnvUaVAve7AgD7EMR6z2rkqeVbZLhrbl6NcZosYn4aP7f26GCzdlTEJTxvxVYiDUbzgsOWpGDrCfyIxH6F-WYDIKfe9CL0LfWK7syIgereJ-vS13QbMSPm1EchzehtPQbjmJnPiWUdC7sshostlYWh2hegrsAGeIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
هم‌اکنون سپاه در بیسیم کانال ۱۶ دریایی.
“از آنجا که خروج اسرائیل از لبنان و لغو کامل محاصره دریایی و خروج نیروهای تروریستی آمریکایی از خلیج فارس و منطقه از جمله شرایط اصلی توافق بین ایران و ایالات متحده است. تنگه هرمز تا زمان تحقق این دو شرط بسته خواهد ماند، به همه کشتی‌ها دستور داده شده برای امنیت و سلامت خود به تنگه هرمز نزدیک نشود، هر شناوری که از این دستور سرپیچی کند مورد هدف قرار خواهد گرفت.”
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66488" target="_blank">📅 14:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66487">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
مرندی عضو تیم مذاکرات :
ترامپ بار دیگر ثابت کرد به تعهداتش پایبند نیست.
رژیم صهیونیستی مجازات میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66487" target="_blank">📅 14:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66485">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شعارهای دیشب مداح حکومتی در مراسم محرم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66485" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66484">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=RaImOcdQDr1V95ZSP8bZkYvgJ5X5BSKMiJ_GYkD8rjDdPSqtmcYSDvxyl5P95TeDKLzot0_V8bcJ6gaGZKUGL5vGnBFAMLJG8c6OayGVmPcNGLaO4SuDr-oIcOVaksKCs0VTENdwQ5fy5Ta24g38B6lWausJZEx2Gtor-L6aO9v7AF-R4C-rBwLjz2HmxIDVqNCs4olmNCaGl_MVXfTvr7wapSREsZ4qhzfZFCSuWWROKDZ3JWNZSolELiggddSG1O54WajiIASZ0CcgzYAc9xX1DDK1gA-hXrFLbUSqUI8nd-A-kZp6xoAgSx9XU-vAP5gv2eBSk5Cc8leIyDEEdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=RaImOcdQDr1V95ZSP8bZkYvgJ5X5BSKMiJ_GYkD8rjDdPSqtmcYSDvxyl5P95TeDKLzot0_V8bcJ6gaGZKUGL5vGnBFAMLJG8c6OayGVmPcNGLaO4SuDr-oIcOVaksKCs0VTENdwQ5fy5Ta24g38B6lWausJZEx2Gtor-L6aO9v7AF-R4C-rBwLjz2HmxIDVqNCs4olmNCaGl_MVXfTvr7wapSREsZ4qhzfZFCSuWWROKDZ3JWNZSolELiggddSG1O54WajiIASZ0CcgzYAc9xX1DDK1gA-hXrFLbUSqUI8nd-A-kZp6xoAgSx9XU-vAP5gv2eBSk5Cc8leIyDEEdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکی در مراسم اعطای مدال هرکاری کرد نتونست گیره مدال رو بندازه داخل و گفت میخوام یک مدل دیگه برات ببندم و مدال رو گره زد و نزدیک بود طرف رو خفه کنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66484" target="_blank">📅 13:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66483">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
‼️
وزیر خارجه پاکستان: مذاکرات سوئیس بدلیل مشغله کاری مسئولان ایرانی در ایام محرم به تعویق افتاد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66483" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66482">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd02588050.mp4?token=vNZuFwFvAceRQ_sBAn2CeTktCJpdh8FxFGKL8X0RBJdRlbPp4Pi_brrfKIUPFgoBegaYfSJWnA72Aor6HVUxdnQqqY99V8wPHhyuZtaU4B2dwhWreSVWtahFdYeQwbUAgNneqjJQVODwNj9WO7AdsKybIa-xwdk0aw9-cqdLPLPRq0bw2U2CMWe5tNqNTs2u5E8tUKYrhq01F5-GRrMuOVOXuojtDGBcSFJBdToUztfncDMuxWSKB4AoXh6bY5aXGkQBQ0jmj30uaTBwOJSCwuueBeIaod2CahmGvFeN6dxidXwKNLsaBvNC4vVF2VDTuDjHtjEum1X1v4bAoreTNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd02588050.mp4?token=vNZuFwFvAceRQ_sBAn2CeTktCJpdh8FxFGKL8X0RBJdRlbPp4Pi_brrfKIUPFgoBegaYfSJWnA72Aor6HVUxdnQqqY99V8wPHhyuZtaU4B2dwhWreSVWtahFdYeQwbUAgNneqjJQVODwNj9WO7AdsKybIa-xwdk0aw9-cqdLPLPRq0bw2U2CMWe5tNqNTs2u5E8tUKYrhq01F5-GRrMuOVOXuojtDGBcSFJBdToUztfncDMuxWSKB4AoXh6bY5aXGkQBQ0jmj30uaTBwOJSCwuueBeIaod2CahmGvFeN6dxidXwKNLsaBvNC4vVF2VDTuDjHtjEum1X1v4bAoreTNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلاش سربازان روس برای سرنگونی پهبادها
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66482" target="_blank">📅 13:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66481">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=feHelQH-GAmRFJRYqIheBm6gqiErdn10ZHzwfpK7Zv-RJiF-Eeo9EFSm2psjvt1QynRhXkd4sNsse1cyYFqccshy1TaWU3ldqnD2iPTpiEn3T-sgV23_rHRR_kxpMaY4-9K47M17f89aqTxs558cepw8tkxCpEer_jQMArBjMBcOFPPuG-WRP6vhGlIxap3Oc-TWaBoEkrYsu6j-F0VmnzhfCaHvZO2ScCpTbbZ_WQczMVLjYGNHv2SBY-a8sljq-dlBB8X_9IBNsAcwdb9k22s7IjYyhVmdPZmghx07wHg1nxUauJYTAWXyQGDOOaPe5zmKzyclPOX7qwb5ppsScg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=feHelQH-GAmRFJRYqIheBm6gqiErdn10ZHzwfpK7Zv-RJiF-Eeo9EFSm2psjvt1QynRhXkd4sNsse1cyYFqccshy1TaWU3ldqnD2iPTpiEn3T-sgV23_rHRR_kxpMaY4-9K47M17f89aqTxs558cepw8tkxCpEer_jQMArBjMBcOFPPuG-WRP6vhGlIxap3Oc-TWaBoEkrYsu6j-F0VmnzhfCaHvZO2ScCpTbbZ_WQczMVLjYGNHv2SBY-a8sljq-dlBB8X_9IBNsAcwdb9k22s7IjYyhVmdPZmghx07wHg1nxUauJYTAWXyQGDOOaPe5zmKzyclPOX7qwb5ppsScg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتز، وزیر دفاع اسرائیل، درباره سوریه:
ما آنجا می‌جنگیم. ما به الجولانی نیاز نداریم. الجولانی، تروریست کت و شلواری، نیازی ندارد که بیاید و به ما کمک کند.
ما سوریه را خوب می‌شناسیم. او قرار نیست در لبنان به ما کمک کند. او باید در سوریه بماند، در کار ما دخالت نکند و ما را مجبور به دخالت در کار خود نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66481" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66480">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=u-6TnmKW1bn8sUlOZQ0OWmewyXxD_qeuhcJuhU1zKvrlk201_ewJFKNfA7cv6eGn8LSMCLwcUKd2SnGCqwUasqmP1QzqBWLOY7UtOONgpd7Ji0EeO422h_6sB8TbOmpGjGUxtTK0kDN3I5bEpmDqp9_xnKjH8gn6AsoTUU3lbQr1Q0Sy4gJ5QNXlYAdfZfo5E3F5k_fmVQ2lD4Mt_b4gYoInyS5TLq-13O48OARIZRygFaiMA-RJZUk19wQtqhaKoAnEnUth5Bd4rE5YIkhig8iT-kLJqJ00y7ZgKbAvnoTHuC9QOdtuwkI9sQELwaOsTxb3E1V7Wyfd8EwJVFKZrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=u-6TnmKW1bn8sUlOZQ0OWmewyXxD_qeuhcJuhU1zKvrlk201_ewJFKNfA7cv6eGn8LSMCLwcUKd2SnGCqwUasqmP1QzqBWLOY7UtOONgpd7Ji0EeO422h_6sB8TbOmpGjGUxtTK0kDN3I5bEpmDqp9_xnKjH8gn6AsoTUU3lbQr1Q0Sy4gJ5QNXlYAdfZfo5E3F5k_fmVQ2lD4Mt_b4gYoInyS5TLq-13O48OARIZRygFaiMA-RJZUk19wQtqhaKoAnEnUth5Bd4rE5YIkhig8iT-kLJqJ00y7ZgKbAvnoTHuC9QOdtuwkI9sQELwaOsTxb3E1V7Wyfd8EwJVFKZrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حملات گسترده ارتش اسرائیل به مواضع حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66480" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66479">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=SfEg6Vj54argJz21lxQGYDKm5qoThN3VhsTjA81fiaegLqRgVY78uf76oEPHK3CTo7ObyIUX2b2YLlIzh6NrX8077D-yJMDM60lo_AtDW7t0nAJKF0_WAWt-Xskedt6ZZ1h00eizCX0VE6-_aSJYD9YBRu_3kBBqaC9FPeorx3JKeVZTtz6fp5m2xbi4QvC7HPs7M2j_Z8yCatR6G2SvOR4ooYx26n2q0jtr7V5scYCxniOA7OiarAxk3k1Q97x2FgboDY63M6USapN38P9wrP2SDRaTl7X5nXvIcxVAk-jpB-fvk2aXna8Y4qs1JrSTybqfe5lsurkHGs0I_eNGTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=SfEg6Vj54argJz21lxQGYDKm5qoThN3VhsTjA81fiaegLqRgVY78uf76oEPHK3CTo7ObyIUX2b2YLlIzh6NrX8077D-yJMDM60lo_AtDW7t0nAJKF0_WAWt-Xskedt6ZZ1h00eizCX0VE6-_aSJYD9YBRu_3kBBqaC9FPeorx3JKeVZTtz6fp5m2xbi4QvC7HPs7M2j_Z8yCatR6G2SvOR4ooYx26n2q0jtr7V5scYCxniOA7OiarAxk3k1Q97x2FgboDY63M6USapN38P9wrP2SDRaTl7X5nXvIcxVAk-jpB-fvk2aXna8Y4qs1JrSTybqfe5lsurkHGs0I_eNGTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
ارتش اسرائیل باید در آن سوی مرز، فراتر از مرز، از کشور اسرائیل در برابر سازمان‌های جهادی در لبنان، سوریه و غزه دفاع کند.
ما از «مناطق امنیتی» حرکت نخواهیم کرد، نه در سوریه، نه در غزه و نه در لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66479" target="_blank">📅 12:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66478">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8o5-hkvzKhg7-PfOeB506rujpN-gDDzb4fB1WBpoouHjxpIQ2VhT5qzH4A9Mj3viUNB1bSxGiNmb8XWgZvW5KHupBF4TZQ6_jmT6MJcd5qdMBKOtU0lhJzKdXpoqcwpV6DjOu66o6My2-L64JNz3dhRAAaKynE4IbKF2ln9b3UfhlqpTxy2cA7mZVu2FM9gTHpoT4vexQH_k9w-6HN6fxqxMJF0p9tppe_GuiLczm8Z49BVu9QlIajudik0VlDz8-VG3Q5mZRBmz-13Pizv2CYbyrOw7IMPZUt4SJBT8l3kJWT2snLzfopVve2IS0FhEPU1rIof48aRu9ido9nNAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
گوش‌بفرمانیم، وظیفهٔ محول‌شده به ما توسط مقام معظم رهبری پیگیری تحقق شروط و بندهای تفاهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66478" target="_blank">📅 12:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66477">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=DILODUinwVd05yzzmsx9mFNWaRx-tDRd7grFsWign4kR4yr8FC30PUSaRlBdODffrzv82Pcs1ooT_j5Ji1pt6NaOMZTejTVsI9Sv-Bjr5n--vp1uXWg8U9HRHcauLSbdEcZNXV2_Ipah4qPp614o3W8AGtlZPTCd_k_wSzUdn3z0E3_LpvWFEHpohk_PHPFSXBo45kkYgZxpvplRDQ69mk6zDi5cAsoAooEX8AwxCjxLp0VIbzZg1olqss0XoiyJ3RwMFHKb40zPE-V-L78SyWNfdarDyMqzH-gNsFdE2EoXPkFLF1hOG-Ih7sbYVD41xnkx7ul12XjsbJK8M4FxAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=DILODUinwVd05yzzmsx9mFNWaRx-tDRd7grFsWign4kR4yr8FC30PUSaRlBdODffrzv82Pcs1ooT_j5Ji1pt6NaOMZTejTVsI9Sv-Bjr5n--vp1uXWg8U9HRHcauLSbdEcZNXV2_Ipah4qPp614o3W8AGtlZPTCd_k_wSzUdn3z0E3_LpvWFEHpohk_PHPFSXBo45kkYgZxpvplRDQ69mk6zDi5cAsoAooEX8AwxCjxLp0VIbzZg1olqss0XoiyJ3RwMFHKb40zPE-V-L78SyWNfdarDyMqzH-gNsFdE2EoXPkFLF1hOG-Ih7sbYVD41xnkx7ul12XjsbJK8M4FxAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بمباران شدید نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66477" target="_blank">📅 12:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66476">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=emBp60vION6caVBd3ctRwY_smK0NU6TaJhW0VI_C1RdmRUtk9FU0ryTAgHTwL6VHJ0i80wbdmBqoPzophXkCMEDodtlciD7e8BRq90awlltv46qaQv5TZHSr-x8ZEguTAVy9pW-Bim8BFZ9WTAedROd7HEwKWqis9X0vs206fksVkiTZXZDiEUcEFmCf9W6HI9SqfFff7Y7KltXE7YrlemyFGC11AwKBktwaunV7UZpXMKejVIlSczE28DSBSzCdwpOYJHatD2p3tE5n78zObtBqLFMg2L6SAxg3sfiUOKwMtZq9xFm0XZ9QneYGosFqzzZUM2T3oo2KbmQ3lXi_5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=emBp60vION6caVBd3ctRwY_smK0NU6TaJhW0VI_C1RdmRUtk9FU0ryTAgHTwL6VHJ0i80wbdmBqoPzophXkCMEDodtlciD7e8BRq90awlltv46qaQv5TZHSr-x8ZEguTAVy9pW-Bim8BFZ9WTAedROd7HEwKWqis9X0vs206fksVkiTZXZDiEUcEFmCf9W6HI9SqfFff7Y7KltXE7YrlemyFGC11AwKBktwaunV7UZpXMKejVIlSczE28DSBSzCdwpOYJHatD2p3tE5n78zObtBqLFMg2L6SAxg3sfiUOKwMtZq9xFm0XZ9QneYGosFqzzZUM2T3oo2KbmQ3lXi_5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر جنگ اسرائیل:«حتی اگر ترامپ چیز دیگری بگوید، هیچ‌کس نمی‌تواند به ما بگوید چه کار کنیم و ما قبلاً این را ثابت کرده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66476" target="_blank">📅 12:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66474">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=Ad8G5iQRHfKX0fBQp1ZT12cQbYywwG9tHvrM3EksFGSd-tWsc4wwAKENTT5YhwwM8tACzaUe1aNUAIagXWiva5R2rdoKtg4pcry_8UpHU3bjxMBaLjuh6gHzYpvNDGejLNCTtA7bfQZR94SXkj3wUZ8eupy1gAWeuLZ8nDhTGIaxXgGgs9pC-0z4RLFpnnNgVAUzN151VHJ8Je80QcC6Bx9S1vDt7R_keP0D_f8vI6rE9Qz-9V4ShTeERgn8PM4rF8shzgKXO-f0ppi5mNRjenASlG-pdhL-aNMxsiD3Hd7neWCjtXE9pGP3uGK1kkLijETujv6pICqQMsAMYa6w2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=Ad8G5iQRHfKX0fBQp1ZT12cQbYywwG9tHvrM3EksFGSd-tWsc4wwAKENTT5YhwwM8tACzaUe1aNUAIagXWiva5R2rdoKtg4pcry_8UpHU3bjxMBaLjuh6gHzYpvNDGejLNCTtA7bfQZR94SXkj3wUZ8eupy1gAWeuLZ8nDhTGIaxXgGgs9pC-0z4RLFpnnNgVAUzN151VHJ8Je80QcC6Bx9S1vDt7R_keP0D_f8vI6rE9Qz-9V4ShTeERgn8PM4rF8shzgKXO-f0ppi5mNRjenASlG-pdhL-aNMxsiD3Hd7neWCjtXE9pGP3uGK1kkLijETujv6pICqQMsAMYa6w2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی شبا میری اعتراضات و روزا میری راهپیمایی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66474" target="_blank">📅 12:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66473">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=ZhYx6GFzCejrHVEgeGTl_1qBdOhItW8CWazyey9sv89yshU0m7c3MGDIcr4RmSent_7ETBsS1RPbaJ9h5C-KKeVGDolrBAcA_Ias0W3uMQ_68sV_R3yns7PZKQR02IUk4oiKtbucSxYd6fNRAldkyjU5vx14oTDA3b8hdjyxtf_S223FhWTtNxIFgm-6DZOCuzj8mk3C1aYDgcOwzG569I98B1O0lT22SiGuoc3aSEptuOp245ytdx004MRsADtGqcsY1Q8ijtBGKnCTIjs5v2SyNp7F4L95wZNrDittP_3Gh5iPXvz78RyJ8x3433vECuBJJlIAUArW64Segk3RLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=ZhYx6GFzCejrHVEgeGTl_1qBdOhItW8CWazyey9sv89yshU0m7c3MGDIcr4RmSent_7ETBsS1RPbaJ9h5C-KKeVGDolrBAcA_Ias0W3uMQ_68sV_R3yns7PZKQR02IUk4oiKtbucSxYd6fNRAldkyjU5vx14oTDA3b8hdjyxtf_S223FhWTtNxIFgm-6DZOCuzj8mk3C1aYDgcOwzG569I98B1O0lT22SiGuoc3aSEptuOp245ytdx004MRsADtGqcsY1Q8ijtBGKnCTIjs5v2SyNp7F4L95wZNrDittP_3Gh5iPXvz78RyJ8x3433vECuBJJlIAUArW64Segk3RLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نبوغ اوکراینی ها در شکار پهباد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66473" target="_blank">📅 11:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66469">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOTFx0uOfi-SaXMivfxyylHFToEcJ2XDKzeLHMYS43aa5ypbL1ad1WIR59Pi57KspoQWCxOiaeuwGcG5Mio_8B6cBLCz0A6VcocQmOpCpmLWM1M6HejORFZ1S8ykUNXssp-JF3ZsNUool7M66akugPwfvt_EmQsvc1gHzdvVD5b6hQQBltKhVSFsb9uOnANPX8heHqJhm8UfMd5U9KB-UnPjLnObtNHvm5PJA-INN6TwucTDIwopvOvaDSfSEj5KNs4V0qYt-_45pIlE3JL5gU59eOFHcCFwfG1wR4N6OBC8uuennM6gwkiz7YPkPTlFy6CKQc5wRUWnRwYKSGo0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t93V6j_buzmEiid7DXcfqKo5sKkLWADHoiIdUYtz0NcOWLlJQDHTjMBSu_BdYaE2-3N-EWD3ZnqEkmC8ecgnQfGVBvlXyjfNWOy5JiJNap4bNC1ws8aNukWiZKbJbOkrPVfgIwQLGjRW9d5nzW-6eHqZvXAmDbdlmcX0V2AVJqSMeslpSKxassJeMsCfybHxdTMBDiSDUNG_gRmXLS-93Zja4CVWBCRRIXeVaUEdqd9kH4Yxpt2GHqGkJcK-mgIfJvQw7I_2SMjNIl-A6lVGHIM7Z6YXO47LxkXcDaXBeaIUJJIJX42OjqRZ9ilRic3oAHwo5gHtPYnwQin2BjK_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gEHcDyseDQEGUpiJOJ6w0RkeLJwOTe4GYl4F08dcaZVBthyfjbgm5ih4RbkKRD2Ia-O6UJd5WXA3EQ89ojLAcYH3BGFZ2iiBTBldGXEO743Oh0AMeH7cFbG3YxZeFdHVZNkHKjpSvF7Yay8SAXudFY6ZkyIXo2fT0AMnh5REaZhmlHMyv1N8UYdVOg2FLW4eQ5F-kfnul-z00thtWuoVLWKVtjaEUxteetsF6cljDuhAFwpz7xgOtlqZjnVhXk6xbfcx7LWwA3iLdgANOxJdBGXE0I-rHIJvf0b5p3ooHpq4Wdbt2U1NeCuB7WHO4NsrHnqYFpOf1g1JWgyISmSQ3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=nX1Ns7ATP3vTYGrigATFOEZ7gUOSkE2_FCjl5OlZgRtefVHU80tmBdNAWIKgHf8C_cEcY-CYFmdVuiKiurIMlo2Rn8GJlSfnCfiiL1sS9ISDh_vRiL_qhJvezgmTVEm7wue4-TwVbf75n4hlRgXHuPzRI2S6rxVBYHMfgC2zVJjJd6c6Gubt6e__7SwP8Qj-lPYubqLUepgrNQO6i9EG_2vnehJx5p-jNgi0hPHpPdO5p7yPr646pyaSSAeAb_uuGz_M7jaXlQfRyrEVUYfrw9Kns9Tq7Jv20oWQ4lNg46Z83EVeFY5uC3-DJ2Eu88m5rzangHOsV5vS49Sfl1umwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=nX1Ns7ATP3vTYGrigATFOEZ7gUOSkE2_FCjl5OlZgRtefVHU80tmBdNAWIKgHf8C_cEcY-CYFmdVuiKiurIMlo2Rn8GJlSfnCfiiL1sS9ISDh_vRiL_qhJvezgmTVEm7wue4-TwVbf75n4hlRgXHuPzRI2S6rxVBYHMfgC2zVJjJd6c6Gubt6e__7SwP8Qj-lPYubqLUepgrNQO6i9EG_2vnehJx5p-jNgi0hPHpPdO5p7yPr646pyaSSAeAb_uuGz_M7jaXlQfRyrEVUYfrw9Kns9Tq7Jv20oWQ4lNg46Z83EVeFY5uC3-DJ2Eu88m5rzangHOsV5vS49Sfl1umwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات ارتش اسرائیل به نقاط مختلف در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66469" target="_blank">📅 11:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66468">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rruOXEl1nNIMLUUX68w5cGTxnKD7PxARhLhZyHHgDk58paAxeJ95iQGtUz3roYhKGFS_UFhoFtmFrAMb7NPkAy5bb4krVK6VXjotpdgn6jn7uuHQfPYQ4ZqokYrS9rW8UTGleJUiRsT3WA8o-DhgngV0ToBSyZzteTruVvq3NVVacn9u3FD_hB-XXR1eMhevAY0GdLwzJ7ddC1lHiz1y3BjjcC3vQrCURpGtzbGqNfNC5u1gYqX3NyyaP6kcEcJiH3Mbi7wIDCIorxWwZTTpYDp0-wVecbe-r6Tf6tnf1XtWk7t9XGvtuGNlDsJzvuvYH0miyGHdDESdIUfxOoE2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت ‏مسکو، روز ۱۵۷۶م عملیات نظامی ‌ویژه ۳ روزه پوتین در اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66468" target="_blank">📅 10:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66467">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7be955089.mp4?token=R07LvFqfCtikA5Uy7VXivIQi3m1KK2dhtTg2Q1MoOoti62iNvvyQ4XP5g1bGKrTZ_U5GEdf6J7F7bVu9CHyn89F9Wg28ilrdmgHyXEXO5hYo8Jn-flIpzys3gp8MDlIEBd1MeNxkOKWHiM57njEiY1oCEwDKR-Yg4yWQwGUnGEBblDNLnfdlDtT2ziezpeBALDpdvx8D2veWs78dB8YFmTmo3tY_l0LS94KCpoid0gBS-WlJULhZ6HhNkYt1fZYf7W_HbN8jtyiH4uH8LYjYL12hHl5hM7i6kTMfjbVvQTm7n3UVFi1l_X-k-nIpA2Gd2OX_1fHn3OnRoxBIGld28g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7be955089.mp4?token=R07LvFqfCtikA5Uy7VXivIQi3m1KK2dhtTg2Q1MoOoti62iNvvyQ4XP5g1bGKrTZ_U5GEdf6J7F7bVu9CHyn89F9Wg28ilrdmgHyXEXO5hYo8Jn-flIpzys3gp8MDlIEBd1MeNxkOKWHiM57njEiY1oCEwDKR-Yg4yWQwGUnGEBblDNLnfdlDtT2ziezpeBALDpdvx8D2veWs78dB8YFmTmo3tY_l0LS94KCpoid0gBS-WlJULhZ6HhNkYt1fZYf7W_HbN8jtyiH4uH8LYjYL12hHl5hM7i6kTMfjbVvQTm7n3UVFi1l_X-k-nIpA2Gd2OX_1fHn3OnRoxBIGld28g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری: شما گفته بودید که فقط تسلیم بی‌قیدوشرط را می‌خواهید. اما این تفاهم‌نامه شبیه تسلیم بی‌قیدوشرط به نظر نمی‌رسد.
ترامپ: خب، در واقع احتمالا تسلیم بی‌قیدوشرط است.
مجری: واقعا؟
ترامپ: من این‌طور فکر می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66467" target="_blank">📅 10:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66466">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=Gak0iytzHiJZ_0foQphZJ8Kgw0x9Rek8zuCVpSUz9cNgWFUhr5YuSFnB5vb_El6DqPMGazK0vJubZ0PCClgG_x5X7nNxThwJlwQcY0QPJq2nQ39tOf-X5mQK1JaX20VmcOzGAdo40Prv37pezYpV2UB_d2iJML9TaJYDF8zYu3f0fxSCd-y0OELhVWi-Eg5KSljYRvB5UYlMd9RxUbyU6qgJeqCxgNujvCVIFrwvWkxkpTdCnGSsgpEJ50YCCGQOx2Wrxo9pPXFDd0IeFjOIAiD-q77CoibNCMstdw3eePFIds1jwwYBlerI6GNwx0qIc1sTiGdoxV7QG6GxjdGilg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=Gak0iytzHiJZ_0foQphZJ8Kgw0x9Rek8zuCVpSUz9cNgWFUhr5YuSFnB5vb_El6DqPMGazK0vJubZ0PCClgG_x5X7nNxThwJlwQcY0QPJq2nQ39tOf-X5mQK1JaX20VmcOzGAdo40Prv37pezYpV2UB_d2iJML9TaJYDF8zYu3f0fxSCd-y0OELhVWi-Eg5KSljYRvB5UYlMd9RxUbyU6qgJeqCxgNujvCVIFrwvWkxkpTdCnGSsgpEJ50YCCGQOx2Wrxo9pPXFDd0IeFjOIAiD-q77CoibNCMstdw3eePFIds1jwwYBlerI6GNwx0qIc1sTiGdoxV7QG6GxjdGilg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ به شیخ محمد بن زاید:
وقتی انقدر ثروتمند باشی، میتونی انقدر آروم صحبت کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66466" target="_blank">📅 10:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66465">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=KOUnp3FcX8acP7MJqCuWmDQNlzVXgeWj_R0CwDY5zTVkVXETTVIXW5M38i6LF0nIrBieAJmHK-tzrf7oCBifP3OHbBQirxvPQAnsbV6lABtJlRNL0zJBh-CvlMT82fKE2E5eJat-VVwlI9AUTOWlDymaHHglisDnTzQSPkEpMXWbfTzFKkXejRU495fq8ufnvHI5N1yfZnRmZcObuy8_XVTURYq0kJBt3DVIlGBK67Ot-Sl9-NZq3CmpGir3hw20wz1DCoOPGGynKzhjhOydT49_H1EytzvxoNajb_XK2tCwsdw-h8N7pV_1LdVyS7MqAio3lVKC74yv8dAzzHmMlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=KOUnp3FcX8acP7MJqCuWmDQNlzVXgeWj_R0CwDY5zTVkVXETTVIXW5M38i6LF0nIrBieAJmHK-tzrf7oCBifP3OHbBQirxvPQAnsbV6lABtJlRNL0zJBh-CvlMT82fKE2E5eJat-VVwlI9AUTOWlDymaHHglisDnTzQSPkEpMXWbfTzFKkXejRU495fq8ufnvHI5N1yfZnRmZcObuy8_XVTURYq0kJBt3DVIlGBK67Ot-Sl9-NZq3CmpGir3hw20wz1DCoOPGGynKzhjhOydT49_H1EytzvxoNajb_XK2tCwsdw-h8N7pV_1LdVyS7MqAio3lVKC74yv8dAzzHmMlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختران حاج گاسم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66465" target="_blank">📅 09:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66461">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX4k-I_vjeTK0fsyrr2HOMi6RThqBYNk1gDP00nHPJq_5WXepDcnmlOvekbGt5fgV7dyV9W7BLLlS7Rge_pJN_oNhGmtnUIp-Y4qs_Xl-oEwsH2fxz8jG3_34vCATxXfsHHcEHF3QNK82YbcxRMslsnAiylNQ5y90kJQDGqLiENc4uLf-ojgSLGQGXMiXPWZu49Ektf1pnexPK7fWAyfnSeWvLmPJNcUhU3XEmEtRtEzChuPQOR6lr5sICyF8wFt6d4M8dsU_9ug36Y4Ic09lL12PT69GAe0dhJeSFEewEMHz_rcgukuMaQJ9Y0NKnbVNcNaKi8c1gPa39uc9i1oAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=VrtPz57wYLNEmqmVdS6O1_puOTV1IGW4ykdHGYjwRml3LF85yxjzWz8Hmghusc9f7-4E6mEPhWEdEbBGCZUWivy6Hl-BRXjkzTeocHV7H8j9UuDLbpBj4Mv5bwYRQEHda-vpOVSxNYoBipooy84JGJJp7L9_w-_87ba-OYQxhwQ3huEdTqLjG2HOE3q8DtBt_rZ54OMEibhmsaNFB_vGxZnbE-L1zM5vwOXy4MQ66AQA3eDe4FHyf-wIsy6igzeNj91_Hke_efPv-gwl_YXQT_AYGTwPTWmIFfLq-ccBKixMgq5xKb3O0B2oCx9EQv4e_dFvevpfI3ZIoynRMNQanA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=VrtPz57wYLNEmqmVdS6O1_puOTV1IGW4ykdHGYjwRml3LF85yxjzWz8Hmghusc9f7-4E6mEPhWEdEbBGCZUWivy6Hl-BRXjkzTeocHV7H8j9UuDLbpBj4Mv5bwYRQEHda-vpOVSxNYoBipooy84JGJJp7L9_w-_87ba-OYQxhwQ3huEdTqLjG2HOE3q8DtBt_rZ54OMEibhmsaNFB_vGxZnbE-L1zM5vwOXy4MQ66AQA3eDe4FHyf-wIsy6igzeNj91_Hke_efPv-gwl_YXQT_AYGTwPTWmIFfLq-ccBKixMgq5xKb3O0B2oCx9EQv4e_dFvevpfI3ZIoynRMNQanA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات شبانه ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66461" target="_blank">📅 09:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66460">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66460" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66459">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N7XdorKJ1ZHrWnLdEW9ZnT8ZqBjMmRk_gjl6dfq8ry-7BV__HWeGMriFa9JBvzRT_2zA1Xfg1ZGyED82BPRifsjP01887sscq7yTGUpl91Ba5HBooGBBFFE1TjHYJIlTNK7t98052XPnlOIssKH1jBzLoGSsEwWLvM_JfGzLot-4oFhRluCu2w1PqJ4QldSkY_czQZbpVxHuAPXcb5Z_YOaI4fXo1kmi4CEiMK_-uCtsqCR3EJ9hwI3Xp1iqQNbIw5oVjClTKRUDYUj4G-oF9ijTkIzfl6BIDeVZTOx7-GSJShRQze5cpkao7MXXH9H_wBBqGSzd1_uenfJdqt4ZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66459" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66458">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
‏به گزارش المیادین، هیات مذاکره‌کننده جمهوری اسلامی در پی تداوم حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس را تعلیق کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66458" target="_blank">📅 00:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66457">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=RNueXJEcEbjqVc-U07qVZdVR_2lj7AYlK-kLU6StmM8g512-4tNFmDiYFbKsZerTkCPprVmQq5VXTowOJ7rl1VNp-k4FUyBwfdhxWeKuZmsOriZZ2EzTr4gIwOAsSnSLe_N6V_BQJYN3FoNsFMemP7XIJfgHs0fFKeI_Y4kJkWbVn1LS-2I_VdZom1_-7247_TUmiKinwipkHpvN6ekYbRqR-dgOT4v7mERerSIo9MG6gyhbkc3Z7ocx_VIcpKhqEUh_zC4HsTHh2e-LhxSFURsT2sr3XL9wGvThRVcLYRmQWLdhE4AV-ackk4RDlvge9WndQeMJNu5yLiLywunK7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=RNueXJEcEbjqVc-U07qVZdVR_2lj7AYlK-kLU6StmM8g512-4tNFmDiYFbKsZerTkCPprVmQq5VXTowOJ7rl1VNp-k4FUyBwfdhxWeKuZmsOriZZ2EzTr4gIwOAsSnSLe_N6V_BQJYN3FoNsFMemP7XIJfgHs0fFKeI_Y4kJkWbVn1LS-2I_VdZom1_-7247_TUmiKinwipkHpvN6ekYbRqR-dgOT4v7mERerSIo9MG6gyhbkc3Z7ocx_VIcpKhqEUh_zC4HsTHh2e-LhxSFURsT2sr3XL9wGvThRVcLYRmQWLdhE4AV-ackk4RDlvge9WndQeMJNu5yLiLywunK7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آیا در جامعه اسرائیل افرادی هستند که بخواهند ایران را به لیبی تبدیل کنند، یعنی یک دولت شکست‌خورده با ۹۰ میلیون جمعیت؟ احتمالا بله.
اما نمی‌دانم که بی‌بی (نتانیاهو) چنین چیزی بخواهد.
من شخصا هیچ‌وقت چنین گفت‌وگویی با او نداشته‌ام. گفت‌وگوی جالبی هم می‌تواند باشد.
اما همین را الان می‌گویم: آیا تبدیل شدن ایران به یک «لیبی ایرانی» برای ایالات متحده آمریکا خوب است؟ قطعا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66457" target="_blank">📅 00:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66456">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=J6MPITn4pdqHZLVaolaOYOlp5tP6u4NaPpQlexhSPyXkF4gDgPaZ8vCLyKHCJGWYjB-_pkYWsbduCU1u5AGtLOoaE8pyFxUvqtdv3RI8DlkbH9MmmovXFfAKvyLA0PBdi8z9GEVx4JjC94wa3el78UPJJjqQAB2Nsyv5ZmRgXL29GBQvDpOX1ZHXwqQ-Iu9aryEjoalzPcwVmmP06CtJJFWDmOiBszRvhP9qfXT8OJfO_eoNSaNi6C8ayaCh7K1aETgMrs7olhSVSxloKmo06yIR9-f5abjGDQo7mhV9X7rmvIAKlg5MpR82pd_O_qClFEv4q8S-UXV0vP2HSLn6jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=J6MPITn4pdqHZLVaolaOYOlp5tP6u4NaPpQlexhSPyXkF4gDgPaZ8vCLyKHCJGWYjB-_pkYWsbduCU1u5AGtLOoaE8pyFxUvqtdv3RI8DlkbH9MmmovXFfAKvyLA0PBdi8z9GEVx4JjC94wa3el78UPJJjqQAB2Nsyv5ZmRgXL29GBQvDpOX1ZHXwqQ-Iu9aryEjoalzPcwVmmP06CtJJFWDmOiBszRvhP9qfXT8OJfO_eoNSaNi6C8ayaCh7K1aETgMrs7olhSVSxloKmo06yIR9-f5abjGDQo7mhV9X7rmvIAKlg5MpR82pd_O_qClFEv4q8S-UXV0vP2HSLn6jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس این انتقام ما چیشد؟
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66456" target="_blank">📅 23:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66455">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=aRrlbANJLhvA40KnY0SXYl95IRwfaJLbW1kgH2Xy4vrCFtsAWvo5VjI1QqeSZ2B5PydLor2Yl-gSe8lg52XN0p4W3hBNN0YMWYQTGo8NJHRlNuqAI0SruHvzr6aEogufsBt3eXp0NOs1dCC5aIrZ4svQi52MAhnFKGjkSefB_M2J7SQ5w1cPdkSUukgEqJjhR7vh-JGTWNonOY8rSaU25g5iP7S1xZX54ivzLvGTpX2BGMEBW5D839lferUP1AjsYOV7ipeqdJBZOUQb0rpmKB_ywZ4Qpm4uDHg0SWQIq_B2lud0r17TsYlHg_R47TSM2L5U_US03tbndEPBgNcTBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=aRrlbANJLhvA40KnY0SXYl95IRwfaJLbW1kgH2Xy4vrCFtsAWvo5VjI1QqeSZ2B5PydLor2Yl-gSe8lg52XN0p4W3hBNN0YMWYQTGo8NJHRlNuqAI0SruHvzr6aEogufsBt3eXp0NOs1dCC5aIrZ4svQi52MAhnFKGjkSefB_M2J7SQ5w1cPdkSUukgEqJjhR7vh-JGTWNonOY8rSaU25g5iP7S1xZX54ivzLvGTpX2BGMEBW5D839lferUP1AjsYOV7ipeqdJBZOUQb0rpmKB_ywZ4Qpm4uDHg0SWQIq_B2lud0r17TsYlHg_R47TSM2L5U_US03tbndEPBgNcTBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آنچه من به برخی از منتقدان این توافق که شنیده‌ام می‌گویم این است که آن‌ها می‌گویند: “خب، ایران این همه منفعت به دست خواهد آورد.”
من دوباره همان چیزی را که قبلاً گفته‌ام تکرار می‌کنم و احتمالاً مجبور خواهم بود چندین بار دیگر هم تکرارش کنم: ایران دقیقاً چه منفعتی به دست می‌آورد که قبلاً نداشت؟ پاسخ این است: هیچ چیز.
آن‌ها هیچ چیزی به دست نمی‌آورند مگر اینکه رفتارشان را تغییر دهند. اگر رفتارشان را تغییر دهند، آن چیزی است که باید از آن استقبال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66455" target="_blank">📅 23:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66453">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‼️
یسرائیل کاتز به کانال ۱۴:
ارتش اسرائیل دستورهایی دریافت کرده است تا در صورت لزوم، برای عملیات دیگری در ایران آماده شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66453" target="_blank">📅 22:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66452">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebiDtTsvevcXdfcHb44jQLuq3bbkcFTUUqxWdts34iMRtUGiDyEWeFd_FZoxbwgvmfqAWgmJDwx7hfNgBb13-BxZ3bm0VfVomZDl6XyCy1kQA0CJABFS0LCWcm1wdxtiiUl45q3asITRHgH8A_Gqo21XFHJxqacqBdHTObaFUIYEymN7v6mqgcWFbe-MUZdvfGnMERHCZIMlToJRlAsGutqo81pyKox-_6oMHi99LyJ6IXIGPlg49kOEOHQZQRui5cfFUYm38aMLKB025MNx_d-01H6IWYSZWxt296Vgl8Tz3Ap6vEcwiqsBCZtgFe9gBVSt_t_615LTgqRhaR65DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در تروث سوشال:
ایالات متحده به صلح متعهد است و ما همه را در منطقه خاورمیانه تشویق می‌کنیم که به تعهد خود برای پیشبرد مذاکرات ما به زیبایی پایبند باشند. بازارها از آنچه که با کاهش قیمت نفت و افزایش سهام اتفاق می‌افتد، لذت می‌برند. ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم. از توجه شما به این موضوع متشکریم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66452" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66451">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هات نیوز | HotNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/news_hut/66451" target="_blank">📅 21:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66450">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66450" target="_blank">📅 21:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66449">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این پیام یعنی پایان پزشکیان و جریان اصلاح‌طلب در ایران، و آغاز حکومت نظامیان به سردستگی قالیباف #hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66449" target="_blank">📅 21:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66448">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66448" target="_blank">📅 21:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66447">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1J8eFdUxjH_xKs8vpqCYZcwGb-9JEfRfg5EesSXv0ZV4apl3fzKEcU_oabPrORtiXesCGEqgFmXGrchV_qbhWvpIsod9ztWSxsZ8VjY6culE2Z8kzBSluE9YwmMPmhhgmeJR6qs6TAA3S-HfUBRQjUg7viA6vHN7-JoUiZaDUcrqzJZbs7fp4uEz3fKaEi9X7BRCcaDYZOQ7TxxkSkQoVGL3uFmJw7cNeZLuXaWbWOfFt2mPx-AYHq-JvzboD43HgTu6CLFtgAdDUUV4dOasLCY6lZ3R16kDG3ztx8ait6i-UCDuP9D4Pzz24lsTFAEARCS1SSEEZtHEd84Qpc6-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66447" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66446">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzqqX0qh9HdrkuqtmMGkHivJJoi0CMrvD4r48-LqDk85MSMCbmOaAa7SAZwvh7LnG4e-yYjBwQ1prOaGhzf_Tpb9_1WyUtVhM9hcE2fpqNcI9Y6HzS3zCQhiDuELN5AxMd1p5K8Yt3tXem4RQJL7e38cuSKTYzlr4mnimNRtoOkJIDxwM3ykdV4UuxPErcK-ojoewXRWJhqT723JZ2xxDgPPFaBrJsm3sD32DYpE-lUUh3MuCRA0BbOTqvXQMlYsowlbLLytNSdBbnw8wd5YjMRaytR97nheizC8v0WCUvpziOzQW_xIHFZRywry73w3wyZ0A_qN7tWkT1Lpjx8aHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ: آمریکا هیچ پولی به ایران نمی‌دهد. اخبار پرداخت 300 میلیارد دلار به ایران فیک است. تمام آنچه برای آمریکا وجود دارد، موفقیت، کاهش قیمت نفت و پیروزی است. وضعیت بازار سهام را بررسی کنید. پروپاگاندای دموکرات‌ها در کار است!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66446" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66445">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏
🚨
🚨
🚨
⭕️
سنتکام اعلام کرد، نیروهای آمریکایی محاصره اعمال‌شده بر تمامی ترددهای دریایی ورودی و خروجی به بنادر و مناطق ساحلی ایران را لغو کرده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66445" target="_blank">📅 20:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66444">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=Eu7Eapvs2rMPdGCMf8q3chaZU0PZRX3FBFK6PjG7CIq-wSKEDdY8VwzPUNa6FENFfMwlXguGlUDr8zFe1twdo0MjEmRbGmwXoxbIAZ26wxhilQ2pAbjD4A6R0YUF8gAzbOdfMeRiP8I4ZDfqSS2VfuOVRr0HF3NutpDAEazogbLPsK-SmHWGLq8OSsaFTbx86Ft7B82BCp1M8xCJJ_3GgcKxslxDKL2o6Ly5SYW0UPhFdTJt32V5RsI7gK9oS7EJAHH1q5h79mIMtJnSLGs2g4m3Q8Nqn5fTuyQog5A3Fub-5bvGdmZniWyqROlEAN2vCPuHRS5vtVZhpnVFCaJwFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=Eu7Eapvs2rMPdGCMf8q3chaZU0PZRX3FBFK6PjG7CIq-wSKEDdY8VwzPUNa6FENFfMwlXguGlUDr8zFe1twdo0MjEmRbGmwXoxbIAZ26wxhilQ2pAbjD4A6R0YUF8gAzbOdfMeRiP8I4ZDfqSS2VfuOVRr0HF3NutpDAEazogbLPsK-SmHWGLq8OSsaFTbx86Ft7B82BCp1M8xCJJ_3GgcKxslxDKL2o6Ly5SYW0UPhFdTJt32V5RsI7gK9oS7EJAHH1q5h79mIMtJnSLGs2g4m3Q8Nqn5fTuyQog5A3Fub-5bvGdmZniWyqROlEAN2vCPuHRS5vtVZhpnVFCaJwFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس در مورد اسرائیل:
در طول سه ماه گذشته، دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند، توسط آمریکایی‌ها ساخته شده و با پول مالیات آمریکایی‌ها هزینه شده‌اند.
مشکل اسرائیل دونالد جی ترامپ نیست و هر کسی در اسرائیل که فکر می‌کند بزرگترین مشکلش رئیس جمهور ایالات متحده است، باید از خواب بیدار شود و واقعیت وضعیتی را که کشور در آن قرار دارد، ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66444" target="_blank">📅 20:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66443">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=NQ5w4qRYmq0t4JQpo9MWOQVkAqdeLHvQDhdOxjIANxpF25p_IKvIZWGKMGx-XL0QMWAT1XW4ULn_ov2YJU4iXn52EmAku9WwNwOicVOqTzHtIAFlz8IvyETMwr1eAZum4LWG7kcVj2BZsjhBOosuPH7RlEkm4IC1JvnJHKaShSzfiHN4Wn256owNuPymKuTMB_ILDkefrrR8aWg6n9GHC46hDc4wwvBOifo5faT1lhsHKsjQPWW8G6Zs22n6uOiJCub6K3AQTznyEh_x1WIdG8vFdtEL8RqnyeUcmQo92lsA0JNzf-aM0cBWTX_eAngul42cIOJYcrn18_SXVJZC0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=NQ5w4qRYmq0t4JQpo9MWOQVkAqdeLHvQDhdOxjIANxpF25p_IKvIZWGKMGx-XL0QMWAT1XW4ULn_ov2YJU4iXn52EmAku9WwNwOicVOqTzHtIAFlz8IvyETMwr1eAZum4LWG7kcVj2BZsjhBOosuPH7RlEkm4IC1JvnJHKaShSzfiHN4Wn256owNuPymKuTMB_ILDkefrrR8aWg6n9GHC46hDc4wwvBOifo5faT1lhsHKsjQPWW8G6Zs22n6uOiJCub6K3AQTznyEh_x1WIdG8vFdtEL8RqnyeUcmQo92lsA0JNzf-aM0cBWTX_eAngul42cIOJYcrn18_SXVJZC0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏جی دی ونس درباره ایران:
آنچه واقعاً اینجا اتفاق افتاد این بود که ما روز یکشنبه تفاهم‌نامه را امضا کردیم. این توافق‌نامه مفاد توافق‌نامه را تثبیت کرد.
چیزی که ایرانی‌ها پیش ما آمدند و گفتند این بود: «ما دوست داریم متن را تا جمعه منتشر نکنیم.» من واقعاً متوجه این موضوع نشدم - می‌خواستم متن را فوراً منتشر کنیم. اما برای اینکه با آنها کنار بیاییم، گفتیم: «مطمئناً، باشه، تا جمعه صبر می‌کنیم.»
و سپس آنچه در روزهای دوشنبه و سه‌شنبه، در حالی که رئیس جمهور در اجلاس گروه 7 بود، اتفاق افتاد این بود که شاید رهبران خارجی با ایرانی‌ها صحبت می‌کردند و آنها را به انجام این کار تشویق می‌کردند.
ما قطعاً به آنها می‌گفتیم: «ما تمایل شما را برای منتشر نشدن متن تا جمعه درک می‌کنیم، اما می‌دانید، ما در یک سیستم دموکراتیک زندگی می‌کنیم. مردم آمریکا می‌خواهند متن این توافق‌نامه را ببینند. ما مطمئناً دوست داریم هر چه زودتر آن را منتشر کنیم.»
و بنابراین آنها به این نتیجه رسیدند که رئیس جمهورشان آن را امضا کند، رئیس جمهور ما آن را امضا کند، و مهمتر از آن، شعار را تکرار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66443" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66442">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66442" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66441">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ivWYynzkCLwnmzw1WoI-n5cCsQh41zra7_EFZ4ua0pgHwDWTqjUw7rmW1vQV7pZwy6hgoGWxjj3OjNCoxtEDYRQ_2N8-Y-hRPJc7XYBU3aXvJ5pkj339QNRMCvEk9ERqyj1F4ySafO9ryvTI-k7wl-_h34jiikLP0Ypfut2LYAUNzvhXYOqUJsYE6xqiCz-kNN9LNVH4XWxz6Z4Itx8-cyMCeYjbVQEaEzw5PI-j3OylgohH2-6WTnxHfEYIR8EkNCPQygXtrLEEk0rUi7I0lYe4q7QE9iSXWKdXuYQS_NE4cvs6crus0vllBrvDhA404J1XpH7sd76HmjXAib5Kqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66441" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66440">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=YEKkTxDuLUqlL0M0_HmFIMSn489U8ZWykNnjbRvpsYw5U5t4L9_c-TIIoagdI0hgFT2n0b16vWBVZ3UxZ0an9T_-3XnSCqnj9921PU-Q-pEAsve4SCGybaUS3l9wNj8n0GrQxfZiYIMslmOfqdOzzjd7ypGsrxZ4PNCTX2FQDvbYBpzHczV8ahvBWI5VbVUF6xQQkcMUHt89Us3VRRSfV1_01-By3Yi4QwfYpAKmxS7VnHsDmIbG1CmuA84DU7atD7TTxIm1Rx1PK6VxWmCr5qK8A74s1ZW1LcypPtuaFsN87x0i3DYUznK1ruxael7lrAFCVbifll6-1THwRh7N5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=YEKkTxDuLUqlL0M0_HmFIMSn489U8ZWykNnjbRvpsYw5U5t4L9_c-TIIoagdI0hgFT2n0b16vWBVZ3UxZ0an9T_-3XnSCqnj9921PU-Q-pEAsve4SCGybaUS3l9wNj8n0GrQxfZiYIMslmOfqdOzzjd7ypGsrxZ4PNCTX2FQDvbYBpzHczV8ahvBWI5VbVUF6xQQkcMUHt89Us3VRRSfV1_01-By3Yi4QwfYpAKmxS7VnHsDmIbG1CmuA84DU7atD7TTxIm1Rx1PK6VxWmCr5qK8A74s1ZW1LcypPtuaFsN87x0i3DYUznK1ruxael7lrAFCVbifll6-1THwRh7N5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا این لحظه، آن‌ها به تعهد خود پایبند بوده‌اند.
سنتکام اجازه داده است دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به سهم خود به تعهدمان پایبند هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66440" target="_blank">📅 20:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66439">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atGD0p_GrtQDhLQ3GeIz-WZNn8zVd3d3tXshyUjbxJ1dXLoMDo_LOVoy8qJC6zvwRh3IuzD5VFMoTddy0iieCeD1l2cefoPGvC9Ybt02ZFAn5LoLfDz268X9IRxcQWoC6s-jUNHzfi2w8AFsX8l_o_XfX_G5QZNygQ03E5B8ISaT_sV8VKo03z0vxBm8CE5oCjJIpSdRb3TMEeeZsyEX72Q3B7nRZjhSt-pOR3vZyjsCBK7ObFQkIri6QeKwmguHwe2GbQOIlixdyHx2ZHuF8rTCR8kj9tMNybeX9SBaV3odf0kVascm3uTX_BHc6vyQeo0GPgOVJY73_dSYVaDbNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
فایننشال تایمز :
گزارش شده است که ایران به ۶ میلیارد دلار از دارایی‌های بلوکه‌شده خود دسترسی خواهد داشت تا کالاهای آمریکایی خریداری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66439" target="_blank">📅 20:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66438">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBIwD_EG6n5pg7IhIS9zIGobA34ZhlIWjYnp-cR-ED5QylQpLheEwzVuFDvM7sg3ZX9fVpuXOL8jSwM8Z750NgT86KYbDtwp0BHAGtjTQx8GdVlaQBnSbsZPkjZJ6mq1tZxlEMxfoKkehF3ZmrmE_qC4DoePWjnsXrbzHKQrhmlQI_OgfpMUAuP2bXKkcsg1uLiLYAJrSfcj_rOQAilEP8SLiMA5-NDKwYZn_riF7Nh6fWw3-27iI3a3QPRJQmV2loOeuqKgkuLVNTZaBwV7kNGPhbu4RqWiAoL2FU3ykxQGEuSwY7vRWGWo_h9VT9m0MDjVIY40juc6Wx31pRiuXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ونس: کجا می روی دونالد! «امام مجتبی» منتظر توست!
دونالد: از روی امام شرم دارم ونس! شرم! توان دیدن جراحات ایشان را ندارم!
ونس: تو هر کار توانستی کردی! تصمیم امام اصلح است بر ما!
دونالد:‌ چه کنم! چه کنم ونس! با این جماعت هزار رنگ٬ که دروغ را چون «رج قالی» میبافند! امام مان تنهای تنهاست! شرم بر من ونس! شرم!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66438" target="_blank">📅 19:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66437">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=HplpYfbSGU3XYl06hkmpsn6DW1m_y8GuAyCSJKPqy_yF7GGdNEnQTSVhTjSyNAFvarf_wz9igG-3QlfuHMZJnNBP8sRygjgNOEO_mV4DyszqJw0kfMJ9U2igzQez6_uKHXena--cM_n41IE19r-6kLID5t3gbBYuZKzyOKW6fYkFOt_aaDb2vGyQfeJ4opaTukDMEaJAg3YnI1RRBgRxsn7zzwgxx0U2h24iA2uKHZgiGmsz2fIOXKvuDaubVfm6UhA8Zce_1mmx5JMlUyBiV4NAjOFG5LEl-oZ4NT2P7NTCjEnhZ63TzDGBEq_T_YeqYcQobL3iwpvDR_xWb435CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=HplpYfbSGU3XYl06hkmpsn6DW1m_y8GuAyCSJKPqy_yF7GGdNEnQTSVhTjSyNAFvarf_wz9igG-3QlfuHMZJnNBP8sRygjgNOEO_mV4DyszqJw0kfMJ9U2igzQez6_uKHXena--cM_n41IE19r-6kLID5t3gbBYuZKzyOKW6fYkFOt_aaDb2vGyQfeJ4opaTukDMEaJAg3YnI1RRBgRxsn7zzwgxx0U2h24iA2uKHZgiGmsz2fIOXKvuDaubVfm6UhA8Zce_1mmx5JMlUyBiV4NAjOFG5LEl-oZ4NT2P7NTCjEnhZ63TzDGBEq_T_YeqYcQobL3iwpvDR_xWb435CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار:یه مرد دانا سال 2020گفت ایران هیچ جنگی رو نبرده اما در هیچ مذاکره ای هم شکست نخورده
ترامپ:کی اینو گفته؟
خبرنگار:دونالد ترامپ.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66437" target="_blank">📅 19:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66436">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdEqC3Tm2Zog7tPpF_dMA4WQoHHs49ZMOkwQLh-UupZED4FgR2XrOC94RX9_21bAlXJ8rc5gep3eJu8nJ-o6wz7x3-ZkpGUQ9RZJaOwTWbL9mwqhxcTD_DjPYKyhDgbiOj2Xf3XxFAQF108UTm-aY9MWenNX5_mR2MoVOQS5Gp_60Mz58yneLxx6Xc9FMgh5YSNOURQk7TMqKYKy1UXA2ElJ1BuZ97b9jS-QCZGNITifPmUZx3aPkqSbXr84oAropdeWg4wDMsbKzntbNUBvtlKG9sb4uOHHvzYeIcJvyZGGKugIPfBjaLxxxtd33F1a8SiRtl1l_eKiNCsvPyWOew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
الجزیره به نقل از تلویزیون پاکستان:
سفر برنامه ریزی شده شهباز شریف به سوییس بدون ذکر دلیل لغو شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66436" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66435">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SplFIzgcLf1mEXXQIuw8oKNwjfdUB3rhv_pZuhGejyIQYkdEWHv1Mf7j0JacW4GLXmNiKLxjFKFdorSWhJrvkuI5sAd_Uo8zgwc1xGHJLxm6Yzk4N389iJtDRjUMIWxXeyRPJkLHpbY95KAcizl3zwsAMFO73dZ7AuL6kL5BfyKBj3WeJP4c4lXOTKoSMfBKTqeGWOeD9ioItyeoxbrgb336xVqTkWNEouGDDDWOQdpWnp82ZyRlbBMFz0vHhqdLNeHmjpMIzfOUMxI8BNZr6aN5_FyNOJOWvaivFA2MGv2mC0yjQZQQdQKjzfmYJJ0lAyziweRdwMWMElLnHLVjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
نفت جریان دارد، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد (جهان امن خواهد بود!)، بازارهای سهام در حال رونق هستند، مشاغل رکورد زده‌اند و قیمت‌ها در حال کاهش هستند (قابلیت خرید!). کشور ما قوی، امن و محترم‌تر از همیشه است. «خواهش می‌کنم!» رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66435" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66432">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TyBoIJJAGhGQH6Y0yJkVOw6x3ZsahQ5j2Fh0QV3nd3LoD7PDlZZ0Rh9Zo3MSpP6LrCuRvylWr7z6e3qRGcPxp506Db9DGSX2TbDc2GGFX_q1WMlN-TYbmPo1B63hUBWmuXrM76kNvEnHWRf8dmOCXJbCVQ9Cxbksd_BYT9mSmphLjm_i5rZl-Tvb-QRzDakxTbOOtxJhLk7GTcpcCW0pcKaLa-CjoJ0KOuorGKQkEps2a4miFvW_PABHGUjWbrpLI8dMdQK1Wjx-6E3x1hGouGR6JEnRfja_-fgypbbELRR5BDvA49HFZ-9_V8uP1qDetKKAP6KWM6eG6L8OBujC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERBDJ8JVRsWLx_yRwD_1pa_MwQqjTtYapDojBeaFJw4h2bg8zvGAwzAVd9lgA93TaEpTsQ1P79YcMLLy11Yz_xS1PLEKBE6rRbghkkExAbGAivK2WWzzpsFGgNyJbwFdsyBZRyuFe2dIudMWADJgrMmAPTJEuYQE7vpLOBO-pshmbfDOGUD9Z8se5D4Ay1kjg8JjHxXG77sgTb0Il4aNOkKt4P3DwDqcOuYAY266QfWiwu7-gy5dX4765OcL6yAC0cgquT0y8KEH3ZP9u1eqKjIszRevvNXHv8VAF1cUx_SSnku_ywKR04l7JBL518Uv2tkwGVePnB-8cC_10_NYog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=dr6-Ocw8ysjCZLQluPnms7zh1iDjovlPJb4gvlLhJbSwxC_jAlK6FgxgUFr3Z94pP0zGoUk6UNjp5V6qYKfBEH_HiXHfWtSjp7yN7s0A8fhMfNMPBFKUa2kLlN1uJUoTLq_ZwG0bMA99NwsFuQsEBMd2bZopn7_dPJ5oI69sn425V4nKA4Lo0zO4H_ULGkbTsDov09y34PZ1AsRZlzXHFSQ7pwOMbRZgX_hNKh4dJDLfF6XEEJtMSZPU59TN1JuHRqP0kIiTh7eQuB8b7hu96GPngGcYvtXk8O-omKDAeYzXRVaVC-JybM5T6F0OuCBP9moIHUH9CA4qk3T0JcpWXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=dr6-Ocw8ysjCZLQluPnms7zh1iDjovlPJb4gvlLhJbSwxC_jAlK6FgxgUFr3Z94pP0zGoUk6UNjp5V6qYKfBEH_HiXHfWtSjp7yN7s0A8fhMfNMPBFKUa2kLlN1uJUoTLq_ZwG0bMA99NwsFuQsEBMd2bZopn7_dPJ5oI69sn425V4nKA4Lo0zO4H_ULGkbTsDov09y34PZ1AsRZlzXHFSQ7pwOMbRZgX_hNKh4dJDLfF6XEEJtMSZPU59TN1JuHRqP0kIiTh7eQuB8b7hu96GPngGcYvtXk8O-omKDAeYzXRVaVC-JybM5T6F0OuCBP9moIHUH9CA4qk3T0JcpWXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پختو پز اوکراین در مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66432" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66431">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=nUkwMYM67J_OZKruUZseWUkY4fqjB6XlirhbUu-1iCMkg2PHaHr8K7Fz7F_PtJ1rQ1hwNbOqJlSqVp8n-qfuuJpzL70hEhKsx19kYMkHWrO-iB7PiN-18m6n9OznMuovDXLbu-ePnMStBBfV36FJBsUGa1j1br3YPeO11LlfySEGu1oEtKEF4A0V8k7GFYncTKIY77Q8zixRTrXAE1mSm1t7QitbiSp4Yqvq2MF8MJT1QT124RJMCe_VkbN-HLqqjZP8nUyj79RQrY8JOxqLUKqjjrbcFcoj-ksg4P_CxdV7QSZstfprHA3Uum_aldHjmoq0bf6eO3i2oqujkmQHKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=nUkwMYM67J_OZKruUZseWUkY4fqjB6XlirhbUu-1iCMkg2PHaHr8K7Fz7F_PtJ1rQ1hwNbOqJlSqVp8n-qfuuJpzL70hEhKsx19kYMkHWrO-iB7PiN-18m6n9OznMuovDXLbu-ePnMStBBfV36FJBsUGa1j1br3YPeO11LlfySEGu1oEtKEF4A0V8k7GFYncTKIY77Q8zixRTrXAE1mSm1t7QitbiSp4Yqvq2MF8MJT1QT124RJMCe_VkbN-HLqqjZP8nUyj79RQrY8JOxqLUKqjjrbcFcoj-ksg4P_CxdV7QSZstfprHA3Uum_aldHjmoq0bf6eO3i2oqujkmQHKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد کشتی ها در تنگه هرمز پس از امضای توافق
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66431" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66430">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL1_FjKx0LYItCuR6DooOf18tcMrkx21ae74xIaDh-eQ2DVYNm7Ph08-g28wqI6wJ-DXia9II4Rf24NzD2jHIXspFKCtphq_GD_FcKDgFuh3t1OzwrDKO5bO2zkmpRtdsTQH9_6JRC5msWG1ZT9wgFWZcEnRD8xcB8xhOfQGwwiQj1putxOpcDX9tI840Psa2Pd2cxTMMDmm3kTtmx_F8LmeoIPDPxdR7BQk1vZArfP9exldn0_SVrnFBig5HCmf0n1d8gdW8nqAAF1e6c80HmkdOmFSsm6HQrrRx40uGbY8Za2kdOioiNwyMMYDIYjV7TgBEt0TJU3nssj37UrhbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ارتش اسرائیل؛منطقه امنیتی فوری در جنوب لبنان:
نقشه منطقه‌ای که نیروهای دفاعی اسرائیل در جنوب لبنان در آن فعالیت می‌کنند
بر اساس نیازهای عملیاتی، نیروهای دفاعی اسرائیل در منطقه امنیتی واقع در حدود 10 کیلومتری داخل خاک لبنان مستقر شده‌اند.
نیروهای ارتش اسرائیل در منطقه عملیاتی جنوب لبنان مستقر شده‌اند و به تلاش برای از بین بردن تهدیدها و بهبود دفاع از جمعیت شمالی ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66430" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66429">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLByvuNxyZaOpyhc2JchZJcJ1WUE5AkwY3b8PEWKkO1qyDDRc74oqoYU2RN-_iDQ-eDBT6a5k7JYd54Uv4XOemyvOwaapYV8gqzczFhL331D0YvPkSBBNVOitoDz-bTVcHaK3AMFEDPQxahXAkyc_KWTUOjsVyVGKcHvnhLCmJwCww6UP-5JKRCxjME9FMCmSz0OleQJjV3HebLiEJLqWvvXMuBMBf6rnFkbgM8R6SsZe3aYSUjVywPq0uSHJ1tQejGYHYZQKgHLTHCBP14bmlL4_35i0P54qlUCg_G1fSSrz9w0z2LUbHyzAla_oHmBxPiJkIJcuHpfPusuc3J_Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان؛این یک سند تاریخی و پیامی از ایران مقتدر است:
صلح در سایه احترام متقابل تحقق خواهد یافت.
جمهوری اسلامی ایران به صلح جهانی با حفظ عزت و استقلال، پیشرفت و همکاری منطقه‌ای همواره متعهد و پایبند است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66429" target="_blank">📅 16:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66428">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622db6728d.mp4?token=OpvL9lYMSYERfWybqc8-kNJAFHXs0tDR9QMMXDOW7dxFfKDkjjMn0TwTj8-MtGrJkoVuHJGMdBtmuxDyQkLBtbKR8JkJ-1Su4GD5zQPpTNQPf5h_eWqsAUZR9GdvoCGwcsu3A6wo8E2or77xEkyfOhovfPpKE_Ue71pFyaL6DMSTCHpoDN06cR9Jm4w8Qklh3BBYIa8hI1lYEma8Hbo5BBsN1qs6AHkI3sJICKjv9tX7SXwjSFWdHS4V48QcuDP5cAvD0koGXvsWbuwI0RcRD5ugHfIOMW7rheBJVSEFDGQPhRB7elefAwoZYf2QISD4pbDYvfjCEATbe2hPq41MtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622db6728d.mp4?token=OpvL9lYMSYERfWybqc8-kNJAFHXs0tDR9QMMXDOW7dxFfKDkjjMn0TwTj8-MtGrJkoVuHJGMdBtmuxDyQkLBtbKR8JkJ-1Su4GD5zQPpTNQPf5h_eWqsAUZR9GdvoCGwcsu3A6wo8E2or77xEkyfOhovfPpKE_Ue71pFyaL6DMSTCHpoDN06cR9Jm4w8Qklh3BBYIa8hI1lYEma8Hbo5BBsN1qs6AHkI3sJICKjv9tX7SXwjSFWdHS4V48QcuDP5cAvD0koGXvsWbuwI0RcRD5ugHfIOMW7rheBJVSEFDGQPhRB7elefAwoZYf2QISD4pbDYvfjCEATbe2hPq41MtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعد سه ماه هرشب توی خیابون موندن و پرچم تکون دادن ، بهت میگن اقلیتی تندرو و خون رهبرتم پایمال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66428" target="_blank">📅 15:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66425">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=KYipMIlKBwfE3-dBR40OOAOxQqAN67LZzHZEMt0gmxsoByXOWziyJ0s_1tOuZfO3WhRUKbqhKcb-I5hHKjnC3Eti_K8-PRDXX2XlHarmO2cpIyVlyi4BwImWQFU5PCK3AbH_G3TWdCsqSQG8mTO_OJw88bYu2K3ESCogmKWRPn8sXmF8SPLkPycI8Bql9WBheexpZGGs20eqXRndVhKZi5YRBgMJkGmf74YEmkLs_Uxvq4V2g-Q8tK-GvZVguB84-AbyEEYaJYkdjnJqwlRCuuSJd_vcrviPS_dwBw1YKzGooMZVVYgZLdw-WPCm5w56fNHdbPmTQBi8KXj2iQMiKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=KYipMIlKBwfE3-dBR40OOAOxQqAN67LZzHZEMt0gmxsoByXOWziyJ0s_1tOuZfO3WhRUKbqhKcb-I5hHKjnC3Eti_K8-PRDXX2XlHarmO2cpIyVlyi4BwImWQFU5PCK3AbH_G3TWdCsqSQG8mTO_OJw88bYu2K3ESCogmKWRPn8sXmF8SPLkPycI8Bql9WBheexpZGGs20eqXRndVhKZi5YRBgMJkGmf74YEmkLs_Uxvq4V2g-Q8tK-GvZVguB84-AbyEEYaJYkdjnJqwlRCuuSJd_vcrviPS_dwBw1YKzGooMZVVYgZLdw-WPCm5w56fNHdbPmTQBi8KXj2iQMiKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین اوکراین به مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66425" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66424">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=fnQTWYQLXZPt2_aAqyz0fooCVEEgrk2UbY4uxo8e-pdsv9w63n1m7eDO-kK_TOkREAOZWTgWZC-fOfu6Ye12DzSmJ8VvaFVbyi7LrK4jXrfHIRLXeLrjEGakAo671eyZhsP_0jStMpLM3xqTyagFJ1TQs6b-SUdMj-ICAt9JEFHkmKUf1R5rqt4kSIcqtSRQ5pJQt4zyR-Bj4lG0t1J91uJk8GuB02C8UHFTuciNRDTVMgtVOBF6viQOaA7v3O2OZS0FMKbuD7oizQwg05Oumah6fxUyzZB0IJr1-lJZNfru9rXwU6JFoAKjn1rQHpGo6FWt3rW0usxcgoszIl4Y7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=fnQTWYQLXZPt2_aAqyz0fooCVEEgrk2UbY4uxo8e-pdsv9w63n1m7eDO-kK_TOkREAOZWTgWZC-fOfu6Ye12DzSmJ8VvaFVbyi7LrK4jXrfHIRLXeLrjEGakAo671eyZhsP_0jStMpLM3xqTyagFJ1TQs6b-SUdMj-ICAt9JEFHkmKUf1R5rqt4kSIcqtSRQ5pJQt4zyR-Bj4lG0t1J91uJk8GuB02C8UHFTuciNRDTVMgtVOBF6viQOaA7v3O2OZS0FMKbuD7oizQwg05Oumah6fxUyzZB0IJr1-lJZNfru9rXwU6JFoAKjn1rQHpGo6FWt3rW0usxcgoszIl4Y7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏جی دی ونس در مورد مسلح کردن معترضان ایرانی:
در واقع تا حدودی دشوار است. می‌دانید، نمی‌توانید همین‌طوری از آسمان سلاح پرتاب کنید. واقعاً زیرساخت لازم برای رساندن سلاح به قلب مردم ایران وجود ندارد.
یکی از چیزهایی که رئیس جمهور خیلی نگرانش بود، همه این معترضان بی‌گناهی بودند که توسط افرادی که چند ماه پیش مسئول بودند، قتل عام می‌شدند.
آن افراد اکنون رفته‌اند. اما خواهیم دید: آیا این رهبران جدید با مردم متفاوت رفتار می‌کنند؟ مطمئناً امیدواریم که اینطور باشد.
و اگر اینطور نباشد، می‌توانیم وقتی رفتار واقعی آنها را ببینیم، بفهمیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66424" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66423">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKCn1hTavyfgWYFPLLZ12_PBb_mFt1gCwCrgHA7emzsiFjDJd_HOTAR16dDoPAU2safem0J57X7y1nsbCkKD5Cwm-J_M5s5ZUynddNx0eb90umv9IKUbaDzBq6IDuKGHVjFDIoAAQUSYFNwIZhah1CqpSNn8upyJlxf0s142yVMK1-baEuKukjdrfET2_Q7MgpRyNRAriETYJq1iqTilcs30rHxVH9e3s4y0Bbklw2Ryf784QOCD0Qm1xXxP9Hk9D7qcKQI_vxF6VPHTZ4RjKhb3W_Gg0KZtO0QNsAE5lV-kv9mIigKfvh9O8smCuqt7NNxSzeAcqap7cjwAuLe7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حملات اسرائیل به جنوب لبنان همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66423" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66422">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66422" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66422" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66421">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUz0f_w7aWoJCypckrWU3WSamQxTP0DPolCxnWQ9ppQ2JiUSMEAvSaxBjHMdbzndxfwYuhVX2kNV5gD75U0_tCmWEdccsKvnjkGv24NJrDKW6RAHS4HbVWSyoP4e9mMxxWJKtaMMvXLOOcM81_basNyOMu1iCbbQjjD0LIdbnRGM03gOJ_LksNMonWlOEvyzEfpOMf0Q9D-Cs08EORxGr3ZSJEN_-ounADeOxdtXlDw-CB0ies-EHfW61JPggrgkhzVD7niRhqe4bgtMmd1e9ZaWkUz4WwxAd1fy8jU1CMAU_Z00Fmr5iL5Mc8Qy5Nro7vI_jYziJfwasSND_rle_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66421" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66420">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pExzPxIjwzB5FkrkK1MRbkrlmy8DO9ajFOQShzThi-LYFKx4lUraHLAE53fM6OGHkZOuvfsgF2ZP1Wr7qELRDNJpy_eEKs2LozuFsgGiie0HYGuBEcTvjkHavhuNcVW0hPVvmWbEj7VKyUrRPLkt9cMR2F8Ss0NJylDH8iF6dzvoRIIisEphQy_EbAf6JRxomWjYMLr_e_LtLovFZF7g1-P4zSiEwA8L_GMXmP8rPi-b8bkon8d5MTd7wCwIZ6OahgVdC4fOBHRhmXrvE9s8p-fi5qoaGYYVKtkMzpGK_nvB2U0NWrW75zQY7ECGRaMsdu_1I8LUbpG1DU1gIx-1kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای پزشکیان از نزدیک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66420" target="_blank">📅 13:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66419">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1890fc432.mp4?token=nzRyQporzDEiNxlqHy0QhsvYV030GcMX9sqioHhQe0Mh7GUBI6pOiu1rvzwVjZcLdbSCKGt_VJjsDh3xWZR0dwsSbutDRRxFcvxq1ArB1sQ5cMhcINrBYs-rB5HTQiJHzKiwUqj0jM_I2D8wk6W4STUVzo4CYRTMYkamCAG3AI_YORANasAbNaqOLtg8tk1vbhKkWDh0wT6F9zyeB3HMCUrBmUNJ0ey7EX4rM-CcbelvkSW1OeYpz3FqiOWoy9vCRoTXUK6LDfK5FVZMCpL_w7e3No1AVJHU-Ah4JKIgEavavRcQk7efzmDR-DHTXODwnMzHdpzGFLP-D426qpt8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1890fc432.mp4?token=nzRyQporzDEiNxlqHy0QhsvYV030GcMX9sqioHhQe0Mh7GUBI6pOiu1rvzwVjZcLdbSCKGt_VJjsDh3xWZR0dwsSbutDRRxFcvxq1ArB1sQ5cMhcINrBYs-rB5HTQiJHzKiwUqj0jM_I2D8wk6W4STUVzo4CYRTMYkamCAG3AI_YORANasAbNaqOLtg8tk1vbhKkWDh0wT6F9zyeB3HMCUrBmUNJ0ey7EX4rM-CcbelvkSW1OeYpz3FqiOWoy9vCRoTXUK6LDfK5FVZMCpL_w7e3No1AVJHU-Ah4JKIgEavavRcQk7efzmDR-DHTXODwnMzHdpzGFLP-D426qpt8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه امضای تفاهم‌نامه توسط شهباز شریف نخست وزیر پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66419" target="_blank">📅 13:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66418">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fdfa7aaf.mp4?token=NSqZ7gyT3-xy1USFfHpiXdEpzq3Pw0t2Z9OoJUU5vqGJ8Vojz1AENaDDa8eIuhmN8qJaUVLLPqp4L0sRrdEsCcbfymbSnuYUha2r7UDrsU_NJDEVGEqPDnrCjGUQLIPpGu_rORHICDLeH5e60NId5OodL-75Aksb3LbL2E1_6jOVJNzT4TlKzL7srG5p-HUyC5MrfJNWWnheWF0jE7oNVHp9JhSZPtymZjQOdG5AIT4IMg_sP68gtKVuPl66mPxztZPbL83Ko7AmieW9aOgmLle-K5hFUWA3MLXQd1ga3Vb-pdif5LY0C3PIczHEoUB4i7PPKvSsSG0h-4Bs72CLwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fdfa7aaf.mp4?token=NSqZ7gyT3-xy1USFfHpiXdEpzq3Pw0t2Z9OoJUU5vqGJ8Vojz1AENaDDa8eIuhmN8qJaUVLLPqp4L0sRrdEsCcbfymbSnuYUha2r7UDrsU_NJDEVGEqPDnrCjGUQLIPpGu_rORHICDLeH5e60NId5OodL-75Aksb3LbL2E1_6jOVJNzT4TlKzL7srG5p-HUyC5MrfJNWWnheWF0jE7oNVHp9JhSZPtymZjQOdG5AIT4IMg_sP68gtKVuPl66mPxztZPbL83Ko7AmieW9aOgmLle-K5hFUWA3MLXQd1ga3Vb-pdif5LY0C3PIczHEoUB4i7PPKvSsSG0h-4Bs72CLwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیرزن کسخل مکرون دیروز موقع عکس یادگاری سران گروه 7 نزدیک بود زمین بخوره و شانس آورد ترامپ بغل دستش بود گرفتش
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66418" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66417">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">قطار پیشرفت آموزش و پرورش کشور خدایا شکرت   @sammfoott</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66417" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66416">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDoSIes3iHuexFMcSB9se38hUZPgWgSoUdW9Ct_rdJqDdDDvUfNS9sSazyuBGAsX4lBH6JJMow9d-iwXoMtPrGqFJoxj6D-Lq4x0u3pyprFOXA9lpQwrQvqoHrWHYoCxzqYs_QGuT1KxcRPiPhgSXTzxfgqx2hFiq1802XCyttUMi-QfHnfVXOpdRlUT4_Khs736YVOK_Dmi54LpNICmqVFP3G7O4rPJVatb6f4g3mfvofa1RrABhSHSAIMkBK8zF8uydDqxegtN0KZ5PMEn7EjgEdDShFZdOp6P_vvegkjGt4y6adgauvLmDxODfZh3E5STKDSrSIh2B29Esn8Wmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«این احمق‌هایی که فکر می‌کنند من با ایران به اندازه کافی قاطع نبودم، در حالی که بازار سهام به تازگی به سطح بی‌سابقه‌ای رسیده و قیمت نفت در حال «سقوط» است، یا حسودند، یا آدم‌های بدی هستند، یا احمق. بیایید دوباره آمریکا را بزرگ کنیم!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66416" target="_blank">📅 12:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66415">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16c0579b45.mp4?token=ZS3QLoYcCOMDccPkcGmAzkEsErUKhSM93CURH87YlW4mHx6-jL1UztFvrmz1bi17JiCXiXv_O7PIpkjpHjqYKqSjV-LjD53uuB_RbuHY7FW_OX9_sAFbskzEW1OyKuH708r-Wu_UKk8MJrWcUVnzKm9gJQzhd1dMlyFUh4hj4Anh_jkp73-5SVMfvGlPBVh4I0of5Dt-AFDLfUCu5Nrg3Yr8208yVaRU-aukrJ-CnzIgulwDid6pGjD_XXlzuJyuS7v1-AaAxI6nRO7qBq5l9dBmbj16TEnC0tKzGFzKmOClLezNxzd5qiAtstPskMvP1yEyRzk_vZSfkJzE6Q-9KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16c0579b45.mp4?token=ZS3QLoYcCOMDccPkcGmAzkEsErUKhSM93CURH87YlW4mHx6-jL1UztFvrmz1bi17JiCXiXv_O7PIpkjpHjqYKqSjV-LjD53uuB_RbuHY7FW_OX9_sAFbskzEW1OyKuH708r-Wu_UKk8MJrWcUVnzKm9gJQzhd1dMlyFUh4hj4Anh_jkp73-5SVMfvGlPBVh4I0of5Dt-AFDLfUCu5Nrg3Yr8208yVaRU-aukrJ-CnzIgulwDid6pGjD_XXlzuJyuS7v1-AaAxI6nRO7qBq5l9dBmbj16TEnC0tKzGFzKmOClLezNxzd5qiAtstPskMvP1yEyRzk_vZSfkJzE6Q-9KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط اونجاش که یه موز و دوتا پرتقال بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66415" target="_blank">📅 12:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66414">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb19ef0a8a.mp4?token=RUoD3e3q-YmCJmpPqmP5myVPsJLEOiNf8w4UZ6qwN4e27nMPMWZz3axy8to32L6oM_gOHLf3V9aDkg3QUJXCTxn14UMyVWq4RWYuT73ivi3qz5tetxnJmu8d-llTbgE5yhepJ1ALW3Hng4iYR2f_wSMpNxi6B8IDs_Eg77xmqsf9x-lKKGDCFJ6lJ_qXSec6xjFkae75D1pB93WFmmh0LAOMb084-7XyfJvXabqpP1qEwEWpkoMUFYOWsecQJQl5ugrCBQfKt-bJ3UsPcPYE_unlnohQHUeNvy5s9NyVmINR0JODyTRiR3HC4NBq3K9PQXbQBUBuR2oferouSHrBNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb19ef0a8a.mp4?token=RUoD3e3q-YmCJmpPqmP5myVPsJLEOiNf8w4UZ6qwN4e27nMPMWZz3axy8to32L6oM_gOHLf3V9aDkg3QUJXCTxn14UMyVWq4RWYuT73ivi3qz5tetxnJmu8d-llTbgE5yhepJ1ALW3Hng4iYR2f_wSMpNxi6B8IDs_Eg77xmqsf9x-lKKGDCFJ6lJ_qXSec6xjFkae75D1pB93WFmmh0LAOMb084-7XyfJvXabqpP1qEwEWpkoMUFYOWsecQJQl5ugrCBQfKt-bJ3UsPcPYE_unlnohQHUeNvy5s9NyVmINR0JODyTRiR3HC4NBq3K9PQXbQBUBuR2oferouSHrBNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
با همچین عزیزانی تو ممکلت هموطنیم :(
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66414" target="_blank">📅 11:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66413">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=GRO4OoceT1WkGOhPxEBWse3LTUDJD4hM4p7lra-xaX3h2laOhLz29RwoUL2V6G86XhmPeMnaLOZIL7OrIi-9n4LZ1l5-EY4PD--E3UFlh36CXfckintEWxGU-oruWCeG6pYMoJFyGHEOMLLA1CRhYGQBIeIpoZm7fraZHJ2qEHtgfKhbabUMrp8NsQTxKLgT1DMKVx2kRsfhDFHW29yP-nAiXd4bBpCOZVpEnjP0395vX5qb_cWhh6c_9z4ltYI7LK5G0JpVdQrK4EWr4F5MnxRW5iXYv5YC7QWAdFxUBnF9t4_ffHpyrjd2Fn7h6ZSna6wvZ4uV8xAS7F6L2kKGSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=GRO4OoceT1WkGOhPxEBWse3LTUDJD4hM4p7lra-xaX3h2laOhLz29RwoUL2V6G86XhmPeMnaLOZIL7OrIi-9n4LZ1l5-EY4PD--E3UFlh36CXfckintEWxGU-oruWCeG6pYMoJFyGHEOMLLA1CRhYGQBIeIpoZm7fraZHJ2qEHtgfKhbabUMrp8NsQTxKLgT1DMKVx2kRsfhDFHW29yP-nAiXd4bBpCOZVpEnjP0395vX5qb_cWhh6c_9z4ltYI7LK5G0JpVdQrK4EWr4F5MnxRW5iXYv5YC7QWAdFxUBnF9t4_ffHpyrjd2Fn7h6ZSna6wvZ4uV8xAS7F6L2kKGSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
برشی از سخنان تند شب‌گذشته قالیباف خطاب به ارزشی‌ها و تندروهای کسمغز
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66413" target="_blank">📅 11:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66412">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04da6f24fd.mp4?token=JYrngMRJYJJfGwjp_A_43EIu12yUtWam03Xgr8mZFLFHfjJveSc7TJFuU__r1kM5fpKmShsE2Dpij4z7TYYGgFImmXr9-yN_DMI_0-1wVI-bTlbFvUbpvHTNWl7NioTZfrX453W-7rZ7NfKXGdRZjHpEGgfjpcmXMTH5sdyRQUuEFP8n06M4ul8ZRB61fsefI-RXkFs-wZSE3wi4-ut8BWs_BrOCGK7PJlWzmw-rvvb8bOyp0axa3QgWYVeGeEBR4YPjpX4NFjUShy1kE5Je7YI9hX8QS_bRR5c0vyF-7jMgSEbGzRKKiEV2983W5Xr84H6wwDiu4RUzBryCpHJWNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04da6f24fd.mp4?token=JYrngMRJYJJfGwjp_A_43EIu12yUtWam03Xgr8mZFLFHfjJveSc7TJFuU__r1kM5fpKmShsE2Dpij4z7TYYGgFImmXr9-yN_DMI_0-1wVI-bTlbFvUbpvHTNWl7NioTZfrX453W-7rZ7NfKXGdRZjHpEGgfjpcmXMTH5sdyRQUuEFP8n06M4ul8ZRB61fsefI-RXkFs-wZSE3wi4-ut8BWs_BrOCGK7PJlWzmw-rvvb8bOyp0axa3QgWYVeGeEBR4YPjpX4NFjUShy1kE5Je7YI9hX8QS_bRR5c0vyF-7jMgSEbGzRKKiEV2983W5Xr84H6wwDiu4RUzBryCpHJWNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66412" target="_blank">📅 10:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66411">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=KnSwVSUHch5Liwp2yzMVCMNdCCEWxhpJoBusJigW-VWdjfDaVBjqIc45Ak6uwR3uLzld-4L1ot6e8xERg6y7uX3gwsSjS0expsYvNWzy-wFCvRlkU7BKF-MyHMJ0pOcsl517Z7Lo210GCAn58cGGyxhF3KxB0k58OBcxBICeSqXz7GCJN3rUpgnFD6erTerzU4VIx97y8FOXLI9m8rLE1dquz_t4q-m5GNBeNJVOHdfH68h4_OF5p8Qy4g1-VMzH8oyuhVGf7fa1Jc_1FzceN6RGxl40Mvcckb8-fSC6ETmI1N5SiFwkCxIQQlb3YuIhtYkOR9ENwvUXsXphm1ugJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=KnSwVSUHch5Liwp2yzMVCMNdCCEWxhpJoBusJigW-VWdjfDaVBjqIc45Ak6uwR3uLzld-4L1ot6e8xERg6y7uX3gwsSjS0expsYvNWzy-wFCvRlkU7BKF-MyHMJ0pOcsl517Z7Lo210GCAn58cGGyxhF3KxB0k58OBcxBICeSqXz7GCJN3rUpgnFD6erTerzU4VIx97y8FOXLI9m8rLE1dquz_t4q-m5GNBeNJVOHdfH68h4_OF5p8Qy4g1-VMzH8oyuhVGf7fa1Jc_1FzceN6RGxl40Mvcckb8-fSC6ETmI1N5SiFwkCxIQQlb3YuIhtYkOR9ENwvUXsXphm1ugJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب دو سال قبل شاهین نجفی درباره قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66411" target="_blank">📅 10:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66410">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=u2ljRS9vDNvarnJdpeguE5hX8aJ0SJx2KsVh_9OARcjypPQKbpDsDxi4xcG5gegF7WWY7ccnG-h3NAXQCi0Mslcm1BIC5c-ykoKTaUp9VeV2nByhCAOcRaJgHYvrQPEkIneCN3i_2nPu92K-pWKDchTeUFUQLXXzu46ldd3gSIFpJaMjCNgVnZStdUYBU-xBpmiP2d0jNOIQ_fMr__pyiZeDvcdrdyeHU49IPbyBWHiVtzinle0A-s0YVycV_F47wSIqZmzfe_lfthjVNEdWBXMl_pXC1-HeD_nFYsIxDNz02eHSnl-vYGNWPIq6f1MYvQ1alLGVQg7-6NrElheZzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=u2ljRS9vDNvarnJdpeguE5hX8aJ0SJx2KsVh_9OARcjypPQKbpDsDxi4xcG5gegF7WWY7ccnG-h3NAXQCi0Mslcm1BIC5c-ykoKTaUp9VeV2nByhCAOcRaJgHYvrQPEkIneCN3i_2nPu92K-pWKDchTeUFUQLXXzu46ldd3gSIFpJaMjCNgVnZStdUYBU-xBpmiP2d0jNOIQ_fMr__pyiZeDvcdrdyeHU49IPbyBWHiVtzinle0A-s0YVycV_F47wSIqZmzfe_lfthjVNEdWBXMl_pXC1-HeD_nFYsIxDNz02eHSnl-vYGNWPIq6f1MYvQ1alLGVQg7-6NrElheZzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
10ثانیه تراپی روح و روان
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66410" target="_blank">📅 09:33 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
