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
<img src="https://cdn4.telesco.pe/file/Lsv8vrJmWs7dCo4aRLyxfGyVD5RW8iMEp4i_borQ2Ow2SZBPiVGjf1v7ohb_dH81uHeMt0nH5ED9BoHADVlz68eo6Zdn5-sTrmRgUZ5qwQSn8iN5Qo0rxCaVYWC2Ass1mlWo1wAV_on2AE9gpmdl0KhtnjZQZBQUeKOSSTfAk_cTenZLT-Lu7BwfLxYO_heU9D0s6xt_EGcVSTuZIdWJyxhpSuLZrMFB1_bSpQBf5sMeODEfQCoKW7OphKUkzuy4kyCL58NJAonai93wkfIp1RAayTmb-3re09CV3uprefRQHlI2ZP-yJONn1KZdkmJXSXM0NK6EXKWhuXBFJajCqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 174K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 15:12:48</div>
<hr>

<div class="tg-post" id="msg-22823">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUlTqLkCFsKe39hHDOGyFmLD-WvmYlYJoQaTxNehfrEhM9YsDlD3OAjNlxI4aZOxQZfJZpY51OKkb_iXNXKeXXkqe-4_HprEgVLAm7odJo3tIbJKuZqqokMJXxSXR2Mpt5gt6N0n__x9ANeKTHuB7fVaKnIca8KZut4FUXZvZpj-XNn1Ehk2MKCMMNNcjh3wJMbERKTImZtSCKAKjJ2DOawE_dtNXCF17P5G4c1FRH_gbP-SewmrPE4PqLJfGJBORLNntSHwHQVwqf8ljYTgqdt2HlVWLXGRxxGaz9amUfi9ukDutqk9bPVhvyF4aGvi-lA77sAa2w45swTVQdHfAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/22823" target="_blank">📅 14:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22822">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoxIbxpO63KOHbQ1lBw1gXafGYDzXfL8l7z-UyTH2ahSeoVBmy7k_uoaUfIauBQe3yYE_9c40xeVsj2Hhk33eAHf4PNVeAIUcbNOyhsBU3QO1i_TGDwsU1OZe1nR0XDEe0IOe8yDjVXFKZCS8IXgsPzbs_x0iE2srNARVrfc5hiyuPwGTahf2ob9yZecx9klIST79SdGt2YMGrBxzmZp0KskHWeIIisvIbNxUL89SVpaYBjiWUcJyhlfIY1dbUlKTo0K22XIuYV0-JfOb_hE3j9NKR2qka8gWY8jqm5qIurZ8NHInXKyu03NKdn_F2cLxCC4lwqSG3jyk4Dznh3svA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22822" target="_blank">📅 14:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22821">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVGcYPkLYw4OJiSfSr4_1jNl4rJ6_VvSksr_zTnYxj7MRr46g7x9SwZyd4Ei_kAGWeBHQ33Zooaui195LH0jKnnSThtPj3NL4CA-ZxG4pMyNzZWdG_PahNfKiIx5yLbC5927v1Ork76odKAdcM7HTLX5N5QTcjhQfypy1gXPrEsCWiqmRQSJIqxT-ORyFc1TngtKh3hWn-c49eBFDtvtawij-ForHERG2IrTJkPRB_13Rf9brKxzHV-9rNGDtNczMsXHVIHFJ8we7xlsczLKoU1EHl5p94Q6PYMMRLb_1opyJX_MvV0TmR2cJ4faRyoyq1lJOrt67bfEhlArcJSxHihk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVGcYPkLYw4OJiSfSr4_1jNl4rJ6_VvSksr_zTnYxj7MRr46g7x9SwZyd4Ei_kAGWeBHQ33Zooaui195LH0jKnnSThtPj3NL4CA-ZxG4pMyNzZWdG_PahNfKiIx5yLbC5927v1Ork76odKAdcM7HTLX5N5QTcjhQfypy1gXPrEsCWiqmRQSJIqxT-ORyFc1TngtKh3hWn-c49eBFDtvtawij-ForHERG2IrTJkPRB_13Rf9brKxzHV-9rNGDtNczMsXHVIHFJ8we7xlsczLKoU1EHl5p94Q6PYMMRLb_1opyJX_MvV0TmR2cJ4faRyoyq1lJOrt67bfEhlArcJSxHihk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی‌از عملکرد خیره‌کننده لامین یامال ستاره 18 ساله بارسلونا در رقابت‌های فصل گذشته لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/22821" target="_blank">📅 14:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22820">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhCfUhG8IoNHkSTziJvhAVr6rCQjBQeRZ29bQJlDa00btF49NO9x_XKCswhFybbA1V6YX7Src6eWZ0h3iTI06OhTTSG10-UCClFa_U6Q2jFDsgXoayr9EEv6KRHoUj_ltSzLBUgoxhojU6BZ0cTEm6g5Q1p_YEGP7LNgvc-4fyz4XSKyoe2ot22gbvE0HfSEhrPmNfm4-JcuyixGk6rGgPScOneQSThrF8qGyNG7lOqq8RG8nmC-dsNKz3EbL-2svsFiG-DV5IpUyXr0K7mtwwkVGNYez0pZkGaz0lNyr_fPZiXBXbyOd3twcP_DJ-hHp_2LR2DT60TeEH50U6LqrzLo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhCfUhG8IoNHkSTziJvhAVr6rCQjBQeRZ29bQJlDa00btF49NO9x_XKCswhFybbA1V6YX7Src6eWZ0h3iTI06OhTTSG10-UCClFa_U6Q2jFDsgXoayr9EEv6KRHoUj_ltSzLBUgoxhojU6BZ0cTEm6g5Q1p_YEGP7LNgvc-4fyz4XSKyoe2ot22gbvE0HfSEhrPmNfm4-JcuyixGk6rGgPScOneQSThrF8qGyNG7lOqq8RG8nmC-dsNKz3EbL-2svsFiG-DV5IpUyXr0K7mtwwkVGNYez0pZkGaz0lNyr_fPZiXBXbyOd3twcP_DJ-hHp_2LR2DT60TeEH50U6LqrzLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
من خرافاتی نیستم ولی شما این بازی ۲ سال پیش پاری سن ژرمن با حضور امباپه مقابل دورتموند رو ببینید؛ واقعا انگار طلسم شده بنده خدا
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/22820" target="_blank">📅 13:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22819">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bpx5Ka55OW9YHQLCSKA2yWfYS86JGDwFjXhlgBPKgeZtu8Ttuwyeylhe5KM3vqzVRjIjphvAUNoSf2xCxf4VjnfKtz01ymEzBVAC7U9bHzb5FWBOUUGcPHFIZrZKH1b8z1cP8PO9-LBGO1z_VQUw3zIgIt0Hv0Y57TgyZryxokYy4zG98qy1RRY513jVzKLn0DrOD917pbkWguLDofoPfbFU8E_qgZEyDdZpOHQhGj3Xc3uR6g2rV8qCEAC_xuiDPBPosERErkWXu7YjZtbpXtL3Uha2ELRjAx_sR1jXJrd0BJ4Ss78aFUOmeFI-M-3PlDBYoqNRU6wY-wBgP2Vlzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
#تکمیلی؛ باشگاه پیکان قصد داره درصورت توافق‌ مالی باباشگاه‌روبین‌کازان، رضایت نامه کسری طاهری مهاجم19ساله و گلزن این‌باشگاه رو بگیره و درتابستان سال آینده با رقم بیشتری به سایر تیم‌های لیگ‌برتری‌بفروشه. رقم‌فعلی‌رضایت‌نامه کسری 800 هزار یورو از سوی باشگاه…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/22819" target="_blank">📅 13:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22818">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=C0G_EIxuFbyz8j2DRT1YTHuVWwpPaRBEaKylG_AjYG0ngjs5fE7iWr4uJh5TWZ4n-86xDJ_Qn7Zs7BLvINIJptQZqSnaSUhywFL-xa9a6pbRTqZhIfmbqqCxMJCOpssjjehmxkdYI_zF92mMOTm8sCSXmFzT1IzOz0qlVK3qMZPj58f1XJsqa8NqYnf0iJDl_h8ctDcigvp3gzCqvz2ShYacVTHJ7mi2otgdszxQhZfcdDXAMXny8fXVLx_EvyPtzGdPs_gsPWV5yVF1GrGyWQC5LNY5vSb_1HN4B0KAb5CPNR1bBA4izQIaFcXKWUAZhMzTi4GacGNE1w4q8hUj4FNDcJ64qMuHVWAmF_K-Uk-S5ZOIkpVebXSgUllARW3Nv61d7Xi1oaVh7Ocbi22pPu1Gkhb2TVbJxUYG1lcUUr1ijm0mA0diGZUFVBknw1ZXwrLlHI0cbDr9AFCbfHEcEoU0EB4BSJZkSgnOZrofip1f1TjrCBvP-CHKocMd1OAFU4oQ3b7OQSgkehwFkRvi6-trVWrGUQ8_xHow9w20N7jif_4Os25hKKFlL-tX6IBoc-7FE5RQXHyWV2A4PSjwUyo3ptkQVxQ-j0qQKlJvjy1VSVlrdZe5nLlroCekOOHlTYqSWTYDX8tniVB8GrCXUEPuaKt7dW0Eq9udSJkoEO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=C0G_EIxuFbyz8j2DRT1YTHuVWwpPaRBEaKylG_AjYG0ngjs5fE7iWr4uJh5TWZ4n-86xDJ_Qn7Zs7BLvINIJptQZqSnaSUhywFL-xa9a6pbRTqZhIfmbqqCxMJCOpssjjehmxkdYI_zF92mMOTm8sCSXmFzT1IzOz0qlVK3qMZPj58f1XJsqa8NqYnf0iJDl_h8ctDcigvp3gzCqvz2ShYacVTHJ7mi2otgdszxQhZfcdDXAMXny8fXVLx_EvyPtzGdPs_gsPWV5yVF1GrGyWQC5LNY5vSb_1HN4B0KAb5CPNR1bBA4izQIaFcXKWUAZhMzTi4GacGNE1w4q8hUj4FNDcJ64qMuHVWAmF_K-Uk-S5ZOIkpVebXSgUllARW3Nv61d7Xi1oaVh7Ocbi22pPu1Gkhb2TVbJxUYG1lcUUr1ijm0mA0diGZUFVBknw1ZXwrLlHI0cbDr9AFCbfHEcEoU0EB4BSJZkSgnOZrofip1f1TjrCBvP-CHKocMd1OAFU4oQ3b7OQSgkehwFkRvi6-trVWrGUQ8_xHow9w20N7jif_4Os25hKKFlL-tX6IBoc-7FE5RQXHyWV2A4PSjwUyo3ptkQVxQ-j0qQKlJvjy1VSVlrdZe5nLlroCekOOHlTYqSWTYDX8tniVB8GrCXUEPuaKt7dW0Eq9udSJkoEO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازلحظات خاص و بامزه پپ گواردیولا سرمربی سابق بارسا، بایرن‌مونیخ و منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/22818" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22817">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGSe_yr7L8gtPF5O5UB8hiKzidkSEtP-rHAWxADSQsRf3RkRmpDGDbzmv7OA2m3TaauCY29ou79X31SKHDGeLLokViAvCoeboS7BklryKW657VLHWw1ZmAAZZeKAy8Y9oXLOUWfrl9JMexRnFhh3TqzvPpF8U5pLrPd0jT99sv0cSqsL1CI-zqWtoQwSoXCQefIuSZfjrlcIon-BP32aYbcrE-Qgd0HidSAURpow0eQVNSaFIT4YifK3brib49XONq4mDjNOGZ90g4E6uZw2zfyoJ_zx31ZNNcL_Pn635Uw3U_EPm7xR0JD-rMEKvDOze3c8-eIOEwolzaj_zxyLxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/22817" target="_blank">📅 12:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22815">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=KkOFlYed8om7B5G_NKLAPxvuSy1DbuTNrH3hWp8OJbtT3dLBvNxtIuRC_PAsfW-rSYqzTSacsaQJpNZ6k2e1uAdTSgmZwguM4Dy2JzuAEejw_Act8tSn_2YOmmogiApk7etgaq_p4uuacBMCu0IxH_PQSkaDJuTiE7KxYxcpnJixVIil0tZpYBTSW72qAsrENSJaTMbqJvzqWeWGfyX0lrfuD8iDxcnqD9RQbLp_Lbyc1Bhjujb09V3GzK1XJQeC1y8VJVxtck1k5IFIDZpWpYcrSVOA_GyCv2oKpTuy2rX-_g8nTFH5fkt2SHgckBvxq0OGTuLv3y6xJmOnHwSodku3MWXKCd6hwiG8x9AHDkxxIf8XFBPLYN5uNuG6UW7vz1juxkWkr9nseNtCILIpz9rFUVXg29fZwUEcv3t8jVfcR1LTZAZk4iQNh4ZVazdW6ZY2crdypgVxQ4D12aEnE5l24KpVaMBTwf4GkfVDd5Lj9EK8-9-mKqu67dnSbLpg6EN32Tfx5Yjm8onFEB9B0dLkyttFVAEY2wVR0lSRnp0O9h9H-EL4lm1_gdM16R_OP3YeSrXFUolBrsj5hfeyV4esD6xQHWeQsF4li-mm8U8u1hZFSC-t74ImHR2RIZEl0_lHOMXKy7h991-YEebgYXg095DqIvziVahONaeP6hI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=KkOFlYed8om7B5G_NKLAPxvuSy1DbuTNrH3hWp8OJbtT3dLBvNxtIuRC_PAsfW-rSYqzTSacsaQJpNZ6k2e1uAdTSgmZwguM4Dy2JzuAEejw_Act8tSn_2YOmmogiApk7etgaq_p4uuacBMCu0IxH_PQSkaDJuTiE7KxYxcpnJixVIil0tZpYBTSW72qAsrENSJaTMbqJvzqWeWGfyX0lrfuD8iDxcnqD9RQbLp_Lbyc1Bhjujb09V3GzK1XJQeC1y8VJVxtck1k5IFIDZpWpYcrSVOA_GyCv2oKpTuy2rX-_g8nTFH5fkt2SHgckBvxq0OGTuLv3y6xJmOnHwSodku3MWXKCd6hwiG8x9AHDkxxIf8XFBPLYN5uNuG6UW7vz1juxkWkr9nseNtCILIpz9rFUVXg29fZwUEcv3t8jVfcR1LTZAZk4iQNh4ZVazdW6ZY2crdypgVxQ4D12aEnE5l24KpVaMBTwf4GkfVDd5Lj9EK8-9-mKqu67dnSbLpg6EN32Tfx5Yjm8onFEB9B0dLkyttFVAEY2wVR0lSRnp0O9h9H-EL4lm1_gdM16R_OP3YeSrXFUolBrsj5hfeyV4esD6xQHWeQsF4li-mm8U8u1hZFSC-t74ImHR2RIZEl0_lHOMXKy7h991-YEebgYXg095DqIvziVahONaeP6hI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
محبوبیت بسیار ارزشمند علی آقا دایی اسطوره مردم ایران و فوتبال آسیا در بین مردمان کشورش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/22815" target="_blank">📅 12:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22814">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM8fKmQVyit-M49HFdlYRRdpqnfvrcM43-GEf-LrC8T-f1B8514NYQN0eVOeZKgXOfZILMJn2HMV9feLaLjt3bKccuKkp3Ro6leBq-9j41aASuix8L8AdfL6esTcNLVPkOAQGQ-geDgoYupHEKSilxLVweZpGrNVInOzifBLnqSa88hLfb9f-YxifNup1-L2fT47WF-KRWKHGGSOjLx0M6CCDZXN7Z7icpJ5BJnaYaHQPDndZJ3dIEiQlQn9NWjN7YHNglrFKBIuGLMM8aWnhOoMtCY-TEZgBQ3rUDBUlf8MWTuNkFG57hBFMULkAT8kWR08mYDB1dhn8jQfaRr-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/22814" target="_blank">📅 11:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22813">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtK_YfCM9GsXk3BV42kPd-2YWk-TbUiz8GoQmjcs2jk7z3zVdA5XQK1szXPMWqkJinh9eZwDvx-BvWSfK0M-F1ZFgI6xV19c_CI11BEuYQN7dzUkQlN1EF7NRokr2uqZ0qiOZhH9I4WdMhXhWIHB2iOBDnMaCaiL0RrJQ7AjCK4tPZkgLiu98NFkiZhTF58eT5MR7hqvAFN1EfNvsQbuiSe4EATvx6nfHVEaS2XoleNlMrzHJznwEE51RGveu8kb-Hw8OFZmWWrpph70vjHSmdh4TW1k54ItYPIMqfPQvigEeA1nm7Gvv7-zDdgz1dXdlk3kTH4nAQd4dhjp8NtgDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت باز شدن پنجره نقل‌وانتقالاتی آبی‌ها؛ باشگاه استقلال برای فصل آتی رقابت‌ها برنامه‌ای برای تمدید قرارداد آنتونیوآدان گلر39 ساله‌خودندارند و سنگربان سابق رئال‌مادرید از جمع آبی پوشان جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/22813" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22812">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRMy5A_GqT_9cC8wQEWbp1UObmCC0Ige5bi0ndUJQFs3Hfy5C5vi3SNa2BdZK-F459oVuIKVhbGzrYuQYZh1YudhUMvsaaajE2hmAQJzepgiLnlHNbs6zzzlo89Q_gq6WfxtBb4OpjgliZlom2M-EaRvjS2jWUJcsEAsG3yC9gF2bTMu9AXcGApxpnhfzFtIvuNbREeR9MdlJXn_laz_4NG9dubIyyEtkLlOM2-l-gMi8qG3yTs0n58gmI4A2OFxBciewtOVYAuyqoanN_mgPwQCLXfPaBpn_m7tEL5U7iGpMDGiFC8JBqbdp48U5hsBCfrxG-IcmFqrvNXVI0bjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
👤
طبق شنیده‌های رسانه پرشیانا؛ سروش رفیعی هافبک 35 ساله‌تیم پرسپولیس که بازیکن آزاد بشمار می‌آید از دوباشگاه‌فولاد خوزستان و ذوب آهن اصفهان افر دریافت کرده. درصورت ماندن اوسمار در پرسپولیس قرارداد سروش با سرخ‌ها تمدید نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/22812" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22811">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚠️
خیلیانمیدونن‌که‌اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس‌خوش‌آمدگویی‌تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/22811" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22810">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcmL1slTDAoSIQcOEA_BeN889ocNz4frm-twDHD0IlBc3Mkc52ozW3wsRFTLDuScPewjK_qAdfjRRrsymBTrjVAbGadXVzdRW7SxiIxlPxJnKadZE19jTxuUJQXKMnPawCcoAR4uu99t4qrlKlMhBXGZTA-GOKvB9bZYdJZLlgGv09m2PMHGH4kZX6B_9Bgud6tb9Pd37RW8AiazQU281tgTQOM6eBGEJPmABk4oFd6l4ucOudX1w0A_txC_us1721spEojV7-pXqu9rMiQChwyuftYFRON7fUJCXK3_l_PzASqeS2FUEDlx8cP8_0i14vR3AVjhSeGLzjAxSokaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22810" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22809">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcmpzYsLJUBYrcGvfACiXG6ZL6xGcKGdmYNA5PBjcb4pqRKfuKFNnBAmg_Y7CB8HLyGzJE3ULFO0gOIIBUF_6aFYIrofwHViuK2Wk_htCFmHs_DgyjoCMS1ZDvGPvcAauEaJk5uGSSFRH0wf-FBzw7b_Bt8Mg9ayg62SH_-0-YwdMelKEAyu9hpqyPOphYdtm_XNBN6C2LqSH2nHDS85XyRVixtFnqsJ2trIqF3FnBPQp0l9g3DMnrlKe47b9J5jb9ofn53WnGIw_xWQjU9R4uYtnKD52gVSUDtLKDxwTV1GN_TJDvcwXMUmheP8T0XLJYk4zhMf9hbDSk4h0Cq5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شماتیک ترکیب تیم منتخب فوق ستاره‌هایی که مفت جام جهانی 2026 آمریکا رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22809" target="_blank">📅 10:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22808">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHw6CB8TEP17boMyUP2JuWXauXs8UaQtvRF6ktfTsQ9cQSB8s0QFqfhfifOqoiWkH-8gpup_VBjHRXGkMdzBlqy8MrHhXnS5m2Pfm0aInbeqgBEd50j6Q7LujDAwdf_0l8VngiOHiR3Qvl9KYz__p4CcpbokqHG0wpib-qpwMlOWD8NaUudpW90YaDir2x6Vk2bT865EYyB9MHmpU07qQbgdoOpgwB1PjmaNiyz9GnUfm56scI1thRUh4EyPpr7Ks2Tf3qjxorxhYXaAMdzWTyL9PejmpiyV1DFK4dGuoEF1iJBhlvFUvHPd-F0qTvhhtG4jVYFbxtM0POAjapVDTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22808" target="_blank">📅 09:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22807">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1n-XJRAuopI_ppvWLDhKXCjYXG228IvBK0gsv-KiT0Tz9AgKQRNqgEevCT0mEaD4GWMQQFwFE4uJXl-IxzPdrnoZzBmoo8aYgmicw22rf3UTq98aslbcUesXgOMzsY67oVK6SMMBBn25zI6ZpPrPUqSo1wtVhIaRHwXllb_nq3eMYKk2Ghv-631H_e36OvmMjETwBhw2tgalizmqgZYveFgdCxr5nwzwuMjOGfBYA3EGhSOLN0alFeNOBQieLh-wPUPlvveyOMr9wxloW6vM6XCNdpLECU3qy-zeM6YuWEUn89HZYkHpoAbO2-HE1_Awru3iAubdKd0isMFOVFS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22807" target="_blank">📅 01:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22805">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMbFNnOY13US0MfjIzLB7zS-y7MHt8TYpTeRzA2HaGS00IG1Dn6bd4T3-rpH3oL3HA5xQk1OVK__0lyPFf8HtaD85Df1RrboB2vVd_dlrgOfN_y8zheNo5kXCMgmABz722B-YFGq5l0tgPtAG_CAgiZXhGvk3LDfReQpAOlU2TN_UIIPLRE7wAQMOpe0e6aTE_KsXI6y4xX0cgIZ2EjzsjkfZAGf1OuLlKP4hp2O7IqGOlk6YTtqpJb3acYueAI91JZr1NsU1HLpNqhB-WlHOypOjp7iIt8P3QHZkh3qTHoOPk5ClUZ23_XcdcykYPPVeG21afyrOgPkLel5KiiSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22805" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22804">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo6tGIHDxDZQiOXSYa615zf-EcBUpgOUXisVB6aTyGIRUZ12XDDyh00ddMmGYov6iNP9qAf9nRuAjNgJwzwHFSlE-tFfnq_yHfhQ-wJ3syn15H1ap8J2Ezb1laMuSOJCkmXQhiNYR3ST6hAG2zNDViyj2rj2e0X6her6ucN2jJBjt8lBCHPxbh4iwt1TjykoPGzqcgNqvJq7nH3kKqNUDTt9Mn6b5CVqvTVcL89gqvbR1_IYiyHwPb-B0ThkP23bgSnOjapSeD_2uI2MvpFO8QCQrYNjJ-5KZvz5cw8RQ_rbv3-Ry6-yfDt7BXlnCdNl22vDTF2g-_vnWwBaSRki8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارهای‌‌ امروز؛
مصاف تدارکاتی تیم ملی مکزیک میزبان جام جهانی برابر یاران میتروویچ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22804" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22803">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTfYhERNlQo_48JnGMB38Ym4LHr9uIRfnv2_GgTXVUsNL5WXgpojte5LPg-TcbXcz8Yu6bnddbBdU3YWAI6Oid1w7i8p-XRZiLv6oOTxlPUEVZXHRoDfFOPDARkOhTxKN71kXcX4XtgsdE3OLtJyAQkV0OlRuKilnTjH3Pgfm8RCsUzhK2V_D_sJmefa07HA5ffR2jFOLj5E3mNqpIaIoCX00-hPwBGlxlN0aqPzeWh4vg1XdEAV6Rn0K7Fux3y7ChtV9wmO-iA6pK5YMLQ1cjYckjsJHPq5KbyJwpJ0XX5gjSL3IpsIYXs3rChlSCuFttHSCJCr6kOZ8j2-fEpU1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌دیروز؛
توقف شاگردان دلافوئنته مقابل عراق و شکست‌عجیب فرانسوی‌ها برابر ساحل عاج در فاصله کمتر از یک هفته تا آغاز جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22803" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22802">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgpAVBh-87OYR1chUbEVnFbpPZcRQFgEcE6CSWIaCIOUSPLRtefAUR-SvCVrt2wZ4_VtRSoyVQQJ1COeMi_DpfZloMeKEC0hWwMD3jUbEHnvIEO5Lmf3mmFWdvw1jnZeprgzPshO7eGGXsLDanrJey5Dl-hNs28GzSFyCQfJX-Ec6FXEmWZXoCtIHkaQYWWRGXNr12r0F0IhjBT73uMMLEGM1vepmk6jJg-JL4XaFzQOHo6vIZmVX4OSZnk-t87cIjseAvD4LiaGKhc9J8WrJdK3H5X5DphVXZhAbsgjarmsAAEcM6i_9D00u3ttWEtBF_EnL2-IKmSNSr2Wu5JSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکثر خبرنگاران و رسانه‌ها میگن منظور فلورنتینو پرز؛ ژائو نوس ستاره 21 ساله  PSG عه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22802" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22801">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGl8ew9Rk4J5Lx_WTE1-mu6oUbto7fYiyLkrhaVNmSLUeeVVNFG_b9z3R62PNw_DPlicmpW5srvAnxjP3rhEQE_EEV0RbBAp6Deo9P1mHzTpzGDoaMAuNWUFBcCWe5Oq8kqiuA2vJeYPkpZsFlkhgFa5dKBlXzQPY9Wra_ZdzbBfj5SJaVrNBtF_IEEUuCILUoz3TO393ASw8VngQ6LwjQBQVPvA6GXmexw4JJRTVJgFQpq-W3pQ8XT2WsvOaGwBEByjsAoYjvHiDmc5Bh-WrT04hXnYWGr_Rd5-Ii0g404e56awWO5SskJ6T-Uu11gQde4L1-QkvPuPVcvvlgY8MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینوپرز رئیس‌باشگاه‌رئال مادرید: روز سه شنبه برای‌خریدیک‌هافبک از یکی از تیم های لیگ قهرمانان‌اروپا پیشنهادی 150 میلیون‌یورویی خواهم دادم. کیفیت‌این بازیکن بشدت بالاست و بارها علاقه خود را برای پیوستن به رئال مادرید نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22801" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22800">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=vz3L8TZn1NFpnkg-KXd_fxQtS7jM5pYm9epHSkJPvcYvaM_Lu3kE253ndb-z9LXuhuBl7gi-mBl0ngT3e6mWfPzXxTpUF4fDDrqgJWyYcKv7cgGST9_JbWFxox85v7NKi_5lGxOXRtk0u2bxZTdRCKIxxCn26kK-QRWCZ8abbBQO67_OyaP2UmGjOI-7Uq64uG_QqFjFQh5eB7WqrfnfS7HODc0AGB_JqoPeNacgJFf1Q-zSlWeyrrmRFtgOn1MmSQCZgmAPakL6U71TUrzU6nK6PfhLcxLrmJMkQVymk7KuF70Cx0Mqs0brUhchECF7gn0DCTT3RySCYg49rEaTTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=vz3L8TZn1NFpnkg-KXd_fxQtS7jM5pYm9epHSkJPvcYvaM_Lu3kE253ndb-z9LXuhuBl7gi-mBl0ngT3e6mWfPzXxTpUF4fDDrqgJWyYcKv7cgGST9_JbWFxox85v7NKi_5lGxOXRtk0u2bxZTdRCKIxxCn26kK-QRWCZ8abbBQO67_OyaP2UmGjOI-7Uq64uG_QqFjFQh5eB7WqrfnfS7HODc0AGB_JqoPeNacgJFf1Q-zSlWeyrrmRFtgOn1MmSQCZgmAPakL6U71TUrzU6nK6PfhLcxLrmJMkQVymk7KuF70Cx0Mqs0brUhchECF7gn0DCTT3RySCYg49rEaTTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22800" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22799">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qx-QA1RzRd4sdWBTfFUeJY8_RMbVKIRma4MAuMml65MwC3QvcbjxTs4j28xVJ8LztI36pftYBdNTdoX4D1Pyge-539ZXsSoM_pvW9UR_PwQlqijECI2AOzVBiVBIG2ibNvrSRG6dQnHdXK6KGoB32Fe3d4dgfjEQjuSliJf4HfpEuMQ7aRq3y1Y19n-SgemdZQdmK0gR2KBbqQV239qEyPKgl7WECYYOac5-mjQX3t95jmgHknGFWU7hvOEi1PXvcandiAv4tY23Ice8Jls7uRZ9W_Bu-x1uKAFGCS6aed9Y5YrT5Ub5s7s6ZWhqS5oiJ5JKhcWovY7FNglbv1vonw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
برخی از خبرنگاران اسپانیایی مدعی هستن که نام‌بزرگی‌که‌فلورنتینو پرز قصد داره بعنوان خرید جدید کهکشانی ها از آن نام ببره انزو فرناندزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22799" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22798">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=h25VnbofPXMHdoLQIrzf4i_UiFi63p8qZqqnb-xzCGzDY1S89zGpBJXvJXlbCFdYCMPmQ76Lri1SJwHUdGQyedAuEb9yvl-YRf8LdT_2-StzEjQMbrcu0caBhmPzvKQpW2Ygi6aXnyM82aWHtuQUaZeYzAyWZHRwKmQWXn9OkI7MLuAuj-O9YG99RG_KBeL4266VVBVaBNCybq099B3UeSD9AU0_mTX5SPnL6yNATosqUF9i6sDcw9Zy3gxmr-hJ5F9EIP6xzOLzaxTNefAALJV9IMr7GPQy01AUPJbLUxTl7zutSnEYjvvLbp9ysXdr4TtkCoCX1Jwub521RpnTeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=h25VnbofPXMHdoLQIrzf4i_UiFi63p8qZqqnb-xzCGzDY1S89zGpBJXvJXlbCFdYCMPmQ76Lri1SJwHUdGQyedAuEb9yvl-YRf8LdT_2-StzEjQMbrcu0caBhmPzvKQpW2Ygi6aXnyM82aWHtuQUaZeYzAyWZHRwKmQWXn9OkI7MLuAuj-O9YG99RG_KBeL4266VVBVaBNCybq099B3UeSD9AU0_mTX5SPnL6yNATosqUF9i6sDcw9Zy3gxmr-hJ5F9EIP6xzOLzaxTNefAALJV9IMr7GPQy01AUPJbLUxTl7zutSnEYjvvLbp9ysXdr4TtkCoCX1Jwub521RpnTeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون‌کره‌شمالی‌بخشی‌ازدیدار کیم جونگ اون رهبر این کشور باتیم‌‌فوتبال زنان کره منتشر کرده‌اند. دراین ویدیو بازیکنان دوتیم‌فوتبال زنان نا‌گو‌هیانگ و تیم‌ملی زیر ۱۷ سال دیده میشوند که هنگام قدردانی رهبر کره شمالی شادی می‌کنند و اشک می‌ریزند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22798" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22795">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7ZjZYd8vcGxJuEk-TSpJEP5efLuiw-mAFh5NHV85rknKCspWQI4hDzNQBM93_H-5Zv1CdJhaWOF6xtwKg7a-K02Pl5KzFNcqHz1twmgPZEbQuUnfjAgM-hwUL3dA4wG8MFK9DWWL4vbM7MLCcfo_f4MwpiLDILfo1cMUMioMUECGYzSArp9c9YDQWAIQV1S4USlVYwGZ02eZS9J6VZwsT2jkDwf-W2pPn_-O9urFYe_oiBUZulCcD1nZZVwJmdrcFqU5uLa8RAv9UKb6gPat9Mi13f2tLBO2YcgKcXQ60bOfl-pEQfYWJ0KuCIJBzOfPCFyW_Uih9QEO8ON4NMNaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ نشریه کوپه: امشب فلورنتینو پرز میخواد یک خبر بسیار بزرگ رو اعلام کنه و ممکنه بسیاری از هواداران رئال مادرید سورپرایز بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22795" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22794">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⚽️
تیزر فوق‌خفن نایکی به مناسبت نزدیک شدن جام جهانی با حضور ستاره‌های فوتبال و سلبریتی ها
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22794" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22793">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUlU1bgPRjS-yrg0WBB55zvIZ2lH1O--B-_4ruZj1jMfzY-Ong-xkXH5Qraa-RHi6jSI6eIS4RwBQHBUfbywVvRcHsRfblsDVE8QaqFkql_NDXL3maj2_U8EVTo3TrY7P7HFEpH6Y4XoFIqi6SJz5z1aw2Ms3Enff-E2ZxL3wGZPGo-ySNZnaKkAH_ZSL9rIiqlKlqUlJNbkTgaVejgBndAG__T5RIi4_ZsAptz8Sbt5xLdaU7XZrBHaL1NbytGFv_WBLHMVSF9guDEmiMKo1ISwZmbwRwdVLrAY2gw71Pb1uc_cV3RHiaxQMRpmwh7cfraguOhcQzArg_sBKSZn-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
با اعلام ایجنت مونیر الحدادی؛ ستاره مراکشی استقلال فصل‌آینده نیز دراین تیم موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22793" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22792">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtseKqVpYRZH0G5IiwIccleucSs6ucRwak_PawnkdqdztsRkPnKpoeEVZGFP-48-N74sFMda8DIlYagczrcBztMbVuBppbdK8VPxcXsEi6YniR-ILWQaVauy7cm3hiozgY4Ysgzi1cANGXNEfonPjbTx0Pw5Lwds6_7oVqfWTY_tzZtxwDj7lqIxnDtGUWZOAKDNcf-JNjVSjHgFQ5dvKZz77hho0HhYe7bfHC8kbFaccpTJccDMZV816gItB-LQxRFDNvjoWy9zPCmq6_Vx3K2Memz7QaCiZvWdfrBzBXJHnkWZ2AwuWPDQFguO9XDmFqCrFTfSHWgBJTDqOH-4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22792" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22791">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPfovjBLJR6-dBfzj8tBc0URlBc7wev1n7DEC_1zPbDfy5Uw-yr9KkilTv6uCoiwB0QFUPufkbiXdDrWJumBJ2t_vwh0tqESMHngciGKKd1sttITf0D4G-1t4nkjS-BcARwe11O_hWSqNihZvdgBYJqSBqEJYqpKNHCNf-Jim94bkQDNKkIyCGOkbsC79ep3IBIrhmXvyMeKm0hQIfXxf0VyUfSZ4GPHYX3JttlFYZdBtyc18jkAaLkXH_JIY3UrpOlWxIPoq8ASj8ObwyVjp5u8EbcSKdTaPSbKShgVZUVocCEHxW2Fg-GYPjRUTKN1Q8uQovGQidfWOTTurGReEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین تیم‌ های تاریخ رقابت‌های جام جهانی؛
برزیل با اختلاف در صدر جدول تاریخ این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22791" target="_blank">📅 22:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22789">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YHvBUYw2CYBkH9dODRAI2dNZ3nVTAg7mFnAEU1BTeVtq3-IZKZ2lWNyt6YJ6af7dtEUyONALFbpH2Sp8rIsT1ClnoSerq138y0HlKZeQCL9LA6oL14ZwVtEyymgum61pw_tF7XJbe7ySsIQ0z_MR33NDHNxeFvSr9wYwGIAoUddmQQ68Ixn-VNgDIn9scbbCjhJnSd0wWSQ-A--Fz1uJCDHj3kWqIThkLjQuiJPK5HsCBzLUzsbGXFI8TKKSmXceMQEJlVNJbHejSZmNCQTzJ3AdrIjeWBROhA5SO9GaSd0rJWB4pGBGQk30xCGFsTxY2LqoAxaQeucGEG6uB7-1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQl9X0R2aaISSJuBrMtd0FKYt7NzxAoHZuP9h7xOQw4pSzsSHm8oeEqVPd8MRJid0lgQvmz-3veF_kcZg1mUgZtUc-nHcOcB0a-qbqrec4nqTHf5pFWp-TA10qXhIcJCa9xml5Db-0zrPz6ccwaO5FmwvleFWdYvrB7PuC_GMXbEHoqjrlYrxf_hjFbtucwpQ0cGu1MkVIjLhdBA6xwrS15_IdSnZvCg1hF9nNmW3QQpjy7t7tLOFEvRyAySOd8P0myEsJIdMaoCBuDsnKD781tRsOp6owNiX0n5Dy5kiwt1dOvQI9D9Ruvgop46YnHdvrcblnHyfxIbrGdZX2Q5Vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو: آندونی ایرائولا سرمربی 43 ساله اسپانیایی با عقد قراردادی 3 ساله رسما بعنوان سرمربی جدید باشگاه لیورپول انگلیس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22789" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22786">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=OqeUJBLvQ8MwOOVW_GoKKIXHJnBpKPJa3ORkFVv4DDKmeZfKreRv-xGog8uxGWZmMu6wASSorCiVc_CCI-c_zaRq8PfLUY9F-priBY9wpdeI1c9X1bh8cSAWBmBMBPsyjqBmyrm2pAvRHxthyLBooimovAs8quf2111uP5d9y8WzFvb0AAyASpDj6mSYJS_pOBU9pfkANtRRzgGRBPrK6EjMAcnn8zEV02EzeQBhjMNdLz4d_8zJ26sQHE1RwM9x16_U-9Gm5SILfSmGvM4m7DDkLUvXV0W891A5Vac0JVXpuRp0WbIgBt_zZb_Y9PnEW2c1geDolikaFyw96G3_IR7cTUN0nX0dbhzEY6iPxm9ovc9hmm-Ad7_CGKpMz3gkz4JZMdPWfy3CMhWWm0WnL69IPCeec4vCsw7rdaY99r15efeXjy94XW7CZu_bRW1Qn6PPOB7RqnwrWu04vZMZFON_swAl06ro1eLfLs1qYjyk7Je2Hpg_MRrfNVeo8TphG1X3kPBqDmw9Q52rKYQkMT3S0lzw9XYTSy_eTfi5Vw_EU4L0FKU6ymvUBHdR2yLr0l2Uoim9YXwSXgVWLIAWUBMtuFFLcfBnCCS2Jkb--YIJkwKBgg7tbeMintMo9mO8OOhsaw9eXL9YIE8WmZLozunwp3TXTDPYwlKrsnQKnf8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=OqeUJBLvQ8MwOOVW_GoKKIXHJnBpKPJa3ORkFVv4DDKmeZfKreRv-xGog8uxGWZmMu6wASSorCiVc_CCI-c_zaRq8PfLUY9F-priBY9wpdeI1c9X1bh8cSAWBmBMBPsyjqBmyrm2pAvRHxthyLBooimovAs8quf2111uP5d9y8WzFvb0AAyASpDj6mSYJS_pOBU9pfkANtRRzgGRBPrK6EjMAcnn8zEV02EzeQBhjMNdLz4d_8zJ26sQHE1RwM9x16_U-9Gm5SILfSmGvM4m7DDkLUvXV0W891A5Vac0JVXpuRp0WbIgBt_zZb_Y9PnEW2c1geDolikaFyw96G3_IR7cTUN0nX0dbhzEY6iPxm9ovc9hmm-Ad7_CGKpMz3gkz4JZMdPWfy3CMhWWm0WnL69IPCeec4vCsw7rdaY99r15efeXjy94XW7CZu_bRW1Qn6PPOB7RqnwrWu04vZMZFON_swAl06ro1eLfLs1qYjyk7Je2Hpg_MRrfNVeo8TphG1X3kPBqDmw9Q52rKYQkMT3S0lzw9XYTSy_eTfi5Vw_EU4L0FKU6ymvUBHdR2yLr0l2Uoim9YXwSXgVWLIAWUBMtuFFLcfBnCCS2Jkb--YIJkwKBgg7tbeMintMo9mO8OOhsaw9eXL9YIE8WmZLozunwp3TXTDPYwlKrsnQKnf8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بمناسبت شروع رقابت های جام جهانی؛
بخشی از صحبت‌های شکیرا خواننده مطرح این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22786" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22785">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=mcDxUS9VmcBMI2NCabO29ZJpQ_186VGdgYNHBmb1lXvNkw29iwkLpehov9L-Jjx2HNgsU8_FJVvm6OA3W7Vs52gnxEKXoJnXiZP18lhXzbcYiJcmK1GTS22UXHemVEoZgLkG3VUqWyYETVyjNU3Ss5C0ysL1-E_-YivMCsEfLrj4wnc8nGNSDoZ5Uf73EaCMjRwV9rZBB682vJ292gc0Yy3gUfteOwurAYEaj7uW6FUW-UlFII4KY-LbRjdAA9VEFcJKhz4crqSZMtNwwzHICq0_ZA9_etbA3YhF1NuA_YCY-5bVgFYo7Kgm7a4GY2Ey-IYlJXH_s_BJA9ZqOYOsUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=mcDxUS9VmcBMI2NCabO29ZJpQ_186VGdgYNHBmb1lXvNkw29iwkLpehov9L-Jjx2HNgsU8_FJVvm6OA3W7Vs52gnxEKXoJnXiZP18lhXzbcYiJcmK1GTS22UXHemVEoZgLkG3VUqWyYETVyjNU3Ss5C0ysL1-E_-YivMCsEfLrj4wnc8nGNSDoZ5Uf73EaCMjRwV9rZBB682vJ292gc0Yy3gUfteOwurAYEaj7uW6FUW-UlFII4KY-LbRjdAA9VEFcJKhz4crqSZMtNwwzHICq0_ZA9_etbA3YhF1NuA_YCY-5bVgFYo7Kgm7a4GY2Ey-IYlJXH_s_BJA9ZqOYOsUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
جمله‌ای که تمام راه‌های فرار رو بست؛
فکر کنم‌مهدی‌طارمی هم‌این‌ویدیو رو دیده بود که جوگیر شد و به میلاد محمدی گفت بره مقابل تیم ازبکستان پنالتی بزنه، که البته اون پنالتی‌اش رو خراب کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22785" target="_blank">📅 21:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22784">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYH0ZtY0HJVgTjPSjSgbiaBetCzzzcGaTyYSZkR5U8hThMn84Onai4Om9OiMXIDZadxX1wTVShwWswHq2L471Fbe6Bzh_qlQSvHuxC_hZy0x_xJK1LAlFd2QE0y0ZVX9tdt0r5ymADutDNxnSXJa_TY3SxHbXluWuOx2wg4hzkE3jpaitZ6OUZ0dg6XbvY-0x5vR6R---_nPgERTt42Qttk3ZHNSMPe10UiHb4lg-6-QYMqN016iLU5Ea8-Z5UTo8OJyIJFoNIFygUxOPpdMu-IbhK1z7IzFX9XeGz67NzkM5rNlvcAqD6JjnA90nzwOr5Qrte8XLHaVEGp6u_qlCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22784" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22782">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mW-QbAj3midvd-7Bu1M6i7J8hiuN7bcAKOJBvdxOw3I4NIaMTGQwIuEziu7hi8U8jsnJtwMchSHsi2Rs4q_V2B-YdsH04uoTQLzQgYFIZ3Ny9ulHlTAmq2fBCMBw0RvRGmu4iEpIacF10hWDVahVPtQualCfwd5vfISvDl_np9VhznTR7Gxz91GjV0OZno8-RImey0x6tJKkm5Sp0SOwTQo63_r5kUzaPBQgCITS5gO-jhBBzxLBLfe2oiqYN2moF2ugIt7D7y0EKIfgyRs0LswWx27xVZcVUiOxu96p4amOeGeR0HW7hlSayAuZnKC9TllTVCvqlfsGNUU2iZzLeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdR098J30fM8N023ojrBuaTjs5TmL5Q5NevaMyJ9s6L_gHr2c1lkUWBHcOnhz1uiGrUJhvMHtkBT6cUkdya6EAf_A0I0ehdZHIc_pzeO8qOprw7djPIDgPURGRNDpNC4G5tOKg3UH0hC6FYfc7dYy4HQyzs0isGdy-ogQXcYZ68ymHOoD3kaP3eRFXXFxgnombJdfIYpRmr1ycs0Q0gdqfN7FzbySq2JMVCg-De9SaSLSM3fOBndGazhrqqZlLkGzbCcNZTsKbN-2YjHsv1dlyFylgmtN3Nxm5wqwiuCe5Vl2wwHnS0MjdCepIAgn-OoVeplYx2_NjZKG7JAjzxvKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22782" target="_blank">📅 21:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22781">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_niwseyiICqU5LkOxLoi_zPA9fSs47Pdb0uc4QW6hCrm--NIzRaOhVycgpXz0ccfMhpAnBA65ReVr0Stz8AKQDdAQmtKIApcLsOxhWhrFNbpBWXCT3eN3_RlzVBO6U7vdIOLkVH4CarRDhIQh28uiGMHdxKdVLYPg25rh73HeOc6IOXy6Hk3RdyAXsTY7ZMAnD_DLlqkIFWW-rpx6BdIWUWv2O2q6rlK8ruJXBmlc1tYZmc07BsK91p0m5ch7bhWJZG8W9WLzSb6jriymlcg-71rZXnYH-2GCnIirgZ6bcevsOXwx9sk-wcmMTIP2jFu0uiCTKAyR0rsP4LrMoYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22781" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22780">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkXxKOTECmeE7AnqcsQnEnnmknpc9lI79sn8aw_Db9peRypL_l6C4ZW4BjRKNpbGxiLjCH10hTX6DccbY2iyfzkZ7kTIX3G6eVlDjC2uFCGRwmAUtdcyr5om-Fssd9ExxBuxgME5PY5l_rfMVnaqXLiNNDozG6etEpINMJx5aku8XmWB2RoQGILQZMXVf_tKLeurWUL0syzoDfyZ4q3BBvQMld9HyPIr9JfwLK5dHv8LVIZYHfnR__cggldeHWsR6O7_wPWTUnqFCVfZwzQti3CVa9DyqPJBLqHjHKDw-1yFL2QPRKoW_aqXbGh4MPsAcgEbUjf46vreftvwfzVsRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ ادرسون سیلوا هافبک برزیلی 26 ساله آتالانتا با عقد قراردادی چهار ساله رسما به منچستر یونایتد پیوست و جانشین کاسمیرو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22780" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22779">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⚽️
اسپید با انتشار آهنگ جدیدش برای جام جهانی، هیجان بزرگ‌ترین رویداد فوتبالی را با انرژی همیشگی خودش ترکیب کرده. اسپید که سال‌هاست عشق خود به فوتبال را به نمایش گذاشته، حالا با این ترک تلاش کرده بخشی از فضای جام جهانی را برای میلیون‌ ها طرفدارش زنده‌کند. پیج‌رسمی جام جهانی هم اعلام کرده که این اهنگ در آلبوم جام‌جهانی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22779" target="_blank">📅 20:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22778">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avqW2ljC8ZuDboQIsayoNUZhVS3Ui9gtdBFJw7mF_Imp3ihs9M-DSQhj1JFVGkcJO7geOIe81RqHiMzY-fr8dySxbdbpV6JphNo2OpLTG77NeAO87aFoZ_xFVqsyRtlSqr8s3h7M9ytpBJbaSG7VPspt2JY-R4BoDHM_35mKbJk8x1NUhuYS3vLUFaILfwTwtDG9a5O9zrkKICWXU0ik-leu8O4dpORhfmC0b7oEpa7C5oI1M59FQ0PJqLsWVWYkzCgWvBeO3n-HGTpLk0kRzJYLNF6d8Y4Zbnxifl7VE4LnmDOfEd8CyFb6NPfLYrRfkg8OTzzkg7psbVkEQRsZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22778" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22777">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG7vIWem1qnn3IzCccECYQYjwK4OPXkd9Q0-K-ghTyNxfNZjWc0bM5pYz_bj5qwxrbh7YhqamOzs6-8Z3nZK2PH8xlLAyFWrXoI-3t5CB0BxsLeDxb5crFumhYdd3dSRaljacTDYAl-mdwoOFRtzVoS2fGUCOPreixdeorrSEqq26Wb3QwO_Lvck2EIA_bcE_m-TNEB8LLHBiJEBWdnjaH6pLdq3EQFjmxB7pDu5AtQp-_YFBpZppzn0MPlgUZjPqoqU0aigcZ1I8xwGAZ7m-JQP5dKUudniQbxrg5SqyscXMlKNfoQVCt2_-AYwTQ-BdavM8W65l0d16FsIQZ4-3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22777" target="_blank">📅 19:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22776">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbDEPYpZioQS9H0fE8O2HmzRpRcZ7mPsdioxF2w2ZnMZEu2WX2II_u1i9ZBfbUDkDiweQmT2P6e34Il5SU2WYhoCCIQF12aLGcOGHrDJALwaGJmvxwkR1jAlOm4wvz1ntH9rlmjr4AmJtM3Xlm3iUa-EL6CxKvxUrqG9EIbFRcK8NDBFDLKnDnV7WPSHdMhoE0mU0tv3hPBjtlwvhEsBskbVdOJn0P-_5mDPZFTGd4zb3K3Lizx1muMPhlfJdpVi5SbD0-p9EaG6I-k8jYIgrcV4OddjU0uiVgc9tcNykkZ2PYdE0y-bAQQ9MpZ-vv6aBlF2qKSk8yyBarfVVI4CVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ فیفا تا 15 روز آینده در مورد باز یا بسته بودن پنجره نقل‌وانتقالات‌تابستانی‌باشگاه استقلال جواب استعلام آبی ها رو خواهد داد. وکیل‌جدید و ایتالیایی که علی تاجرنیا استخدام‌کرده به او قول داده به هر شکلی که شده رضایت‌شاکیان‌وفیفا…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22776" target="_blank">📅 18:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22775">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW5FEI0Vj10UNfunk2hcU6Z5Yx5S9-LFcW6gYcBRvb-0lWjWCfMvfWjhwQZb5OnYBqP4zH5BF853nHP6cY-wWQ8lup6nHgrm7BI2HS0_6KRIzCSrRBC0jS7HsMCusnNAdCitGCMT07JkMGRZjysbh9ZIWOx6AAWXGP4wnmhYgQbLjFqgSxwvCDvZFhM92ND1OvgW3FPy-GwSfEv53pT2yHT6v00UcOmERnDIxlq9PgASG-5TP9oWDRVT2p9C8J4SI-v8rrcRH7JmqwTW26-f942p0F9ZTvvCKEEXHQY7SHwEiSE0k2O2aPXs92QUqtETf61C7E2-HjjSEGgJMNMEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22775" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22774">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERgVKPylVLtMY3WqYpW6qWjLRur8Xygi6M3092uI9zLtHXfm0t4y8T2CSxIBgQ8Okgp0BQz0OshmRtO8GpH3V6xbUxsmYPmBassTmGTT_SvKhF1kvR8WtiukRPzog5tq9_TFdrnVTQCnk9g1QZYZYB6kf5XUn9w1brGYnDxX5Nc4GsoJXrgxtmUsfjkwpCuKjr_30yuSv_gn-kOlW6Perx_1stcqx_zjLAtVRCUmAc7lBubAnIcjdeKUFVr4jpxQqfUIJRiqLVO25YCyaF4jNf7MhwlovQ1NobU20ZLQ0mWruqLBM3IELH4Ygh_t5l8N8UPptZGjuJpbHlSUcoD8Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22774" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22772">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c00997812.mp4?token=QYIRbCPPw4rLmmEcnSnRO_c_D0pvUQwVDGDxWIAvVfwRcf0UKArj_OXJqv3_37wNg9hfmSVzb9Hs0UB_4_yK3upEY3fs8xFKEWd5sDBtYivLFmYmrnijvVoNwYaueSJtPdu7610hBlcBgIIMkfh4F6XUwDpdyzjclYcRYUrWON9h6H6rRWWCoP50u1DgJ8BO-apraVJW_V2m6J3pMngm85wAl0lmN29zlOSh95geUlxn4tLIl81DZzKi4RN-PonzsoPqgWx4FFCWCdmjPgOQM4a2ToDqijiYhhl1H5Hrg03P13w4hg6yWadREk2AZODHpZvp6nY4KMJXvvxodhEGHYvL_QPRHWweuleRwtdSr2rZ7Nmg9NBWnlUzpIGhvr709lF4ouEJt45bbwkF3eDYsaaCdFqFfbEQ4GaWN3_ONBI3IVtvUcL68RLymChEZnQsYWvG8wo2OUeKW9Zr-qjMfZ0uAByJUo9_lo6KE2DVB3ZKWrS64Wh6FO8raK6uJoxa0k_mfBBobeONcZw2_TLnLztU7K9xFzWM5hzP7ypP8rfkxzRzjNqffjBASACsbo1LTgt5wN6f8pRlxXBeXrguWEx7rRV3BZdpewbEybhv7IGmS6D_-Bm80Tc77DaOeUpfkpXUmBenYy5NuklDy96No13GlAXToEohFgab8vz6Rrk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c00997812.mp4?token=QYIRbCPPw4rLmmEcnSnRO_c_D0pvUQwVDGDxWIAvVfwRcf0UKArj_OXJqv3_37wNg9hfmSVzb9Hs0UB_4_yK3upEY3fs8xFKEWd5sDBtYivLFmYmrnijvVoNwYaueSJtPdu7610hBlcBgIIMkfh4F6XUwDpdyzjclYcRYUrWON9h6H6rRWWCoP50u1DgJ8BO-apraVJW_V2m6J3pMngm85wAl0lmN29zlOSh95geUlxn4tLIl81DZzKi4RN-PonzsoPqgWx4FFCWCdmjPgOQM4a2ToDqijiYhhl1H5Hrg03P13w4hg6yWadREk2AZODHpZvp6nY4KMJXvvxodhEGHYvL_QPRHWweuleRwtdSr2rZ7Nmg9NBWnlUzpIGhvr709lF4ouEJt45bbwkF3eDYsaaCdFqFfbEQ4GaWN3_ONBI3IVtvUcL68RLymChEZnQsYWvG8wo2OUeKW9Zr-qjMfZ0uAByJUo9_lo6KE2DVB3ZKWrS64Wh6FO8raK6uJoxa0k_mfBBobeONcZw2_TLnLztU7K9xFzWM5hzP7ypP8rfkxzRzjNqffjBASACsbo1LTgt5wN6f8pRlxXBeXrguWEx7rRV3BZdpewbEybhv7IGmS6D_-Bm80Tc77DaOeUpfkpXUmBenYy5NuklDy96No13GlAXToEohFgab8vz6Rrk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ترکیه پس از ۲۴ سال بار دیگر به جام جهانی باز می‌گردد؛ تیمی‌که با تکیه بر نسل جدیدی از بازیکنان مستعد، از جمله نان ییلدیز یووه و آردا گولر، هافبک رئال مادرید و با خاطره شیرین صعود به نیمه‌نهایی جام جهانی ۲۰۰۲، وارد این رقابت‌ها می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22772" target="_blank">📅 17:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22771">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMKNGp7fJkm2oXtBl8z_N0WNriR0j7R-tgSd75mu_HNztEZqYwK2NZF6zdXp3BQByuHmgM_uMRe5crpA7graZ44OirSVGBs5_VnY7CGrhun4n7vm842IPyzBfGDJ09haqRWikrXT7KCh4P9Uq2syosyRhfV1UxaK7SjBpINju6XNTNsjHCV9bFC99gFdw7LAvSQriICqNCIfhFB8S8ypP3obk0xnY_qL5EpN0VuklTiciX-Tmjo6tL03r8He-F_2k_n50Im-ciILqPLXHzvZvxBuZyYjjsMvROjsV9vvMx8B7PrFc3U6T4_slNAqwXWviIiRPDJ_RgW7att644q2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22771" target="_blank">📅 17:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22770">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=lqhw9cfMVgCoLX-6aKyJfZ9eboTYnscyqv3hLMxeIKTvN_2tkHRMj5d01VATvrhf7RcRqF9yzr2I9ohe5Q3TP1CNaEX2DWwtCycv8K6cEBepsNDqA4p6nhqo5n15-eA5FREfuGf60SVmI5U6oH0e7JL8NQewVlAKIqGVlCLZIsQ3VoHnxEoFzzsGy95rnHgA7kwJ5sV62w2b5MCVNw6qwpHlfRAyIWEcvAs5VyeWlMXXCBQ5ZCeJSAjvuBibBbpcAd5DQtd5Rff_AtFhSioZs3aXKI6h4f4_O1QbMkfrhj4D9nXNFKRAiP4K_M0xnVr0EdE6UTYSCdEHrKqwkjxlQDb7ileqJELHqdlOHax373i624HcgHESYSBa4PgUFs9EGnkuL1Ze38f4tXjNZvjr_MCCxDQxw5Z3FXNlf_r_Ch7wYJ3-iRNoqqV0nQRdzwTkTmN_1X_qEt1AmnXBY3ObKP_dW2jyMvZJMVLGEncMH8JitJm_-NezF0MgIWkQ_Q6LP-myE6_Lid6Tzp73wqwbZr3jXvhBrbshnnsXZGr7Kfy7SSi0LaYHD7PRqs90v5JDkcxiCmdE5jsgL6JWVOHfcnTvqQp5Evr4HKNzCwvJ793PDOWarpu7nVfuwXo8qetP2HH19feF3E1489P0xivjjO1Ocyu-bJ-jhc_HtN4aipo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=lqhw9cfMVgCoLX-6aKyJfZ9eboTYnscyqv3hLMxeIKTvN_2tkHRMj5d01VATvrhf7RcRqF9yzr2I9ohe5Q3TP1CNaEX2DWwtCycv8K6cEBepsNDqA4p6nhqo5n15-eA5FREfuGf60SVmI5U6oH0e7JL8NQewVlAKIqGVlCLZIsQ3VoHnxEoFzzsGy95rnHgA7kwJ5sV62w2b5MCVNw6qwpHlfRAyIWEcvAs5VyeWlMXXCBQ5ZCeJSAjvuBibBbpcAd5DQtd5Rff_AtFhSioZs3aXKI6h4f4_O1QbMkfrhj4D9nXNFKRAiP4K_M0xnVr0EdE6UTYSCdEHrKqwkjxlQDb7ileqJELHqdlOHax373i624HcgHESYSBa4PgUFs9EGnkuL1Ze38f4tXjNZvjr_MCCxDQxw5Z3FXNlf_r_Ch7wYJ3-iRNoqqV0nQRdzwTkTmN_1X_qEt1AmnXBY3ObKP_dW2jyMvZJMVLGEncMH8JitJm_-NezF0MgIWkQ_Q6LP-myE6_Lid6Tzp73wqwbZr3jXvhBrbshnnsXZGr7Kfy7SSi0LaYHD7PRqs90v5JDkcxiCmdE5jsgL6JWVOHfcnTvqQp5Evr4HKNzCwvJ793PDOWarpu7nVfuwXo8qetP2HH19feF3E1489P0xivjjO1Ocyu-bJ-jhc_HtN4aipo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22770" target="_blank">📅 17:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22769">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7bZWZlDeWEAIInZhYlmUDSFFYcbsYYRLGgGr4DWXKnrCN5JidpBDRqEVYtcobQ5djrOy5Zz7KdMfXC_sTuBLRv5WMpxVVxg0S3y9fBfu1KeAY5WHrNcwPmESFJuwR9KUt_IDnUca6sDe2KBYr6qZR308UY2RPrqctVgPoI6G60LTBgjYft8QKI5Yik9pkdJKuG8b3w2c9hFOr9CzcSGgy7lccoagKw5UCV83o5LILWf5zO1jYz0S7LrB0QeDCAfNbNLKAaAJWw2biDyVVbP1onoe3SgV6WSFUyUJq4Nir8SK8vRc50WR-ADR0l6-VErBHQheogyjkEoYq87x9uNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22769" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22768">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhz-5MXXzTsxEuLdmbRKQPXpzh4k749kE64RNVKk6BhLZkh0C7Y3zN5ZVKDC1Nqp73AfbEqqsWgVEEwB3uuUXjKdBOUjZR7zLCshMwlQH7ESkx3le9f1j717OG81lvi_APCyRyN3jtDaPFKpJXFghR4urRYogN8QB7qImEXf8qF4hjh0J_zFfmNYrTDn883Af0OYU6SkfOXjGl6FXOvSMgWrK_g6kPdGm-stLDlGDsG-w0OcSdZr8HRQi1T5TbMlI0eAfgzRBwMLjAWVbq4GT_qmFUi2CvnMQK3-dWr9y5kMmmbIBg-WtNxoZZOb6ZV_M--Q2WX4GTLyyXKij59UhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی 30 ساله استقلال شب گذشته بدلیل‌عدم‌پرداخت‌حدود 3 ماه مطالباتش به‌باشگاه خود نویس ارسال کرد. هلدینگ قول داده تا 72 ساعت آینده 250  هزار دلار به او پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22768" target="_blank">📅 16:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22767">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jp56fjn11wwbKRnQObgptnVDNPDDgzKDOTZE4yEC43wGR__BCbAFORfIAigGgakP8L-qFkGYAhkYViqwXeYNIfBAPjgl12NCGIJlE-VEXMH_Eqaz-8heew1WXWnAGfFUa3vg1YtsEK4vEw3MfGWBdopi7_A0rS74Ckd8eB-669QIWeLFRuwhmC9SmlybkO4D4IMO0VHUs-kcnM6yr68UJGKup-pFkbLUHu_KDJVuEFeZNw35fCIrb5Y0hjAG1Ed45zvbpPFfde7-BOgNDfv34xTeEjlQ8EhK4NinsuDxw62qw7ch59fhqWXjUzqY4mpRte8JHWMd_TTHCxu5pfN87w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22767" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22766">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOuq8TGrhMQNqlO5Sr2GWVQz86XYUfNRV4zsU8GlZDzZbRyvGCDOhA6dN4lkTfMaolv7nnOSr3GtPU8VdxIJ2SWvXuIX4Iba_YT33pVrGSIHbh6FLevLmMq3SbrJrMJ5UeH7RtfBV9QEpmnK9A2Gv2RTwBfcSgB2qPaa0_rAJNPcsHGtHC8KvMwt86zw3D8C5YbLmi0WUMCXzXSgGpaVmExv9K3-1rMjawS8piTqvQLNDR5HUiPuwPCrqOng9zK3ZLpSC-5HsDiT3bqCtwOWP7IXOpeP-pw08tzPfCQaqXlXLuTL0fiheOZeFl0tcqh7v5i1sBvRxTCtzlRvw-Gqcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاوه‌برجذب‌قطعی‌کوناته و دامفریس؛ ژائو نوس ستاره پاریسن ژرمن و یوشکو گواردیول ستاره خط دفاعی منچستر سیتی دو بازیکن دیگری هستند که هفته آینده فلورنتینو پرز بعدانتخاب‌شدن بعنوان ریاست باشگاه به تیم رئال مادرید خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22766" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22765">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔵
مسابقه جالب بین کیلیان امباپه و نیمار جونیور زمانی که هردو در پاری سن ژرمن حضور داشتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22765" target="_blank">📅 15:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22764">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRtFaSBH2qkpkvwZOgwDjfvg3Wpwsv0qHgolxt0wlTLcVASaqfwTGCcLWjsQM6kiZ9gNPWBLBQ8d16R7fNzbc877D8OFEVouESFlwIFMZudCMPlp9_zqjxYIEsZwxW9OypQY3-2Lz4pdskoK1xMdh73MHbKP16aYeGSKCE0KctMNIiRdFmvGV1rNWuW3Wkg3gVK3rsNTVyhDbufvOhMpQssMgcIJO7JTInXDbcJrdPYXExqymm8tXBPNJd6BufUfk1-hiFxwI4m66sdbrHZgzJhxux1zJnyXZdTxNyDeGSmQzOuKVwk6ZUmiBAiIzrUeahJaohs2TXK6kf-PLiZwFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22764" target="_blank">📅 15:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22763">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mv09Ba3phDtJWGb4uD7em1181kxME9mXIpZ80Edf8wh2uQrYIXbh_gkaQFhxPb1PFVzkkQa11tU4YLROptjLE_B2hGabyegTZMfeJGP6eUTHcULZVIt9XqZAHcwBwj93kJwIal_ugiLCKqYXdURDux2T4JI8XVs9Zf7bj9wNJR53o8RG2fpY6McgItAaBsLL1KQ7jd5ncCUYJZ2JAjl4mqgQLraOMxfKuYPluQbhUtzOWidlsRraoeRHApJMiP5BI5CEa3rpJ28qjfAn9IwhX7sK8nTvx5yfEh6yBXKMtXT4asiA8wbs_uu9BH09-q4JKlFKdAmZ3F7XkI4EKkowbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این چهره که زندگیِ سرشار از خوشبختی‌اش رو درکنار زن و بچه‌ش مشاهده می‌کنید، همین چند روز پیش برای دومین فصل متوالی تیمش قهرمان اروپا شد و خودشم یکی از بهترین فوتبالیست‌های جهانه. عامل موفقیتش هم نه مربیش بوده و نه همسرش، بلکه فتحعلی‌شاه بود با تصویب عهدنامه گلستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22763" target="_blank">📅 14:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22762">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iV58sUn4uiS3z5ReI075aStjZNq4POb_c-BpOo2DYqIJmt2kbkKGQNsSktY889QWC65x0RmC2bYi-IlOAMQ4M3xmuh6NJ7UwJZOZJIx1ZobkQRA122EB18qclHHwTEUF3TQUbbvlcIAxaBbIgtOy3A3WSMcYiRUe_wRbzZMz7P93GsA_zCbDaKIgBYQaN08B7Onccmo9086UI6M285S1-bRJJDTvbe1dRQDlKFdoiWVt-6ecK88NYqILflwqIqU-mIqGN1fukKCf3esHVkhbdhK2LnVRFtWLKGplP2MTBhhN4nMZV4WINWvlCRKAerqXGbypWEMnXTw0bKJrAU-85w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
رسانه‌ معتبر اسپورت 4TV کرواسی: دراگان اسکوچیچ سرمربی سابق تراکتور از باشگاه استقلال تهران آفر رسمی دریافت کرده و احتمال بازگشت دوباره او به فوتبال ایران وجود دارد.
‼️
پ.ن: اکثر رسانه‌های‌کرواسی خبراز مذاکرات ابی ها با اسکوچیچ‌ میدهند امارسانه‌های حکومتی…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22762" target="_blank">📅 14:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EugP01lRRkZ7ztVruHqUZAQOZkXX1ZyjU2Qza-46i8AdwrPPjdecmlvUr3tLyjKNLeZMJ3S0MLHbm367YFzSAzjm4ZBhJSMLofsdxio6p32Rb9Z5ku3LIIq8mKMaGWN8ig0L7_ARy9TxCFe1KLkZVmwZQB4KvngOzUb7nc-vuKMYmtJrGLoU3Q5XAj76Mepnzvy2t_RBEaIVR6l596ewCaL0xbIC4RlD0b52FMn2ooT0h0S7gGkx2rOu3oswJtU-zpvuLpcnfw81Jh-FCjBMRLxsL0KplbS9g8UkQRxDztbKmaY_teRLypp7kMUuLTtMjo9c_udgGzB1kTEZcm1pRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ سرمربی‌کروات، موفق‌وسابق‌تراکتور از طریق ایجنت ایرانی نزدیک‌به‌خودگفته درصورتیکه تکلیف مذاکرات جمهوری اسلامی با آمریکامشخص‌شود و دیگر جنگی رخ ندهد به قطعا لیگ برتر باز خواهد گشت و به آفر مدیران باشگاه استقلال پاسخ مثبت…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22761" target="_blank">📅 13:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7oEbe1MQWng9dx60z_W20dBetw9152Kz_8H-ED9Tmxle2HXfvJy4iBUelFhuz0HIZPqY1MlyWOen3LlMI5oP7ipFTlcW-_1jEaJ6_Esm1ds_aOe9-roIAgFC5ebKw1FdBvuk3dqdRa2V3b1wxGfmC692oEu1xjsBsG8LqqsE39dlMAmNyr3w0FPxZdg5UsyFTTYOSVqgm40IfhN_tfd0K3rUWQZbAx-qk6pGZKa-Ww8M8qzchUDlVb-l7tolAEoY9Vh6NhwjIEZfsfSW8Lzze4TKi0g9GuGMtx3peVNF9wZ9i_sizoZiyqOta_ebcLxnno1yNL4LSJlb0Xqb08rng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22760" target="_blank">📅 12:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nohYTu1PJM0fAs82wnlcxw9jggoPsyfcNj5pIT2gFL2qGbZ1WZUJqAeDq4102pBELwaKQDqOdg9bmMz5C312ht-c2rheTUwNlK3w7m_y75vZZh_Rocvv2xl_vkw8SvtUhwe7HZ2HAimYbLBDL8fAVQoEejoHfzQspKfBhmfKdCyOtEH6Db_2n-QR8BPP47c20--uU8FV5O0muw81x27CvkrY9-67G-DNMc2nvdzf7KDO__zKMzbcWYLPZ3KmM0NVwHRI30YcmykcvmK_qFlqgKUxLMPEpgDEZB4P-isE7_wUN4TLQVa5ZVnY2QuySgjVJEWhbtizgGekJureYvzpgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باشگاه‌های رکورددار بیشترین بازیکن در رقابت های جام جهانی؛ منچسترسیتی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22759" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22758">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=rP4RR2g8atJzH_OjRkhlgfTmSraixJvLb4VTp-zyL34oi3ED3H-L09JHFFcz5eFep3jcJSPEvPCY7i-i6FabrJ7W1sN0oVqJHlrZrhO71qToelSbhOW1rivdrA8z9cm9L14OR1NAApWGL72sH1dSm9MZbTAoJjTAJ9Ue5pI1J5KdcjESWg8R3H6-Zvz8_V_rMwi-1RZSWxCKqujdH0znhMdUtiGa6sYw656dDvGzdaimuPk-SGyAjkzZ5x3CKw7w_sfWTJjdrb_sCTx7BODdO5SPVMzSXPooC-LpGCM2ZfeFTAADSEVpgXL78HWVowDFqIU-cbtqD5tnLhtuc-178A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=rP4RR2g8atJzH_OjRkhlgfTmSraixJvLb4VTp-zyL34oi3ED3H-L09JHFFcz5eFep3jcJSPEvPCY7i-i6FabrJ7W1sN0oVqJHlrZrhO71qToelSbhOW1rivdrA8z9cm9L14OR1NAApWGL72sH1dSm9MZbTAoJjTAJ9Ue5pI1J5KdcjESWg8R3H6-Zvz8_V_rMwi-1RZSWxCKqujdH0znhMdUtiGa6sYw656dDvGzdaimuPk-SGyAjkzZ5x3CKw7w_sfWTJjdrb_sCTx7BODdO5SPVMzSXPooC-LpGCM2ZfeFTAADSEVpgXL78HWVowDFqIU-cbtqD5tnLhtuc-178A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
تعدادی‌ازسوپرگل‌های این فصل آردا گولر در رئال مادرید؛ شلیک۶۸متری آردا گولر مقابل الچه، به عنوان بهترین‌گل‌فصل رقابت‌های لالیگا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22758" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22757">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtsAJlJLlVP-LUluB5QQH8Vrsy1uLNIMlXolDSFLrBZ8qklzfmuWisbHJ74wWjaAYgoIMcWUfEQyon9vYGmtoLolCc-rQQm6fLRqXfoBzsVWUWRoNkieUUQ6tZHv0LVnRqoX5qECPQIiX5lE8XDppK4rXCHdoNPKrfcbP6f7WN91byLavCJJ75w0f_KrU-jCq4iQiqWt1V6JupIJwyPm0Amjz0jBFrlpJxtByVzt-_EhD1VUllS74pftmf0_9JhABQPt2skBmDsnX0beCREEbtnGSNm9hFT1YnDFCiqroYEKWh5ywiY_71smNjSZxPmUTpcRYTPeZL_f1YfECDpXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22757" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22756">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMX0Gx-_wy-6_iyaULI_mF_ON9lvk5wxmzfSPP1c-OuKFLbSpfJXHFp8tbqC1BQuIVv-PXEGkb-T7uDDEvXUzx-m-nZS7Pl8h_x8xTwTIvxKMJBpQjEOOcDSqWtQopmzlNsCbwUIcZr6bt-WcXFDGlEVVreSiazYDTteBNWqPn48b_wxoBMwy_So1qG-ads2KpaI9QjyVlOFYnfvsa13MBz4jHvMtZEwKkkl0mp1-M_RYg32pK0MuDGm0yf8v4yCX0nH4vkB7ORUC1OLZJW8E958exwXev13M7IQ5n7bSZcOk5FbrcmA7SVMl3TDylTY0tq2nXsKPvOD5If1HTlDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های رایگان پخش جذاب مسابقات جام جهانی 2026 که از 21 خرداد استارت میخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22756" target="_blank">📅 10:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22755">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVkZ4KmiIk5W61824CrZaTTtLqEKOpPXN0X7rF3jhYazrOz8xkPoCcRz-QdFy2TyRjhma4eBBijRJVHx2JQrwNQ-kA3Wj8MgwwiYiHguhdYemeADDL-_pdheMbsLjr6DgLUT3rIqpI7n35Q4KQcH9IYpZEZCTPldKssAlSZAd0eHRdGHxZqM8cdVV0H8Un40tHkVQ8Gk1J6yS3Zh9YYlZf7z4-AFVeuwJkmwzLTct_SrEJ79xn00zgfZfsrGakZc0yjHkI9OPnWDoOe1GrNgdB1-ZnKKpu32d7uFQzCy_kGcmf7iRY7N7ciOUVt8rCtiNJxRkllPUUtTcXdNYCFezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دانیال ایری مدافع‌میانی‌ذوب‌آهن‌که دو فصل گذشته بعنوان سرباز در ملوان بازی میکرد قراردادش با گاندو ها به پایان‌رسیده و بعداز جام جهانی بعنوان بازیکن آزاد میتواند راهی باشگاه جدیدش شود. ایری هم از استقلال و پرسپولیس پیشنهاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22755" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=Y8cMcZrmd7MvCDPbA19x5mI6h5ZAJImte80Qp_VocyNaQoVRNbQ3Ry-g7-bMdwYDQr-BmmWJZLIX2rSuilgzMvMX828GndnTOm5qQl2X3F_k-L5xzk5cYjlS58_dhHW8tCk1sxtvz86mVCsVJa4FNocrsu-ZspOIhEcOgnUKCUpefET6HV38z4vJJ1jABMPRWIgvo3Ftgslpjjxvlo7if1w7vIbyPyssD8EsCnqGGIuCwHOuBz0d1vHrkXUZ13BCXrTO9XTsvcWBcKmoPV5cVC5PFJqAIPBXfPORmqScfhz9cP7Y_I2Q0MYGJpLpLN7cAoE8sR_F1K8MHapvjbLzIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=Y8cMcZrmd7MvCDPbA19x5mI6h5ZAJImte80Qp_VocyNaQoVRNbQ3Ry-g7-bMdwYDQr-BmmWJZLIX2rSuilgzMvMX828GndnTOm5qQl2X3F_k-L5xzk5cYjlS58_dhHW8tCk1sxtvz86mVCsVJa4FNocrsu-ZspOIhEcOgnUKCUpefET6HV38z4vJJ1jABMPRWIgvo3Ftgslpjjxvlo7if1w7vIbyPyssD8EsCnqGGIuCwHOuBz0d1vHrkXUZ13BCXrTO9XTsvcWBcKmoPV5cVC5PFJqAIPBXfPORmqScfhz9cP7Y_I2Q0MYGJpLpLN7cAoE8sR_F1K8MHapvjbLzIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تکل‌فوق‌العاده‌مارکینیوش در فینال چمپونزلیگ ونجات PSG؛
ولی‌واقعا برام باورش سخته که فقط 32 سالشه، فکر میکردم نزدیک 15 20 ساله داریم بازیشو میبینیم حداقل‌تو ذهنم 38 39 سالش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22754" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8jHnQLXdcZ2xvhoa1jnTDoAGDA_dkzF9VBWjQj2SK5xCZtNdNiqVT07R_Sx4xANWexkiOJafkwZJTWezjOupTtcyAMCGxkglu4efvsk5QwYz89shMCTIE0BhjSk19dwwEpV3ZULXzLF_jZhnmV9SVGuTS1sLupISt4AX7PQXsvWmvthR46wAj17h6vMAf_lxMvN94_kOscyhA23YGw6RcC-MLS0OioFemqwTkjmHtTarMVqHuAGJ6ZIMIGX3WoDJvgMxn1Zk8Tc6XJCWLJvcv6HPDA6ntEUgWNh8_dXCchk8j9hezOcac7FfiW5B2T5uLVrU-wh92ihbyW_EpuGOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
درسته برزیل از سال ۲۰۰۲ جام جهانی رو نبرده، اما همچنان پادشاهان بی‌چون‌وچرای این مسابقاته و با بیش از ۲۰ امتیاز در صدر جدول کلی قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22752" target="_blank">📅 09:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HG-oT3xbQy06vC_xs6XbcXOckIgRRNNnOa_LOBERb2NNrOKWDBm-Rp9kqbQzS6qDi706hQni_15F-XO5Rk8uKrdcYJl0bWm98jyj-Fpz2JU0RmEc65N0gNlsjKiQe_18_dkdZ8SAmUL9cMjUyLy8fVc10zO08OHrmNWYMYFPJXvJJgdZFRaGRJmaiW3tJ2YORZIM6xP7IQUpio05VSbeM84ofC4sQLWL_M7w72OOUjsiNbeQjnzZRcla69hhNoqHtrd2obJgi-OsleqPHZEQS4fQrv9ZMYRucxxlMKL5cvITJ0jSkzAQc5JQVlpf0dwLjUvj6i1bHr8L6MoodginKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جوان‌ترین سرمربیان جام جهانی 2026
؛ یولین ناگلزمن آلمانی‌ها با 38 سال سن جوان‌ترین سرمربی حاضر در رقابت‌های جام جهانی 2026 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22751" target="_blank">📅 09:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPJDJH99P3r7F44H2ZsbLAL7YlLZA1r4fklNIfJC1yFAAVv9WJXHZyJCSt5OqMXqfo-mvYxEUsO0jt6AXCR1F2TRQ2ddiY87MB6f6fz6QYBAd2xomLxxcsudnyDRy7QEbXpPM2xTmDmPjcK2w9381oTP_jWmrBeLZokvY21h0ZtafU84wIHozvyFuwryz8h08HpsOWaPsNLys3R3JePNVLlG6qDwlT5hg50p08mX7nMPvVnu8qeEGwkF1B00-ri0KnEsyhYLKZ2dw6R9bvYgA3Hr-CrQAZuTP4JCbVF_TaJPnPiuagi6MdMkJZdejELON31aCv4k-d9nmN82AY3t4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22750" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZChQS-upNP8jQQnnm3sZ8o-yROlxZzsmEwKKJioxzbqrlL1IQBgE6oOrshRBzXK06ooEjoP0wIEsdo5OXWSYKHkJ99sh9Z0CDRxMDeHsQtUAWyctbvd0WoY-l6XG-0SppLNykZLQ--WTt5TyRmKwPcrO_9shacnrwK9TSY52mlsszxbNeIp3IeHpbwsJ81-sFOUDsPZgoie7mcMLQ_y6JHSfZAt_AVE48e0j0oqJiCJ8eO-Ft-wnvsLVXlPtv7Wa0OxNUFMNL-aFix2zI2ggh199EUC0bw-P0z8glw5cFjZBdQ70IjeAtkbIofXrP18Xsqjz3Fpfxn2AeppaP5w-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: رئال‌مادرید مستقیما به ریکارو کالافیوری مدافع‌چپ خوش‌اتیه آرسنال تماس گرفته و میخواد این‌بازیکن‌ رو بدرخواست ژوزه مورینیو به خدمت بگیره. احتمال این انتقال‌جذاب‌بسیار بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22749" target="_blank">📅 02:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMIbieXmx0Gcn5dTt8QANl2Iybgor0ONhnVYrjp8iNT8nsgPhryRi-32YAe2KdBR0vo5TTHz_yjySvvTnglkNRwP2VOd1dwOvD-VC0pPzbMSGDwHbQPm32IhStIV5DkBGN2xu1eJnPJE4KcjDxJ12-6-pe8Qh5nPwq-GmI9YjfLSEmE-Qc7l5NEB052gHmlykQCk3E3q8lMUZPgdZYbG0t0nLaPtrDRVH9LsayBbNLP-vKwUBBf-ic5DFHt0NmKG_g4vepSidy0oLJdmgxEJ4BA1FtbkQbGAvB-3N2MaGzvRdzfDcAi_Vws2U27YzIUYF-om9HAhCG2xJOA79mAUPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22748" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZUWU0Xdmx9fujGJs2-KPq4QXeVCvZPyyUArd7QRF6EMfPsr03NGxBAQCm2dVotqrMblBMusaNeHXQ-Cc6aiWoGNeaw4cXuWbxXvPxMFX9oGTE-RW3hAQ8CMp5w7K9mikSYFYdgtQQ8VFN1R19Hv1c_IP6GLa_Un57QHz1NXc2QZXDKfABxelByQ4zaF6Y-RAxCIeQcLv3grmKBIsYLAVXqUN5ClZAFPoxDcKLazSgi2SOwFN2xtrl_6PwR0vUKjHBr4EZi-lHv3RShqf6u2NIRbVfcSiMCVpifTBbgm8juN3B-0RIHKtbMU_EzkkAGUKA5rz-deqxVQ3QoSMmxqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ مدافع‌فرانسویی بالاخره به آرزویش رسید؛ ابراهیم کوناته مدافع‌میانی تیم ملی فرانسه با عقد قرار دادی چهار ساله به رئال مادرید پیوست.
‼️
کوناته در ژانویه خیلی تلاش کرد که با لیورپول توافق کنه و راهی رئال‌مادرید بشه که سران باشگاه انگلیسی اجازه ندادند…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22747" target="_blank">📅 01:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlXrDQZfIPv8uJjlbntwuYIPUW3wimk_xqDgxJkAs4FdJ1etX4NxR6NvDLrLF8jYY_ZsQAp_hrSUqFt4iLBD65i1sMTjqRIaevq1UqOKeB176HC-1_7SJr8RiZvwMtnAgSwrox23EoedGTLwIk_TpSN8kTBz9P98MdF9OoVStGkBlS-JtDsCQPpFRdUvBnPEsiUAlN_L5YSxIgtvSyJwQW5haNPBvipcGTSoE-ABk6eulO13DzlWdQCXPL6m7UifJT2-X5H_Yd4iz7baCLrThFTtOK4ofVowpbYEJxlvgWev4cd-5GnW4I1X--eQDB5YhBRVvZyLBRRBz5jwKH2LGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=Jg51GMxQkMVN0g-2w3g_AWaon7mqY8ZagQaFr5NMtAR03ObviekhVypkz_OQoCR6M9PZtkQR26xobAiv2Hq8CVnCOsSvk5EF-8THxMjKnJcLq6EDgLiPgGqfj9Ojt2SAtY5-pEXdXyyCsdYUWHJphv569b0AkEXO7muCF0DAMmllBeX2O-zPeQDdsTUqUrCuhly2EgyVX2H6ELU58ccCR1hQLqqIfZsxtmh2zKqN-ZBD8z2CB_Jqf5icmWK7RUJrLhf2cAHGYYeOstZm7ZsC0L-WUvJykq2jb8x2L63O3Nml_Meqw6xM9yoNi1FUud7R0dxwx0oLdsV__0J-E16Z-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=Jg51GMxQkMVN0g-2w3g_AWaon7mqY8ZagQaFr5NMtAR03ObviekhVypkz_OQoCR6M9PZtkQR26xobAiv2Hq8CVnCOsSvk5EF-8THxMjKnJcLq6EDgLiPgGqfj9Ojt2SAtY5-pEXdXyyCsdYUWHJphv569b0AkEXO7muCF0DAMmllBeX2O-zPeQDdsTUqUrCuhly2EgyVX2H6ELU58ccCR1hQLqqIfZsxtmh2zKqN-ZBD8z2CB_Jqf5icmWK7RUJrLhf2cAHGYYeOstZm7ZsC0L-WUvJykq2jb8x2L63O3Nml_Meqw6xM9yoNi1FUud7R0dxwx0oLdsV__0J-E16Z-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22745" target="_blank">📅 01:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfVTB2yTp6I5dijPPm22ObFoZKjP8wpTGZycLb1xrk1FmPZOC4FbI5LbB0VC35l2QQzgGUZtzrP7j35EyNOd3NqqMbbrCmV6vVOtVGAhbEhlkltgkvFLBuAhBkokkbKAm9sp3gbrFLgniTCmR7Wq09OJveiJGSf0eRAZib3hZYPl0O9mgp3naAcZnjsMoR9_KFXl9vZyktrTtjVTro9vXWuLpVUCg0TbUSwMHx-cFLXC1W-Td2A2LhBBbh_u6QjZwxDaK0oe2-nE-Oa7tzt40GAyQNGOaxPu_rSMMxRicZ2zgd1O7dNLoggIXnXN4U1W7GHLLYZUhvpts5o6TbIfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22744" target="_blank">📅 01:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT2suH6KsZCrco2XgjdtlyhzjaOwCnUvTniysNc9j6SGBx0Jtiq16pwVYqDKcMIwv4zr6oLTyF5TNlQubaLa8MA0D0hPCoJr25dnKF77TQZHwGPDztPbngtrFDgkCJT97UvD_m0m3IokWsoTtioRDPJUYw83XPbqKIe5rSyxC6E6xd45-ko4duhy8iwtUp0FW7Wc84UFs2mixa1Y-lBCgZabaX9B1PHRV3T8IMMY8NnsmN1wFPm_n5R3dlmMI1OnFjA7U-qSkn0Ir4F5rjQ_9lZMzJNeNsoPf1Z9Eni8_pj8naRwPYcNhP3MQwkcmvSSDyqTJnhhcztPbKYeR0TOEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از بازی تیم امیر قلعه‌نویی با مالی تا مصاف عراقی‌ها با تیم دوم رنکینگ فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22742" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd8C5EihM_GJSg7kIPZDPvejKtlHdJHNEMgiTVT4iOTdR-O7L4l7bban3N3_hYblywAYFtTmuVWvCC30QeBl7KiNW5S9Zkt_WaGujKeUuVzyI14a15bVIrQ8Xc4cEbSikZerML4bYdG37-Vg_eXkvbVpUOePNw5u62c1w0mH3xfWcZeg1tJUDKzPucuLPQ2qOFf3-7js9PgR7wh11e2xix4W32lK9BGJ8afVG2yiufH-XhScd3NsSgZeVRzVnnCrVzzm3d-EvKiIyGUWfWVNxYvtOfxDaLX_JtBFv-Fbj1e9uJ31ZblJ6uqfqed6tMhs9wCX1NocpuVhMC5VvOPO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست سنگین نیوزیلند پیش از آغاز جام جهانی 2026 و باخت غیرمنتظره شاگردان کومان در دیداری دوستانه برابر الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22741" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3vSSZhiP13hopy4cIGxU8gxuM48DrNpleWABbSdXUSLa-1OD4d1D_rd51DVvnQudFXFbvQnMyZANimq0aIgjC1RNVyh21mHQl0-gQ1h9-nGywn_TKyZRkiaaQXH6tHWuJJgEN06JIm9BaAWL1M_O-rqsgDvjsQVPFhVDGpmnJKVdimjsIspFvylJxv35qem1_ip2lj-Gf5hhYoyWpJz_HoKC28sdJh08hweIdBnoa9tQgWiQ8Qo8J0QpzNdr3YagwxNpIS6W5LiEllEn6YL6A2KLNB1nRnRIpDijrc9e-yzTVhb2iSM44Kq0bF43OgKti8-OeUnadXrl4Tup1rElw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22740" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIsOa9QaQ9fcJ9MYFNU-UuNkZn01URCggXPSHZIrikrfYhF1quUVL3goX4rdRacaU1x3YrQCyySChtoDKkhbkBpXyneWo0Cm2n0772UCpdU-u1ehmTGo-p2vh4iJ5NfHIJKezDFBgO01mGeXUPGnJT-s0Lfn7bkjbv48MYi5Gk94FjTSbYIjePd0MlfGlu4v09BBcKTvBN0q0CPaGLlQ9KWksTiToRNWSQwOM0RhBfdImt9PG8VqPHr7NWmkV4uYh6RQLe5r1yizZ_Al7EAUlJBxFxNbQGFKy1ydp2lmECg-6M2PC16msIOaxODASSVSIQnDk0tjxk0S44tF8VG18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22739" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22737">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo1VdQOiKDqZlFK0JvzVVI8LUI3TzS3Clgm-mBoEen_U8nArbay23SPkAH8P3ls1Z6WntzbUx2MOjeZLAF9RxlzHp6Kl8uaFJcsgEA7a6vEBNkyaORPRFnzCifH9wDaVnxz7X3iSCfrQhqyyxc9UJ1YXZReMgt1gndCn6c1-YcUN2AT1EDDpvX_Nfwo3jMMdBMHiB2b0a2RxybMcQIvkBZaM59Jq5TeqFAxpWSiuF8uyi0vQNFfRuJTttRADh_PKuRIiDALviAU0pGXz9EHVzUhwU8f9bybDlM1ctvEuXWuN79FmWnMZlzv-3DS4lCIWOMCUndn9lEFhZEsZCrgFVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22737" target="_blank">📅 00:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22736">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1314be179f.mp4?token=uuWtuigyuZb-74PEcv686ypp6r31dbIiwNOSoMIUDIq8Nx1pJYQU57994mFVu39NQuxvh0I6rHm_lwyw-g1MkP8VWEE1JEbZXkOobmdGffZyU3B6upqYfdE9ZLED1odGr5zLg6-ZDL0-3IAkHj6neNSJqIqdToMLK6vkpOzfFacVfu-y3lrdQkDybwPItOw9lCwPKyKTrndLgQG-PZUXntRMIxeAD1pMIdiQ19Ovj86nCTZbSLob_dnOCSNpPeTvaDHtASzHGIe73eUm18HKr1xXdXdhx4Ken2LkEMB25DW0lEIdsMr3jgh4bq9v0S1wApggROp79SbuzWKt4EoiOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1314be179f.mp4?token=uuWtuigyuZb-74PEcv686ypp6r31dbIiwNOSoMIUDIq8Nx1pJYQU57994mFVu39NQuxvh0I6rHm_lwyw-g1MkP8VWEE1JEbZXkOobmdGffZyU3B6upqYfdE9ZLED1odGr5zLg6-ZDL0-3IAkHj6neNSJqIqdToMLK6vkpOzfFacVfu-y3lrdQkDybwPItOw9lCwPKyKTrndLgQG-PZUXntRMIxeAD1pMIdiQ19Ovj86nCTZbSLob_dnOCSNpPeTvaDHtASzHGIe73eUm18HKr1xXdXdhx4Ken2LkEMB25DW0lEIdsMr3jgh4bq9v0S1wApggROp79SbuzWKt4EoiOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اسطوره‌آبی‌ها50ساله‌شد
؛فرهادمجیدی ستاره و سرمربی سابق‌استقلال وارد دهه 50 زندگی‌اش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22736" target="_blank">📅 00:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22735">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=PZ31Jp3TJSACwtxqlX9b0cZaKJQvSSHEwty0OZ_mj6gvYtZ4W1gPp-5QIeJpcZhaQj6hOVFx7dsEVjcSxEgIJ9DEhz7bKhyIRjMMpr3pG-quOHACbT1pIhacYm3EJrKUDrEQP8-P5ePySWMkv9o-kR8WyBKstcWM6XhjWEkpKWyPM9ovx_olVP-ECnILv1i3bS6IN29y8GXSfuTb4m2645ZHYwQDI8cp29Qiyn2PIEOSnksiwIGxFxmVuDSG-WJx9tkbgPEPxIrqzzkqZ8_tAST7vxL3aGm8MEASCvlRtbmDin9PVlkqvkATAVdhN0Z2ws6AEskZX91tIpAPhEwtfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=PZ31Jp3TJSACwtxqlX9b0cZaKJQvSSHEwty0OZ_mj6gvYtZ4W1gPp-5QIeJpcZhaQj6hOVFx7dsEVjcSxEgIJ9DEhz7bKhyIRjMMpr3pG-quOHACbT1pIhacYm3EJrKUDrEQP8-P5ePySWMkv9o-kR8WyBKstcWM6XhjWEkpKWyPM9ovx_olVP-ECnILv1i3bS6IN29y8GXSfuTb4m2645ZHYwQDI8cp29Qiyn2PIEOSnksiwIGxFxmVuDSG-WJx9tkbgPEPxIrqzzkqZ8_tAST7vxL3aGm8MEASCvlRtbmDin9PVlkqvkATAVdhN0Z2ws6AEskZX91tIpAPhEwtfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروزقربانی سرمربی‌فجرسپاسی:
امیر تتلو یک اهنگ داره اول تااخرش فحشه ولی خیلی خوبه. قبل هر بازی مهمی اونو چند بار برای خودم پخش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22735" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDcvR5b5UK-aQGLUv8FjDUs8BNA0YuXmB5WUWcPi2yL3zxx1qUiFDJ3irdPsvulHjAZSJzQFBYt2DnT-b5U8QIYsPgdd2lE10qYzEXNYof-No5O4rYVoS5GIb2YlSmyCWAkfRdQl9spvVAlePjj3oJsN4lcgjAMPYVJPA9SvhcnGCIFuzmB4pmdHBxG71yQv2Sq_D86FrH8B7e28K-RRlpSahstm-rIUtaR_r6BjpRtS7GzQ6vvuyQ3Em5xvMVjFxNIQpPyuOXdtBKFYpcuuF855glmoKWlyiJAJK6w875wOtCFMoKCGxO4JJX5XErH6n3UdjqO0p-99b1Nz4fJPvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فکت‌های جالب از جام جهانی 2026:
1️⃣
۲۲ قهرمان جام‌ دراین دوره حضور دارند. حضور ۴۴۹ تیم‌مختلف‌از ۷۱ کشور جهان. ۳۵۷ بازیکن حداقل در یک دوره از جام جهانی‌های گذشته بازی کرده‌اند.
2️⃣
۸۹۱ بازیکن برای اولین بار حضور در جام جهانی را تجربه می‌کنند.»جوان‌ترین‌بازیکن: خیلبرتو مورا از مکزیک با ۱۷سال و ۲۴۰ روز سن.»«مسن‌ترین بازیکن: کریگ گوردون از اسکاتلند با ۴۳ سال و ۱۶۲ روز سن.
3️⃣
کشورهای کیپ‌ورد، جمهوری دموکراتیک کنگو، ساحل‌عاج،کوراسائو،سنگال و اروگوئه هیچ بازیکنی ازلیگ داخلی‌شان دعوت نشده است.» «۷ بازیکن با سن ۴۰ سال یا بالاتر.» «۲۲ بازیکن زیر ۲۰ سال.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22734" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22733">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugGf02acQOnwfQVe5NB68gXmTShYcAJs9FrWT2Ztgtud_6Mu0-bA0ux4DZwucAzRPMWXNkU0VOwJCU7TZvux92LfpeNpnPmMlrg3QRigIOqKp7SxxkCOZIJRZgmxqlI48oCleZJ3J4ktgH8eoJu8OAggkoRNzUh2Tm4IffMRf7QuG7SrrE_wRAdx0X-96NL-d7a_t6I5nghKO9-zi6cHDygv4zIdmYmeR4HlTtgnmrlKLEFr30Y_-dAk1KY7WXogFQq7jA3WsGd0_5T_lcz-sKB6x935Lp7WX9vDjXH11PEpOepvXOKX1MB-Pb_3ObnmdvQG6pmtfCWeLVkmDpymCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد دنزل دامفریس با باشگاه رئال مادرید تا سال 2030 خواهد بود. او ساعاتی قبل تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22733" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzTe2JqVHhkXVt3viVZ69rx6aRbEvwINS4JtHVE7C0_CSNex4ZMOs4GbEPQLN8_d0G-tNz12BWg4-aqfprKkkj3iB9SgSqFebnl2285AN_XrwUCmbjSq4P_GjXbipY7SUJe6zJuNUwszeJq5llVMNlh-zo__qpH2Rmx_RlrYGBJk-UXUVuF6m-i14KU7ULGI3FGfMaL4aNhOUPAP1udeIgsXmHBNDkU3civqZ61HS0N_fhV_5X7WccVmDifg3OTjiZaCF5ZnRdnCk6zTvYnd7yau_gkv0cg7GKcv70XTd1-nYd1KzzbSvvpARHOdgd0u8hsFK--BtKyVQfiIyW169w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22732" target="_blank">📅 23:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=TJqDZAw-nCxsdT44aTTUmmtHhyTUCLS6RVKHzMWmh8looyQKAE5Pstz0nOmwlLPmF4ZKJyI9xMB-EWnHAgpjq6ShemBs5m8eXhdweCaxTIR5b0nGrITmS_sUDpxMkKOPAk5K2duN_91M89jJhjSVH_RvCSjcLUSaABrhTnKa1-emj04uzzLAnfsm41PqfmFnqMWNMx08lCBvtYIN7tTc5Xt1bX7WX1tb2uQgjTha7RIyBwOFW_rrOjiVUjdanxNU3EKV0PPR1FqCeCCA5HHyePyhqvhlY2xQ3FeuP_TdPsKM0meux0rF6-hIKAIpd7Cen78Yahvw4QeHyfNnuX6Prw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=TJqDZAw-nCxsdT44aTTUmmtHhyTUCLS6RVKHzMWmh8looyQKAE5Pstz0nOmwlLPmF4ZKJyI9xMB-EWnHAgpjq6ShemBs5m8eXhdweCaxTIR5b0nGrITmS_sUDpxMkKOPAk5K2duN_91M89jJhjSVH_RvCSjcLUSaABrhTnKa1-emj04uzzLAnfsm41PqfmFnqMWNMx08lCBvtYIN7tTc5Xt1bX7WX1tb2uQgjTha7RIyBwOFW_rrOjiVUjdanxNU3EKV0PPR1FqCeCCA5HHyePyhqvhlY2xQ3FeuP_TdPsKM0meux0rF6-hIKAIpd7Cen78Yahvw4QeHyfNnuX6Prw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22731" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22730">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsLzmwf-PnxbBCIeOtFforP9Owh42sVYiOb9o0PgV52zVaysIdrfFbm3USxCq7UMDUDcTLEVuUjQEK_nNx1QV49efmyCIWun-KIP1TCIUzRizGXzPlD6XBd6w8GIlZPz7JeWlCgAXIoRJq55GyOdp0o68NEPalhzX8dDO7qra8u4OJhIYxQ2yeXRNAQECpDQsktCvmXVoNarIYp3tlbbOlS3NvMJ6lukedbGPdg2-qNmbZTxULHI6MVGz2A2HtGApSmer6alDnZ6uxkXztZhTe2IGyKN4WAvc2u1mz8uNPq83t2law7kfFneZA8e8-qHejBJvI9NUKNFHvAmvmR2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییرات‌جدید در‌قوانین‌فوتبال برای جام‌جهانی:
برای اوت و ضربه دروازه، شمارش معکوس 5 ثانیه‌ ای در نظر گرفته می‌شه. بازیکنانی که موقع درگیری دهانشون رو بپوشونن با کارت قرمز جریمه میشن.
تیم‌هایی که در اعتراض زمین‌مسابقه رو ترک کنن، با مجازات روبه‌رو میشن. بازیکنان مصدوم باید حداقل یک دقیقه بیرون از زمین تحت درمان قرار بگیرن.
وار اجازه داره که خطاهای رخ داده قبل از شروع مجدد بازی روی ضربات ایستگاهی رو بررسی کنه. VAR همچنین اجازه داره کارت زرد دوم اشتباه و تصمیمات نادرست مربوط به کرنرها رو اصلاح کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22730" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22729">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_IzvkjovkQyD3ruwmafg0oetOXdHm6iWjkjNmRncma-WuAOfmxDPzs_j-Ewb2Uh_InBKbZ0AjdKi1LWSHBLuL570U7Y-4WIEhS5_RPMLdqihOXPBJKJQ8-QJVimiTsYklasWdPICfl18WeW11Bgm49nFM8hACdlIH79d56LCASzZjH3EnP3BAXMv5Q8JEvgNOg1OH0vDF42f_pR9S9NmD_93mKmYegqzonDfFkSg-0yu-VpFkAsOqiJEJTuvQW9sNBhOAlw2jlLnD2Sb-c1ZWHLgLKNVncn5uUZFM81wmbDhC316U44SZ9M2atfrHzBp1Ywu16FXYruDVwhnjXC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برسی دوپیشنهاد برناردو سیلوا ستاره پرتغالی:
🇪🇸
اتلتیکومادرید: تا سال 2029؛ سالانه 18M€
🇪🇸
بارسلونا: تا سال 2028؛ سالانه 8M€
‼️
ستاره تیم‌ملی پرتغال آفر بارسلونا رو قبول کرده و بزودی این انتقال به شکل رسمی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22729" target="_blank">📅 22:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22727">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEMarF6BiSzRFoc8FyM-Cq0tRmOnOeAW9n2yDR7o1kGrEv3O1xw6yn4j1ornkz_JsYqY-fV39kV3vhtPTCznbIubVLJSaMSWQQcBLjB-z3fbjwGAtqFWDWlMGYLpzgH9krv9Ods-FeWT2SkwGP4VIynF82RsWNE4yivH5fpP65RQXOjj_S9AfktIMXjrdnVZACgqfiC-MXo7qRRGhC7wXTr5bz3O9bDGztXkdT8mr1t0WhaD8MbBWQ5NHC2RDh4b-sJSD968qyLLVsZjOAy0jPY-62fuTsrQ4XmedCpkt6Rq9_IU09IJdInJSRwVzDjHdHOQqvvfj4OtJ7gi9sGRuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22727" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22726">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsJtVu0xsfj-ydAsu75rXnktD4ApZo36Vmk7PdRqvch2QOerGM8nZPyd_N80KVIiDhOT0eZhWRY7wZUn1AgnfO1AOVtSaR7RcJdyUE9bYTOK25cD7B8PSBaFIHHy1ketuxFphC_3hNnFaPSYr1yTRC1mkSanHB31t0C4Ck5R_KynSRFJBuFTtTNimXeDrbaZ2ZBTvkCZ5iBhKWArYU_DCiS5I-ualIHqPFyUO-8o64kzUQFcTkYCjhpa1X_24LHZR7m1_J_g-xU1KDaPOVQr8xA3UQ8_qhs-TbEp81JV_vnl_9e4PiT7gPzyDa9EGCnB4b3MsNQQ4z3-V-o8nqolFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوارجام‌جهانی باکسب نمره ۹ در سال ۱۹۸۶ رکورددار تاریخ‌شده و‌ تاامروز هیچ بازیکنی نتونسته دریک‌دوره‌ازمسابقات چنین نمره‌ای رو بدست بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22726" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22725">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdlH_w8FioZmImJRpC1dTzO2Yrs65cygRlcMez5JPSmTOau9l2Fdz6LZ3sX69RD-EJRZfwbY3Sscw2YRGnPRtpm841aA7K8y_GkuX0LYJ9_MR8yLTo3Io02uw4S-KFE-sYV9Coreic3U0fA5Fz1bU28mdPAKTfy3oZIirqftMlIXGuVIufVZMe5i1MvSWey5xWgMRIBhXVCpKwEuUWWxQSAUA21OI-L1tiv6UxtrDImaIKZ00L2aTrAeFhEDmpIdGnIZY7Z_qFYm0FI2tYzFUtoZBRCBpXwPV8ZOw2QTpyOPpqUvJwg0Pa1TMo5oOyHXBxweGjU6ACj2nGtq2XEOdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیوید اورنشتاین خبرنگار معتبر انگلیسی: دنزل دامفریس به احتمال‌بسیارزیاد بعداز انتخابات ریاست باشگاه رئال‌مادرید باسران این باشگاه مذاکرات نهایی رو انجام خواهد داد و راهی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22725" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22724">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">توپ ترایوندا آدیداس یکی از پیشرفته‌ترین توپ‌های دنیاست که فیفا برای جام جهانی ۲۰۲۶ انتخاب کرده. این توپ میتواند در هر ثانیه ۵۰۰ بار سرعت، جهت و چرخش توپ رامحاسبه‌کند و داده‌های خود را با اتاق VAR به اشتراک بگذارد.آدیداس‌معتقداست این توپ می‌تواند بادقت میلی‌متری و زودتراز داوران آفساید را تشخیص دهد و به سیستم تشخیص آفساید نیمه خودکار کمک شایانی کند. این توپ بدون سنسور در فروشگاه آدیداس با قیمت ۱۵۰ دلار بفروش میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22724" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22722">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnD24-uUTLK3KdqNETwltbpiFYb40hQPniUZ-K6xpSDkHvpHTzWPOCvAT9NsuanHhF2D5X837mtNF4C7idUK4DgmLUsYII7UaX9oPYg3oro7y73pCc6lc4i3PhyasDikpY3T34MsUERExVtu0mja2uIB2PcrUYlY--eTMBiNtCKYuZo-voLXD1A-RqvjbcBtCqomQKa9i5ZbMuPx30-rEqY8XPAH1-NqhFoT9vsYURYTjbYzVxq2rD6WrSjOd0vb0IiytWeIIjqx1-yKEKcRYGFJsqWDgjlvLGJ1r2ggUUzM3a_JpnGcHZ7LRTHmOnUoLzbszzrtjZAXpr0T0F19jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
لوئیز فیگو اسطوره‌پرتغال:به‌جرات‌میتونم بگم که اسکواد این دوره تیم‌ملی‌پرتغال خوشبختانه‌ یکی از بهترین اسکواد های تاریخه که امیدوارم با کریس رونالدو بتونند به قهرمانی جام جهانی برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22722" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22721">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-3VMClv1Wdpn9f4ltBeqAjxlYGjstiyfxDSnwzGlwybRbCuaObu676ZzGKZoXZrz3oFVmUwlNJIZRc-5c91VdLxoFm7UgaK9jBQEOHk8mt-9hyIAMmTINbroHc-LYGwnwFZq7DnrRSzh5Z9iOB3mrwC-zFgLcxzY4571roDZZh8sgM5t9hMzGFEl8wI1fLE2fihB9uJ1iubG-0UVtGnrsVjNxLKPbaF7XJjS7Q0xLFYYfCB2ScuVtk7uvgnwmjfWmsUGvXJ9PU8_ehULKJ4MwHw2KlH-ddkY7cNIdV6WYqLAqXeYGiPRwZ5vtQn-IaZvEenLrBGaa3THErsUhpRYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛اتلتیک:انزو فرناندز ستاره چلسی به سران این باشگاه خبر داده که قطعی میخواهد در این تابستون از این تیم جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22721" target="_blank">📅 19:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22720">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5L9E7RMGTu4rzCeCLgrMTsBp6sRiyz6hFTzo2zyRLEv26sPQfrApIjArxL4EWEjd645mj_t3uvKdlu_Xn6y5qFktEF65kMIavqoBj8DrYOLBXI3x1pjK7r5Hw2aj7FomFMiSwWQyL6c9Q3-LvObgVrLSU6d1iqnRxPho6Gp1DStpjdIo261-fJc2nazCKnqFFkP7KZETjrw0GY_9ED2TfeGC71pq8hIb33tX-Y6-BGP4OlErzJt-9_NF27oNckZB-BOTHBgvqKdikw3zwe2CFMOY2X5SFWb1MrYLCMY5sKI3EUz2y3LCBb7aMJGXSQnE-DiCUz2h4uF5JdjM0ffZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌آمارمثلث‌هجومی PSG فصل 2025/26 و آمار لیونل مسی به تنهایی در فصل 2014/15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22720" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22719">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1cKmTBKEMpKKuFdcvxfitOU11eEKoAbLeDwG_1GoKnM2j6iQrjXUXiqdb0thWBtSIULcVOo2cv1NAruKUihVWwoDZAVSX_xL3KZmEpQtWeowpqQSkpJzUj-5BLkSawDuAat1alCFzCyE7fkTqpEJ795s8guIIJ3A9bk3Q6tPNsDnLhwe_n5xCM74yJzeZONbERXIMANPaBN-UQqrx_jkoeTeqOYID9HDrvxs0rPRiILWpom9Vvijv01KiY1MqD-GhFghp_mUCk6-MoSD-_Li0JOqkgN4bpCrTQhP2fSoLraGvgFPCWnB9Qnkq81odaHb3hbv42GB9K0YEPvYAwUIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22719" target="_blank">📅 18:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22718">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeA-r1TrbQU9fLVHZM2E8ZLdH9eI0d8U7i1_H1tipN_7Jz9TafTIfH7tLf1t81y7M6A2kTctflukblvbdEjXRI2e7LNGnZVV-KppjR8yi7G5FkWoNmqWd-hixKotZhKm48MBxyy06fCedoL0ckcOO_vKNkH9Sj2RHokA2Q8GWkcrBSR96MuSaUxj8obClz7er4QUyAP-c1lLrOom8EsOzwllcpgPqjXl-8t0EV7pEKCXqJdpf4kfDa3PheyFU8yXEdKDgy22S1OjsTVl3zahPeUwR6YkkA9KRvP4h_v8NGfxIIAsVFoTl_ml--6MBzrtmpDZuRDqvR-JLbWitIaiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22718" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22717">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvlmDwgoUPX7vnnQ-Dbvag8Ie4IdvkZLMVPAw50aSW9EuzKKL4mYazd3S2RnfUGPCg3LpT7CwkDzDB0ae6rEwrmjbti6sC-niQkCmlhFlXXifcSdlBcY_HjVBwFparLMC4Zp4gURnQArZArh9GDc3-ir_7_WIM1K6TABFLyQIC9KjwfSgk1cRQasbsTHFf0Ss22V9p6eOFPo-lID5KI_oWssOO6kFNV1sWLihk6vbl1YKmZ0V96ZgSCjLD3JruLNBFot1hqD__yuPcdm5qwvE2bETGKI_TjvrDyv6LekvsEmYlAlYD0dGOYLhQ5btSdj6K8GW7Fnx45Ar-fRz2Cx5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت عراق با انتشار این پوستر؛ خبر از عقد قرارداد دو ساله یحیی گلمحمدی با دهوک عراق طی ساعات آینده داد. هنوز قرارداد رسمی امضا نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22717" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22715">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWixqm0ZT-lbHCTtXr4Zjk_MnJSIi42xKQqN25V1N3QsZ7NcD9FCza8p-vUaQRye7CGFSOTbzZWWp6H5_IcpW0arl0K0vk0hzlXaEyMXWqkbf5Zgfd36fs3eI0XyfNxBWw23P4srYwRoMrgD5QNw4oGRdoGmjDKxulMPB_j-0dPheTc-5hgwVt2CSWuEbm85o6FJ8PG4L1YdljR2ApLXyioCuYzvHSjWGxXl4UqgJjOFm3c65R5idfYavX2Ie2xGiTum3rlBWqubGGzoZ0M_jB9sW4IjRbVdjQ3R3wASv4OymRuafg61USqnZhr5SxJHbmu7KSD8nXTqaB696uD6Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c24u3-uxU3cEzDWpLNJkpvf12E28BF5V1gV8kDSfbqX-fpA8EaVLLtOsDyDC-vHB9NWZyTcLjYMP7kRvC46xENhU9wnmvSCKZ6BsQYRW-MC5ZVaWVXJK6UfqcStEhr6DV9yIi9ohKe_Dfr2qxtjfBjEiBKdZhfU-KqKhZS9kCp8SD16n3QEsOaroo00oYRql9jQCpclqydC6EO1y04zCh0468fTEqXNJrlBwoemBPFwLvhAhj7GKRGKCfnp-nAhryMEKwBHeivZ5SM_JG_KnVV5nGb-jvYkkeEElMJB-Q32HJtnd60hnk_ZZ2YFgZTti6Y9jzunv7OEA8qd24CT8ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇿
🇮🇷
ترکیب احتمالی تیم ملی ازبکستان و تیم جمهوری اسلامی برای رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22715" target="_blank">📅 17:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22714">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=m-2qG7eGIMlXeMWcPSi2xMafAkCLzDoqqPVOb-jdupGFcDu-kLPX7G_oRbilWwDEqKbFadnyk-mH89Jw9o48RO5wBkztFjwquWeSisbrOPfID6OTM6mQ2eB6dAYb6_TN9ynWyV1XaFq2p9GxiqDNaZ157hZVTJuO9A1RuCRAhkitVpKPA4NUlfD-e3KizHR7wbPBSC9PY_9xVMoEM32y15tJsJeoFJd8thX15tM6GSiRb8GX7lb7ahHrQCiBDmE6zyM8Is3OgknccJOwL2ISQnHIm4JBwIui0UNENWwk1EPrxiubIGhBJVYAf5ANE95DctQXIrjL1U37_tXtp0q6eIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=m-2qG7eGIMlXeMWcPSi2xMafAkCLzDoqqPVOb-jdupGFcDu-kLPX7G_oRbilWwDEqKbFadnyk-mH89Jw9o48RO5wBkztFjwquWeSisbrOPfID6OTM6mQ2eB6dAYb6_TN9ynWyV1XaFq2p9GxiqDNaZ157hZVTJuO9A1RuCRAhkitVpKPA4NUlfD-e3KizHR7wbPBSC9PY_9xVMoEM32y15tJsJeoFJd8thX15tM6GSiRb8GX7lb7ahHrQCiBDmE6zyM8Is3OgknccJOwL2ISQnHIm4JBwIui0UNENWwk1EPrxiubIGhBJVYAf5ANE95DctQXIrjL1U37_tXtp0q6eIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازشوت‌های فوق تماشایی گرت بیل فوق ستاره سابق رئال مادرید در دوران حضور در تاتنهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22714" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22713">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z07OejpfFlzEPVA5PTFFcTqIKTWx41Bg-0_6hFrOO1uE6cQ0Sg70prEz1-BkWszYU3AWXZXxpou3CAhioMM6mwO-Vsv3hdunXjPgsA2dXlLm7uJucYrussZ7NxQ_Zbk2Zr03aLDQH2Xcrtf92P69HBrojKbqSh5ST6_eJssfLRvsGIc77i3klhjNbWHW5ebe9vtDRcZDR6JgEXdHL9H7rSuguha3Mib9hHLLv-40yd5Cak38ouy5xCP6qv5guvbDmhknjTS4XjxHqlBLIReKcuYZ0zTHl_KnkwVKrpvhTYNApY-mrxqhSQTU8droSCC0Nkv-RLluxJ5w9hInSjjFkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ یحیی گلمحمدی در روز های گذشته مذاکرات مثبتی رو با باشگاه عراقی خواهانش‌ داشته و حتی توافقات لازم بین طرفین انجام شده اما منتظره تا تکلیف نیمکت پرسپولیس برای فصل بعد رقابت ها رسما مشخص شودتا درصورتیکی بنا به‌هردلیلی‌اوسمار از…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22713" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22712">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BR5NB2OqdSaom1iiary4Kn4vJi4e-lE0RDOJDTDRYmPW8ls3QIwnj9VwsUoZSPpTylt--R_VFaG5vKUOpcJGGLy7zmHCgCE0pQFJeccDCDziw4oJIjF1YbbsmHECKe3CRUTTee1nofXzCWXis9L-nvfikjCE4dwdB615DjUfGprxVzrA8vghI5FxP-Q1FfHoTjCwJAXfpXwAEa1yP_w4oQl98XBd1HMyP10xCrGPHatCCJ_1NwyXRt6riS78CrrUO1OZpxaes6tvt9JvQcFCjqprwpvgU3o0eEq9RhQx1Zqqx_2MfcagMHkYAPcO-MakehEryQ6R4Ok-HF9O_DlrWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22712" target="_blank">📅 16:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22711">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=Vw6X4xELpmLfoPWjUIe4oedc2JCIstLK_E1WVoFPEruxWSCtTeipK9SB3W3CXQ-TdR4hP5OdRMW__OeGMmypiRgdk0OHqn6S5ot1c7N7R9fvvu--nuLPwaKQ1s030EoBU2ycyNvtSTE5Lypya0toNCyymSjB7mF_Urhx7yO866HYvvFHh6QG_fj5ACbBw6Y5OTjqERFP0z8bNF5-sWjL7CBiPvGVSRvpAWSAI8D6wJC_4P4ZhCUo6RN45tlN2Cs16TZebheat3AzJzK4P23M9ywO67FearfOGb8dSmUPQdp-fc2w5qXQp4BsEpNmn83K5LEHrbEFR_p7iqu0KYzXboWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=Vw6X4xELpmLfoPWjUIe4oedc2JCIstLK_E1WVoFPEruxWSCtTeipK9SB3W3CXQ-TdR4hP5OdRMW__OeGMmypiRgdk0OHqn6S5ot1c7N7R9fvvu--nuLPwaKQ1s030EoBU2ycyNvtSTE5Lypya0toNCyymSjB7mF_Urhx7yO866HYvvFHh6QG_fj5ACbBw6Y5OTjqERFP0z8bNF5-sWjL7CBiPvGVSRvpAWSAI8D6wJC_4P4ZhCUo6RN45tlN2Cs16TZebheat3AzJzK4P23M9ywO67FearfOGb8dSmUPQdp-fc2w5qXQp4BsEpNmn83K5LEHrbEFR_p7iqu0KYzXboWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
توپ فوتبالی مجهز به هوش مصنوعی که به تشخیص آفساید کمک میکند در جام جهانی استفاده خواهد شد. توپ رسمی مسابقه می‌تواند داده‌ها را با سرعت 500 بار در ثانیه ثبت کند، به این معنا که هر ضربه به توپ تحت نظارت قرار دارد.⁩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22711" target="_blank">📅 16:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22710">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcONhykQFdjOn7dbPh40ZWxc-DB9GKmUda7x1Ha5zuWP2mvWDYY_e5z47T_dtWxzxP6dbegXNEkZHGhGng1nocKsa25smCRDTxyZBOWzitnGyAtX61fWfBOakLgPtR3cvytrDey6ugvFEDCsv-gHrZXOjdw8I2_jUUzzZdrPcT81ET-skB8imSuo5DMyBYU_cWyaPPrr2OB7lpxkqCtGqBFkqYvsO-VsCojl3Y9lWsPSXrv0u4OJlXzpC6UYaQsOH0AVl0WHe5VHY9o5A_gOAefbHl5An5vUbHwT8Ga7sbbfm4HRJPVXJVoBJIaYZZIMSRK-dcarOS7k4uRcnhAMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22710" target="_blank">📅 15:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22709">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouOryuLvcS4z29I92o6qSLihUTduUL0UQxesGDvY5jv06sDCqj2JeG-gzUZxe6t8Ns8CmhI50Pcg_qjeFiztj5JziFGzE8BkgHt8LkLFsou3JB8z_NXKklRNz7Gl0KBzMyiwY0ckF05ihmY_n6psI32MuUrHHIZDNifO7jIDQxr2yj2vFVhHnFpyMLyOrcDUoW-Gh_ydH939D_0b3eURgf9D1M_6xpHpp82kR4LRlmHQM3AxT2kyehETrU1gDPXYwehIA841XL8bT-Vc8dfflyC_5P8ARgfQPR85I5hfPqSkrk-jSZbO_lDxvUPdu8tZAQ9OcP_KsWKYLjeK1EOS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باحضور دنیس‌وسامان‌از تیم جمهوری اسلامی؛
لیست کامل ۲۸۹ بازیکن در جام جهانی ۲۰۲۶ حاضرند وبرای کشوری بازی می‌کنند که در آن متولد نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22709" target="_blank">📅 15:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22708">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sX7Eo6GxvtTV9H2sIh8lgV7UV2HRX3U3mhD9exaDytHBpiC2OA-qrYATwW0hGsErEQ3BjS1jw9KWoY2_T3zNlJnjXLnAZPDKwjH7gJKjTod1D0c9HrYTPj5pW4a-8_A9S3Q0ZhHSJJSjI4Btej_iVVEFNlmPZfSGLVijFRU6WJw23eyJG3Q8WLew0mX_GMYfNbh6M61uS-cpma5ZQFeS-6i9hW5NcrRG5Iso_92dhWC_tk6Ds1eLG9LEoxLwxtYYM_9CZR4afYxDvcEmJqnWtaWtWh4FwsLJhQbrfBqaq_sAx21pjDE7fyfroVEIk7JIlY-g2p1UO3AOZNVqigGqbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار هری‌کین‌مهاجم بایرن‌ و عثمان دمبله مهاجم PSG در این فصل؛ کدومشون لایق توپ‌طلاعه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22708" target="_blank">📅 15:04 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
