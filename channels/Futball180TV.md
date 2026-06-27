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
<img src="https://cdn5.telesco.pe/file/PpQsdMp-cW7KjfsaJ0lPWHcJhECRgDQ9-uk8ulpl2eNhgByEqOVTHiFRDSxstdUiNSw-6AXQZ6CALjNlDYjVQLHbP07LlEoBnSkweytOOhCZu5r9DoW0VCtzIrgJHfKen-C28xTxbBMZFDDEtFaxfuTb0wkGfq-i0oEbf6hnEtbRA62RN732XhhT3ybdIrFXfvPzthclRxLA1dGEEZeSE-CvxmUmdp_Kw-6Xzgeh_UFz1N7s9p4sSsY-ZUXXct7bfcK1aU3JySFKdtK4JI7IIULPVJkoiNtC1Ct0WrTMLaC_QJ86uyNEdEaVp1d9iUSPp7OUblsyP4SDIycUnlcvHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 698K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 20:29:13</div>
<hr>

<div class="tg-post" id="msg-96399">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-CzKdWvyKznyiIsOhx3a7zvQTbiOpGLEx2xzU4AZr1jvbiCAhAbi5Fc2C8oojPrVlzvBo3ifWXrH3-IQo4zlH2WPbOBE2dLQl0HhnHdiodOEw8XdNiDlFtBR8fK4fStTodjPZ691Dw_Z3nkoYWmcgUBGmUwkaTmYmfN0mUS9tBV5xhuhZQXMKqlmiuiC2u-50rpAaGnDiwSfv5aXvNQKI0IHOdlrDjX7sVgdWj7rJBu0rhZVwjH6-Blsx8Zbt61LSOFl5nSl746t0tsdQlHhdCysBMaS2JaLF6Rygfgjlt8YrN4ChZWvw1Djps0buU8YXtEFXzuZdjPWlsH4LIBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت بده مورینیو
حقیقت رو بگو سیمئونه
اعتراف کن آرتتا
آیا او بهترین حرامبال نیست؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/96399" target="_blank">📅 20:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96396">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmupZgQ2GPc2ZlTRfwFlpFcTuO7By1J-Ntl7aXyzT9MJHe9jyWhjO0NE7Yi-qSsRES78TEk14vXv--z22QIEerFRj-4RaB8b62qJcsDRT_faEjDj5owjo8wI9VLWctGgYxFjFHpFOq4Y4Lxo14sHamnqNatx7JQ-YY2JFCWQmjUiU8COagl-CYYvtLEfFOyBYFNgh4-0Qj1i920RQEaR9uk7vrOBVPrmQIpixfWShKdWGYvnNYdJm8KQW-rrBU18LBeTaU-WeLIiuaFGW8mXvXryTJRapweMQJ-ZWJPSD4wwh5cZBOw6-fc4Z_TdKObyDKChbh9D9likksVfNokp2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GLCNtaq8MEbvTGTx0tvk0Q4_lPNJkK_UKYciXkyhpwtrN_W5_xhfZ9PuQu0kXHzTQKTgPJpyQl6s1VT4n4T8Xrt5I8kr9HMEJNqlv33HgZbAqEgFLQd7gdjwGfsoxwncueF0wcgYqcDCum5vmyYvyHVkG-yCpLmQVJ6IhDFfMW_zfB9hWXTaTSHWYQ1BRA1Nzz2rXWdlz9k9JHfEgf0nZu-ZIjopF8LhvywbLXghJFjfESXn0KKqdygfqFwA5eyjOmdoor9gj5cj2fe244hbNDgk0Fc145Npcl0y4MyjQl95ozF8zW9jp1osARoHMArnAH7i-deF3vqYhMA3F1S87w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ioqnJiLRvw8cwHUuDOz9_yn6Ppcjis0O-J1F8B2xeBSoo-elBis87k5EQNwYDBXzasAP3-zhjIBpBt3b7D_t7DXkmfkaMkMyhTVVb3miWzEWEpeEPlEF5GeJ9bJQUwIamVwujD3HJMePQi-2723302B5Cy0iTwNaWz80oko4ANK0WmrpKoBdR3zY6D2xw0zzA5dyCHrHkFNaShs0z6L6bkoI543lL1cuY5A2jkBJBmwjOchYOo1SQ4MxNkbBf1gB8BNb_AJC9jCrOqS2zVnX_CfjSDtnfURQoiZIw-YSWvme6WUkbPg99zA4jS9ObB6CaYS8UGcEiMwTuQq58BxNfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
🇨🇴
کلمبیا سابقه بدی در بازی جوانمردانه مقابل برخی از بزرگ‌ترین ستاره‌های این نسل دارد:
🚑
🇧🇷
نیمار در مقابل کلمبیا در جام جهانی ۲۰۱۴ دچار مصدومیت شد.
🚑
🤩
لیونل مسی در مقابل کلمبیا در کوپا آمریکا ۲۰۲۴ مصدوم شد.
🇵🇹
- امشب... قرار ملاقات با کریستیانو رونالدو
⌛️
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/96396" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96395">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaVTgcdeYihiFSRPhAu0f_QWOllNLxoTTpuaffvwDKMydPT-TcEcFCVFC5-bXC01sr6d1h7npPdsy7p8lqMO894UD9f4y44BSI9o7FMH5eCJJHUnotqylob9LzDYgfyI6mwUjA8bmIjE3ZfbeDFQIZDc7jOIX7L7meoqoUIpVrtSuZUC3CqH_1-41sJ41t5jOqY3p6Ni5dVUmgtK9Ws8RkLWQszG7e0GkI52iQvRXbAFrg3hqVXyEB-_cL4LON09SHwDbhiGr96YVtQcJERFGDhPM6Akb88kHVoHCOlZgUAmokrJPEGKzzusJYZT8Nx39fp84_VloLyW52r9w1a7mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووری
؛ فلوریان پلتنبرگ: چلسی با ساندرلند برای جذب گرانیت‌ژاکا‌به توافق رسید. ارزش این انتقال حدود ۳۰ میلیون یورو خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/96395" target="_blank">📅 20:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96394">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c7a6696a.mp4?token=rwXonryIWz3sIphycdXKw5agXC7GpbNOIJTXThsCaadoisUavkt3PUto_WjTHM3ylgXIgCZi7JvJz8wWQpU_eY0ycQrPOK7ahlTF8fsBFpaXtelholZ8b3XmJkH3FL4mvYffgv17mNOxVaJ2KMZkYxp85FnOOm2cWeunHV4GYbv8X3JaIMuO-Vhr_jYszno0t4gvXqKh_ISZn4LEmIvkjCt45cLFzPO6v11weTagA-uY3IvfU6PAQC9pyvxJZCE35jjPrcNoGgzctT6shp_m_oL6sxM0Nd1-3yaZ2LLFEOGssWlzxf4YK9ya-rYQbSuhWi1h2SXI1W1Yxb6J28XzhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c7a6696a.mp4?token=rwXonryIWz3sIphycdXKw5agXC7GpbNOIJTXThsCaadoisUavkt3PUto_WjTHM3ylgXIgCZi7JvJz8wWQpU_eY0ycQrPOK7ahlTF8fsBFpaXtelholZ8b3XmJkH3FL4mvYffgv17mNOxVaJ2KMZkYxp85FnOOm2cWeunHV4GYbv8X3JaIMuO-Vhr_jYszno0t4gvXqKh_ISZn4LEmIvkjCt45cLFzPO6v11weTagA-uY3IvfU6PAQC9pyvxJZCE35jjPrcNoGgzctT6shp_m_oL6sxM0Nd1-3yaZ2LLFEOGssWlzxf4YK9ya-rYQbSuhWi1h2SXI1W1Yxb6J28XzhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فحاشی‌ هواداران داخل ورزشگاه به کنعانی‌زادگان موقع گرم‌کردن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/96394" target="_blank">📅 20:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96393">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwjgT4mszYiHSHhpP680dM3Td5gqb9oLS65CdHhfRfhnKXwibP9Ssv6wU772Sn_q6zX4zsJb-VZAflXIgpp_FLnQwmmtR0HJiItgKBmIyIjZB3lWaT0J0zpcFNKjY88Af7yABfGseYm_r5mCDRWVOA-ISpqW44LVUkJ-R6-cua_wzEqeWzmLkzE5-ssgQ4wFaKkCd3ZFCGGVjEqyaxcEHJDlk7wz62hMYtuFAEf9WFALkIWFgAr4cic3L-q6czX3hL_MaMM01FfIJQRkW5pfMfCzJuYhDUF87YEox9dLa6TJPhQF_T6oCBQGYuE1VM_9X8RlWcbmOYExsVSkPLIuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
نوزاد کودی گاکپو ستاره تیم‌ملی هلند و لیورپول امروز بدلیل بیماری درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/96393" target="_blank">📅 19:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96392">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad3a9c910.mp4?token=OElBu9lxTJ8MjrRLV4-mdg0UtHGiA9x246dMmBaVnMJzw7A-lWbsvm0AXjpwQVwBVwXCqZ-xFEekI1kPLMCpeZ6siMeytLHdPNDEXOSeOvl8uUQC2sr7GOTubAj5VziLt9UJLSSSrHk-1LEtiXVgR6zbnl5ViDJCl6CpPz1_EbgQnEvObtNnOP0KYKnzA9NShnkhjZyf5maqtzXJhY6clxfpXflcT9KOanVwQk1BJULRls6HyfgE6CED_4vc-vMfMNxTzkmne5CLBDlLFMmyjRzFOkalTxLQbD4Bsa5_kSquCo3SjG5N_FrgiOkPJFVVsu5tZylEtSlvO-mkDJKNjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad3a9c910.mp4?token=OElBu9lxTJ8MjrRLV4-mdg0UtHGiA9x246dMmBaVnMJzw7A-lWbsvm0AXjpwQVwBVwXCqZ-xFEekI1kPLMCpeZ6siMeytLHdPNDEXOSeOvl8uUQC2sr7GOTubAj5VziLt9UJLSSSrHk-1LEtiXVgR6zbnl5ViDJCl6CpPz1_EbgQnEvObtNnOP0KYKnzA9NShnkhjZyf5maqtzXJhY6clxfpXflcT9KOanVwQk1BJULRls6HyfgE6CED_4vc-vMfMNxTzkmne5CLBDlLFMmyjRzFOkalTxLQbD4Bsa5_kSquCo3SjG5N_FrgiOkPJFVVsu5tZylEtSlvO-mkDJKNjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
انتقاد تند شریفی‌مقدم مجری صداوسیما از امیر قلعه‌نویی سرمربی تیم‌منتخب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/96392" target="_blank">📅 19:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96391">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7Clvc2jety22C5s9FtA6oyKlnB8oNXTbzlMTeOYIZv_QtcH1mIiNtCUG2lEiRiWyKZTIUahbWKew4aQr2UWszf2tC9osCZgYn7z_ufqmc-rSVFnnqmJM8WYOenrDGwdC54-Cnx0N6bpP-mHoP4JIBluNH5mq0Nok2ooIkohFIJUnYxh5lSjWZDKizGC5DOd3l_X3zXazQW2dHhhr1gUSpoXrzizstocPGbCRhhZBbL6CA_OpopOlhBHSNbnaG8TQDrujkblQDwQ301nsGRS-MDF3xQCqcILesIYicDWJG8TiYMTBVodH3L-feq8FtxwMCquyX1RAeULzCV7NEy_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عثمان دمبله در ۱۹ بازی اولش برای فرانسه در تورنمنت‌های بین‌المللی نتونست گلزنی کنه.
🔺
این درحالیه که دمبله در جام جهانی ۲۰۲۶ در تنها ۳ بازی، ۴ گل به ثمر رسونده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/96391" target="_blank">📅 19:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96390">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcc5deaca3.mp4?token=LV-MNBQ_pveE_HBR6FjOE0mXX3sp8I4y7n1Z_Vk0MV78ReC6wbNOtZnEKVx5EeiNInbfdJd1AdryKX_FJlZxIiUPOFAxM0HwglFqZM3i9kMNa7JaBZMuRMi-sepk09Rvl3l3NRg64SUdhL0TDv8YTVmGgDb7XA93oBjOrRtgHIraW0eNTOHMaI-7sD8yJcys7IBaT8R8SK3esVbiuNKsK3y1H_vQ-rTcHVXoCAVJdPOsNZI1MZDKjd6j4HDY5zmD8NOyXrbN_6jcEqDIy9vyqzu68HPxCSf_NkAuWRYrKI5fM2e78FSgaaDWAdJOuTvLytI8S2VAyL0J043DFG4bxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcc5deaca3.mp4?token=LV-MNBQ_pveE_HBR6FjOE0mXX3sp8I4y7n1Z_Vk0MV78ReC6wbNOtZnEKVx5EeiNInbfdJd1AdryKX_FJlZxIiUPOFAxM0HwglFqZM3i9kMNa7JaBZMuRMi-sepk09Rvl3l3NRg64SUdhL0TDv8YTVmGgDb7XA93oBjOrRtgHIraW0eNTOHMaI-7sD8yJcys7IBaT8R8SK3esVbiuNKsK3y1H_vQ-rTcHVXoCAVJdPOsNZI1MZDKjd6j4HDY5zmD8NOyXrbN_6jcEqDIy9vyqzu68HPxCSf_NkAuWRYrKI5fM2e78FSgaaDWAdJOuTvLytI8S2VAyL0J043DFG4bxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرمربی مصر از لحظه گل شجاع خلیل زاده تا آفساید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/96390" target="_blank">📅 19:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96389">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/96389" target="_blank">📅 19:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96388">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IYEUolvJdejmDUIMpx3FK0vt13rTAFdz2qElY3LtPVtfDpTfAyi7W7vzcZA55rYHlShGUOJXvhpHADI2r2OcH2Gmqt4QuKynooSNV_JHBwdMHarqz7AF5gzN9Z6hz5uHLwuBryN9NCSq1grKDSvlr8IKfW0mGQNVPsWguZNa3LTBuvd_oZnPMDXVok1DcqWsnip2lpVT6kURBAU7msc82XApnBzt-PtXR4Dhf9Kv-1aPVMcpPZNLFDucMBy1mRkCjUrcKZkW3eXQ-U7Jg4DpBJaaHJLxdgWxA5k8RlKPSSBfPaFaSL1FFOEg05K1qEYv4auLgjkZK5kG9G7iUGYCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/96388" target="_blank">📅 19:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96387">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0acf3e8fc9.mp4?token=Vi_iD45RtxMR_Qv6BrO3UuuvfWgCiRZJo3HpqT4kZdBOkVd9Yxym1IhSb_rUskgrdSecn3E2rJk_w54rCDV1r2iJlRildQYjS0JwcRqyiAPey1029tegdvwmy4XjscFtiCZ4qdinZjR-w1vH8hyjI7dOixpsv_Jx_wlovoJtmP7gIt6o2ej4c9-yE0C5-TKamxTQh_wVgkdCn8k5Ssx7REHOGv79QN3lQTqNne36lDyHXqGa6wGpW-s7GCI-HDl1h63Lojrye8DnfGzl4lKNZy7dCh4qPZA6akT1YrWI-NHArOQo0iERpLLSq5mAg5pOYYBXM9GD8zm_jkDLfgnl8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0acf3e8fc9.mp4?token=Vi_iD45RtxMR_Qv6BrO3UuuvfWgCiRZJo3HpqT4kZdBOkVd9Yxym1IhSb_rUskgrdSecn3E2rJk_w54rCDV1r2iJlRildQYjS0JwcRqyiAPey1029tegdvwmy4XjscFtiCZ4qdinZjR-w1vH8hyjI7dOixpsv_Jx_wlovoJtmP7gIt6o2ej4c9-yE0C5-TKamxTQh_wVgkdCn8k5Ssx7REHOGv79QN3lQTqNne36lDyHXqGa6wGpW-s7GCI-HDl1h63Lojrye8DnfGzl4lKNZy7dCh4qPZA6akT1YrWI-NHArOQo0iERpLLSq5mAg5pOYYBXM9GD8zm_jkDLfgnl8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چی میگذره کلیپای بیشتری رو میشه؛ وسط خوشحالی بعد گل شجاع خلیل‌زاده اون وسط یه دماغم باخت دادن
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/96387" target="_blank">📅 19:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96386">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53c9100fbd.mp4?token=e4WuhNiq1xCFe-0QHR7mC9gJwfRwVZiD3aChd1jigC0gnC8U2K1M99fVudMY3tkzEUyTUEAWV8OJx3j6Gq5nA3R_Ih49E1K2ei40GVRlOW7XhCobXcPdZhUgxyKcYGeSOQpstGVqi0FyieJblvATVSg0HEHzlIk8WeunxF2K3NBiU9yTwSGqUd7ipjIU6qkscMd-CluMT_IAYFZNMt2-v6Us_mmS9PA2p9-8SPE2VN-HlOtGL-hyN107spH7DS8ayFU0wi6FE4ihRc704x4eMoqrUgllBgGjET-WfeMgROlNSX3JtGiHsnjDNUnNwVYIcesZATwk98RF5NMyCEvIww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53c9100fbd.mp4?token=e4WuhNiq1xCFe-0QHR7mC9gJwfRwVZiD3aChd1jigC0gnC8U2K1M99fVudMY3tkzEUyTUEAWV8OJx3j6Gq5nA3R_Ih49E1K2ei40GVRlOW7XhCobXcPdZhUgxyKcYGeSOQpstGVqi0FyieJblvATVSg0HEHzlIk8WeunxF2K3NBiU9yTwSGqUd7ipjIU6qkscMd-CluMT_IAYFZNMt2-v6Us_mmS9PA2p9-8SPE2VN-HlOtGL-hyN107spH7DS8ayFU0wi6FE4ihRc704x4eMoqrUgllBgGjET-WfeMgROlNSX3JtGiHsnjDNUnNwVYIcesZATwk98RF5NMyCEvIww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
جلالی: سر حرفم هستم و قلعه‌نویی از مورینیو بهتره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/96386" target="_blank">📅 19:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96385">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCuN_eil9WDgGbUqprblUqxDWVINIvYdu3SX0bbSojNztecAjtd7fRanzuatD89h0Aj55qo9JvMLPycOJ30442W_p8dgJaPVm70CtLBn4d2sFV520NbCMUrc8KxDxCNqjr9tT1gr7J6pYSXn9LD8ylWNp1DE3ofh5Pd1uSDrBfDwwSsev_sVnpodqiwzlRZUKcA9li-Wyu0rmIVSaBlDU5gCrfLgeaw1_uR3mS0BMQEyo8ska4osCuql8Dax-05X5KX4QbWNaQ9qEl6ADQzLBY5uSl6IuGamzKSyrWIkN3dQy-qe4HMwAEfsrhPLoVI81Gek4haTCLBVAk64u5KGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مربی های با بیشترین برد در تاریخ جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/96385" target="_blank">📅 18:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96384">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quXhV6E4CzkH_rBUDTUmMK5NKv6xtoL8UyJRC07ysr2V0QCziVjpPx79TQAc9_XdKXdSBR0WyYFA3XkKGafLnLDjjMmP-gL6SD2tFdA2jLHOcJS2OtV1u0bKT-jCDGxhH_zuB69TrswN7VVC3GmgKSQR56G3_TMuHMy0-Eo42PDm7c6QRNxEOGCseou2QCIJLNngEKlLB95ZgAUTbvAtOpSAmQWVj8recses5OS7_bMDYzB9HlMOAfxreE4izkh0U7XTjf3umjK_dVjxasdi-meIulCZY99B_FmfvavgImxGHa5mJdPTPBYgz8GlBK8fG81geu_AhTsHqYO7HJnrWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کفش‌طلایی کریس‌رونالدو در تمرینات پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96384" target="_blank">📅 18:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96383">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IymxLAZjEPh5_UnSdV_DEK57mxgJiYfX_0xJL1f5I1_uT2Fz5dwWtVscSe3M89rK6VKnY5zTf6gkqUx3eKw00mmV5nzzFBvUHjvvYi99h2ZmDIJnaql3GTTqf5W4gnbVyegaGefBoQ7f6axBBmKaiPckenr__OhRzXJVCKrbxeNSM-1cXMDqUHzZf_dqWtJKUppSwNzWy-wofjvJwm7dr7R_d6rRSphCMPDPKSEVh3wcEdEv1yhqILsdrSIGfK5QwJSx_fshKWQrH4W45xv9vaUlFj2aAW7quSN_VXlAsyidvVzPem7hX0q4D74PKtewojK36UT-Y-xQgXgJeFVjVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده مسی از سال 2022 تا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/96383" target="_blank">📅 17:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96382">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9jsd_zLWi9RSIV1aV7brXucob8g5lfh2XeXQaehkLZnhp21wuDpHcEKStgMPbBUhmzt1lvoLHa9uwnBtJkd_LttQfZCwfwTR833UGgyU7qvvSpb6Nuf0aKUXD53bHLJKvLD3CMY7-Gw9794gwOATzfuVDTBrTBkVdm4aVc95VGHEQdqjLN3V5_5Sm6TaNoeK8fuMhT2JvYCZzR_ML4wMPD6L9-y2bgvkLa7lnvaSBP1rw27sFwCRyYMIKkUyM1d0T8T1p6UVRFFcfhu4VSi2Enbsgk1YWR1UjIu5MHZmiPBHzDBTTSvQmZnaG_ZLBW2C8Yke4B7ABacAvDkmQGgHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رودری تاکنون 328 پاس دقیق در جام جهانی ثبت کرده است که 109 پاس بیشتر از هر هافبک دیگر در مسابقات است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/96382" target="_blank">📅 17:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96381">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzAm3I_WlnY0KqVIrKqI7zDMz6HmfOu1QzkPMqMgb4GaWFTgQOmAA4Nn9X-NCQXXFGkvKXrml1-g2u1h8gYx2LgYMTgCXA-inC109uJybQQYBKclLGOVbcyy-Vr6H2f_SFBxXAylX8rHplKiYOFaHdxAWJm73QAOVs5gIhfUBgaOFyJ9wbgwaWceLPJwh5dqE-h4cDL38Ga_yFsW1CCKowuTD2fEcTGI9hPfq7x7sRMV21G6t64-GVul62TKKC7Nvo1THqs6NG_ZckUM0vfJsDlPTPVEbQaQbPrUGIAWwomFON3Tz38vcjfxojgZt349Us0k5egQe4aaR3xlPnOBTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسامی برندگان جشنواره ۹۳×۹۳ بانک کشاورزی تا این لحظه
⬇️
⬇️
⬇️
https://www.bki.ir/fifa2026lottery
‌
🔹
برای شرکت در ‌قرعه‌کشی
اینجا
رو کلیک کن.
⚽️
فقط تا پایان بازی‌های جام جهانی فرصت دارید
‌
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/96381" target="_blank">📅 17:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96380">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cke6ZmcYnr6GQVf8fULcro-ZxM4OVJTzWtYnZTi3Z6GrGIv__RpgDId4UquK9WL5PmnvLmSUSXbEkbBR31US5xEfo5FF2dX2HPuSbwdHADcXSFjNT2h0F2U9QZNXXV_NqzgYXsU7n7OA_w5iZy5cVXzslRA08J0j_tx-qox-OlJFFwbJSYTYPvqjON8zhlT2A_rh5deTQuiXc9dIaonJNRydBx9RwpjuiPw4RLVrKiUIGHiad5yuI4VGIfHYXo2LOL5RLKIPNMQRcjhyunha_kywWrncy7yia4bes89cPyPgj7Cjd8Fz-pssbWGWFb5yWfMkBXXmejBUv1lrZ4PqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به پرز بگید حرکت نکنه که اوضاع خیطه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/96380" target="_blank">📅 17:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96379">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgwQNZNN_SwC4pu7Zq3jx5hO5xnIZwLuFoACFBSOwH6ACVR_qaGZ_eyAdR9P2SpZDjn3eYJGfYmf7l05QpAgCz-6NXVLtwOEaru_pXvXJ_SLro5RA0ppMTmQ0fnpyZwRLkhV8bibGOvzGacHOYAP1pwdbj32KW_UAKSX6Zx3KAhZ1wDMdVOErThyo14-ctuyT8dl8bBkytCDx7F5syfxjJ6yXl_Iyi6o2Rx_9hsuasEDr1FZkpsKei3wV8vfLNuyqohz-KSZBa9iVv6qrth4dzVd6_gWuddXcSnQE2CTLBo82wyQ09IadoF2F3Qa63DdE7IwRWhDNm17i_v6fkWnHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آبرومون رفت و شجاع خلیل‌زاده تبدیل به ترندترین میم حال حاضر جام جهانی شد.🫪
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/96379" target="_blank">📅 16:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96375">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tINOzXAoAZV_IsI9qQoemWvl2ltwUsLg9W8SAZYbP1xA1wvWEC9lL0WE-H20zOoGqZ8VVzqm1pt90uw_Yf-5sAqHGeVoJ7qawYvQoyTLjJsMeiadAoHdpigM4gOC-J6miUoiZA1q29VNEMNXfqkZfB00Aw9QoX3Qn8BKcsBh7hiJYWBcGvNAD41i26dUi9dhHNuZR4Ex4m-lt-Jn6xA4ru5ZKOv0FBEiKW0pG0OV-K-3DVZrBNQ0WvO_01c4PGKdWFZaiBDJnm2IovbUBwycN99KfDVNVIXT00Wf8SWc6mZMhl8uV6R-1gIbPGEOQQfsO35MFpNmVQyPkKgLAycM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bd5QsJImBjdOrixrtgJbr3mwbxpd2HsyiE0mWAL5ozJYM3c7Kv2g2-enA8PAfAJRZFM3beIifl28gXvPKjIQKKdnL48P6UCC_uZfe6Mtx5utqvdom2i8hl44InvfxrEeuwYvipwPhf6lyM8U4B9JthRh98ennXdhGvPEnGu_oDetASo_8FxD-_BD7tcpLrjADCtnrS5q4l48Mlcqif4nulTyYlPorE_ddf0rtWzTH_DBaJ6048ehe-zoSbQ1AU2UgA_gWV6aQcftY9DOfSbqkhBxn6UVepkTQSKZA5_ArvEqwHQrWOL4tYseY1tvPRH4qRdxjxYwEj05GvvrvQak-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vPrTeVnEfytaFchEBcbPLTdvBSh6pzUs-l4ohZ7jM6QP5lIEk9adLsrgbuSEUYrPKTR9RKlyUTHDRmvq2OhLjwf76zBdAmdoBOd5vWY2riIRvaYy8UiSgq1K9EUUbCIEInT1udJGQYH_28adjy_iTkdeROQ9YYcGdPKwuiy-Xeqdo-P8ZfUH2_R7eHkfQU41OzwRCXYP-Htk4QGefl26-a98HcMFKrYkvAERjRCe2FwvHgl9i7puPOHXxe-CkBXu5V-MlFzuVEGuuWZVWjvq4wAGRE0enz1lk9YhNRVok1ZdjekOZEF3PVEde6p3fkGRxCkyjH3fM_Jw0rDkETZxfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FG_H9vInuFVxx9dFs1N89Ej9IXLeJ_fatPsEAEOAD3WpoU8W1TFz808D1UDAgu8qfxfVAsfPsB12f5VwV0YBSk0VYigHRJ_7eKObTKHeM-UIQtHzskqxOBexCj6OgfOjXQXDB4cyZst_DGqOC3rP5JFNqOX1xc7iH-UP8JL8LnS--WKgOQThUAuWvVlYmxnsybyMB9DozwRGgOQL7RLoYgNIGHsBQBl8HPlWVjhphsD3XMqMfTOqO4iRgYvOOTPbpE1iR1OfqDDu0vJ42rsIKZNuU_ASyprT-3RSqx9FXYfSDZd4ewcKOgj79gvR1X15YHQHSHtl9aeNIKEGQZEpPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حیف شد عربستان دیشب حذف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/96375" target="_blank">📅 16:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96374">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/96374" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/96374" target="_blank">📅 16:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96373">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=Dl3MX69AgDV1FQoOkxFrv4ElnTdHkpjxMij_knJYKbIv_1jKNDzJmrbaetKN9-RlSdjt7DvWLwbbTVluKW0HRgtQ4fuIu-Z40MzsD4WFaUGynfBA2fXtTaksF3EHDnqV7uy1ZMH3csiqaZqGGsvW9asHZiTFQE6UlYcEnkAerosZDSmCbcWZ35EjQ83IJHE543n9Rzpnox_5v5TtNUyX_z9O6t6oFHJK63ZLQvR0Jqu-PRhgojGCX8uOZ1kjOUXMNiQMIENwbwK4HyXuSw7Xj6G5kYFRJSjIE-3Bjm3iuB-Xh5v3xvAe61q0sOYUG9fdF7LVySSoyPj7NVAiuClqADNo_Moav7wMAzWUX9K8oV2C9hBjwwCEJwIrWiIp5RpO_422yBquOMbNoErQsZrYEh2qG91tskjBGb-UpzMmsm9f7mIYNLNcZ1-dbD-hbFn7JmVRw0RAi5YqMUbL99OJsvHS2POJpJyg47cMMqeink9ZlPHCvY03dF53vYxbG4gwme2cox0qdFrH7fown6Fq73uS1lC96ngZdI2zaP1zsG0rCexh61lOr02iGlrYE-B6L6vZHP9hsV7nL7J2ghOkWSxsfnTqGdpgmRtbOrl67peWHb4OIBCdUdJ8X5rZlubDzoQXv4l8DMayCfySqLacNWsbmDPQ66Yhc6af9IHrJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=Dl3MX69AgDV1FQoOkxFrv4ElnTdHkpjxMij_knJYKbIv_1jKNDzJmrbaetKN9-RlSdjt7DvWLwbbTVluKW0HRgtQ4fuIu-Z40MzsD4WFaUGynfBA2fXtTaksF3EHDnqV7uy1ZMH3csiqaZqGGsvW9asHZiTFQE6UlYcEnkAerosZDSmCbcWZ35EjQ83IJHE543n9Rzpnox_5v5TtNUyX_z9O6t6oFHJK63ZLQvR0Jqu-PRhgojGCX8uOZ1kjOUXMNiQMIENwbwK4HyXuSw7Xj6G5kYFRJSjIE-3Bjm3iuB-Xh5v3xvAe61q0sOYUG9fdF7LVySSoyPj7NVAiuClqADNo_Moav7wMAzWUX9K8oV2C9hBjwwCEJwIrWiIp5RpO_422yBquOMbNoErQsZrYEh2qG91tskjBGb-UpzMmsm9f7mIYNLNcZ1-dbD-hbFn7JmVRw0RAi5YqMUbL99OJsvHS2POJpJyg47cMMqeink9ZlPHCvY03dF53vYxbG4gwme2cox0qdFrH7fown6Fq73uS1lC96ngZdI2zaP1zsG0rCexh61lOr02iGlrYE-B6L6vZHP9hsV7nL7J2ghOkWSxsfnTqGdpgmRtbOrl67peWHb4OIBCdUdJ8X5rZlubDzoQXv4l8DMayCfySqLacNWsbmDPQ66Yhc6af9IHrJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/96373" target="_blank">📅 16:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96372">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6f86a272c.mp4?token=YNPev_NsGFFo3jmUF1K_FAco2iqQsMT2bEroe6qoTvqmvB28UMdv2-bfNeOl5Aueb18_LMi6orpt5eGj2PgDlqamaCNFy9qnE7sErRfT6M7t6dz_PBojOfUxbP5XxVK1S1wuNrEWPRpiIJna-O3Wac9MdrJcYkwufx2HuTrzdo9HV9rfS_iUg7m33tKrjatLJGm20jynvvzY3szRhjlck1iyL3ClUtl4GjVHKCS3NrQ1gci10ekM62Ugo7HqnbEUvQf2SHpTtzCczZYHFPk4wwnjXkxRAqAOSL2pTM_RB1w6M1M4hMpBfKOAA1YuoYrBJwBjg-VCXIaCiKaKaKgkkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6f86a272c.mp4?token=YNPev_NsGFFo3jmUF1K_FAco2iqQsMT2bEroe6qoTvqmvB28UMdv2-bfNeOl5Aueb18_LMi6orpt5eGj2PgDlqamaCNFy9qnE7sErRfT6M7t6dz_PBojOfUxbP5XxVK1S1wuNrEWPRpiIJna-O3Wac9MdrJcYkwufx2HuTrzdo9HV9rfS_iUg7m33tKrjatLJGm20jynvvzY3szRhjlck1iyL3ClUtl4GjVHKCS3NrQ1gci10ekM62Ugo7HqnbEUvQf2SHpTtzCczZYHFPk4wwnjXkxRAqAOSL2pTM_RB1w6M1M4hMpBfKOAA1YuoYrBJwBjg-VCXIaCiKaKaKgkkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
دستم را بگیر و مرا دوباره به آن روزهای خوب ببر سپس رهایم کن و برگرد؛ من نمی‌آیم...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/96372" target="_blank">📅 16:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96371">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTW6_PtOCXCM6hiQeEe7dbsKb2gf7_p0IEGRZdoe7-8oqONC9OVXBc-LaQEwRmyOIb9U0EfH1VRDQV_NyEUKrHzDBaXN-JJbXJrMA4XK6wChaB1D4a_grx1gy_mz9PeuWojaBIFho_lXNiWzYnUy1huWrQ7ioxTmcaKOixQrbcSiS_R1qoIP9Kz_CCDwUv05QXx4UUIiNjtMMFl_IY7TnVICFmhpwH5REXWQCAFIWBWpKPF116klkxdUcSugD8CazA1zmNuOFmggRAZkwvCCQBZf15tdG7H5sN1k2F-th836MwG1XFNZn8qEQMUC-QvEe6d82z2SCSNSPq1lAFP0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هکتور بیو ، بازیکن تیم ملی ونزوئلا اعلام کرد که همسرش در زلزله 7.3 ریشتری این کشور هنگام مراقبت از دخترشان کشته شده است
همسر بیو زمانی که ساختمان در حال فرو ریختن بود با در آغوش گرفتن دخترش از ریخته شدن آوار روی او جلوگیری کرد اما خودش کشته شد، ساعتی بعد ماموران آتش‌نشانی فرزند یکساله این بازیکن را در آغوش جسد مادرش زنده پیدا کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/96371" target="_blank">📅 16:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96370">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuVIFtQmwZ4NsTp2mdAv7OG5uX1hY9MSIZipQzYTRoMvF429da54d2ihO26iD9XIf3L3YAeTYCP54IS2eDYZVt8pgqcLJwgBZasg2ZNdRRvDYVfm7g3Kv76eO13ZwNYOgHGUxBKrprKKBLdjWYx0vk5dEnA7YGx-FWai0qBrHizrdXKAH_ILQUodV1xKd6wIcgKzSL0whU2qsVHcKu5EWGzJXnnLXPH_wPtylXqb-lLur7gpcWPlY49J9uOIJBsWkELmli87vTNE50hz4APsEkPd3fueJdEok71cc89eJaOeNYxhd7amJkJvB_o8zRVUrkVDa5uasMkrJPl8LuA9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
رکورد تاریخی به نام لوکاکو!
🇧🇪
روملو لوکاکو در سن ۳۳ سالگی جوان‌ترین بازیکن در تاریخ فوتبال است که ۹۱ گل برای تیم‌های ملی به ثمر رسانده است
🇧🇪
:
‏
✅
جوان‌تر از علی‌دایی
‏
✅
جوان‌تر از کریستیانو رونالدو
‏
✅
جوان‌تر از لیونل مسی
‏
✅
جوان‌تر از سونیل چتری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/96370" target="_blank">📅 16:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96369">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b68a2145c.mp4?token=Yf6wxom624GJVMIwqepOTdB66f4q9glWZ0wuzjaKCxwID75F2EHtRbE1761x0FQxv6bP8cCNpTYP-rl4L2Zw2yhEcZenNGOEzlK0BBKYEtBUvpgJPjZ7WUiWQXG28JOcWi8GKBO8LWwzc97Fc20fm7TUu0eEZJCo9TSvdtml8A3EZYe1gOsZvqBa61NbWchJdY_Hwobl4N04OaUSXw3VXlTUoCULPa7NJvpamGZ-SqtAWAR-DqmfpinXgnbN-Jg4FPMGE3tjJV12EYm3ftzH-SDgjajLznNEwRWJbZSlHmql1ZpFYW2mUqXExXLA83YKXfWOuYNFac80hmnZVOlFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b68a2145c.mp4?token=Yf6wxom624GJVMIwqepOTdB66f4q9glWZ0wuzjaKCxwID75F2EHtRbE1761x0FQxv6bP8cCNpTYP-rl4L2Zw2yhEcZenNGOEzlK0BBKYEtBUvpgJPjZ7WUiWQXG28JOcWi8GKBO8LWwzc97Fc20fm7TUu0eEZJCo9TSvdtml8A3EZYe1gOsZvqBa61NbWchJdY_Hwobl4N04OaUSXw3VXlTUoCULPa7NJvpamGZ-SqtAWAR-DqmfpinXgnbN-Jg4FPMGE3tjJV12EYm3ftzH-SDgjajLznNEwRWJbZSlHmql1ZpFYW2mUqXExXLA83YKXfWOuYNFac80hmnZVOlFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میثاقی: اوسمار بعد از بازی دیشب اخراج شد و پرسپولیس با اسکوچیچ بسته است
مدیرعامل پرسپولیس وعده داده بود که اگر پرسپولیس قهرمان نشود کل حقوق و مزایای ۳ سال گذشته‌اش را پس بدهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/96369" target="_blank">📅 16:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96368">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ffa49c692.mp4?token=qG7HPAdja19adN5UiGMGxGGRnmobmKFjFAMJ2vhidSJvLLFu3Ske3FjqezjpTqF-lIxf6xqvv_b350AJP3UjX8uS-8uO2ZRw2zzO-IJlYrbXQIo147Rp7o_NCj3DXKi1Bdh1TffI8GVdeWlSNse2_DC1iJ_wk1VCb6BrzYAkflESex6JKreEVJhS4Bk2DJyaYoAsNAxMcyWRwMP49-yzSwNH9KWZJscLxDFS1f52rPKGiTGSSCb_Rrt986bVVFxU3xXTBwYuD-kX2yycy1nICYSjATTam1ZFX-zueZ4tw0DDTv1fhU8QYoNnX8LTOYiqxK2LFEIepQTwsxZgsqu20w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ffa49c692.mp4?token=qG7HPAdja19adN5UiGMGxGGRnmobmKFjFAMJ2vhidSJvLLFu3Ske3FjqezjpTqF-lIxf6xqvv_b350AJP3UjX8uS-8uO2ZRw2zzO-IJlYrbXQIo147Rp7o_NCj3DXKi1Bdh1TffI8GVdeWlSNse2_DC1iJ_wk1VCb6BrzYAkflESex6JKreEVJhS4Bk2DJyaYoAsNAxMcyWRwMP49-yzSwNH9KWZJscLxDFS1f52rPKGiTGSSCb_Rrt986bVVFxU3xXTBwYuD-kX2yycy1nICYSjATTam1ZFX-zueZ4tw0DDTv1fhU8QYoNnX8LTOYiqxK2LFEIepQTwsxZgsqu20w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مارچلو بیلسا بعد از حذف اروگوئه از جام جهانی: «خود موسلرا این تصمیم رو گرفت که تعویض بشه. درباره‌ی تعویض والورده هم، راستش دنبال این بودم که با دو تا مهاجم نوک بازی کنیم تا بتونیم موقعیت‌های هجومی بیشتری روی دروازه خلق کنیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/96368" target="_blank">📅 16:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96367">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b871ffb756.mp4?token=JJHloOba9ixYFHPEFD2z5mnJOsAIA8a_57MuS3x7njJZJUh4nOEIHENHWDTGFme6Sbe0hPJFjgBeJOedsTQBZHiR5S7cXHA3XTinbrO-nlahkkNb_7_PKz7mQGkZpoDtLlMhWnPreVVHxBcfy6gf4YrPk1EcvoT8oF-KWR4hUsrD6iLxXRSgzemQq7o2fw0lqAmqDFqQ3f7UPznm37RzaaI6Iwfa9qjIUsEjff0hzLtkiwxw8ko2uLkjMyrRFGnlczpp4lcCUjSpadmnfAYIwOKdw0BNZ7UOyl2coVU2M9YJ9eWcTj5RDESoVwfNJNlq-6f6lNezR-a6sXZ7uSlAZ6shPPtXBZ_kVBQBNSmuJp1GQjrhzepoNXJHUcJGirdT9VFfdkeFw4p9VOZ_KKVSoKtAUP0eGrRW72W-QPTfsuxiw-2k3TxTYF7f7sMsZ6In8Cza6V4WoqQfobB8q6N0BKFMuZfOrviwf-4grshyp-Q4MX7--K4KWjWvUbyC2UvjC0pv9Sa5K989tYpNRWhh576ehAKDOyL1u9tkG5kOhvLM2Iv-fO1G86_wjnaRk4ArV2MkUIN_Lq7uPwL_0dgbFbCAhrtiIqNb58MbcxwyTb7GJDRK4Ugvh_fkIrsr8cNIM7lF-NGmZEOtz6V4n787vxPerIOoONpOo18d1GIf66c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b871ffb756.mp4?token=JJHloOba9ixYFHPEFD2z5mnJOsAIA8a_57MuS3x7njJZJUh4nOEIHENHWDTGFme6Sbe0hPJFjgBeJOedsTQBZHiR5S7cXHA3XTinbrO-nlahkkNb_7_PKz7mQGkZpoDtLlMhWnPreVVHxBcfy6gf4YrPk1EcvoT8oF-KWR4hUsrD6iLxXRSgzemQq7o2fw0lqAmqDFqQ3f7UPznm37RzaaI6Iwfa9qjIUsEjff0hzLtkiwxw8ko2uLkjMyrRFGnlczpp4lcCUjSpadmnfAYIwOKdw0BNZ7UOyl2coVU2M9YJ9eWcTj5RDESoVwfNJNlq-6f6lNezR-a6sXZ7uSlAZ6shPPtXBZ_kVBQBNSmuJp1GQjrhzepoNXJHUcJGirdT9VFfdkeFw4p9VOZ_KKVSoKtAUP0eGrRW72W-QPTfsuxiw-2k3TxTYF7f7sMsZ6In8Cza6V4WoqQfobB8q6N0BKFMuZfOrviwf-4grshyp-Q4MX7--K4KWjWvUbyC2UvjC0pv9Sa5K989tYpNRWhh576ehAKDOyL1u9tkG5kOhvLM2Iv-fO1G86_wjnaRk4ArV2MkUIN_Lq7uPwL_0dgbFbCAhrtiIqNb58MbcxwyTb7GJDRK4Ugvh_fkIrsr8cNIM7lF-NGmZEOtz6V4n787vxPerIOoONpOo18d1GIf66c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
عشق و عشق‌بازی کف آمریکای شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/96367" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96366">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f23a0551.mp4?token=a-qEhzjNu8BPVubC9mQ4B7rHL8s6DeeQwVp29wuFeCjvNr1TBycTzDhs_YzyLsw-EmFXMO4FXzkIBAZ0CIqlz2ZZySwS879k1mECmmvhRlgBoIT3FiEjBsWRS68kG_-6IDSuu-_HJ6_6JKEAzX-SK2XVJq_DNFheXlMKvzzUc0PVr9LejrfKm2fFMQt26wI4yasLbyRmmQjkees83sLmWTpNNK5xMwuGug-3hVTG-GhzCNiqw9VfLfVYIOwoaDmD5Xwml5QjZdEpbck_S3gvLciSRXBLq5K_hJ8CC7TkdjLO0K7gVvTPPet0WUToLJVJGBV_G15uvHHWYhw5PGl4xoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f23a0551.mp4?token=a-qEhzjNu8BPVubC9mQ4B7rHL8s6DeeQwVp29wuFeCjvNr1TBycTzDhs_YzyLsw-EmFXMO4FXzkIBAZ0CIqlz2ZZySwS879k1mECmmvhRlgBoIT3FiEjBsWRS68kG_-6IDSuu-_HJ6_6JKEAzX-SK2XVJq_DNFheXlMKvzzUc0PVr9LejrfKm2fFMQt26wI4yasLbyRmmQjkees83sLmWTpNNK5xMwuGug-3hVTG-GhzCNiqw9VfLfVYIOwoaDmD5Xwml5QjZdEpbck_S3gvLciSRXBLq5K_hJ8CC7TkdjLO0K7gVvTPPet0WUToLJVJGBV_G15uvHHWYhw5PGl4xoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
🇫🇷
شادی دیشب فرانسوی‌ها به سبک وایکینگ‌ها بعد برد پرگل مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96366" target="_blank">📅 15:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96365">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f46f8116.mp4?token=BNDLDErOp4hUhLk17Ky5fnrp5wAsgeFkt2fkGkEOkPbABr6qk1jZLyPy4CwflgV0B6e_yzqIt8v84pczwwxFHbjgqosdvnWpbvAusVYmHq5Nh321h5ia-LodoPTBx0CezygVrhGIUJnam7oPDOw248j62WYFcP4Xo0ZUDFI1OU5M5d7KMktMPvc6rxV79tj7HgfLwYXH7DbvLotgFQL70OSIer4kRLK_TkDjpWyjHigrbZI5VUQrACjBam7aec0EJ332gmjYJjHexnkcxsUPtV6jbIejZjAg_PiZP4BNkzgVKS_quVJjlxpL9G7GqTtk-T-8NnIfFluDpfTPpzyCOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f46f8116.mp4?token=BNDLDErOp4hUhLk17Ky5fnrp5wAsgeFkt2fkGkEOkPbABr6qk1jZLyPy4CwflgV0B6e_yzqIt8v84pczwwxFHbjgqosdvnWpbvAusVYmHq5Nh321h5ia-LodoPTBx0CezygVrhGIUJnam7oPDOw248j62WYFcP4Xo0ZUDFI1OU5M5d7KMktMPvc6rxV79tj7HgfLwYXH7DbvLotgFQL70OSIer4kRLK_TkDjpWyjHigrbZI5VUQrACjBam7aec0EJ332gmjYJjHexnkcxsUPtV6jbIejZjAg_PiZP4BNkzgVKS_quVJjlxpL9G7GqTtk-T-8NnIfFluDpfTPpzyCOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇳🇴
شادی نروژی‌ها در میان سربازان ارتش‌کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/96365" target="_blank">📅 15:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96364">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b317fa40.mp4?token=hPRMHAtPZVH7qpTGXrRORFTjKiUNGiD-iQZ6Vc-T1yzPIvzFHVE-xDQzlYQoqVRDTjPXZLrcRs11wAqR35iutaHpcecO7LEYWVUbzBKRYr4k1dfxiSQcmKQyodVC8LP2qVGOWvVkUt_KPBp_9m6pDMDCXey_lUOrg28nvff8F2R1oRYp53XxaQGoCJIrypKT7s1cbRxRhYpZMwuOap5JhlHa_AHR-bXrVap-wDJx_V-oXLpw1H4xDVVBA-DBbwJCJrVNLN6arUn0vXvZpRbFjEke2YNx7ee4otq6HmXqa1E5JdJMoZYSZ4hV51U6Bgp28a9hvKz-dI9xSAUA1WbHBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b317fa40.mp4?token=hPRMHAtPZVH7qpTGXrRORFTjKiUNGiD-iQZ6Vc-T1yzPIvzFHVE-xDQzlYQoqVRDTjPXZLrcRs11wAqR35iutaHpcecO7LEYWVUbzBKRYr4k1dfxiSQcmKQyodVC8LP2qVGOWvVkUt_KPBp_9m6pDMDCXey_lUOrg28nvff8F2R1oRYp53XxaQGoCJIrypKT7s1cbRxRhYpZMwuOap5JhlHa_AHR-bXrVap-wDJx_V-oXLpw1H4xDVVBA-DBbwJCJrVNLN6arUn0vXvZpRbFjEke2YNx7ee4otq6HmXqa1E5JdJMoZYSZ4hV51U6Bgp28a9hvKz-dI9xSAUA1WbHBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
مارچلو بیلسا سرمربی اروگوئه دیشب بعد بازی با اسپانیا کلش کیری بود سر خبرنگار خالی کرد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/96364" target="_blank">📅 14:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96363">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025a2a9a9e.mp4?token=Vw7G5pwIhg59-9XKPxy_L9yJ3bIXsRvht0h8dfks5wD25MySZ-v8p3l6R5kZsQMPoFir9TevYEjYalzk_xWrQQ0Ckgcr1b7OUrWonk6mXekKLgDwfZXIvklfWmIviSHzJJ8xlyyPg9aPzcRipVnfvBl8KFqOrDiASo5t-X6J5cV6ZMJtB6UAnNhkdsbW0MSj74ohDJ3L08SmN5s4Co-7KmBG-EJs3g4b7tTrfhhF6tJtcwH13QCdv4XxsfsOWkOgMnXRyu1ZrWZoPBRcXelKWxgzq1j9n3gJb-X3KuHG7rlNI9dvngmikcYLxL0NJ8xHjxsZpWrecnDMHIwwMrQ-3Q9rWhlvBkkL4zfFr_nFJisrNmtydRzUMC-Sm9muvBdIHuRzIGgllIShiGdZaxf5Kk-G4IPxECdEVivbnFcNNZb_bgMPQkAeuEk6mQ0g2emr6a-T0kd40q5Jk2_f0Ax6bX8owAeCxP4De4_nZpP82tJ87pnIMvMY9bwAN9qJN4ofk9fBUO9ToPt7T5ijBqwVvfHKzzvNqz8oOV298a0tK9ei6mv4R1MnpGuuEcdN-IN5gMQvF0hC0IglRmzTT3Wyul8muoUhE9MfD3hKM3py_JSy4e0ZtpjirKmfYhUGITTThzPNDuTRBrLWMjDqP3BtCMYw0q_iQyFHScajIco59mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025a2a9a9e.mp4?token=Vw7G5pwIhg59-9XKPxy_L9yJ3bIXsRvht0h8dfks5wD25MySZ-v8p3l6R5kZsQMPoFir9TevYEjYalzk_xWrQQ0Ckgcr1b7OUrWonk6mXekKLgDwfZXIvklfWmIviSHzJJ8xlyyPg9aPzcRipVnfvBl8KFqOrDiASo5t-X6J5cV6ZMJtB6UAnNhkdsbW0MSj74ohDJ3L08SmN5s4Co-7KmBG-EJs3g4b7tTrfhhF6tJtcwH13QCdv4XxsfsOWkOgMnXRyu1ZrWZoPBRcXelKWxgzq1j9n3gJb-X3KuHG7rlNI9dvngmikcYLxL0NJ8xHjxsZpWrecnDMHIwwMrQ-3Q9rWhlvBkkL4zfFr_nFJisrNmtydRzUMC-Sm9muvBdIHuRzIGgllIShiGdZaxf5Kk-G4IPxECdEVivbnFcNNZb_bgMPQkAeuEk6mQ0g2emr6a-T0kd40q5Jk2_f0Ax6bX8owAeCxP4De4_nZpP82tJ87pnIMvMY9bwAN9qJN4ofk9fBUO9ToPt7T5ijBqwVvfHKzzvNqz8oOV298a0tK9ei6mv4R1MnpGuuEcdN-IN5gMQvF0hC0IglRmzTT3Wyul8muoUhE9MfD3hKM3py_JSy4e0ZtpjirKmfYhUGITTThzPNDuTRBrLWMjDqP3BtCMYw0q_iQyFHScajIco59mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو رسانه مطرح مارکا اسپانیا از درگیری میان طرفداران و مخالفان حکومت در سیاتل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/96363" target="_blank">📅 14:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96362">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=fz9aQSp-Z-JuKvPv4SUZQZVZQhtAqLHFrG98oihjkPbbxDjmjqeTeVDaMqqm9yvlSxO4TqOvdwPY7Q6dLEyK40MkXqv2xoWmayDBiqYHb-l3zLlP-hMYKuEhS6HBz5mfE9aS_jooMZdjh3vGQWpZRlWhmTcMUDRKijSO6J_V7_fFjx_zTbCQ_KgOB3GvYC2WUT7yBziqGT1F0GDi_nvcSEyesCPy0GjY6_k9xiVzu54pZTIeci8HECg9HyRtG1YQF2uSxVUiaPEjBNCGDV5-kElVkYP19HBxXvQ-DJRtRdFJnHb7FY-mXaIqcsCvtfWqUigQ3DBlvHyZeHppEbywJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=fz9aQSp-Z-JuKvPv4SUZQZVZQhtAqLHFrG98oihjkPbbxDjmjqeTeVDaMqqm9yvlSxO4TqOvdwPY7Q6dLEyK40MkXqv2xoWmayDBiqYHb-l3zLlP-hMYKuEhS6HBz5mfE9aS_jooMZdjh3vGQWpZRlWhmTcMUDRKijSO6J_V7_fFjx_zTbCQ_KgOB3GvYC2WUT7yBziqGT1F0GDi_nvcSEyesCPy0GjY6_k9xiVzu54pZTIeci8HECg9HyRtG1YQF2uSxVUiaPEjBNCGDV5-kElVkYP19HBxXvQ-DJRtRdFJnHb7FY-mXaIqcsCvtfWqUigQ3DBlvHyZeHppEbywJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
گزارش تلویزیون الجزیره از خوشحالی مردم مظلوم غزه بعد از گل مصر به ایران.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/Futball180TV/96362" target="_blank">📅 14:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96361">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdEY2h-SC0TT-3TV6J-R4aJoIeETBJQogduOkxrKQLrzZjU5IMPBDelxESbTb4xBICt9QzuOSrq37Opm6iEshAAKz3qdIao_rJQZE_60kxIR8saVzcOwjJHIYqo2sfNu0q2FGfXmoisVdAeRfZOHkaBByeD2S6TjW5quaf2Kud_sy5Qy_gYPLJySYQeh1PhHkuyCT7duR9V6RE4VtORF-eZNcqoi0KxRCEcGQTr0sklcP2LHl-T41-g845Lzwp7X5_X003w8keE3lmPy83vUoew2E3G-ABf0TNbvxNgunDOgWkadGEqQYARPjwFa9FNmPR57B6VHFQ-ZMWpxz2NZAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
آژاکس در حال بررسی احتمال جذب تراشتگن به صورت قرضی است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/96361" target="_blank">📅 14:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96360">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12bac0d662.mp4?token=kkwZe4bsx-2rrqeHAye1Cvvq73rjxz3TK68eGH33Zq2tbExcXnPd6bN5E37Ld5dQhZ0FPheeWqfbfOENeqSXVL5Hb75J6wnpk5WYECKUlsmlXWk2JqdBKEP1oDtcmwrXZogfOkQPUYINKiT-9L_J1w0NQ9xzL_EjfHNXUr-3rptrNrC6hgDs4TPiQ93CabwpxdHIuJnPpIQW8Irg6sU-zkDPTRONNx-oo0Lg5VzAX_J0pNJNzQsTpNYPS-6rBvkIelD8ERK8ucbsfe3lJrpHUbcutc_JZbpMgzwk8_wrMkdldIGZEtDJBT1UOGY7V-LwAqy3srK80PRnnu9AWNvWkXq5Qch_yyLYScGErIvLUaCC_3wnVuoVMPMJnA0vIPXQ-shSOxRm_M1raYiLA-sPrPjp-AhBw0cAUjXfs2kfSuuXgkgWj0W4tVAzhhhmVolgKEZYHegic5e5ak8w66g-F1XmdCtIS5LmRo_IHH39wC8sHdt5lx9Vo8oEoRUhIriQBNcATY_f9maaLzz1uDRBUIrxkTJpLPnKKmpR1gh-8nvZhLBcQUDBr7t8G4KJtOUCU6LAxVu7q7_NJQ6rFsWyLNMA6jvYW970FWr55fR34J-NrRZHwyilut9eFjg-ZUaXT2sGxr917y-ScQsm3F4QbtBYki6ZII5D9RR9d9U7iDc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12bac0d662.mp4?token=kkwZe4bsx-2rrqeHAye1Cvvq73rjxz3TK68eGH33Zq2tbExcXnPd6bN5E37Ld5dQhZ0FPheeWqfbfOENeqSXVL5Hb75J6wnpk5WYECKUlsmlXWk2JqdBKEP1oDtcmwrXZogfOkQPUYINKiT-9L_J1w0NQ9xzL_EjfHNXUr-3rptrNrC6hgDs4TPiQ93CabwpxdHIuJnPpIQW8Irg6sU-zkDPTRONNx-oo0Lg5VzAX_J0pNJNzQsTpNYPS-6rBvkIelD8ERK8ucbsfe3lJrpHUbcutc_JZbpMgzwk8_wrMkdldIGZEtDJBT1UOGY7V-LwAqy3srK80PRnnu9AWNvWkXq5Qch_yyLYScGErIvLUaCC_3wnVuoVMPMJnA0vIPXQ-shSOxRm_M1raYiLA-sPrPjp-AhBw0cAUjXfs2kfSuuXgkgWj0W4tVAzhhhmVolgKEZYHegic5e5ak8w66g-F1XmdCtIS5LmRo_IHH39wC8sHdt5lx9Vo8oEoRUhIriQBNcATY_f9maaLzz1uDRBUIrxkTJpLPnKKmpR1gh-8nvZhLBcQUDBr7t8G4KJtOUCU6LAxVu7q7_NJQ6rFsWyLNMA6jvYW970FWr55fR34J-NrRZHwyilut9eFjg-ZUaXT2sGxr917y-ScQsm3F4QbtBYki6ZII5D9RR9d9U7iDc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🤩
🤩
کنایه بازیکنان چادرملو به پرسپولیس: به 2 روز تمرین بردیمشون!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/96360" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96359">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czroTHHYzr5K5yrCUQLDU1M6WMvfVGXUsf-zodOyc_G9Q35B9h29tdmJJhFl40Ewq8pU9CTiDYk-xAQbVzf9gm92aAfZ01Ohz-f43jNm0p5XZivywzh3Nxbv_FD_jQnOaQbhtWiHelHGdIZN2XBxVa0M4AlvxWYfLBJ214MmlSvpljjTz-xnjhcNYM_jIWxTs9IOMK4PHgtuAoie7xrXZuVdT8sqUdYK55MNQoJvSGGz3n-ZZBwekMVp7WVq5mKoBZ5015twtEFgH2IJfAnhvJ3TlEAjtgdKztHnPHvwDRxi6H91pSHgkST9QlN5SeKeH3PFYzVnPEn2NUPz1ggSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه چلسی از لوگوی جدید خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/96359" target="_blank">📅 14:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96358">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe474ed8e.mp4?token=ijid_Y8f26sTDvkJTkRM7yFOzGPM8rg0ggHVZOJ5qEgwWLOH1_hXusQmIphaMSe1wpKrDQZCUKBS87Rs2ik77W8_jajlIXawWguP_RBYdxXqpNSDtdyOA4bPy8HBohrvX8FXnJh_YjGkz8vCfJlDyHU17NoA-XT7QB0U8qfXZukSEmvvl9-6J8YFpuopfFBFy1Bh0CSqN1IAFuxTPnBN2sfFkx-16mdzhjkEDQmF1k2kfke-QfNQ2pv-N5TZJGS53aIV0B7-FeLjdNAt_7LOQN4MVy1dCrPC0CtmQ135JFRCJrsUNP2iX2Bcwu2UC6XkBx5EuJPkKm5I7GeeAofNww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe474ed8e.mp4?token=ijid_Y8f26sTDvkJTkRM7yFOzGPM8rg0ggHVZOJ5qEgwWLOH1_hXusQmIphaMSe1wpKrDQZCUKBS87Rs2ik77W8_jajlIXawWguP_RBYdxXqpNSDtdyOA4bPy8HBohrvX8FXnJh_YjGkz8vCfJlDyHU17NoA-XT7QB0U8qfXZukSEmvvl9-6J8YFpuopfFBFy1Bh0CSqN1IAFuxTPnBN2sfFkx-16mdzhjkEDQmF1k2kfke-QfNQ2pv-N5TZJGS53aIV0B7-FeLjdNAt_7LOQN4MVy1dCrPC0CtmQ135JFRCJrsUNP2iX2Bcwu2UC6XkBx5EuJPkKm5I7GeeAofNww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌈
مهدی طارمی:
همجنسگراها نظر خودشونو دارن و قابل احترامن و ما به همه این عزیزان احترام میذاریم چون این موضوع به ما ربطی نداره.
💞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/96358" target="_blank">📅 14:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96357">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDCGIDMbxNLUOHZFk8lOz4Dt7B_N_krVyQtJV_vmG-pYB1QQcu8DYJnzATsrS4QbnMvnBmDv71B5Wi3cSp4ShxUf5gsX6T7v2JQri0kKpYOQkZGv-URnV0MvgeRI6rYWL9sRBrryYx6M6P0IYhMhQ7Y3qCtd3W6Fyne-wjoDVVBxcnwRff4SPcct8b80eDkRkRSvhrRqvUOiawKLS8HBagt0sIkH4rNHYL94KBmqwZZrLA6-sU5QMcCrJzRol8jA7FNExH8os6azb9ZAElh-WCWHLI7aNslfpYM2vzroDwmTsi2mc5K3dMqpIKVasSYS8XCFJQgzn98vj82Ozcfasg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
🇳🇴
در میانه بازی نروژ و فرانسه، یک زوج نروژی در جایگاه‌ها نامزدی خود را جشن گرفتند و شبی در جام جهانی را به خاطره‌ای مادام‌العمر تبدیل کردند.
💍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/96357" target="_blank">📅 13:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96356">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d12d8ac3.mp4?token=dtyR8xGaGWMXyHUZujAnDjdzhvm9ESVrADJYyABcikFNDu2PvVwJVZ5s_oMRHUixdU49RfbPFhQ1Oliogbj76Yk6tvvaOs71pd1SohtUXJJiXPsxPk_u-Et-a2p24TYVldjEtxq0fmO-UsY5oLFHhlS9uYDakYQGnC8reQFbt6Mhe7VAEG_fM3USSkOQL1j8b1Eti6-bEB7ohjLDvxQyOdr1a984toKugNSaKp6bPhbVKdZrpaCgjn9v0inomdy1C7WNi1n4kDha6FtOeuz6YTuRDlpX1teO83n6Ef-WwbyCAbmEOI78wkaw9d9Jvkx_FeDteFnNJZ8PtKuJpLc-Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d12d8ac3.mp4?token=dtyR8xGaGWMXyHUZujAnDjdzhvm9ESVrADJYyABcikFNDu2PvVwJVZ5s_oMRHUixdU49RfbPFhQ1Oliogbj76Yk6tvvaOs71pd1SohtUXJJiXPsxPk_u-Et-a2p24TYVldjEtxq0fmO-UsY5oLFHhlS9uYDakYQGnC8reQFbt6Mhe7VAEG_fM3USSkOQL1j8b1Eti6-bEB7ohjLDvxQyOdr1a984toKugNSaKp6bPhbVKdZrpaCgjn9v0inomdy1C7WNi1n4kDha6FtOeuz6YTuRDlpX1teO83n6Ef-WwbyCAbmEOI78wkaw9d9Jvkx_FeDteFnNJZ8PtKuJpLc-Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این شجاع هم حسابی سوژه مصری‌ها شده‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/96356" target="_blank">📅 13:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96355">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/014d5401dc.mp4?token=vZUFXhdwSrmOoGJcH4Gg0qezeCy7kbK1XP63FgelTmcjIEjz6NgNXVx14SF2pZDjW2VseJt15g5ZNKQBplsICMJKnK3ZasalLf4bs9W9SiN_3sw2EYaGv8e2maMzJFD79L-_YQEZHyhEE1cjk-u2mixV0uLyRxDzpfGhzqJUHhs9OnJulpRijgUvihzOlXbOe1NIXKRZXW1jWwFu3-5xtPsru_ZPWELOeK_iftIKlQ6QAxOPqbvbJUqXW0cQCrtp9Dwz8eyMPdcSIgg0WPbp0Tip4jUJP8NNIydwkpap7kP18H9jIyhX63dT3BetI2HZivR1oPkHhVgKNO0ZQWK7dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/014d5401dc.mp4?token=vZUFXhdwSrmOoGJcH4Gg0qezeCy7kbK1XP63FgelTmcjIEjz6NgNXVx14SF2pZDjW2VseJt15g5ZNKQBplsICMJKnK3ZasalLf4bs9W9SiN_3sw2EYaGv8e2maMzJFD79L-_YQEZHyhEE1cjk-u2mixV0uLyRxDzpfGhzqJUHhs9OnJulpRijgUvihzOlXbOe1NIXKRZXW1jWwFu3-5xtPsru_ZPWELOeK_iftIKlQ6QAxOPqbvbJUqXW0cQCrtp9Dwz8eyMPdcSIgg0WPbp0Tip4jUJP8NNIydwkpap7kP18H9jIyhX63dT3BetI2HZivR1oPkHhVgKNO0ZQWK7dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
زلاتان هم از شادی وایکینگ‌ها بی‌نصیب نماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/96355" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96354">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ql1JpjWoxFLPIWRnmIxdkzPX2fqUP6qCyYK1f6CYZd2w5acjvXDoGzFLGqSLeedOfMTOmin3pybMu4OCQZeRP7yDeer7_DmQKWIx3OLXNm5G-Aq3xTRPSyE5lYjc0VA3PlywELE73ErYUthLYpbTYTy2tXoKKWHv69hoSjVjPvX4WRhIgj14ura9mEyY5BbOxz3d3qceoGpbMsN6xwv533akKSwxEtLpUiUq8pEY2KH0CsLYNLbS7JC-qX97f8_1rv82TCm0gln7T8n8PTWGN_BWG3NAxxxVaQzRTp838wK3QkyPIDHY4dGtlPtdM9voLLQ0BulpHHai7gEbIjsi8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بهترین تفاضل گل‌ها در بین تیم‌هایی که ۳ بازی در جام جهانی ۲۰۲۶ انجام داده‌اند:
🇫🇷
فرانسه — +۸
🇧🇷
برزیل — +۶
🇩🇪
آلمان — +۶
🇲🇽
مکزیک — +۶
🇳🇱
هلند — +۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/96354" target="_blank">📅 13:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96353">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1942a3cf51.mp4?token=XgqpitE6KMT6p-elmESVAhzYgQEjMTtXeEfIh_LvC0XApdjnZLTy6qab17CyCS7-ig5Fi57lLGHCK7jUbW_fCgbTx5zLsU4AYfCJwq2MX4W13G4HbGAQ6D5JyiF2-1o-Bzfg8yI7VR5lh3sqvoiv8ufhe35RjLCvJMmnXDu9AtGT-wIlrQ3g6-DrUAMY6w9008ZoVQEfGRfVPMKAuwtmh-qI65Ow6KRPCxi5bu0FnlQ07dkcerz8YqAp2IlxXnKa1KYBfICBwqya3H39KpmcplbIFUZriHq0EWLVmp3xXuPkQ866sjcFQX-bTM6rcCetwtP505T6nj58puWsnP-QYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1942a3cf51.mp4?token=XgqpitE6KMT6p-elmESVAhzYgQEjMTtXeEfIh_LvC0XApdjnZLTy6qab17CyCS7-ig5Fi57lLGHCK7jUbW_fCgbTx5zLsU4AYfCJwq2MX4W13G4HbGAQ6D5JyiF2-1o-Bzfg8yI7VR5lh3sqvoiv8ufhe35RjLCvJMmnXDu9AtGT-wIlrQ3g6-DrUAMY6w9008ZoVQEfGRfVPMKAuwtmh-qI65Ow6KRPCxi5bu0FnlQ07dkcerz8YqAp2IlxXnKa1KYBfICBwqya3H39KpmcplbIFUZriHq0EWLVmp3xXuPkQ866sjcFQX-bTM6rcCetwtP505T6nj58puWsnP-QYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
دیکتاتور امباپه تو بازی دیشب هم نشون داد که چرا بهش این لقب رو دادن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/Futball180TV/96353" target="_blank">📅 12:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96352">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5c4a20441.mp4?token=q_RpGG2eFsv1_y4xrPGycyONCSLp-Lc_SbeG8S0bdS5aJhstemtq73BIBOTP_mLMMuZMu26oT550wsvtHCoLqxOt1847kqc2S3YZMT7gcIefTResmWRr0grUdm8hq01-CPzn62rwF8JNH_spksdna0WMS-BBO5iyLM62tWfYyeSaH-gxMKe91SRG0GP2fsJkydTsorQRZqzYBenpsGdOEsytnOwBi6kzTZPkClZo_XaiS8B4j5_fwv-8Odu9tZyYi9MjAR3PeyZpdlJgPTuf10V2T4GMcMERUplofs96Pa2aU2zjqYZZZmk-whZ0ApS7jrI-3gGsYmu8CJaIljoUB6o4AHr82ji5v8kFNalrGAUem88T1yLgHB9ekQjNGLYSWRdlyaSTVque6khMxN7knBN7cGMcE1yvJyNy30CS2sRuTJcPEjqVtnyZpgdVAu_NZmw23CBZtCLIq5e7TveIJrJNNBsbSqBCuyiHmhkoTrTEei0vFTSc8OMRMQGIr4AS35W-4_FdrE9Zd_pSlLTOr7xQPbZs-YNVgpDUfdwotQyCIUkhuZHh0RYmTxVYtLcSZQznaoKvFDJAJPdJEgr9cxWjHxT8lepGIsmG7WTYxZbzn6q7lLnnJfG6F8fMoNvmXlUSdIZJc_gqWMCAJ0sYwxwK7UiapkQYTCtRgXEIdz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5c4a20441.mp4?token=q_RpGG2eFsv1_y4xrPGycyONCSLp-Lc_SbeG8S0bdS5aJhstemtq73BIBOTP_mLMMuZMu26oT550wsvtHCoLqxOt1847kqc2S3YZMT7gcIefTResmWRr0grUdm8hq01-CPzn62rwF8JNH_spksdna0WMS-BBO5iyLM62tWfYyeSaH-gxMKe91SRG0GP2fsJkydTsorQRZqzYBenpsGdOEsytnOwBi6kzTZPkClZo_XaiS8B4j5_fwv-8Odu9tZyYi9MjAR3PeyZpdlJgPTuf10V2T4GMcMERUplofs96Pa2aU2zjqYZZZmk-whZ0ApS7jrI-3gGsYmu8CJaIljoUB6o4AHr82ji5v8kFNalrGAUem88T1yLgHB9ekQjNGLYSWRdlyaSTVque6khMxN7knBN7cGMcE1yvJyNy30CS2sRuTJcPEjqVtnyZpgdVAu_NZmw23CBZtCLIq5e7TveIJrJNNBsbSqBCuyiHmhkoTrTEei0vFTSc8OMRMQGIr4AS35W-4_FdrE9Zd_pSlLTOr7xQPbZs-YNVgpDUfdwotQyCIUkhuZHh0RYmTxVYtLcSZQznaoKvFDJAJPdJEgr9cxWjHxT8lepGIsmG7WTYxZbzn6q7lLnnJfG6F8fMoNvmXlUSdIZJc_gqWMCAJ0sYwxwK7UiapkQYTCtRgXEIdz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
تفریحات تماشاگران جام‌جهانی در محل بازیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/96352" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96351">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGeAPVxu6zypOjHY0K2j0-5j07i0stN70fgW3a68AVPKo11yJHsEffttaFplUn2j0JWL10tMC6pIlgJxdqbxaXutXQtVywizhh_o9wEIAovEa--925iNivq9FNYkrYrmXP1xGDgjud-yYX7BkUz6HOC6ByH-Tg_focobK5-U2-FiMJyT8ft4Nfbx_Kn5oP6g74fi-e1oRiqy1WkifKJCWCMe27uHVD7pfn0iDBD9WchXrwSOpjY4ucqpCWB_s-Zj5yuI9x9dKEcufW-UhKjA4nAk2HILJ-IYdyszRWS2YWYPKlXmaxsI0Mys0a3NvEd8lhREVs9eZUsvbG7br81VWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در چنین روزی در سال ۲۰۰۹؛ رئال مادرید قرارداد خود را با کریستیانو رونالدو پرتغالی ۲۴ ساله به مبلغ ۹۴ میلیون یورو اعلام کرد.
🇵🇹
🇪🇸
😊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/Futball180TV/96351" target="_blank">📅 12:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96350">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b9d3e103.mp4?token=gVvl4VJgunU2Jo2j4Cq9WM2p6_SznM5LIbECMSUnib5ZFgiqMvtx5s21wn3Nazn8HWHlEezXYI0WPwyxEuHrl-Eg8eJn8ogPrArmZUv8lawb7dNOmKJYxLthL1J1mzN1N7DnpwMqsO9n_oWa2OG5wBlN0Qni0rpq8vR2w8ii6_sq1-mG_sfrTyRnnqVPf8EkbJxre2eVWU_SgvMrFwyFviLJ-b0W2Eh09-OMJMvM4dSVyPaLDfmrSxxzVoLP-p3AUp1PjX2gSqDGKPhsYSNLhQgDB3apIByDrvBH0kdGiAogc-K7IcgWo8sCRM3vBgs0sGP6Erc1z3LeLhCxbhz5SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b9d3e103.mp4?token=gVvl4VJgunU2Jo2j4Cq9WM2p6_SznM5LIbECMSUnib5ZFgiqMvtx5s21wn3Nazn8HWHlEezXYI0WPwyxEuHrl-Eg8eJn8ogPrArmZUv8lawb7dNOmKJYxLthL1J1mzN1N7DnpwMqsO9n_oWa2OG5wBlN0Qni0rpq8vR2w8ii6_sq1-mG_sfrTyRnnqVPf8EkbJxre2eVWU_SgvMrFwyFviLJ-b0W2Eh09-OMJMvM4dSVyPaLDfmrSxxzVoLP-p3AUp1PjX2gSqDGKPhsYSNLhQgDB3apIByDrvBH0kdGiAogc-K7IcgWo8sCRM3vBgs0sGP6Erc1z3LeLhCxbhz5SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
صحبت‌های جالب و تکان‌دهنده تبریزی خطاب به بازیکنان جوان
: گوشی رو بگذارید کنار، عشق و حال زمانی کنید که جایگاه خودتان در فوتبال را محکم کرده باشید! بازیکن ۱۷-۱۸ ساله نباید مشروب بخورد…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/Futball180TV/96350" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96349">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CilKlrbYj0UeOYr0GgKX_zZrxL_9vSIhDYhwyJ_djixD7-QNTBoQd9v9n2zZ3i0z_fA4Ucx7skIBa8RFMdc23qd0U3LBv6naAA3Tsom1Ce7fxfBnVjOKmCewiG2WgpnUbh1NWRJDrr5QJdxLkybRSUenuenuHpWz0szTVrTIccBqGW54YbH8hFVFwrCaBm8HB2ivQIgtTZQZgb5g4kU3Ua1qFQzMRKsEcF-95z0QSH05OVTvjolYK12knPIW7sWN3GPB7T-eHXeH3BV3j54kbhlPzlGq_sED9GOZrxOStdd5uBvSWQbWBIdnwjtZcNsT0ozOX5CViVcZVjGs5lAVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
رامین رضاییان با گلی که امروز زد، به کافو اسطوره برزیل رسید و با 3 گل، گلزن ترین دفاع راست تاریخ جام جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/Futball180TV/96349" target="_blank">📅 12:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96348">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee48f95460.mp4?token=MPmkBnTSfvDJJM9DUyFuwDEgWN6GAYGwDxlCZSn9txgcb67FBMUqauOwlWx-VDmp9B3IL-jY76VuzVknmOHvUkR-P3VPLCRjZ1YMBOfYK00myZ57Ht9f9j_zl-tah3sOhyNpr3_PryBQOr7XEmAqPQs6c07NWdVBXuB4rKYlIJFcrdl0SQB-vlY0xO6BNzeKh_eq14JV7j4H8d_sli8FDy-laNbhy99n7Gbkn2UoFpDC3m1-h0qEzJMhoegDH0DqakwQCCxfm44GrjVLkWlaTkvM4xCtjeYMM_AweFmdgkY4xfEW6tc5vjrvoW39qJwLYFJlhCJBgu6hLWowOKJ_wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee48f95460.mp4?token=MPmkBnTSfvDJJM9DUyFuwDEgWN6GAYGwDxlCZSn9txgcb67FBMUqauOwlWx-VDmp9B3IL-jY76VuzVknmOHvUkR-P3VPLCRjZ1YMBOfYK00myZ57Ht9f9j_zl-tah3sOhyNpr3_PryBQOr7XEmAqPQs6c07NWdVBXuB4rKYlIJFcrdl0SQB-vlY0xO6BNzeKh_eq14JV7j4H8d_sli8FDy-laNbhy99n7Gbkn2UoFpDC3m1-h0qEzJMhoegDH0DqakwQCCxfm44GrjVLkWlaTkvM4xCtjeYMM_AweFmdgkY4xfEW6tc5vjrvoW39qJwLYFJlhCJBgu6hLWowOKJ_wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
اثر جدید حمید سحری از درخشش دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/Futball180TV/96348" target="_blank">📅 11:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96347">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBGKXgViLFtF3OHrZ6b39QCHRBH_gD56SELJOlvSomq-P_KXrKgyE_LrelWQgFzm-FcY5fm9GviHbYk4MV75LL3b9GgQM2_2YQdxApNLPycuc_gqnm17MxAgIBmyqDQNkJWpPOlRyKQFa3X50Ktz8eikTVWiLOxcMcBFi9hOQMKeJqCC5a2VWn1cL8V9oh6O_kZaKIZkWCaXsSn_9Z_r9uyo6L2FjU7oyksFYsgvVXw8aiQRFgTvGGNn4dB2YyHzYu75ehtSmZ31mgpvxYAcfkC7gUF4LWnD8216JtqmK0QwjQIWwwYjRri07St5OO4805x-TM6kSvaxppybeyyiXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
آرزوی هوادار بانوی برزیلی
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/Futball180TV/96347" target="_blank">📅 11:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96346">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/330a09c36c.mp4?token=MWbHYLGJWcEcaKrCxpWaeAMWMxGyOHorfTCXEhq59K9Xx5irdmFBRXMo433xM15kX47YE7gt5zPu78QU28D9Sd6aGjMylF9Q4c9pz8fO-wObZE-ZGyGJcfUaKHwp4Hg_BFciJTLuewLIo1pp4VK0JEkZuN1E1aAk8bd4WAdVpPRUiG-zUfBV1w0ilDN9CBpu3y6SEAna1AAWeuIf9Xvgbf50N2c3d2WAHMTzkI1Dv_6k4h771o2nnRUVYaQOVGKDI7GLwI-K-dsSkuIcUFcr5BABzxz0UiHHvmZ1M7mIBD2qu7HrDuzqkGHVI_Q4WpPZZG8EJ4FJBZi5DKIP-swpmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/330a09c36c.mp4?token=MWbHYLGJWcEcaKrCxpWaeAMWMxGyOHorfTCXEhq59K9Xx5irdmFBRXMo433xM15kX47YE7gt5zPu78QU28D9Sd6aGjMylF9Q4c9pz8fO-wObZE-ZGyGJcfUaKHwp4Hg_BFciJTLuewLIo1pp4VK0JEkZuN1E1aAk8bd4WAdVpPRUiG-zUfBV1w0ilDN9CBpu3y6SEAna1AAWeuIf9Xvgbf50N2c3d2WAHMTzkI1Dv_6k4h771o2nnRUVYaQOVGKDI7GLwI-K-dsSkuIcUFcr5BABzxz0UiHHvmZ1M7mIBD2qu7HrDuzqkGHVI_Q4WpPZZG8EJ4FJBZi5DKIP-swpmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
از هواداران جذاب و پرفکت رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/96346" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96345">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml3QOcjzH7aiHpbyz0p4Wo_ysELdWnn600FDQcvCjVBBUtKXeM39hL0PidN9tVByE_vFtzdB1tD8D1ltOq7zx5LYboAG3LRomv-xvfNiO6MiisCerNlwrHBLiXrK00phqQEIDO-jL8qKCZQPWT87LCBgshCmnXR4hK_01Tl3NZUqsKUI0NqgBm0juHMIFz1TYlVv-X4pkRNq0ZGiNSJdQmtcy8mzxDo5wiY1a2NlVVzu919E6B0OfM_e6GD1GtG3RgYt38ewdje_SO2DgUJjiR59MXXgjyNIMhmdz06BtCVN__6gL-m2zQHCvM7zYe6Mn6uvJJoIGLJGN3_0cu4UFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووری
؛ مارکا: نیکو ویلیامز ستاره تیم‌ملی اسپانیا بدلیل مصدومیت از ادامه جام‌جهانی بازماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/Futball180TV/96345" target="_blank">📅 11:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96344">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXfSbk9vWlK0QlSfD-7Q1BluFCbTA4EjfULzcKjXl7oRQP3t27q9PP9bNOt_BI_o46clFPF6JzSiPw2uy-Z3pTiqQJfCHXtOvrJUqQPFU9aCWpxYqcHLXUBaE0KZt8_4mAjHYTcndunhQD7CMloTIm5YdPD89fPT-Bo7MNZKJaTrGfqTuJct-sYA1o1YCmOMQo1jsIBXurut0ncm-k1CW53TFNicwUq6XZdEDUq5piKkIlJLsI7GGcBK00-O6kl7gK4tMGH4_WdHqsY36_47Fh8ePZ61IOFWRCLisAFU2M4hFp4uvgIqppQ-A3yErC45XWubRHX2XjGBq31S5xxA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
کیت‌دوم پاری‌سن‌ژرمن در فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/Futball180TV/96344" target="_blank">📅 10:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96343">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4d474911.mp4?token=UJejX2-0fWBMlKQb2Tn7quNr-jNlsjlbCINmpnMLt3rZyVwQ7kZP1aUVC3PnGOCrqeEWLbHCtTX7Sq5oBbts0E-7sp4zAEl5bj-HCL6U_AVd5MAK4pWYLMjY221G4SXy7-T_v9JWYZLRfmjZeyTq5EGKB2g0YEXTXbeihZJPRwRtHFWQxryd4tCgQuM6knrqKzKbQL1g0INUBZXV88GEsW7YrNgd7fOeaA7_t_f4v2vqyuRXJTgP0jEd0NwEU2wrHKMDlEryQOyUMGqMtkydq6rfZcrj8sINtQkpZa2-FFPfmU9YBa5625-8G2XJsuvKbuRsUIemjSlVHP8A_gY-nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4d474911.mp4?token=UJejX2-0fWBMlKQb2Tn7quNr-jNlsjlbCINmpnMLt3rZyVwQ7kZP1aUVC3PnGOCrqeEWLbHCtTX7Sq5oBbts0E-7sp4zAEl5bj-HCL6U_AVd5MAK4pWYLMjY221G4SXy7-T_v9JWYZLRfmjZeyTq5EGKB2g0YEXTXbeihZJPRwRtHFWQxryd4tCgQuM6knrqKzKbQL1g0INUBZXV88GEsW7YrNgd7fOeaA7_t_f4v2vqyuRXJTgP0jEd0NwEU2wrHKMDlEryQOyUMGqMtkydq6rfZcrj8sINtQkpZa2-FFPfmU9YBa5625-8G2XJsuvKbuRsUIemjSlVHP8A_gY-nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🤣
تو برنامه پخش زنده ورزش سه پژمان راهبر به خیابانی میگه انقدر از قلعه نویی انتقاد نکن، خیابانی هم کلا برنامه رو ترک میکنه و میگه از یه جای دیگه بهت زنگ زدن پرت کردن:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/Futball180TV/96343" target="_blank">📅 10:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96342">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86220511a3.mp4?token=D3VvG4egteKovZjV1BL87kF0pn3v9zs0al30BD_C6YR7uVphepRMebykerH350Xc3mbCqx_vQ8ukZ2SBwRlfU3lab1gmZtBJmXEqgcUgsNrzzKoyZP0Tb8_wa8oL9ucY8D1rDYeDwxbALOJJrteKhukVceX-zbJU8xseFyJ2mWjDjldefuzZdY-lnvxoY58z7b3SJmppks8ZxGED9f7zDBBvHExwrU-j-KeFYUHMGwaWt0fFavfU9zow1j6HCwvmbdUi9Nul4JcR4MMM1TOpfM0haVGEUztpUClybCq5_yiwcYHUUgUlQ7wJcgZzJIV-8x3xCaE1ukWy3IuNw9SMUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86220511a3.mp4?token=D3VvG4egteKovZjV1BL87kF0pn3v9zs0al30BD_C6YR7uVphepRMebykerH350Xc3mbCqx_vQ8ukZ2SBwRlfU3lab1gmZtBJmXEqgcUgsNrzzKoyZP0Tb8_wa8oL9ucY8D1rDYeDwxbALOJJrteKhukVceX-zbJU8xseFyJ2mWjDjldefuzZdY-lnvxoY58z7b3SJmppks8ZxGED9f7zDBBvHExwrU-j-KeFYUHMGwaWt0fFavfU9zow1j6HCwvmbdUi9Nul4JcR4MMM1TOpfM0haVGEUztpUClybCq5_yiwcYHUUgUlQ7wJcgZzJIV-8x3xCaE1ukWy3IuNw9SMUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👀
آقای‌هری‌کین امشب لاشی بازیو بذار کنار تا این طرفدارت ناراحت نشه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/Futball180TV/96342" target="_blank">📅 10:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96341">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a81f32bd6c.mp4?token=AjBNlV44tSfJvEbhfCtnfe6wNqVvlnVOgKShsqBqLWHz6snYASAKuz2MVqYrT79ZMrdFp9174PJfJnSsoPmWORq54JDiYkm4LmP2OFLpPwVx4buE4464SNmT4izLKJfkfYxBKX-Zaj4PFSEUGZEuWAqiSHxV7NaKqk-EF_Tl0gMrG9AzRMhU_kAZhuGSAowVVCuCPDhJZiBNs3Ovf4qYLyX_KnRJ28H5fh7xriXeeL7nQNfVGJ2YlnQAf2BpUC-JVIhYdbqbjEhSs1iLMQpufR2kuN4ty_S02XGST40ht7nq_yjqeW0T9LkafmwaLjBaCNHUwGxL-o2nzhWQSoiUhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a81f32bd6c.mp4?token=AjBNlV44tSfJvEbhfCtnfe6wNqVvlnVOgKShsqBqLWHz6snYASAKuz2MVqYrT79ZMrdFp9174PJfJnSsoPmWORq54JDiYkm4LmP2OFLpPwVx4buE4464SNmT4izLKJfkfYxBKX-Zaj4PFSEUGZEuWAqiSHxV7NaKqk-EF_Tl0gMrG9AzRMhU_kAZhuGSAowVVCuCPDhJZiBNs3Ovf4qYLyX_KnRJ28H5fh7xriXeeL7nQNfVGJ2YlnQAf2BpUC-JVIhYdbqbjEhSs1iLMQpufR2kuN4ty_S02XGST40ht7nq_yjqeW0T9LkafmwaLjBaCNHUwGxL-o2nzhWQSoiUhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🏆
وضعیت قلعه‌نویی بعد تساوی با مصر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/Futball180TV/96341" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96340">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e7871462.mp4?token=fR7-GE1cpTGmgz3h4bupssXvaJOx0V8z_5G9y34Atr6iEisogY4BkVguRXGYMtjKjyil1QaT5Z9VNIUsMm_kpKkwAv998erw9dVQ8mARj3CGFuzK_xchGQhnfNjNqpTV4Xukzt8YpSDJDgK0ZFlhdWVdIe5hetFlqfeVGmY7fK6FxFleJB8h3SzAC8H6hEB7Sm5pfhNILS3PfOtyK3Km_F6SbP9aKhaNl892kY4j3JsZt6u46GSF3gIF7qNnzQX7HpcMlvOispLAOCfvUAMhbYvJ5DyimR77fqzGy6CFqk1b9Idp31w81IKtIzCeJKUqoNAG3NGSWnkokl58PTJVpFG15rIhwnWfCbId07TJCSXrwA9LRTY4J6sNqCVr4CfX5ksLr6l5RONmWBfuMULh5Hk-EVSecxsFkZyreGy6ptxsrOLSpCCUv83IZCiK_Q1CxlPQgBn1tM-5-oZGuP3cGj9XVW5pv4PD0D0NUJ6LnnNJ0DGF_gMmhLDDhhoSXB7KuCYeT4afOEvogCvVUmcyYqcFO0x2P9oYKqAoSA38cyX5uF1tUWrcOKsJMzdUu0Eti-C93pkuUzlCRpER9XhnzUlqJiFLGRiD_ngn_IT5vMIYz9LIRWSDA8ko3hLcrAyvNsEQcFdJsmmzUm7rBEfkRZSSbmlqUqsBAE_WOh0I708" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e7871462.mp4?token=fR7-GE1cpTGmgz3h4bupssXvaJOx0V8z_5G9y34Atr6iEisogY4BkVguRXGYMtjKjyil1QaT5Z9VNIUsMm_kpKkwAv998erw9dVQ8mARj3CGFuzK_xchGQhnfNjNqpTV4Xukzt8YpSDJDgK0ZFlhdWVdIe5hetFlqfeVGmY7fK6FxFleJB8h3SzAC8H6hEB7Sm5pfhNILS3PfOtyK3Km_F6SbP9aKhaNl892kY4j3JsZt6u46GSF3gIF7qNnzQX7HpcMlvOispLAOCfvUAMhbYvJ5DyimR77fqzGy6CFqk1b9Idp31w81IKtIzCeJKUqoNAG3NGSWnkokl58PTJVpFG15rIhwnWfCbId07TJCSXrwA9LRTY4J6sNqCVr4CfX5ksLr6l5RONmWBfuMULh5Hk-EVSecxsFkZyreGy6ptxsrOLSpCCUv83IZCiK_Q1CxlPQgBn1tM-5-oZGuP3cGj9XVW5pv4PD0D0NUJ6LnnNJ0DGF_gMmhLDDhhoSXB7KuCYeT4afOEvogCvVUmcyYqcFO0x2P9oYKqAoSA38cyX5uF1tUWrcOKsJMzdUu0Eti-C93pkuUzlCRpER9XhnzUlqJiFLGRiD_ngn_IT5vMIYz9LIRWSDA8ko3hLcrAyvNsEQcFdJsmmzUm7rBEfkRZSSbmlqUqsBAE_WOh0I708" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
این یارو هم از شدت خوشحالی سر گل دوم و مردود ایران نزدیک بود جررررر بخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/Futball180TV/96340" target="_blank">📅 09:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96339">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🎙
میثاقی: اگر بازی در لیگ خودمون برگزار میشد، چون هوش مصنوعی و تجهیزات پیشرفته var نداریم الان گلمون آفساید نبود و برده بودیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/Futball180TV/96339" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96338">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03b41f5781.mp4?token=opl5hkDbMMBWreOm269f8m_3O1qW1607lvZ3_CwXb-FCEVNVcn2QNRzwXEJBTDkJ9gY1yGsxZD2ZVvzQ7Ds2WPExs-xUHrAagRLOvjjHnkKW-IlpP4l3iQhjspJeL4Uqm-GEW-ktXzd51lC2K-6cdIL3HwPxNKgbVGky7TqvGgbR6pNm5LbFfioxV4RYoAPKCSGajppmc7ACu19nQGTsGUB22M81A9yMyahU-kHuSbo7eLk9Aft9-gqxS7yqXJGRPSCCnAVG4LKakgYC64CxHM1e2ny4i4g7YvHG5HCsv0ldSvcz3OiL6XLFG6n7I3mSHr_SyHSAlmhbOfd0Wdw6sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03b41f5781.mp4?token=opl5hkDbMMBWreOm269f8m_3O1qW1607lvZ3_CwXb-FCEVNVcn2QNRzwXEJBTDkJ9gY1yGsxZD2ZVvzQ7Ds2WPExs-xUHrAagRLOvjjHnkKW-IlpP4l3iQhjspJeL4Uqm-GEW-ktXzd51lC2K-6cdIL3HwPxNKgbVGky7TqvGgbR6pNm5LbFfioxV4RYoAPKCSGajppmc7ACu19nQGTsGUB22M81A9yMyahU-kHuSbo7eLk9Aft9-gqxS7yqXJGRPSCCnAVG4LKakgYC64CxHM1e2ny4i4g7YvHG5HCsv0ldSvcz3OiL6XLFG6n7I3mSHr_SyHSAlmhbOfd0Wdw6sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وقتی وسط سیاتل تریاک ناب گیرت میاد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/Futball180TV/96338" target="_blank">📅 09:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96337">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdrwaaTm8YCgQZZ2uogvtaK_35xs8sxyDDo3TIeO1NooB1_t-337PIIVU0e9nZskDMhwVBZqCJdclzHgrfSbjv-LXhN1b2ndoNpFw14dwNwTyWgRv4vrHyjRojedYIfL5WuWXEfIHY3AbU7K-BqL9RBLG9-osHE4oIXRKO9i01yvZBW-xuYPdlsFRQudNf2Fji7pf2L7XQkd0AqTpkJh_Lj-A96HeRY9kffAUMPe_EGzyeMohX1qtVWEglyC70AiuKeB43J-HEBsE2Gb8emcugqEIWyCUqUdNQFuHO4guYkbrh_8kzSzj3-C8MBP126lYigXg7qei2Xp6kTDV0jCIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق var بازی ایران و مصر
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/Futball180TV/96337" target="_blank">📅 09:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96336">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG6WfDXaQfyNpuE1ofCJb5I5qIfeFdSXBj-L9-vDgsfjzg6kSLWyp-9PetEx_sBpajUvuhFDYVexjXik8AbEqAkhNADk5kAbpBVsQotFTFQ10VzndC64T4_M6OWXh-3jxs5J4pWp16ZGyaXJjisz_7kJNNl0tQxZfPeCObmoERtiNFHzT00BcrTEiKWBIRdxRM4eGfvvaByaZ3bfI1ao0Hoi9tb_DVK8GhrclB0OMpPWhDdksKlu4bY8t9P6pJBvVClRnCE4q91XjaeZmB2lGR5i0P-qWLYLkYv1TGAGXlrEoEK7mBzpbCSxdw8vADbCm5WAqnEk7WMjfMmvBEIn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤣
🤣
تفاوت‌سطح از این عکس مشخصه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/Futball180TV/96336" target="_blank">📅 09:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96335">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57704b3690.mp4?token=TyFdyfw334wbLuDdV5TW0h4G-TEXEt_VfgsuoiIZhBzhuRAPTmUJa4AYbboL2WPi2gZXJRTHKOQth13Gt2PQ8J_yOHpECRLAqyxOo4pBzuNw_mx7R14-aA2r3nsvxl8O5O18Zje-Iojedb8yjI02IlMdr2szFR_bGs-MX6z2KqmGhV87jor7O3TZHg0dzldK2WsXSVN1EEfbT0RySP-zBcyiYHUlLnVwA53ak5xRGF9ZWZLMNW2Q9p56X6vACQYcwtMn5c0t6oke6bbOvJLtbCt45cOgZ9hoHHT_ceGJJYv-2whADqsIu5GsZSTOB8kW1yM90j6BzMauL2GHz2h3rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57704b3690.mp4?token=TyFdyfw334wbLuDdV5TW0h4G-TEXEt_VfgsuoiIZhBzhuRAPTmUJa4AYbboL2WPi2gZXJRTHKOQth13Gt2PQ8J_yOHpECRLAqyxOo4pBzuNw_mx7R14-aA2r3nsvxl8O5O18Zje-Iojedb8yjI02IlMdr2szFR_bGs-MX6z2KqmGhV87jor7O3TZHg0dzldK2WsXSVN1EEfbT0RySP-zBcyiYHUlLnVwA53ak5xRGF9ZWZLMNW2Q9p56X6vACQYcwtMn5c0t6oke6bbOvJLtbCt45cOgZ9hoHHT_ceGJJYv-2whADqsIu5GsZSTOB8kW1yM90j6BzMauL2GHz2h3rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
قلعه نویی:
شاید خدا داره منو میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/Futball180TV/96335" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96334">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmR0KwTnxaVLzvGNdDoNSuVNnOdqzQObb5P80jLeM7D1GjOQaM91aLBjdLD557e7LFAk8jMIa9vUBb6XYAdU4Dv71Ko5BG93uaZgB13EaGRwRncAPZvkyuqxBU5l6ChrWLY1K-wEA5ykbvawGSyEyG0JN0FKHrZjHaoeCZ4SQH72NiW83MR85fC4CTlbBmC73fzFO007_VeA5-po9PrptIP_T8zURUuR2eWgR0jxN-Safj0KggcCsTlTSB7F2vrbzOgk9ATyjYw4HkRtE3TYQJIdR1Jkz03rE3VtGFWVjfPruLbRXdJNxcOSsNmio2OlGCuutvc0r4tIPjY1eUnOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک حالت از سه حالت رخ بدهد، منتخب ایران صعود می‌کند
🇩🇿
🇦🇹
گروه j بازی الجزایر اتریش باید برنده داشته باشد.
🇺🇿
گروه K ازبکستان مقابل کنگو شکست نخورد.
🇬🇭
گروه L برد غنا برابر کرواسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/Futball180TV/96334" target="_blank">📅 09:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96333">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juibrClU431R2RD3gMFPB5ZSMf8mrkVtIzRbtSqh7zSoLjID2ivGdhY24mG9n9aDlOwxCqJx6xw7ZNiV5N7KRyDZqx6cP1qbifKlWl8uUJmUGB1UaONaANwAYtbMhWoKoZXb7OV5pMz6FEH9ghK2jRr0xCzPoAEdzvGMESsUn_KisjIEU-mgsvZxHUZl3j1_zr7XG0LklBVil2d6nfnvdVAeZzchDmo9CqKCsG4IS7ruKVeXr51gz4fNnF9k5KTPK13P6JDQ6fpBvDBfYI8x2nk1shcww_9fmQhO-a5Bew2CuqiYtFewWsi8gDnmDd9qB1sbv6UG2DcEtLC6C0eVEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
جدول‌فعلی بهترین تیم‌های سوم مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/Futball180TV/96333" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96332">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHYwkwHK_jjqAaMWxbfs1CErAz3cSNkJ2_6ab8d-SwxuX3BduyXgRDYYF15jIQz-kd5qPw5wNl08H_ipRqlA2t-Fk-x-3kywo2weedQBEgaNmVngYFNKAs1CrXCCFk5QqnrdX5nwF_C4ToSfRN2V_GoY3S3--f0mqlOFKI-DGtBKTGShR06kCPsv8GlIHmUePmGM1N2lXknQe19KaCi2oSddbwToLuQPtb6makL8FW2Enswu_mxpDUW2ZL8MqNVCqnwfDbzgeXPysYMQ5hXWmJWzEbqcx4_QaL81aYAKxoUL19OvRK_unn8GKcNyS9IUaS6NEsjmmdAmdZnqzUubYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خلاصه ی بازی واسه کسایی که خوابیدن ندیدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/Futball180TV/96332" target="_blank">📅 08:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96331">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMN5OaVt-VYBJl2L6naIvRV2fnFnIk2qGTxIudr0mUHrWPiDEbullveZZgLfn4taSR6siH0uBwApB3Saw7th2L9ToJv1QzeaRDhg0KfwUW-TjjFyGiduVKqJOISyTFbT2iX8pfmZxiMXYxS_3l51-WyA0xuKsJeLvjS3XxJXoDfjzLd_2ZyNw5406GPeMAmrETtzIx-5qiPGDqwcBUjVUhHQQaP8HEJt6EBALOtmvYpw4Xft1xJZ6ucVxkgQB2hI3GtUr0O-f6Q3onUDblXqIt0CgrtH-F4LwOq0fec9zNA_yGuaNQc4J8EHLCERx2mPNwd1pDj1Zjxwvp5MqOLh4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
سه‌بازی حساس برای منتخب ایران:
🇬🇭
غنا - کرواسی
🇭🇷
ساعت 00:30 بامداد
🇺🇿
ازبکستان-کنگو
🇨🇩
ساعت 03:30 بامداد
🇩🇿
الجزایر-اتریش
🇦🇹
ساعت 05:30 صبح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/Futball180TV/96331" target="_blank">📅 08:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96330">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxPr5QBwQa-pGPnqx9CaALnpHThzg_G9NyIiCrF93Yvgp0qPc__xHtDf4RnYwqWNOg8LZZr81RxNHgzYoHaUIObqte4KZ4WnN9f5DM2BRx4cJcvBtEKaMevVv9hJW9n8jUDmICRJhphT1Jika7d0pgNR4ZoLCYR_TQa0juor7rvOMIqIbXghIwnH9PDgD3PMMAPXfsQlDl6dX5nnu51jHe-KOj_q0IcpQ7gbURVXdgiWhBF-5aCAG1D1mUXXa0JVWEofr5koezTUawgCgWoz2o5WlHxtO7tXpaQr3My8DNwyt7VCXBu-pnvZw3HSwRE7LCT6E4I2QuTMmFLZZhtcAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤣
جلو جلو ذوق کنی، کیررررررر میشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/Futball180TV/96330" target="_blank">📅 08:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96329">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
یک حالت از سه حالت رخ بدهد، منتخب ایران صعود می‌کند
🇩🇿
🇦🇹
گروه j بازی الجزایر اتریش باید برنده داشته باشد.
🇺🇿
گروه K ازبکستان مقابل کنگو شکست نخورد.
🇬🇭
گروه L برد غنا برابر کرواسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/Futball180TV/96329" target="_blank">📅 08:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96328">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
یک حالت از سه حالت رخ بدهد، منتخب ایران صعود می‌کند
🇩🇿
🇦🇹
گروه j بازی الجزایر اتریش باید برنده داشته باشد.
🇺🇿
گروه K ازبکستان مقابل کنگو شکست نخورد.
🇬🇭
گروه L برد غنا برابر کرواسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/Futball180TV/96328" target="_blank">📅 08:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96327">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4D5mKVR43L40CJhf4CnDFQY4QXN1gLSKKREBSwiXLFFtP2siAsajexVyrE_aaprfaCQ4FY43JG5kFClDLtRU_NRvPNOOlLn-GxZBkf-r-Vu98vZ8AiId2e_60fauNf7Mx51xVFocTO8D0FPgOyrAWnjzMHZiA9JMZsfWXJmKiS84CJNJGJ9H9p03Cd96EP2OHZVCpPRjDMJJw_ayKWIXn1m9A5MS74wvKJeihCkgaQ_SUYXQkGh36-t8kyQrhVgZ-Naj65vqIs70zOywcuabS1L1QKwlU5G12SihMHHO-tbwfDAAhSLq1dqEI9ORINCwdH04dSFPOF3GfEgA5cvHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله یک‌شانزدهم نهایی جام‌جهانی
🇪🇬
مصر
🆚
استرالیا
🇦🇺
🗓
جمعه 12 تیرماه ساعت 21:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/Futball180TV/96327" target="_blank">📅 08:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96326">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBWLx198oAI_z-b4Mnz6XTbvwmPNCpPzvzx1qTyS0qv76DkMtNZIB8L2tKAUsHJ-Y33ECsD17X8ZdkPe3V-gIaoaOA2-SVnKNL6LVp8YXvjZENtvAQ_FB_pT9cSXDmEiGoLAgKTCw0SYJ6eiBadxFUwX55TrLj4rf7xJGb_fvI050xq-yCBXXwY_azjaTlGNbFnqH8APIjzC_ymAYFjnQMAgsLAwe7EdULZ3pqCbCaNKN3uiNQ_pioMLNLZU-5NpdhMzi-GkSwKpkMMCT_rFG8HHwci1EDTCjIAjJmzm0tdPV-79M5AfTdBHwu_pLWFHFfF-L0bCkg4o-a6ilAtDGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌های راه‌یافته به مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/Futball180TV/96326" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96325">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgJwpjDxHH4UJHNEB08vFv4327IykCOKt6osRqZelsWyNbebjmTYiZxHUip1Sv0_BlKbMFcAH42Ko1qBxmY4YD4zWhA1tWlGG6vXqG8r4UxZgnTP6xGd0jnyOz_caChsiSywIGpQpNofWQg_KPAXMcbFa5XoatbdRn6vzz-k7h0KjREpfKAqsRb0HvH6hIn3IJWmJfXx9epYrZ0t5KHNFs5TPXWwpacQfiRWdVvIFgsMIvdNAzqVvd1iwF4o3dqrQ2d4TzVmQEHipP_G82SemOcrPvGUJnOzBcy2mw9wlVIWh8eIaW-3qbmu-M-OyR194IwRDSDIW06Cqi7QeYvzcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ بازی کثیف و زشت تیم قلعه‌نویی در روزی که برای صعود نیاز به برد داشت؛ منتخب ایران حالا باید منتظر معجزه باشد
🇪🇬
مصر
😃
😃
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/Futball180TV/96325" target="_blank">📅 08:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96324">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇧🇪
تیم‌ملی بلژیک به عنوان صدرنشین راهی مرحله حذفی مسابقات شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/Futball180TV/96324" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96323">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGEHgh1ZNPNhXdqgRb-9tRHO5dXcBKxrIUdcNMn_Jt9s1xjBws6anUbNG-CoedHm-d5gKerkE9wjydBRpTL_dmfl4mULMeYvG5miYYxpOa6xqrQIMUbPuJ2tv5ZxBo2oEP7q7LbV9KI5f8aDSrbemKIyNUxEkCT-CsWUHEqvlQNHtmUkG5VRZrAfDg2qKeIb19uJx19fvyQpVJLrWgMaiIOQRpkCIZHxTijEIFawTgfH_8J7ykMeoHZVZjUP119rIeFaCmPsb53cpmwtxU5fualPiuTLQFUraKCwV5r6tvBSuJQUdPpEcaNLWt8sqv2pKAamHTA13V6130lp9GxxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گل‌مردود منتخب ایران به مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/Futball180TV/96323" target="_blank">📅 08:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96322">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37f359e5c0.mp4?token=iNeUCYIdaaNywfHpYiyUDn1O_GUXyy9M8Bbrsv3l_x1Men28cvcF6o5Ywaoy4At1v76hWZv4ifp8ndSXm35v9iZonKqrNgPnslmxjB637C2yPMZkN6ag7G1z43TcZzxGhFNvM4mf-zChQOUOOEfUlXRnn9mCPxB1AGGKq9aTFmLl9fZ7BDLjAvlcYUWVhbEdKmZdLuQ6REy9PY6NC7kG8Bl8-zBG5mDA638CKsTI0wiQ_u8nKdful2C2NWki6lBJaUYW5gXXtZddt8gcaMriAVSATax4nuJeydkupV60VlEQ-u9XqE1xCnjSD6XgWtnv0jDKHGp8TUhKzhlxiG4z8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37f359e5c0.mp4?token=iNeUCYIdaaNywfHpYiyUDn1O_GUXyy9M8Bbrsv3l_x1Men28cvcF6o5Ywaoy4At1v76hWZv4ifp8ndSXm35v9iZonKqrNgPnslmxjB637C2yPMZkN6ag7G1z43TcZzxGhFNvM4mf-zChQOUOOEfUlXRnn9mCPxB1AGGKq9aTFmLl9fZ7BDLjAvlcYUWVhbEdKmZdLuQ6REy9PY6NC7kG8Bl8-zBG5mDA638CKsTI0wiQ_u8nKdful2C2NWki6lBJaUYW5gXXtZddt8gcaMriAVSATax4nuJeydkupV60VlEQ-u9XqE1xCnjSD6XgWtnv0jDKHGp8TUhKzhlxiG4z8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
گل‌مردود منتخب ایران به مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/Futball180TV/96322" target="_blank">📅 08:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96321">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گل رد شددددددد</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/Futball180TV/96321" target="_blank">📅 08:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96320">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گل رد شددددددد</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/Futball180TV/96320" target="_blank">📅 08:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96319">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بنظر گل مردوده</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/Futball180TV/96319" target="_blank">📅 08:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96318">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">صحنه رفته وار</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/Futball180TV/96318" target="_blank">📅 08:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96317">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شجاع خلیل‌زادهههههه
🤣
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/Futball180TV/96317" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96316">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">😂
😂
😂
🔥
🔥
😂</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/Futball180TV/96316" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96315">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گل برای ایران شجاع</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/Futball180TV/96315" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96314">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ایرااااان زدددددد</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/96314" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96313">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گلگگلگلگلگلگگل</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/Futball180TV/96313" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96312">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/Futball180TV/96312" target="_blank">📅 08:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96311">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جهانبخش رو آورد زمین
😂
😂</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/Futball180TV/96311" target="_blank">📅 08:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96310">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پشمامممم چی گل نشدددد</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/Futball180TV/96310" target="_blank">📅 08:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96309">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بعد بازی قراره رسانه‌ها قلعه‌نویی رو دوتا شکم دیگه حامله کنن منتظر باشید
😂
😂</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/96309" target="_blank">📅 08:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96308">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">منتخب ایران بخاطر وقت‌کشی داره هو میشه
😂
😐</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/Futball180TV/96308" target="_blank">📅 08:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96307">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">قلعه‌نویی تو این گرما چرا کاپشن پوشیده
😐</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/Futball180TV/96307" target="_blank">📅 08:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96306">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fb07e42f4b.mp4?token=FBvxTzgw8lOKqklWI2FRxHIF6BKh0T1XfcvL33Tp9LaLFXn8lEZIdQFh4fia_pWMfQbWmZpm7RkeVGV3xix4ewUGGMqKPJ7eFYw9sRSVCR1mVI38_Qtn1J79YUb9obRtzG3XrVU3d-kFv_54_2CLME4fTNBe71Ucbrz3gHpWAeR1v6bfos5PianeydQ1GggQ_F-UgMnSuwJZtJ83lx5BpRIiyxtmVB9YDjr1H2SInHYtPP_BGxGxHAm3AKtTJZWssK6ee0H1qdfAPG2IjQcad3XhMt5N8n02LVuQfTxSL2_dx6Hs85Bok_hHryPMcKiBdakzFIwvqIzB0AtoP02nyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fb07e42f4b.mp4?token=FBvxTzgw8lOKqklWI2FRxHIF6BKh0T1XfcvL33Tp9LaLFXn8lEZIdQFh4fia_pWMfQbWmZpm7RkeVGV3xix4ewUGGMqKPJ7eFYw9sRSVCR1mVI38_Qtn1J79YUb9obRtzG3XrVU3d-kFv_54_2CLME4fTNBe71Ucbrz3gHpWAeR1v6bfos5PianeydQ1GggQ_F-UgMnSuwJZtJ83lx5BpRIiyxtmVB9YDjr1H2SInHYtPP_BGxGxHAm3AKtTJZWssK6ee0H1qdfAPG2IjQcad3XhMt5N8n02LVuQfTxSL2_dx6Hs85Bok_hHryPMcKiBdakzFIwvqIzB0AtoP02nyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌چهارم بلژیک به نیوزیلند توسط لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/96306" target="_blank">📅 08:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96305">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مصر صعود کرده کیرشه
تیم قلعه‌نویی ۹۹ درصد حذفه داره وقت کشی میکنه
😂
😂
😂</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/96305" target="_blank">📅 08:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96304">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a3fbcca7fc.mp4?token=sQYS5TlY9v0yd-a9K_rp4mBjFgSrQ9Doy7o1-doXTI8DNcveIdydDrIQ2ZSMucJHjyLjQ1SsWQeQR-WcvzsxK8tHtTPykrcOQT0-H1cznDB5PkeQuKj4WA5ISxAWTtpKo04tUOrSzWgVzutEvKX3su1IZ8FNRAJTHnXqRs8-9KJzw-08IVbUbyca4KxvUQrRD2jvCI2n-wVLKbnzGl9ruzUAGzOMiuRQxtTTVlcCZDWKOLBaG3MZcEbQoR-K42_e_JVG4MtKAtBy6AtG-A0wctBkVeB5b-J8jzTJFqLv8P7foytN-JGu-PC0lGeWSgJMmY5ZdUJhE4kZojXZRtwPhA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a3fbcca7fc.mp4?token=sQYS5TlY9v0yd-a9K_rp4mBjFgSrQ9Doy7o1-doXTI8DNcveIdydDrIQ2ZSMucJHjyLjQ1SsWQeQR-WcvzsxK8tHtTPykrcOQT0-H1cznDB5PkeQuKj4WA5ISxAWTtpKo04tUOrSzWgVzutEvKX3su1IZ8FNRAJTHnXqRs8-9KJzw-08IVbUbyca4KxvUQrRD2jvCI2n-wVLKbnzGl9ruzUAGzOMiuRQxtTTVlcCZDWKOLBaG3MZcEbQoR-K42_e_JVG4MtKAtBy6AtG-A0wctBkVeB5b-J8jzTJFqLv8P7foytN-JGu-PC0lGeWSgJMmY5ZdUJhE4kZojXZRtwPhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول نیوزیلند به بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/96304" target="_blank">📅 08:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96303">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بلژیک چهارمی رو زد</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/96303" target="_blank">📅 08:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96302">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/96302" target="_blank">📅 08:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96301">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سعید سحرخیزان، آزمون، کسری طاهری و ... چی کم داشتن که نیاوردی
😂
حداقل میفهمیدن مردم که بازیکنای با کیفیتی هستن
دنیس درگاهی رو آورده بجاشون که نه میدونیم کیه نه بازیشو دیدیم
😂
😂</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/96301" target="_blank">📅 08:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96300">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گلگلگگلگلگلگا</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/96300" target="_blank">📅 08:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96299">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گلگلگگلگلگلگا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/96299" target="_blank">📅 08:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96298">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ژنرال داره تشویق میکنه سربازاشو</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/96298" target="_blank">📅 08:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96297">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کارت زرد برای عزت‌اللهی که داره زنش از خستگی گاییده میشه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/96297" target="_blank">📅 08:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96296">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">طارمی از تیم‌ملی خداحافظی کنه سنگین تره</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/96296" target="_blank">📅 08:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96295">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA4ODseVkDInorJU6VhsYTqBrqgVXPrySZO0G-iZed1xcbyerhJPjg2xQIQ_a2ucKREx0Tsg_vcApBeER3qIiZ2uKwsDNfkt4Lt_b96wkoKkJeTK9B13-Y9BThW1PjrFTgpqgPkY3RvN91A_L8btSIU8ZvQZYtqp-xaUPHDywbvEkAN4GEqDMNqkNcfeJP96dkQ4ISUi_821Haq9SZdDnBv2RN00iKG7XhISC27-4W31u9xehz8Hjys0Zyp9d-iquiI0HcBJcSrOr0R-bOWJfYIS7UIj6lQm4jid5ojzJtAGDzqhzio41D426SRCJY2Gq-9_VvIaB_NSwMnMdU7Jmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
گویا صداوسیما هم دلش رنگین‌کمونی میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/96295" target="_blank">📅 08:11 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
