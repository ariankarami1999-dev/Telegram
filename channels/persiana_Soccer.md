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
<img src="https://cdn4.telesco.pe/file/sY03fOO74UUqHjBwbIYUHnNakDRd_FWvEc3vMxQWpkj93fGTSGMN6vRgHYzTKCR5bZSoPIw45Dcr1iO9XknY9TmLARE62SAylc7G1tQgTTkjPsgZJ7TB9-DrkDfW8ULn3A5SsrC9cijMMOHJ8qRMiYSNOj5P0L58VX2KILWL99yM8BOqIBYqmea4WY-JnYIVUVUW8Pfsz8l1_Cgahn6nF4MRNM_eZu8GV4TvQoiCBs1cs8xGHvObU3hHGWzRDCu2HL421TSTJo16cNhU7Fl4esKuoKTM3yvphoHXKrqxsdmdsxf_H8CvYk_bkmnpMZq0D2t407-vBp2iYBMlr-pLdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 365K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 06:02:13</div>
<hr>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anbSbDZktwwjSk6fK6Tbjpk7ZvTr25LzIuUTsMbFZVKyB_ffy6CnRn9mSOLP408mzumr1Y7-CC22VkNpZBHPbE7UQarrA5nYHNFXBc8iJL5kkynZc_HH5VCD8sLXoOX-eoc7hT0pFXBiRCib7dLY48Z3HdyKO7AzwXwlwXp-sLjAry1dnRCoI9ZLnbHJ_BF7SpWNwEuUjQukizbnO5u5tV0tYbZ2778R2yridNBLzRycgKLuMzx5hVLU-NFPXQiL6TRgRTmx4lLNWgHhCE1Wjlu-IFIgZbnhwoTUtvSBbYz9M75kgqkFhELQ-MWR9mkq9I2yVGLb7ZXsx-39NDzd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/24839" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swlr9SIaCrOQF4UWOreEPwTOScGoYV4mfQplUWCmdAG6kmQY5eEdMQO6EcTpGBPtJ-LC0PbaHxOE0FFlLD6gZPaug1g_y3p6fCc3bUR8GXZZeGlYEDKyVURd60m_574EXzCtIjmzJViOTvUQTDRAN2IcQ9Cni8joMovyvkK9omDEfPa5O2ot-vLUeHbOkXIkGCLs5XRFxi1QZRPvmQOaGv-NKOnrO3jsY75pfVrJjaSHbs_VpeywgFRrd0nNI1M8r_MWo3BRBJD5UJ9iwIGxL8w8nl4b092Ac4suMa7QNAWbV3ad-oLPXb_06FOQ6uVHMCijc-v58qzAOyRJ-uJJ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSszuRasUzDwaXcd5rvbUBMJnSKuIA2bWq4gT-H1VwRo8-y-G29EYc7KrFI-6SgFg2RKNakwr4IudiMMCP2c7b5XE_9EzZ2HV0gD69655uaZX-svIZRh2fe90STIjQ39OvpjoDP5HVsjWUD94_3CyaneU-aXpSBZHw1uh4LV8EvcB8-z6Gkp3xBUsaFBVwwgaU_f_kNXBhwImluhHW2PA0ldOfPuplZRpLGhS9z6WaPJTQBHqwbTmaux5CxwlM2cB1GO2M6v71Xqg1mC-p_lcXH6zPljGQ_giumfqwkWfq8ijVpG2IoHFPJ-toZIqHx_uOsGrlDN-NtyKP1Ft3Bukg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام
‌
جهانی
؛شماتیک ترکیب دو تیم ملی پرتغال
🆚
کرواسی؛ ساعت 02:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/24837" target="_blank">📅 01:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24836">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJVz-uRXOIpJQpyPxL-v8zgiX3rhUnO8_2FNBgr11YMWQzxpxD7Kq0pMMWbJRbbwflFkgVTXtouOmfQNXhb1AS_rr8eXqXsmLbzYUJWNLokmDIT7lip_MtJPOdfcFqjfqMHd0J3DDDXeo2wYdI-T-4JjTcOzyyuyBCwoKcVpTpWfSwm4zh-l8nid4h2roTa0xzQxH6DqzszDylDgdm4UvY1-zZtGawpXATBQAUpJRSKWUz4Y61brynFr00jUhjEHfsb6rcJ71qjslsxifSUHYG9FQ1WYtzowIUjxpOIK5isBZi8PyPs4FAWzah8KYiXyJJJkSHFmLe_o1cfaUsba2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسول‌خطیبی درگفتگو باعادل: قلب محمدرضا زنوزی روتیغ‌بزنن روش‌نوشته رسول خطیبی
🙄
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/24836" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeHRhZ_TbzB9mfo3nATNy5WYIGpTVR_NagvLv9JoYYLPbpIoq95GKiHi5dm93KDlaDhTejBBW6lZUxhs2ANvZpnfAEwCwcyerHtWlFe9xKHAzU8Fp5OQbdfk-UCAK2vauCOCthWI1bt3dFQY6A3Wy4Gv3ShGtBvIow0MumTIVe34WIoWuSvfwkYHFnzAZ9wuZp0wM6wUFUXLsrVxusSALJoQ6rXgvZNF6aaJ7Ci0dPz8XSYbWk0Fxhwyz-YQ8ooearjphbr1euJFHlpP66o7ROgqr8hmVgjDPkKr8eukPy0d-KVvLAuNvMHhoYdEuw_uFLpiLAQ72DXSsl8HrIHLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد فوق‌العاده حساس و تماشایی یاران رونالدو
🆚
مودریچ در تورنتو
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/24835" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24834">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUPl_xPmE4s3_gsTHzlprBPaDb46Hzf-90HrhnyA9Nb1NlW4biYe7bcjsH6n8xhkXP_PvNrvoydU_7mPabEXhQLObpRngJUvsOi7SRLRojj-koDUtA8qMigCjkp6MgX4MjPDFMVWGLP1RQTSOw5yBFmyz9Yri1pkvrYL-pgcs9gQ1y03Rp8om_9r1uJ-vYdc_QOaUhPRE7-pU2aLJcJmdzJYT2wzVZxLBbQ2mUtYiVSfSKWuLpdWDLRILLmE5BpARYOHsfqchSfjZm-jiBbtSvZ8dngpkHo1Q1SqjrdGCypLsw6IKz2mgvFESECZ2l4iTXTaaK-ibB1vN52UDRUU5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدارهای‌دیروز؛
صعودمورد انتظار آمریکا و اسپانیا به مرحله یک‌هشتم‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/24834" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24833">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG0CmPIJQJp6frYKO1GYKHVB0IcJ08m_-2oLZt0lcl0BCZ5IkCCxx_KiCMZh29KADo4pGvubY85OVb1OHwcea0lh7YeCxmn557GWRT6j9ftR4XDcYIbh_5066AMqAOcolWxw7rpGuLibT0eYEEGUh7-At67jx9MhYHzo8TZPZyDnFjagg8xM2rUEhHdOND00kxWRr5LEnOrCyt5rFYyGsUjcuwRDAMFhMzKlwKEJObZsssl5C0P0nAXH952V5-4BX17I4kjSm3Zm9eTfQfzIwxT2BODZgHlsMi3hD3INqbBjHkN0QsO3LLG0oKaENaK8H7Y-HrCMIOj-Ic_yK_WjXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تجربه پیشبینی مطمئن با
🅰️
🅰️
🅰️
شارژ اضافی و ریسک خیلی پایین در
#پرشیانابت
رو از دست نده
❌
🛍
ازاین‌لحظه به‌ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
🤩
🤩
درصد برگشت وجه در  صورت باخت
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a11
@betinjabet</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/24833" target="_blank">📅 01:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24831">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IveLVxIkRFWqDIHcD9BdEkyYDSRARR0MMCoHVPZhoNhlYi2rv8bdBY8PG6z0MD743krKlna4GizF9AZ7YBWMtlldR1K77Yl8tLMXo3Wu0Wyj1KehMIRfnnQzRMrD9yJq7_V-0dEnBoji5FcztB4ZeQLa6fO3dAfpZccrlI7tQgMEPsff_03AehPznD56mQ9bjdCMaWHnkNa3j4ni57YwId9o3Nt27j0LqlMJvvb_PT82sYTgYmB-HkHRduqmpaWJ6DwLUTJJUdVUC_BacjF7wRainrZ_rIiR41PtkPBP-Mvre_ZNerlquqhZyMDWqj-LUl4IPUJfotGLy5-jW-WkXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IveLVxIkRFWqDIHcD9BdEkyYDSRARR0MMCoHVPZhoNhlYi2rv8bdBY8PG6z0MD743krKlna4GizF9AZ7YBWMtlldR1K77Yl8tLMXo3Wu0Wyj1KehMIRfnnQzRMrD9yJq7_V-0dEnBoji5FcztB4ZeQLa6fO3dAfpZccrlI7tQgMEPsff_03AehPznD56mQ9bjdCMaWHnkNa3j4ni57YwId9o3Nt27j0LqlMJvvb_PT82sYTgYmB-HkHRduqmpaWJ6DwLUTJJUdVUC_BacjF7wRainrZ_rIiR41PtkPBP-Mvre_ZNerlquqhZyMDWqj-LUl4IPUJfotGLy5-jW-WkXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌باشگاه‌تراکتور؛خدادادعزیزی همچنان به فعالیت خود به‌عنوان مدیرتیم ادامه می‌دهد. عزیزی بعداز عدم‌آسیایی شدن پرسپولیس از حضور در این تیم خودداری کرد و قید توافق با سرخ ها رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/24831" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrAnHaoutHVmpwJGDM0rq71j9A-m3tPPU9HzGk4D55FVGbpV5J8S_nHZ3i8Apq2QDb4lZkC5lsjF9MLSRGA_MBI7uT0BlPMORO_ApJXP01gYOLv73X8KX3_2ElQe-6Tksw9v0Q3HpXgdJbHwIDbyvNmpA6o3u2ZZ4whgM9NIBh3_BRlIOIzq6ApkMOGWXI0NpROFLBl_osqntVCbKgghUu3kYL3t2NtCKUVuZShhIPOBKJvPmsN2Q4Mbh4sadbDt4VgzLgUSH63XXjGGDNXcOXWGBG1_1r22qjsmgFLnvIGHJZ3_8HhwtyE7CwISFussRJVv7XnEFEdKiLLQIkJjOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی رقابت‌های جام جهانی بعد از پیروزی سه گله اسپانیا مقابل اتریش. بین پرتغال و کرواسی یکیشون حریف بعدی لاروخاعه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/24830" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24829">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U04UyirZYpSNoUlzbEf6WZ4b6UEcGNPwhMPXyldOOHp1iAz2AqUJzt4A8_ZRGPk3sWxOrJddwHhsVcUaHPjH1xGYgdHXN9thU_JKbKfCT-QsWL1gTA-FAeUM6zs_BKTWU3WLBm_8XTzCvvSO7odWURqRchljUls4_f44LYSiwZm3WhhwD0Tp-ATXB0PB_Uc1-M6lVHy_m2fUbdLwond-bruKLscuBOly3F4r9ZDeJ1vk5IQALuZ6OBVI81kV7_IVJ6qEJ92trob_Tnbdwo5dGNljBng-R0jvV07hfxaJhrL-G3PkOJJxPQ4kHNlUPmQxgtS4wYmsG1IjCqg8pvpGSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمراسم استقبال از کاروان تیم قلعه نویی؛ تو جمعیت و شلوغی گویا علی نعمتی یه لحظه غفلت کرده گوشی آیفون 17 پرومکسش رو دزدیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/24829" target="_blank">📅 00:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24828">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7X1YSIvNKkMq0pVRarmbwPBMsfLrq8t_eDCa6OfK3cnassKdE5e9rlRAxz2o2cLGdLHVftstXN97lYJdQ_d4fH-Gm51EJr7siwpzxoYSNeLaTjlEaYz_X743WBF-a2oMIlj5VYOBko3NhcQJcdOYp6sta1yMPiDJRklq03QG8ayCC06QTk8zNRgsOuKeW7s5teJZRTpR4_-gNX3547hcLcEGcKPrZS0w6e8E8XApjsb2eYQ7Pb18tab1jRRFR7pgtOrROHf1AGubutUaY6YrCRUE0c6HNm9Q2tIZC8WRUSVr4XVLPytcklJyZ7RJf9UTvRGV669H-iTnzcQ-b4I0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/24828" target="_blank">📅 00:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24827">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=iIYJCijMXqZ2llf6vtlAI-bpYf7shZ5LP813XguGTPLRqEV2KhceEbN099D9YSzMGLy8e8JDHWmNQIXpeJwPGHM66DMgX97YDIcVMrOMpW5OjRkdxz2ZokDYkogzjM5xmEHpfIucFXz07TvdDp5wNrlzDe2GHMFFXGSwP2ulzjoOt8WdBMiba3_zWk-Ep-56n0PBPE35hPXKVaApC3ZLLQgiUphk-jm8SrwyN_h8fVRI1oAWfvI7BQ0S9TDokcm2ZF05yoRTMEXspN0S9EBSFLTnD058m4ZSHZhcsqRDP9xpWcGHb7n1SmJYxTYOweFhfYi1DTiuJnv0G38_mE4YUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=iIYJCijMXqZ2llf6vtlAI-bpYf7shZ5LP813XguGTPLRqEV2KhceEbN099D9YSzMGLy8e8JDHWmNQIXpeJwPGHM66DMgX97YDIcVMrOMpW5OjRkdxz2ZokDYkogzjM5xmEHpfIucFXz07TvdDp5wNrlzDe2GHMFFXGSwP2ulzjoOt8WdBMiba3_zWk-Ep-56n0PBPE35hPXKVaApC3ZLLQgiUphk-jm8SrwyN_h8fVRI1oAWfvI7BQ0S9TDokcm2ZF05yoRTMEXspN0S9EBSFLTnD058m4ZSHZhcsqRDP9xpWcGHb7n1SmJYxTYOweFhfYi1DTiuJnv0G38_mE4YUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
رونمایی‌از قانونی‌جدید درمستطیل سبز بنام "قانون شجاع" که توسط ابوطالب تصویب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/24827" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLLNuIuDQuHeA9_cNVA2TU2NzWe7jGhOH997aZta73702QU3nfycN7rlQW-OQIa-N73hI8VEibjrvZqTF-qzfCggJ3N4llda_oCU9fE0li7uoQnNpGXLTTHTyFEZU3QnBNe6oT-4-rCl6zVJ1E1dV48EtK7USY590T0upZabxWSPoqwEKT6jskrepc8TGjlrZIUw4ph3crVm_8rASDak8fHx9fx5UsMTWQ4etbSreph-R8xQ4kQVzDw5bXAFvrmIY7uelY42WHytL4uFIfbvyMF4Ei87_02PI4qfGeRz-1hYluXtyEx3FI1Ak9h6GRO5lYH4CGteDJA1lcShFVM2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
رسانه Smashi Sports مصری خیلی جدی اومده گفته ژاوی روایران‌میخوادجایگزین ژنرال کنه‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/24826" target="_blank">📅 23:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=bizl5PlOMNGG2lynmSeobky986No7w85ZilC7IAypxAbU-5nGNQ3BXOjkdL5DyZELStDMxvqGUvL8BqL8n2GXqSrQOlpUjbAoqwS-UUUQ8RmqoqLrtn2FmTPJ8F-YW53Hf-f9RQAQvSLX1PR0pIrGq9_Nb9K9Fc935Zu8t_FtZl5oOY2RHEXSWlwe7ozdLdby0Fx8-mLvyzJ2XhryfhUk_aLzohqPGSHzI5jh0FTg-XE9GTGWVaQ8Ikm22XVyasxbXM_GjaWOpooDcjx2sTzsOSdXbTvcDjQX8BsjwC6XTcXYqpaUESYfDWuT0zUS5WBKRTOBlJs3r1V2ZIb0wTjvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=bizl5PlOMNGG2lynmSeobky986No7w85ZilC7IAypxAbU-5nGNQ3BXOjkdL5DyZELStDMxvqGUvL8BqL8n2GXqSrQOlpUjbAoqwS-UUUQ8RmqoqLrtn2FmTPJ8F-YW53Hf-f9RQAQvSLX1PR0pIrGq9_Nb9K9Fc935Zu8t_FtZl5oOY2RHEXSWlwe7ozdLdby0Fx8-mLvyzJ2XhryfhUk_aLzohqPGSHzI5jh0FTg-XE9GTGWVaQ8Ikm22XVyasxbXM_GjaWOpooDcjx2sTzsOSdXbTvcDjQX8BsjwC6XTcXYqpaUESYfDWuT0zUS5WBKRTOBlJs3r1V2ZIb0wTjvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره کریستیانو رونالدو در یورو 2016: از برد مقابل کرواسی خوشحالم، اما چون برادرم لوکا مودریچ گریه می‌کرد، نتوانستم جشن بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/24825" target="_blank">📅 23:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic9v7ryG-wSYgI_BHdv7LznsCkMYOBQPnexzB7qk2KVcBZ6r5I554UGQyvYCb11NzafAMWlshMG-Popjg82qcI_pdk0ZrpvONVuhha94cZ8_sfcJ6-OSFa2rtz8mPCo8kXC2Ou_HYNHwOOP8Jn7jFXjV8HIPqdGSzKxEn_EaAxfCAaRoBLPwTKjGizUYh6ttkoizQeL12SL-u77UMlYKF4tR2dBz2rsBpfi1AD9aZ2qJKML-FnmaGsBph9ZpTKDDX8N3o6UYHqI1-0MAiWW8LE4SJ9HkVSg_ArdVTg2ytIJ85bLxZRS6oz9Lm4CWn_-Fs0ctYlyfQ3UmzBchziYPXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/24824" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvnP3TbPIKGfn55KonGhMOkYespjZj_0uirOO_oLMleKBB8jNJ3tp-Viah299LaOebIXs6Mwqnfv5s1ml9uVnlXT7u4bS2ntgAeyGKp4SilkQq8_w3lC77SJb0YZXvhWFuVgkFTu3uQPA6RRBl6wv7G0HqhSYtner5DVsE-5ecTrRD3sFBBK1R0pC0_VTj_qf25mkJ5o37t3CwRn2_bTONBWDo4TEcTc-iB4nra8xAeS4c-FUE-4IH0Ki-SoPmONb8w_3FyH1XTdlu23z8y3SU4BiGxI8d1NNBAy63gneBNyhDvVs6aUmiW58bYaviF8iB-biPhAWWFEzj5KKGfMpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/24823" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdB-I0YVe5p7hQMHTM0GARecNw96Du1NRy9XVtMdYhwJeKBZX_-LAPNvcXaZSfVQxKf6i3xEaZNncowFAq-C2FCMjoHsMPDy_Tbtmb_ehwj1gML6bqjRgUyzcB5V54VrO0XiURD1faSaLqHpy8pEl4pUiiGhih7IF-hGk3lt9rRAWMzhl-ZcgXFt33krifMPdjS_uGuVZt1LrH9l2FyorNf0mgQfLM5YRW6Ki6sJVgBbGtkhQMhFW76zO2lyxQJ8h4KTB9YB1Rq4OK1nbdmoC7OYauuvTkr_DN_vyrJxBFQUMIIrMaMBSK8TZlwsMQx14G-yGngtewyQaNRLEX2oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24822" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24821">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtDRFVBi9ijMOGpe82BCFVaihCi_UogxchFj78rB_b7oyyOlky65f7HKxt1jtQ-LWZ2V5EhrOtW3iOm5931juyUKvqksN_6GV_0IylZ5_BT09_93aL3hRPbv3DYTFbWd3YfEfq2UxpRY-Vuv025VxdShVUvV3gTNFIaxMuMMyULBb-wVkDxBU2P7rGzpBw4nx5nHDEsT_S-8TWKcm48LQBNDPsKkOvFV9I8LrcVJDqepnVBbuLMhuNdkv1myK2Xqtog7obXXWhWVCQh2RAo2CkVhqA4-G5mFkKIqdyK_RcWyvcZ8Qf7COCU7GRoy_nqdnTTuRWpkvdV3GtvxoF_tgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/24821" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaw3tZvzTc_bI10qtXn1WVEnhEEC0FJVob2Idj9iiX2diBkHvbp0uwZ1IrKJyajtSnO4S2n-FRzkpxfabci4c3ANZT6SoQwoTNh0ffcwYg-cSQ04fXfV-FWat1GD2ifsh-0RfEwTdaiN-d2BbBsGKhpEfywO7HifGFamWoFUL3ZT2KHA6aR5xr5AFYJdmomeGhX4_uCS8ARpXDT-vO1ciPs3gwL98URDOHW4IZ6eFaCaqwRADsmmuBgjLLeoc24VVNj88ZEP7XpPq4SKYC2uZefStv-DjBW4eTB07knwLGX-B5OBodtQv63xkiQcSNuoZWHiaITki2XcPFsoDqWqxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا 72 ساعت به‌باشگاه تراکتور فرصت داده تابه آفر مالی‌اوپاسخ بدهد. اگه‌پاسخ مثبت باشه ویرا بزودی بار دیگر به لیگ‌ایران بازخواهدگشت. همانطور که دیشب گفتیم قرارداد او با پرسپولیس فسخ شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/24820" target="_blank">📅 22:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gar4xpOZGhJYAuX-f1Gl3-a6AmFFJ73xTSrtu5ZFCE6st3mXDEEmvTkNe-urFvmgUKcmK0NH9SRCqTm1T_5U5oDg8_gCJIdtdmfuDwUqO44e7vd1OprBDZUVFmLPYoTcWjXg7gPqkIlollKo5dCus_q9yoUhZKA-V6-eEHQMbwBoR51j3xWGV9xYaBtefK5YlHAN0o0jDSvWuUPG4a1oI9LYN1VxLaTNXqG_e3R97LbTlDe9pqBh6PGaMKAJks-azs8NxIghTiZ4cAbBdgtdUNEAnz8PdaAXmlKH86V6l03XVlfFl4PuVB8zL8dwdoIHnsAKH5jATEOjaq9igsl1oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حجت کریمی مدیرعامل سابق استقلال امروز به عنوان مدیرعامل جدید باشگاه تراکتور منصوب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24819" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOtfK9rS0QCl774ALR0MZtEr7Kf2TV1StW47jY3e70MDskglPpQz9IyHC3cDDgybingYMbzghg92BN6LNyqWgxGgiP-fubY8FZ8tHMLOF4Z9H35gh5hFckv7SbAHBBCb42l6mqeg4Tj3frKalFbi6w7bF4-1qfFYBQrzdRGX4RBq9TOuSaZ69BojHQWZjVFSi2uEvxyrsKUncDb2TPStjY_9H0GdmqHKTY4FAWJsWQlt1Au6UQXAc_qI7rHJ8qgbTATtgV1BM339NzB7-4z2SvVtX31xo7KDn9nA1fAI---wUmF4iz71DFVPFzzSCqOEqqBcOn0nEttG_hbhTMNh0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امشب یکی از این دو نفر آخرین بازیش تو ادوار جام جهانی و احتمالا آخرین مسابقه ملیش رو انجام میده. شب سخت‌برای‌هواداران باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24817" target="_blank">📅 21:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1cOaGHfO2bXf-HfUbk5jDEhwFOhxBVFhWwP5CSFWDHRyeyASb4P6hiyWvlQVd8-UrBMZ5hUbDp9kNNKkA8Ae7Hgj6ZaVDewhO_kLbLZ1z1XNeYK6pTv1vY7U3hj2DUZOBggLmeW55yw79WRyr7BidCIM46Qmppv3cPsGv8tBWP-AaCe-d5go0wHttYMBvOkiLaOTWZ7faPiiqzJ1qOHpBuGriuxvTy1bq3ASdi4NiNEFZOaZlxesIJLbC2wS_MAXq17oS5Nn_2oxnOW1LW0k-Px5RKvMypxvfH8w0MolHqVuGEEeM36ylnPa9ygjGyjgj9z_1hxR5cqkg6CZ6QbZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یوفاقانون‌کارت‌قرمز برای بازیکنانی که دهانشون رو میپوشونن رو وارد UCL و لیگ اروپا نمیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24816" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkQ9Dl2SQsI39-KChvfrx5CPMexZpTEKVq0XmJ3mGZ05I9IsTfUGkZpTwocYdvUEdVpyOqiFr5ZttV29qsqbBeH-FQFoBkg1m1rERSxqtsCMzfiU0wPnrEt1tTM8vSec5zbEF9X1X037PsiV2pl7OzutpR2nfP6-BNyOPmUhWVm9WLcgoEcOd37wzdf-qLosHlyeR1vG-lPD5MlpeWw0AxYtS1Cu9uiAAu-XTjFMRBqImgnr7nq--1IJyJRJQg0QifchFxwYRgQFOdQ07zHPnUk4ssJsg4K8BHIN1E594wkrQ3rrCaC4pSKDXUnBzPKzn3IPANf4JU715hUTa2Z1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24815" target="_blank">📅 20:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8NiN9iYUa1derQ9tHgxPVCQVEozTv8Jcd3pZ_Dr4Yr1EI41p2WKsLkUSfYD8kpz_xWnkSg_jV6d6E94BnWrS4_82OjFilDeyHLAxrOGBEbef8WDcrWFmVDRiM36pvozBkLf7VpalphfT8VhBoYX1FAb8M29l4_HWAYhhhcz5sh33BnGWUAZT9nmFoOFvWf5p8l4KGgyWEvBYkfvd-gQ4-wSJ2B1c58pIx-g5ySuJezZRrjt65Ix-b2d_goysxFaRDsHJ1fb9lglbQ8r29m-dmwfLfBMKPzZecQ95_o3o5XYAiMGENxuoULZr829pBcmD4kwtTBOOFWnudyXTmTebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی
؛ شماتیک ترکیب اسپانیا برای دیدار امشب با اتریش؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24814" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnTPB_wMzPuJ_MQdvdGa7EpHH7CN5tOwWTDZ1gmCt5p6oz3zmuikoMKHOG-ev3fv4tUK8LXjHgyihxMXO0BlT2th5o80KTX86tWAXkC-wK3Ya3PipFxfabZFtL8sAaB2AdxIMYTIlOGlgCcw-xIeDJ7JtlsWwhjs4dBTW_N_W0sEs8WgaOE7m05KX0VNKrt_uaxVt_pa9pHJe_hsjYflSt-Xb0w58lzGz63mJRGkiox4kR0KlB7UM6w0QG_38rPYlGpqCkLhWui-Hr4veJGcPvkUKiayKhELyVn4I7puzjWHsJytoyFxFcu18KVOJyfhrml6ZKFRwhhKHDEn24Rgcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24813" target="_blank">📅 20:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTEiAlGioQIygdXPVYaXgTeo4uyy6JZuE6bkrrS8rZ_t8XT_30sBKYIrZVfmmVYECJxASz9DWdD8pcBLU-6VADV1NaJAa7O3EeGatN4CpRTmqpyIqKFPt5CxX7xbYN3sZapRgzkp_gHKpcP2I6ZxEXTNUtDF9WStmgH5ewg5IdaU9tmYOyMl-D0jJKS_2dgzbCD057YhUYBw57Umj3XBBfrCprElHCuLJVs_PZVmaf8LoyElxF3INARipBjkzbjqhkaiT0MHiIxOSQbBuVzJ8XM0MblyIeQqCk_Cm6wq52Tpx7nfMUewd1MNdtn1-EmCkWWCTSIRxenjlgu92KX9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایح مسابقات‌جام‌جهانی 2026 تا اینجای کار تا قبل از شروع رقابت‌های امشب مرحله یک شانزدهم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24812" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Swi_e-nLoMjByrXTbv3MPp6XWBN5YXI_n-06AR5V4tkd7LtPXdoN-KI96aAH9KlC2R86Ts7BQsSgtPNksv12qUxaW4GZWwYHVkAlC91aLmawVMAwSSYb2EZBYTSpDnTsFn1P41D0N2SZXcdsd3eM4TuJTKNl953Oymoqn5nQQTK03gCfC3_AVikrGa5FM3jywCXpEoWSdZTnDe8sWy0RSxbrL6jQ08BywbU4MBwqUNYpgGCHxgeZOTGiYkS-lKCoK6jSKbLZX4fzy4T9H3zhFY2Wmm3OAoKMcwXO0QFP-l0cFCHRnUdjnSJGa3IhH4i0nZFi9IJIIdmHC_G3t3Etfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش: تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24811" target="_blank">📅 19:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q999psRSudkRJR1kdMvRcHNd23DfV3RCXX0eABKxOB4hVVeDfzkyThb8lGlVt-1P1_lVPuqyYCGgEj87Zb6JlRk3qWx-1kVcENR5KcffegOH9MW-jjKlyq9IBTrIlHdCD6_T80XmqLOFEfG6l4rsWqeFuWW5LJWhYKPQVuxS1uy606NG84udkCV2e4I5CI70SHOakF4pmHGLkEa9mweLyVUEw-7Om-yFiVvTtZt29P3nXbmNv1tqEsbZI7z5R2d8wsWimetRUYgeJaiSAVfW2JG_HOsQWuFYUpFiq0HJCtSisRX6N2guA4Fijcfb0ojfUMEFZQzN3GULUZ7l51nllA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24810" target="_blank">📅 19:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmhS0D82oGIBpRbFlFJVv8AG04v88UWMkwVQXbkKFjo-bSS5Ff2lR-_KypGfDz_IIRDIEsFtJtMly7lbaHXKeQ96-t0nTV9HWfWl9rDOLnCvxePMIn8WuWC33qThigOk6r6EnEAv9KSCuUQCTtJo7ox5mNtURCTDuxYxkCdIXbWMIG-H3OYDfLIpJzfJdXJcmFgzoOgVYuNexdYvuN_s0H9Vxye3scnJwzFr1GrW1gQiKiX0As_YMP2quwpi34Ja9CXnfg-WS7fNbIW9-n5H7qqbj0kbRHMR6nVyVT-fLnGMHd-NxwOZw__EpaPyfkpe_524A4-Vog5hLGEAhBrcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24809" target="_blank">📅 17:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/raGBElf3DcxUBKi-Dq61oGsgHmeAFE_q8kSXukw-KANLebC2RlsE_Ep_dVbZPOnTSUPO2nBiKMdNkzC30uuD1wdevcZoylfV3P-Vum5umC-uX71Ypj-_5K1TvK1XI2nuMjZ9MaIyoqI-k3s58bM10N6NQhToSJ34lDbUNeY3LsSYxVmLWR8wMonv2G00-HrUh-mBfzFGmIbQeenkM_U4xO1b1JYi1gTr5W3iYk2DgxlUYzhvlnxXgjcVF03WwMrWTKpCmrqmL91EE87nEfVzJ6WHzXMwEsGKLu-WnURVCxbUh5U9e2Z9e-V81zEE44WsQGZitvLhWwfhe1l7mPEW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULeSItuNl_nbWBCuO9SmGj_69dVb6RHFqAVwSe7NnXQ4MlXRm7cRwO6zjjAXGivUPialwfqZuVK7EAtyxaB15MSoTs5l_igQrM6lGXhPxs2UHD5i45I42ViXFSHaT_Ez-8fffPwOpkJVFwgvNKxn3u0LCOFjcBbXCLkr73XYWH_5B8hP4YSqSwwGTu2Zg27xJtjzJBSx_T0Fw1vkHqqdxqydBX-T-MuMQjeRpbGwIp14ujaLKFI2yek7KGvHBKBmStZx6XFI8NtYHixdZW21H5bpzblZbMSHfxuAvFmHJNZI0tpyrchCjrvQdZoioSAIosLOyrYV_UTnJkCJRf2DiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24807" target="_blank">📅 16:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c080f226.mp4?token=RsMMkr7mFJToL04t_07sbUJCyBAQBOoMzklRUUwLym0-VgP5BH6vGxGO0EWJyzi_Oj5nsHa-lt2sdkRBexYJ9EqbredzIIFAHiElKEKQQtGJjvy-ceJH9m-8t5wmMCTfYoNz0OEDjoSy35fyrJBDddHhrX0ttkzKyslNeT4OqUKvEVigGjTq5-vPCKs8VXbEB9-JSGQU6r4agwXww2V0W5xPt0yZCCF628LFTmPxpqkkYZ8OIAwZzcyL5rhuO8fLTUi3dXeke3pKkSNBn6xXvuUZVaoMDzbFYPVFOPmkgiacbLORYWsip-KKaxbQqKbaPmA9BS5R8sbs3ap8y483bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c080f226.mp4?token=RsMMkr7mFJToL04t_07sbUJCyBAQBOoMzklRUUwLym0-VgP5BH6vGxGO0EWJyzi_Oj5nsHa-lt2sdkRBexYJ9EqbredzIIFAHiElKEKQQtGJjvy-ceJH9m-8t5wmMCTfYoNz0OEDjoSy35fyrJBDddHhrX0ttkzKyslNeT4OqUKvEVigGjTq5-vPCKs8VXbEB9-JSGQU6r4agwXww2V0W5xPt0yZCCF628LFTmPxpqkkYZ8OIAwZzcyL5rhuO8fLTUi3dXeke3pKkSNBn6xXvuUZVaoMDzbFYPVFOPmkgiacbLORYWsip-KKaxbQqKbaPmA9BS5R8sbs3ap8y483bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqZ9grzEwpX3t1dP-AY9aK0tb4NAlgiyxW1eUmIVYaaWBg1CRbOEfiwtaA16dVdPnPpm3o98WcItJ4PYQc2RXVypioOKInXWu3v-HvJwfVS7_WZWIqmsnx9gZSzBk9QSz0kUuTx4UiOM8TjVZ-2MMnA0JtCfYixDA8owHKKJWg_Vp1x2IZQhvVkGxuLTRl3YZqomxSZh5NBRq81I3fvAElalDnE-T3xIml1bdhg0IcdOKlmXf9CSTkQL-bLW8tsR0XycEcFGylpkmKaMNtcwQDLMnKyYyCVM52cOA02WC-cloKVSitHFS4q2uVpvRbuiOZYEN02IPFqcY0rRvnNSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل در یک فصل در تاریخ فوتبال:
🇦🇷
لیونل مسی فصل 2011/12: 82 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین فصل 2025/26: 72 گل
🇵🇹
کریستیانو رونالدو فصل 2011/12: 69 گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=P38yjv8L5jz1R58ZTSGZSgltyamYM5EmxM2wR7mbTLiaa_iz32Mlz4ri2y4XZ5pqiK2TB6eYFViHrOcuyB4QOl2Vz5hi-Hi-4Y4dXKiAlVtNtpJidsBUeNWwLI-QW-BGly5_BjC5kM-fuElH6UtDzUny2oT8vGAgtOZBHSusVRF8UtRkz7x-kxuQePTkGrlc_fSKmXWN4tDKa_ATvoMDWe7Ft3BT68ebkVj83N1WW2uO5tmzvxzyREQ5hyVdDslKf62r9KdJWWhf5u8nFl1DlktCEvcB3yao9_0AUOfHd-JMnGiytP5v62G06p8ofxr5F87Plz0_RtRK-JKfg0W_TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=P38yjv8L5jz1R58ZTSGZSgltyamYM5EmxM2wR7mbTLiaa_iz32Mlz4ri2y4XZ5pqiK2TB6eYFViHrOcuyB4QOl2Vz5hi-Hi-4Y4dXKiAlVtNtpJidsBUeNWwLI-QW-BGly5_BjC5kM-fuElH6UtDzUny2oT8vGAgtOZBHSusVRF8UtRkz7x-kxuQePTkGrlc_fSKmXWN4tDKa_ATvoMDWe7Ft3BT68ebkVj83N1WW2uO5tmzvxzyREQ5hyVdDslKf62r9KdJWWhf5u8nFl1DlktCEvcB3yao9_0AUOfHd-JMnGiytP5v62G06p8ofxr5F87Plz0_RtRK-JKfg0W_TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u869ydJBFP6Yomh4M-yEOJaLDkb8lW39qcSrhS6s7szXb6NywtAbPV4pCYOf7vnyQViHeCRT6RbgY7KNzqHjI5LtNtYEz44N_zW1gL3GN_SJKoFWdDw8c4qZmhvuNjzofBkFAQYkZv4xcODtI01TG02xCE4TFyQELD8n3MMDdZjcCJvUQwH3S_cSPlt1YUgWeDb_Ymr0aKQOH7Uk5Emnl9gLRwZ-5WPC-wZ0HPu1yT8giIl8omHiDJpu1jYbxM7nB3JFpPkydhDa0UWF0OoYHyd6djd7KGTjKdWfKsEdQsg8umFHmD00_D4Kyq5mRBOgvaSVKv2LpbbsvaYVUJB9cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=X-APK2C--05MYV5QIvE087loGmk16eFsIGGZZIg4Jb5v58fNEvrLWc9i9kY3V7yLBcktY0zXcMeR7mfUsP9-KxuDNZhDvX00GHtHKZNseSf9ludgJApracB6MzDT18Tm8GgHYhNKXvtlzigYKDFXyk7tJ2FoPEya_4k69MPea_uOaharPpgOmOlNN1DOjDJm-YJDlBwB09-AKfOYt0VVSpMIbFQrZV1IXW9a_q7r5TT1u5zfyMOH7vq1MQQ9G80ht9qrT1KwfECx9Qo6WVPLG3s9C8nF7g7WzFKLMqe7DZBvvK0CPcLB7j-etbKkpynkTulZbzbTRaDKr1AgVS0llQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=X-APK2C--05MYV5QIvE087loGmk16eFsIGGZZIg4Jb5v58fNEvrLWc9i9kY3V7yLBcktY0zXcMeR7mfUsP9-KxuDNZhDvX00GHtHKZNseSf9ludgJApracB6MzDT18Tm8GgHYhNKXvtlzigYKDFXyk7tJ2FoPEya_4k69MPea_uOaharPpgOmOlNN1DOjDJm-YJDlBwB09-AKfOYt0VVSpMIbFQrZV1IXW9a_q7r5TT1u5zfyMOH7vq1MQQ9G80ht9qrT1KwfECx9Qo6WVPLG3s9C8nF7g7WzFKLMqe7DZBvvK0CPcLB7j-etbKkpynkTulZbzbTRaDKr1AgVS0llQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آقای تونی‌کروس عزیز؛ مگه تو چند نفر بودی که بعداز رفتنت نه آلمان روز خوش دید نه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8E5_5YgEuhJzxV5iWlMSJCePczSq0jenREZFopqKrxxo9xZWlr5sZFf7JpyjPBnfpMycTT0idNgLFs2oUd8h800aiH8-rF0JuCEDHC45EQt8IPY09TGLpD5twu7jFKBsZy55ywmbsjBZK_z46byiceceNHgMB4hb6cbc3ZuPguJHCCt5aa9wto_IrGj4eYgAUttd6yjxlJLuYGVXObVlBfxWpPkGzo-ZhPd25uotOvLWI767lTNO8Uf7H7na-uMIwWoiuHmM2lJyD2_q70xwijX-2AN8geFwX1pv1nOvK202k88PnebWIa7-9ZhxhOWhwmkIUSOHyebrTRa9zqMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZF7TVHVnWqO5XPdSW25-okgu0srU2yZkJboDZaYGmbyZ6Zmb9MSUgJDzURZfcPOF8OItq03garngrqWVekdn-J3j4p9n893FLAxWSix3NCESvg9BwyYQ2xReeGYUhem10EtIfa3tb-NHmaz22HEYGOBhaf5ZhmGSJEvdkqfoP8mUfKUpSCtSIm8-CENUiEzvVcSBfUUsSU0MpsoyA61_vDxPJBCNRcPNSO6ceqcFLcqlcI1tLp7GCqP1HQ-HXimYb97mhUAgqI9dtpnIyN0i-N8T16wiSdlhxPF7N2wCKI71PesnvfePXbTgZARcOhJxB-7VYPMsgpmtR6Axf2sRlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nb_muqI6Z-ITCvz5KxjS9TvBeE-SRKsCoorLShK9Uv9CowF14Cp-slZmFrBCI_0GashSOp2rNN4b9Up0AorrMUq7iv0xGsnFBUnS7fQIXvB2psKemPgcxJK34OGXePRVpMWbpWC55NWCq3yl54GImBzC0w11-hlPhZJwsM42u-_Y_czcv1j1PdDixMdN95Cjs3WvUsRNerPd362NyQHK9IPeTAyNFxO3qQ2U_-ETgABlTzyTmYh67OfirEElk2EzytaTg74BC5xda9zh4gz8S5Np1t-uAwIRlxvPj335zweL3fr8LoomCbaFhOEsJ_KyJmAwk0I7DR9KNHuSk0UlcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=uXUZvusY6Fcu_S6cWRSX_PdN9AE6wpmXp4PHP2JVcdLyZfC1iG3UTdRLd_dlYA2jOxUDbDR_8TPhNzZGDXcnQj-waKvpGN2FobIGnOAlDyWSHLxD6M7pfIIwxIKxIZK-lVizZ7qKZhg5fHx4u3FmogYPJofbDjSY5cm8Thf4iV0Fcf2edqeNfheDuhTPerbKW2Mol-jXBx2Mr8gEAJNDxk7uRnpGejKACJahxKgps9lfLtZURNIAClk37B97FHhw48-XhPYU5dIV3-4vCproTxu-We8NjQ1Jr431bFSAwQ39T1EF6zPD8AVtrUlUXXZY_9_gFETMWhfjR4umdBRRYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=uXUZvusY6Fcu_S6cWRSX_PdN9AE6wpmXp4PHP2JVcdLyZfC1iG3UTdRLd_dlYA2jOxUDbDR_8TPhNzZGDXcnQj-waKvpGN2FobIGnOAlDyWSHLxD6M7pfIIwxIKxIZK-lVizZ7qKZhg5fHx4u3FmogYPJofbDjSY5cm8Thf4iV0Fcf2edqeNfheDuhTPerbKW2Mol-jXBx2Mr8gEAJNDxk7uRnpGejKACJahxKgps9lfLtZURNIAClk37B97FHhw48-XhPYU5dIV3-4vCproTxu-We8NjQ1Jr431bFSAwQ39T1EF6zPD8AVtrUlUXXZY_9_gFETMWhfjR4umdBRRYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyOz9Q72tfa9bQwz9if06Jw0gEvzyw1kco-Kd0RHKHK8i75JMHSti1p04am7mbt7L-R0Tnc--xFUmmF5q-cyay589xYT5HrgdLgi4j0ya81jQYLMuC7-RK2p7QiZwP9Wm4RhEAXpgMbBv7i_bi0SGcThVpbK0sXs9_bQU944p1TDXKmDPZIdKxmDQj8_jYR9r3tSGk8l5bodqQpXPzlASXwOypJqT2OERjsoynoyX9Q8cSUMPWUG3FPpVcL_mQ34AKieIzhXbXJ9MF9qYkPeUfzylruyTCYIAViDccIjphyArsjvnsElRx6HtIWqi4MSdoZhXGTmS0bkQWJ7G7bkwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSWm1rLWdrfy8c5jUeFzGFr5M3EeuWypXJi0RgVMN4BqMmjnMPNFlctBs-Sa8EpZNKT4gdkYFW4LcMHtsxUmjDnEhXoJTQ4a4gHdvDOrjbDyiV8y6KWNogdN26bn8STCGkLXIH_G1W8ujaRDVI7WpGAF8yk7C3ZIwfh1URUOy6-WbdS36mTrmT6Y4T2Z8DwqXHZn_-IEPRXeDIh64ew6Sxkk6xO_r6aUqjrOcF7gycNgXrga5xpyZFrukCXUKc2zRKsSc_2RevEH3SK-RR_i3lhnxRBBo0nKrLtVRFgv4QA9AI9PCfksJR9nrU1FP1WDOBGHXyIyIPK3t6DtWVRlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyIF9AIndP6zHQ5fkqfqjg4pINva7xhBAWNWEpSvj663tkCt82rTnNEtqBBLErcNTyd7w_JslNDG6xuPd42s_ag2-KQrpIZJCjzukhWAdxp6CxhjDESCJswUfWDX1n_hPj8cu46SqFX1Yw1NArbqXomyvLeMy0rHTBqjPHKWvZZbrtgZWaS9DokvZQJ04_q-MKakg4QMsFlMSlww8b8bSYPxAiZUcfBddWYHUHxUOh6LOS_1fwDp6fv93XDx_V_GR15RSXIqlaCvsiMgo5mm8g5JNQ2gG46J6tfT-sbOXtCNWHVIngnRkfBft59yt28_jf_e1DeVd3kPozdtw4MNCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIv_ZM_Ud_UWK4DOnabpuVEXu6SYMaddKE-vB4gYKPcnyJmzOg63ZxlDdVjAAgJ8_08pLrULTzwwyA2wB80GWlH12BHNr4FmU0wgSNURX3hu044XeknKlklMDhq0_wnyhqM3xyQNaM07kP-CKdNeOmkVFaFrihfGsQDkjRSyHe-bz9UJZUuBqcKH0_b6Vb0UpEUZXn-XmYUZnqR1XfK_guEwEfQJisqYfSIQ3Bws-05dv14XS0FsUpmWyiaSUlFHC8brBZmIBciuZyXu2OH_tk4vgv_fDoMCS9-gBHEvgebbaz9GAyPhNstLavAaYYrnpsKhx_6jI52s7zWqPC_AdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxsrQsawIN0z0UgtN8I9kotQaJ2TVArVGfxKeJVooNMnADjsiYTkaPX0-cjoYG2r_3PL4_lFVUetEN09HnL2l-2hLx3S2uG4CrOjRzG5NUVTNT0vz3BXHvWFLPFGY7EjwyeFBJ4aTvG_kWYLS5iAkrAFGAQ_sy-EzLhqOTfHHSmiZJFZg8HTiKYX7Rh6mccFlfei2nBxgmxx8KXIEaGAZf-ZM-r5b3rZZImTrIWuXJgk3QNoW5JAFujTy0qhDXwcIm0ZeBoJgy7t3nFTg-tQIXYARHVYz3wEUYtmLHzLKC4GnW1xs7NDF93JtKauPu4Ec4FNmAw2UaLTxYSAF1zNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4kRCBZuwzvnNN51QWhCrxxWXqp5d1pZ1J_15qYGEuDZRrZh9Ar60PJ0gv7eRDdvvjBdUETloCLzAOPmSV87zLCqAWwlcpsoSwf1Z0CSb2PtGxwas5Nvtpv5v8wPqC_vrhLITgULvgKd0Ej9pDBiPT3Uy0F9p_vsPKJ6Y5rr-5M8rVHI_L0VRdQz2TXHtB4G2ENUIErR8i7T4EonLR1Srb7ja-EJnT-mXtHAUN0Nfd3e82ObQKQXQ9jN3_jypJlBOR5ZJE5q4NSKBf2wA4725dg1xn5WxGuJLvnMHMTNoukH8yY5ykOBaOtTsf2RSkA0O5MJ0k8uJ7CJOChNez9GPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b48uVRAf4sWn6TgAYWWNiBQRBIE2nqsIhT54MzHcMgFH6MQ5FoebAfogRPwo785QdfU_hHUQFh3lsIHcYRIz8C7Ix6foCP1a74DjZBWfBhAjQROVL3PgqWM6C4ujISNge5Ztqdfa5Del9tZbMlwd2xW-B1O9u66cO2gpN6ARlmjnDxLz51hFO02UbAMMsM24h0Pfl4C1-HtMqi3qtTJc31pzJCrGaGpXtr3IChWr0fzHdsvKSrxLILdLMkTRSpbZds5PCX6Datg83mrudWb-zKEgeFm5TUbQPEexPxQNr7Z47KH5-4NusxkG9Ma1Nt7rcSzRqxiSf3KvSS6Ee6-eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paT8LMaSwLr0keU2qLjZ-iBZ4-emJdU5fsdbH_oL0JDHqoRXxdJFWmzFxSmPkfA_OeWtCzoVnyvsxZKtN4kXzQ8FtjZ6xw0s4x8Mp8ubLTfVXPfn3hmontxvaJT1CQwih8yw8KQ_VDdTFUyUsD5dJMWGJRaCRDAFYeDIYuixagDcXHh6s3IoLtVONOGPwQfpwi-i4Vdv29gc89evf_z7ZXBpHxyTupA2yU_IR7eCGhSrIktOYDKyB5uakJTs634EU37KYub7K_O9ynAA2I3v1pq-C7_w-TGMJvtxEXIaMdK70v-CbNu-hSfjf2vLTSqVlEOAVyPv5wrU9jj1WIbMiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=bVGQLBcOJsypTz3lkLpcZDg-xedZ8haS4TI78BPMxgZrP7SQANLCK_cWjl2HrPme5bCHV9ng_uTtr8gpn1A4rEfCRXMBPsLiaenRXIKlvuOFLpv6exjgy3rHwKpjYyMoOgLMnTPW448JQS5XUcKmONPgqDaWpbnX1urHKvSkIhltk2us7twM1Jdvb7_TqJvBzvpAeYYiW1fL4cCn8E_UzW6b7t3U4kjeljip4zmBAiC2u_1e_1ickIJQO6iHeridK8dUpH--oY5-QMAj3qqu_R3pvcTWZxF2Xp8X2jvUVf53XJATJ4q4bpfQtZhzTvHaBLtgpOSMkQv8aANxhfJKwXBAkCijDkBgC1tT7qEtFLm7Ui3wFVdyEtV4h13OeU1jIyWezyPGvCQhmGkdbuWrRiSoQZ6Ir5sBE6VBST5f9zp9sgkJjB18a9QhhRJcWTbeXexgyOUxfg1A_YEEpuw0ADh8OK97Xr2fgzSAliPZFktIHRlNn5_fM18Jk3aKzc6EnisXVIelGgObzorQ7kN6fncVEd8-xUh2WS5wbONIKEPSc0enCxxOFwmCsEDk3QAXoUCoyovlGzNodcNpTFyLKx_NQPcNbwZjIZb62mz6DX2DiHcgw9NT6B6hSKwXe013RPz1R9_9-68yvEFbpZLWzXzMBkaeEA3NJsS-bAi_aSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=bVGQLBcOJsypTz3lkLpcZDg-xedZ8haS4TI78BPMxgZrP7SQANLCK_cWjl2HrPme5bCHV9ng_uTtr8gpn1A4rEfCRXMBPsLiaenRXIKlvuOFLpv6exjgy3rHwKpjYyMoOgLMnTPW448JQS5XUcKmONPgqDaWpbnX1urHKvSkIhltk2us7twM1Jdvb7_TqJvBzvpAeYYiW1fL4cCn8E_UzW6b7t3U4kjeljip4zmBAiC2u_1e_1ickIJQO6iHeridK8dUpH--oY5-QMAj3qqu_R3pvcTWZxF2Xp8X2jvUVf53XJATJ4q4bpfQtZhzTvHaBLtgpOSMkQv8aANxhfJKwXBAkCijDkBgC1tT7qEtFLm7Ui3wFVdyEtV4h13OeU1jIyWezyPGvCQhmGkdbuWrRiSoQZ6Ir5sBE6VBST5f9zp9sgkJjB18a9QhhRJcWTbeXexgyOUxfg1A_YEEpuw0ADh8OK97Xr2fgzSAliPZFktIHRlNn5_fM18Jk3aKzc6EnisXVIelGgObzorQ7kN6fncVEd8-xUh2WS5wbONIKEPSc0enCxxOFwmCsEDk3QAXoUCoyovlGzNodcNpTFyLKx_NQPcNbwZjIZb62mz6DX2DiHcgw9NT6B6hSKwXe013RPz1R9_9-68yvEFbpZLWzXzMBkaeEA3NJsS-bAi_aSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی:
همش فیک بود
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0glSzm1S-bT3m_MUeaZXKKyYo-Nr07DHG-MXe3AMxpt7OhTvW9sh33XseZF5a1l4BkNcsD_2R1GBt9aY42vA_FkRrCEfVMuyn_gebQqPYUdXo09ebwYl7tsAsVSrD7nw1yP6b513eb5tx-1xqASWlYq7eBLwNN7KAqgyqSCYoByrNloTFxuH6-l9siEyLYbVTeOT45Sc1L1Yld9OMtircxiNSXf9-McCp670w9jysbA3Uphjv0CCLSeg2q58e8IpDhufhNnzhicyZbn1GAULjOygQJOz5bDc5THCZj4ofmtoHirPq_sNjcUdqgCBkXbDkAysdsVSGScFOsAxxuODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDNfjeYZZQfNtx22SA1ANoj9nMlkkZEnmM2O_dMflwct4AOn97FCspiPF3W4KOAOgJwVd_euD8o5VFq8pUo1eLJNOreMIRw487Kj9SFRIBd0m3mnef1hbqeEOlHjXB7KFMx_xwVU3tj6VcWR4i4JnhzwTv4_uAT7HD7d_6Fg4n8YmcpKf6fxWB7k5yTMWJ_rGCDYSTCT5oX-dSLaaXXvS6prJxJA4elTjX22IFvjYBzE6yEt_5CVs53Za3fFG2YU_dVbDnFkqueG_cclyOXxT6IfxXyo7595MviK5F5hgjKr-QxfYqiS_O5tmqJ2W_TIu2miG_0TPqo3SH9hgCGt0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=swmkTaP53XwTSv2btONvOCRq-IdbvQcE-H4JtRHBTnq9HV6kZWtqB3hPX55-L9wCLxQhVkI219KO4WsEfjNpnIJrMa5FX0v1e_DF8XM5Fk-4w9j694s8Ks6iDG_3qwhRHXI2JisqMum_7qmsUS3vL7BmhmR1Z_wybjmyUXY--fn3uDw__XOpR_H-2oxCj_WhN2SgozPjcOtXduuLi2pRjPfXtgukXGx7yFcjjzl5gHwRpL7c3GJDux6qndExkdrlBlTpu1jlEpG7RsXNOBOeWpZk7jJjG4r0DtmxVBYykEi7Sapg4PKa404n2CUur7rhN0P6aN5ot9PeQc-Q3ICP9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=swmkTaP53XwTSv2btONvOCRq-IdbvQcE-H4JtRHBTnq9HV6kZWtqB3hPX55-L9wCLxQhVkI219KO4WsEfjNpnIJrMa5FX0v1e_DF8XM5Fk-4w9j694s8Ks6iDG_3qwhRHXI2JisqMum_7qmsUS3vL7BmhmR1Z_wybjmyUXY--fn3uDw__XOpR_H-2oxCj_WhN2SgozPjcOtXduuLi2pRjPfXtgukXGx7yFcjjzl5gHwRpL7c3GJDux6qndExkdrlBlTpu1jlEpG7RsXNOBOeWpZk7jJjG4r0DtmxVBYykEi7Sapg4PKa404n2CUur7rhN0P6aN5ot9PeQc-Q3ICP9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSkBltCEy5c4LgnolqjGa18svj-VRoifkvbh-7Dkc7moIfcgFZ-NWuGni-pmfhXy5LZ-xUe32WIzC5ue2Qv12qfZSSi1LSaUZoxCN3eFuTLJNZpS24mUwUXn6MeCq2vpq11qdSEYQgKetkzyZ_r2j2_W0Iwqu-34Ybox18CWuU35bijcY5gict68_DoErr_HUhITy7CMSgD4d23uDJI87sX8waFoJkJiUBpLpQ7rUU90BM5vaJVidVBweXvq7Wl0kqXYDUjyVlL6mV9Uo5_UbiJRZ9VrhMugpCdxX8HXvGLmE_JsvpLIkSPEfRSrnk5RVGlUtdu3145zxSAVsqIYCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuMvvztFp9Kzu6AhvU9o1mcczDg4Bs5IGe_w7-Unjwo1BCm6v-FZnUs__fSeuGZadq0jjKdTtNcYJ0rJUIPw6juLb4bXBMhI5W09svUp9zWOIQZjnQmwV3a2dpcYIAPW9oeLNfNemu2FjC_Nap5WS8aZHy0UODd27Jo-AHXHGGgpLzB2sbuA-RV1zO5rYcufnlZZGWSp-lPjtqIyGxniBXC_bAJcKdPcJa2xkeQHbuWm0exJ-9uaHzQi5q-77uYcMvJZdsFHSnPrtsxjsy_3bUFpgPC_fXLLjqLvwbabO-UxNYSZaX28Xc1kVfYU5iPxW72qIvY8Cfo3Ravhvv12rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=p3p6TlKI5hlKKzHEY4fXWT2AhfC_3VD4Cb00CD08CA7Na5ngUwtz_T6Ta_x7T1reFPYsqqboTAR-A6o-BrcIfsRk6x0hG8Wiks7t8n2RAqowQ38L9bycl14hZ21WdU-av1whm4xKY7v01Eg17G_ka-6NQT5C2VcI_NkMAEG-8vtTzcLyXFOaNflou1gPA1mRab144Mm_v_p4GH__BAtv-aV2bTj31QE-0fmLDcHUY_1pq1K3Htsejm7Ze_As-eHTKH-NRGBcTvRglfW9399FScf-jF3DGjet18NoRZDWSUVhY102tWAA8d-7ZtCrCqcMD1ZXBG5m3YPYOT5QaAgtXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=p3p6TlKI5hlKKzHEY4fXWT2AhfC_3VD4Cb00CD08CA7Na5ngUwtz_T6Ta_x7T1reFPYsqqboTAR-A6o-BrcIfsRk6x0hG8Wiks7t8n2RAqowQ38L9bycl14hZ21WdU-av1whm4xKY7v01Eg17G_ka-6NQT5C2VcI_NkMAEG-8vtTzcLyXFOaNflou1gPA1mRab144Mm_v_p4GH__BAtv-aV2bTj31QE-0fmLDcHUY_1pq1K3Htsejm7Ze_As-eHTKH-NRGBcTvRglfW9399FScf-jF3DGjet18NoRZDWSUVhY102tWAA8d-7ZtCrCqcMD1ZXBG5m3YPYOT5QaAgtXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knDDii-IjULf7Fct2IfFl0HrtL3hUVPBJ-oUyq41rcR5JkwBjdvrFZRaliyYFDoI_2j5j9-Gd98BG_zPGzak3NvS8lpCO3nEK7wC2p0-n0W1hMsqZHfcn5A9z1APQat_3yRj48TVIUbTpM9FmTVhMfbGmt-gAEq4nW7IrZisTxhm1JC_A1l_hvyitQqOkR7uZiY46l9ytveVVVXPlNAfK4sz_izKh9EzLV_qJyM61bKb5uqAQjHBP08DdRgoN0Sxn3CrntoeC2x2UnoReMB0OADZeJ_QdPpeCRSuazVxIu0vCY1_fXx_qGbAXZlEkR31tTzQKTXs7argKeRBFhMeZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=JHEEmWgoDvRzBxHt1BUmNq-I0RUkXH5rapOIz7VOED1WUhsMSrW1Nyoe9aUdc2R6OydJYvrKM4DDVdvDJt6RLQWygqQUEZ0h2LBvlHVuT4Qut2-WisrbY8AL25gZYtbbIyNLtvmHL0W3wXadARrq0jGDbA-IUDYWJDt475uIsAEsmUnPy8sKPA-7GM8JrfZK9iKm25Rw7ocv5f0c1NHSD5oRZw_EbiEmMKHX2IlCYLF5FDOaVf3hYNRc8VR7DtS_fvVyq7TR6c8NlVAd_03V0vHevAn0LQYHuxmDJizdbpZ4OaPqu8bdy7yVCjpzUkQLQgNKCmUaGHVDFjuWXOHQXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=JHEEmWgoDvRzBxHt1BUmNq-I0RUkXH5rapOIz7VOED1WUhsMSrW1Nyoe9aUdc2R6OydJYvrKM4DDVdvDJt6RLQWygqQUEZ0h2LBvlHVuT4Qut2-WisrbY8AL25gZYtbbIyNLtvmHL0W3wXadARrq0jGDbA-IUDYWJDt475uIsAEsmUnPy8sKPA-7GM8JrfZK9iKm25Rw7ocv5f0c1NHSD5oRZw_EbiEmMKHX2IlCYLF5FDOaVf3hYNRc8VR7DtS_fvVyq7TR6c8NlVAd_03V0vHevAn0LQYHuxmDJizdbpZ4OaPqu8bdy7yVCjpzUkQLQgNKCmUaGHVDFjuWXOHQXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpFqKU0slCvJ-bfuKz98uwEGnSoXJp44BGFoClw0h_n4RbLLCNLgIkI4JmZ6ElVVyt8iTVRGzuzQWjQurIDW5zJuIV4ygO17SPtL9G0G92GMSmNtHLHpO4utqZGjB3IYq9tS6R4gsyN2P7j1urwOj7VRfsBJtlz45c3q5kZBksTjNBvJhWZGUpZqYMMigKQ5w72se78pa-Qb2wNgYGvca_qFJGL-3Uv3ime70RswbihmFXXDPdt6Pd2878WCQ9KC9ak6SHxhiu_gWaEvoVz-RaxOOC09kk9fLxwO4Dflik3aDYetdX26ocFT5Yb4Vgjk0Tlb5e6KBEmWYt25Ye8x1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSiF5dVk0agc9NGZqoCxWb2iY5-baoEFbKNhZVU7Z2T5TQLC6KqRBx_pUJ7jOVj4UARJHh3BbJ5UhRn8_ix5vFkHrpw-1Mq9BEF48B-kAaGIIWeK4xKoekBnRBmeJE4VDWEfq_FpUpmjwZwp_P1uew7bD4eQWFGH1rbbya2k7NgX-Wss2LTTBsA0W9VpknjxM8tKKp1BSBEad_ZV_XGTOW9cifxaO0ZoTXF6qvLibhWEvddF2B8uJV8rXijG8n5VrhdIh0j-e9oTrtC1GSZWIsKSdB3favqmynLd1vvyCHNX3nL5pTsgLUCHGeLVzXtH3tPsVaEELVEIg1Ffft8-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=O0g8YkwdA0pinxYeZEhdsrU_y9nnvsfQX2-Seu_HnedVeSHMSSEMueOhYKRPSX24y9GXgRlROpZsemCxf9K5vBJWdC1Ja10ta7TAydcYHJrDbnBSiqiEDWhr6mDOSnalts_Z0DVHXMjk30sPwOCBJzivsca-OIkGgAb5ngb4n3i4cJv-I-fwRO_DzkbwDPNmbTtWyddPmw7w0n3DtrUANAB4fE-YVTqTLxwKreR1-SH_Ksiz_s-He-WdTIgA8s6BI-Lxundzg7fbBz42n19Iq47nd_LvhL7AkHuFJOCjhkKt00V_st7Zoe6lh-VXHqdmG4uRjcxoKvwbDsL7OBbCig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=O0g8YkwdA0pinxYeZEhdsrU_y9nnvsfQX2-Seu_HnedVeSHMSSEMueOhYKRPSX24y9GXgRlROpZsemCxf9K5vBJWdC1Ja10ta7TAydcYHJrDbnBSiqiEDWhr6mDOSnalts_Z0DVHXMjk30sPwOCBJzivsca-OIkGgAb5ngb4n3i4cJv-I-fwRO_DzkbwDPNmbTtWyddPmw7w0n3DtrUANAB4fE-YVTqTLxwKreR1-SH_Ksiz_s-He-WdTIgA8s6BI-Lxundzg7fbBz42n19Iq47nd_LvhL7AkHuFJOCjhkKt00V_st7Zoe6lh-VXHqdmG4uRjcxoKvwbDsL7OBbCig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=cP--Dkq8l_QQ-ip2ioU92TzosYyPl-2K_uhUXaoGqagWZchDE4MhKgcZeu5rapGfhGcSQ-01MStG_FyYlQd_zA-unlV9Vs2FuBAgQXHwosjVeKwHD9cYJ2v8Os9Pri1D99cKVsJUfqZPLiLKpiqqZJpAuAgqrlyuGWwk-SyaIlu5K5tzCczZ_R5UubF2SUO4GQrZT-uyjS-b6QtYjLLoCMimOWAPjY7IM6QE5A4XJ8N3N37dj2vCWiN9w7LhmEZ0gmJEiMvToG1xIEEaooSEiyRzwSaiz0gO_bjyHMInFShaCkSTvH2v9ZiJ3z1lNtfYVPMM1VSmaeaXfDuT_vPomA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=cP--Dkq8l_QQ-ip2ioU92TzosYyPl-2K_uhUXaoGqagWZchDE4MhKgcZeu5rapGfhGcSQ-01MStG_FyYlQd_zA-unlV9Vs2FuBAgQXHwosjVeKwHD9cYJ2v8Os9Pri1D99cKVsJUfqZPLiLKpiqqZJpAuAgqrlyuGWwk-SyaIlu5K5tzCczZ_R5UubF2SUO4GQrZT-uyjS-b6QtYjLLoCMimOWAPjY7IM6QE5A4XJ8N3N37dj2vCWiN9w7LhmEZ0gmJEiMvToG1xIEEaooSEiyRzwSaiz0gO_bjyHMInFShaCkSTvH2v9ZiJ3z1lNtfYVPMM1VSmaeaXfDuT_vPomA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3xDAiY_NXBCKY2g2J0y2GpG08VCZnoiIyZBTHkDl2vUj1gItEYsk0HASHWfOnsE3CaLZDczkypK5S131MzuYaqzoGaDmgjBmVHa3viOcRZQnklyLliHwO9AFsCGdhqmzEmP61XYqMi97Gq5RPCsIrDUoe2pBU1WHFO6GnNl_rHheOYiI0lZQHPzyrneQJF0_z3oN8SRK0eKVpMKMFn0jx8xL5VZYtlSUSHHHAEAe1c_GefbH_xg3rl5MzsBQaiyssxsSRXSd09K4Ytpx1UyQ0uDiLU-PtVjekF4v-EdcO6ByHyMkGkhvc3oWbgKNZ93a9Uzr5UtH5OE_g3s-pdFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWhdU7MGEiWZIguIJTXXVB_kOeTHV3cvKOAoHy20LN54yWwnqkoT4Qy44xElwf7P5HcSo6vuzGCR_hY1MqF9WnCAl8UoQOtoX2n5vJoLOXVdoI3e8eVH5Z7ZWkvnqCGXLqy4VQSbXC2a3Hq9qMV9Q31qbd3zByFULnkUHQKAuyZHeBAcU2hBPZd6K8Pw55PuzW6XpoZ2o3JyQ0gxZBSwqcK_FruG-PAdvdNUq6Td1z__WGjGVijvGn_j5NjdigSvvjGFxjLwzZoENtW80K-lXzOdu5mi4YMoKIIkZHYdVfykfVTip2iV_SwJhuUBjsDcKhni64rhix4YfJ8p8x3Buw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvcR-_hHpVI42v4Da8MqDL5fWi65KUnAPwtWcR7fs3QPQhwAuHSAZCrNBDV0wnuOJOy9zNxNQcGOVTw9-qD6hOpdEhVdUQrgpn177fujRL2j_GK1CQjZvlAq5bjkFDQHXAKv-T822H1lcSW1XmiDDBlLCi7hsgMOcW8-tQzdgwwS5ltQAVXIkndsIPRSFLyjNhcuR2OZDqLwxb_75_g6LK1TOA6soWIPxDE9Lh1hi1zXdrswpSLjgmP2bXjniOaUMbYZi0TVaP6xoEe637qb41RroIWBT7q6NRMbYhCAUhLHYj1mrYpDDBIury32IBOH6mvrx1DNvnGfLbVUg84t5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=BkncxgDfASmX1yabU5iRTXYqG9FVp0KIOSo74QvI1qqJTYnqdEq8jUzJmJ71xD76zsR955O4_gaKuYjLRBcWqyCj9QRqGuXHIEiUKYmpvALuJo6cm7fpGTdmLeJEb0exNIQbSltf_9yCQtNv50rH48o0Ys2nXk_5pGdzISdkfdcmgIvI0_75itZGQUmy_QV1Vb3HLjH7BB8jlkPk3oBc0ZvpSDKDI_QcHU04f7n9NrsgOSetqHboQC9NgTPhAx-kEdA5Z1y0lzjyOxwy-jVAkOGMNYYb6DnGp0v9Hjugql9m28HRYiK4JQiZh-kO3sCcgmGypVhtu4XHEE52jsL-lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=BkncxgDfASmX1yabU5iRTXYqG9FVp0KIOSo74QvI1qqJTYnqdEq8jUzJmJ71xD76zsR955O4_gaKuYjLRBcWqyCj9QRqGuXHIEiUKYmpvALuJo6cm7fpGTdmLeJEb0exNIQbSltf_9yCQtNv50rH48o0Ys2nXk_5pGdzISdkfdcmgIvI0_75itZGQUmy_QV1Vb3HLjH7BB8jlkPk3oBc0ZvpSDKDI_QcHU04f7n9NrsgOSetqHboQC9NgTPhAx-kEdA5Z1y0lzjyOxwy-jVAkOGMNYYb6DnGp0v9Hjugql9m28HRYiK4JQiZh-kO3sCcgmGypVhtu4XHEE52jsL-lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eC1cIRQ0ltS2YkwekkLsjJOAUUHQcogl0xuNw18Ep43dYu1wzWjy2CX6XO127sgLefulgdLf3cVsyo8sxCm-QDdPg1HzXoDB7rFucC7lDmOeTfDdOygXS4p3EFbJ3Fi2zqfg6ErPMu8jDxoPoPGT2Tk6WauM46ofT4pKHq4Za9GTQn3OcZFvLOg11LsGZF1UIeDqeFu1K1WAhFijjZMGdctGCo-kuXKHmCdgTMir0kM3v5CnpcdAovks9i023Vng5NNdiJwXNPp1jV3LQmZs4j-XjNKzNomx8wCBwLW87qqEfTWXtTp0uZlKv_Qud6brB80vVIRUrXM2bcDXQn6-xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=WDvaSmRcDx9x1ln3-aWl78M_iCIWOUq0XFYvTSwLrPzyGHEe5av0vvMKLVpxKMGFYx-KwtAEGaFJ4SSQQgry-HMcObgXk3bCcQOpzLoqUaywHBoPLU37aTzotxK4OUENITDqPG4mLVejs9GYwbtKig_dlRA00VG2W5o2Lnt5cJIhGc9aHqetR_-7lKsS_-i-kvmYbhWzJszgcaU7RteylQRzvZib7nZa1vEEGsqEWItnYpH2T4_gdsgiDYa4c3BgNvh8x4LqASwJgIG_1daOaOApfktTR-PEMlbZqoeRi5Px1vuwisAsd4SiNKo96HQIjOEhJ_n6xIxoM2sGNnh2jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=WDvaSmRcDx9x1ln3-aWl78M_iCIWOUq0XFYvTSwLrPzyGHEe5av0vvMKLVpxKMGFYx-KwtAEGaFJ4SSQQgry-HMcObgXk3bCcQOpzLoqUaywHBoPLU37aTzotxK4OUENITDqPG4mLVejs9GYwbtKig_dlRA00VG2W5o2Lnt5cJIhGc9aHqetR_-7lKsS_-i-kvmYbhWzJszgcaU7RteylQRzvZib7nZa1vEEGsqEWItnYpH2T4_gdsgiDYa4c3BgNvh8x4LqASwJgIG_1daOaOApfktTR-PEMlbZqoeRi5Px1vuwisAsd4SiNKo96HQIjOEhJ_n6xIxoM2sGNnh2jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhkGrg3EFq2NWReorzC9T6x35AdiTX6icqqc7cnH9vOOP-dFODqa0f-gSz_ckBLGrSO7no2V5GFsP3yFpQTtsJQykweDkAOPUYja6XIY22TIImu0r3hXwQeL1_ZpJB2ISvYz80_h3Yz-JXh3hfF4IbjUlNmC5bibGCQ00V0LVtyPyFnhM6E2d6y1_y-KoZFOQC7WsSSDoYt8_wFpi8Jcl4Svi0sxa4Rm1Onhh5DLujyRPJmym0ZB1am-E4uG_3MTAUFWbpQxKqS-O_idav28jIGuWTKxu1ie07Br0SSXzFM1I8H_iTPM_Mskt-n-60jBmQya_L0AXRxaw6CWnNRcKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=Ckg6JCrzYUyhfRR9YMeE8eFAxVzkFeUUIda9FWfO3lTymT1toFeDAyzuBnsTTzTRcDYVSc1MExHLSw-hAU0mhCI4vxmk_6K1Vdj926GUra_IoHsP1310NiPW0B1kicP_5NPz_ZMbeDKZjZ9zU4ilbZCacHfbHKgHg37rq42GbSTzXjHSRPbmH13RnpmRBpqlwHJCG6cv2IifVVbCm9otoaMuX4zkCaYp5jFtkUZEPkSk6ph0-fNM5RyXnysCMI_iM6Y8BGb6kA1cQNk-7tk01cCmJF0ES2CE7sht-5bmbmC9iX8utFHfzpIE57AgT57YxBWEUwGPd-Zg5gTJsQ-UHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=Ckg6JCrzYUyhfRR9YMeE8eFAxVzkFeUUIda9FWfO3lTymT1toFeDAyzuBnsTTzTRcDYVSc1MExHLSw-hAU0mhCI4vxmk_6K1Vdj926GUra_IoHsP1310NiPW0B1kicP_5NPz_ZMbeDKZjZ9zU4ilbZCacHfbHKgHg37rq42GbSTzXjHSRPbmH13RnpmRBpqlwHJCG6cv2IifVVbCm9otoaMuX4zkCaYp5jFtkUZEPkSk6ph0-fNM5RyXnysCMI_iM6Y8BGb6kA1cQNk-7tk01cCmJF0ES2CE7sht-5bmbmC9iX8utFHfzpIE57AgT57YxBWEUwGPd-Zg5gTJsQ-UHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMb1lPUMedHtEK3rU9YTn5wkoxAQFDo5dD_hiuTS3luzKW_2SOsfqsNSUXMtICMFsEZABzjRwSlnnWGLnIRNgxqkHoqrotzn1WzN-R3NUc_2h_ECtLX5VaH90xljmqsb6emtg5dRopeml0V6qL23_yERKxfEx6eg_UcVFP3jG2xZjBW6FC0ouAnAQJ3X-rVcrq2-mukTLs6-qgDsCtGi1llpg-mbs84eif-zN70VUcCmWOYza9rTiNF6K3ITeuOlDGhUMkO6btxw_RQXXSQQjs9bHpSRhvmpQ6bu0R85HZ9F0tGjqiS9z4OV44P9PVhzqBNCP0vpX81AcWy9rqdKoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSjnSx6fVvcYRBBhbDOszf6zz6VdEEDCBM_yGhiFM-H8jgkY1xWJo9ahNynl0oDHZNHLS0PQaM_Hrhknqgjzn1ZajPuuz00KgdDPYlvwSTsGzaExpCgb2_DKtFRmTuFaRyZFBNnw8d46JrUgaLonKMDCM-tBim0atD_K4u6lNQghS4zpL1nyZDvLN1KhJ_9xbWSe47X_g-rDI2EmWZuc-mMhicrrowHftFqsSxASbr0zA7_J2i-FqSqa9-qPuxV5uyLtuTcYQKkp23njsPiG0XrNF9RFEreMf_6JltF-McEJ1w-Ov7uAQ2FI10WdRxbN5Ns_bE_-qXjqMVsy2dFLBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BukHCi__7WZwIHnFNH-PMDgIgpntyYPBsVWhbd2AkevHKcVVtqT3_sdpjL5VJjPkRnfutlGttCGbWV-yi5aL4P_LE_4uB4aSp2b1CaEay_RE5q04DQP00ZrWUA9A6EFhwNqyotYp7vU02mJnkwzjUyVOG_ZGynfrb71XCua0bTyJymBy7u-TCjFDwQcyZwfmnuMC7wA11m9z0ZN6XEYH_qfT9DI4i6bx3QAdaguqsbMxHn3y09we-m58sBTLVeGc8Ttn59U0b2e3KMV8LuNKY_j-AvkDgCo6DNirqlXlVnv0cBZqS_gJwr9INQVH6AR_88xHmepP10wf4iAENol2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jppV_FIatoIJgvO8gLqTswEiY7nM641Nd_6Ws9odlKJPpSsTRrMoVGgGNWck6HDYfSeJVMaVjDfJl9derwJ1K1he-yTILcb2Cue7CU4wLRAN6yzBNRNLGRB6AdolOZ-N1v3NmqHedzXSjbPF3OQAyH9D0kpqMUJiB_qm_D4LKk3d0DujtlxnSWcfbI5NhHrDJCGZsC1-FGUdCPRRPinIgjSC63iZzsQF2AwZww6_4FdpAFEpfef9y7gKpKbs4v5Jckz8nYECj6ah3RjIjPvDR8Un6qrJmaavxoD_Ymp5jBiNmuyuOLEDbVPNYoXwX-btF8SWh9JWwiu5XzT-G8qjUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lg6jPP8fnAWIP2Jgy66k4C7DPwYJFtmKxpyIJpZJlwKpSjgS4trNht4E4lYmDxp4O4zpazPicvnCiSI4iVCkByRfUoP75SWuaUrsedlCOq_hrYV1Cpppt66CrOIBJxXwLPiFbISOr-H5Jd0DKtHfXNSXdDfTW1lt_KWjvVyjAUh6ER_kXIQLhD2DabbiC116rPE8FoSQOsUuu0faKFHu1lV4m-SAcOjTTYoeQ1hrhmXL6QVks5jMLB0EN9m-4taihNq-owF2D5oekQR-we2sa4ROvxmfa_6JvdgU6I7gaXfX-D3VjEXDXcJTeLF4FgRUWAe_h15moNklw25U6Sqdsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=sWkjo13pduEyKNOpyDCz8MMXe60fXMDflEvjJFkXcRgkpzlGgC9KWlgPp56wzHcgkmwkQIhTAdATPGvRLCIitS_HOdx7nf7CjwquLyOAhv_4oR2ws6rmPNEvVpQzymSKArZNt9LFIaPJTlr20x8SfMKSZZm7SHmbMHb7siCIF7-_G_5BSOKNj0oskssvaoqY4ta9wiYhQ2fyRxJDHsvcg-b1AcCwoeXEVioW3dq5RGBm_6ochoT7qX0-e5PzPr2jqnY8QUjoBIVajFwNsYenaoaTVdIrr5qDwWQZwQjTTa9KE3xuqUJn2eyt-GkATzJbd6gU7rjHUSCbd4RCBVK8DJH4hPMEIRPOE-3KY-BCNpb_2ed4nGYK9o6CYofjzZkHTp4KwCYyPXorN0orbJDZtbO60zxvqaj-OPKh9UySEDnHmEDPnLGuo37gMpYJEMdVu0MBEEe8ZmcebbA02fWKvYx1ijgNmOgNdgAe0_De2Tn7Qn5MX7i3Cr9RigIOMp9YuMwi_KY1zZafACJt-T7AIXHRBp_L2aUzmUATRhhTxK_qvaqXh_yKMPcn9XWKYaj0KNHnPsamaeG-KZ_D0z7jve7_54U1i2PuAfQmOo_1c5o4pkGDAqK1_ILCykAbHJGGp6wMUFrSpH_e1wUHBc0Ms2J4oh-KZJ6yrIZIG1FdNo8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=sWkjo13pduEyKNOpyDCz8MMXe60fXMDflEvjJFkXcRgkpzlGgC9KWlgPp56wzHcgkmwkQIhTAdATPGvRLCIitS_HOdx7nf7CjwquLyOAhv_4oR2ws6rmPNEvVpQzymSKArZNt9LFIaPJTlr20x8SfMKSZZm7SHmbMHb7siCIF7-_G_5BSOKNj0oskssvaoqY4ta9wiYhQ2fyRxJDHsvcg-b1AcCwoeXEVioW3dq5RGBm_6ochoT7qX0-e5PzPr2jqnY8QUjoBIVajFwNsYenaoaTVdIrr5qDwWQZwQjTTa9KE3xuqUJn2eyt-GkATzJbd6gU7rjHUSCbd4RCBVK8DJH4hPMEIRPOE-3KY-BCNpb_2ed4nGYK9o6CYofjzZkHTp4KwCYyPXorN0orbJDZtbO60zxvqaj-OPKh9UySEDnHmEDPnLGuo37gMpYJEMdVu0MBEEe8ZmcebbA02fWKvYx1ijgNmOgNdgAe0_De2Tn7Qn5MX7i3Cr9RigIOMp9YuMwi_KY1zZafACJt-T7AIXHRBp_L2aUzmUATRhhTxK_qvaqXh_yKMPcn9XWKYaj0KNHnPsamaeG-KZ_D0z7jve7_54U1i2PuAfQmOo_1c5o4pkGDAqK1_ILCykAbHJGGp6wMUFrSpH_e1wUHBc0Ms2J4oh-KZJ6yrIZIG1FdNo8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برسی‌کامل‌ودقیق‌شدیدترین‌مصدومیتهای مرحله گروهی جام جهانی 2026؛ عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=NllNpWNYuXdCW2lsGrtwgIfipu-T-RslZydKUZ0vmdkpEj9KlkWayndSY84O7lnrkvdsE4yRFxh9iVja8sCxz0rx59r5UsX9LavLDjEC9N73kgiWDo5ONGYw_IbTWk-CRpqCE56SK79SA-D3KDkkShupasaJquURmCpdsShDVJZKMVX-zCDNr7fooE5ukWqguZG3EWAMOK6CJy-cO68Q1XbyywNgGEtn21MwrwOTcjglOMEqJwLjUke-pdkSNt3_IgvLMNl2qL3YFE8PJA5zSQn0PcHyhtmqTw5XcxXQ5kyfVlvXNBTIgoQRKue5pxNwu6f4zBZLZidxANoDpGTwCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=NllNpWNYuXdCW2lsGrtwgIfipu-T-RslZydKUZ0vmdkpEj9KlkWayndSY84O7lnrkvdsE4yRFxh9iVja8sCxz0rx59r5UsX9LavLDjEC9N73kgiWDo5ONGYw_IbTWk-CRpqCE56SK79SA-D3KDkkShupasaJquURmCpdsShDVJZKMVX-zCDNr7fooE5ukWqguZG3EWAMOK6CJy-cO68Q1XbyywNgGEtn21MwrwOTcjglOMEqJwLjUke-pdkSNt3_IgvLMNl2qL3YFE8PJA5zSQn0PcHyhtmqTw5XcxXQ5kyfVlvXNBTIgoQRKue5pxNwu6f4zBZLZidxANoDpGTwCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2wTbf442eh6fLaLRnvHIoTIKndD2ge9Li-X0gie19anuFTBHXKwWmG8Nm9mriRuA2xr5G6qNE7jJ-7Z_mlEbN_1QzLMFDVnJDgNFAHftcssDtPYRsXgU9ODYGObCCFBHC03myrKk5cu7ccVk6yldmEckSbEz_WID6-xtAjlE_ELJYPoq_73ONQkjPfSMj0kovJlsDe_bexhhTjIfBHY2LWlRKN4coWFJXe4RzUuj1vtVGaiiALFf-3D_EV9pph8buwcLUvtu4q-2pb1aAmdrP7sBJWgIGpgbNVrT4lRsOOHfICtihDV04fHrizN-KEPAoaGT_uucb23RcCYcO9VBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=ad3F-LRxq0dHr7c-a6kervi74c6ladzGeQqc45v3n1NedA0X0Dyw1xpdYJYeJMlVl-iZ7USwtJrNYd9m7n4KfXK3h-lyO6ub0M-wRrHZSE4euat1PAve6qJ86hyM-kCyUkgAx1mBsGCzbAXMtJ6AWTsaHx6aDaVn7pKNXYyn0EJlZounRde5tcfBTb5AARGDJ2-k_GCNxZ_tTGcMypyO_D6Z9aOLhk-lQVJdo4vUHwQBXH-qqBlk_qGcqJY1gaD5yKehrtw0-HSDiw3DwmMZonT3l4b2lkubi2cAnZ8--qszf2PPaZ89dDMTJjEvYlVEuicCYQoOsAHzfrAL06dDLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=ad3F-LRxq0dHr7c-a6kervi74c6ladzGeQqc45v3n1NedA0X0Dyw1xpdYJYeJMlVl-iZ7USwtJrNYd9m7n4KfXK3h-lyO6ub0M-wRrHZSE4euat1PAve6qJ86hyM-kCyUkgAx1mBsGCzbAXMtJ6AWTsaHx6aDaVn7pKNXYyn0EJlZounRde5tcfBTb5AARGDJ2-k_GCNxZ_tTGcMypyO_D6Z9aOLhk-lQVJdo4vUHwQBXH-qqBlk_qGcqJY1gaD5yKehrtw0-HSDiw3DwmMZonT3l4b2lkubi2cAnZ8--qszf2PPaZ89dDMTJjEvYlVEuicCYQoOsAHzfrAL06dDLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=GKVGaJ02oo7jpWN2jDcvTUl9OneosUS7cJfdZS_wezDMND0F5tLC9XQ8y_kq_Ss_oYqWA1td_3a7e2Rc8OC6UR1V3kpWSVrcXwIOJh5LbjrJVAPa9gekW-YWf7aZcCBDTMShCAcRKfFvE4qGFhg26-_g7EOJgilZrxhVpvdPRGMVTX9swQi9rppVNL39eZzmMvjDEd-rXpdm80r0Fi4SJ-TXSvhyHeSWDXvLNw3nAgDzCCr82f9g_cDgLvBpmbaE76Wwhh-7xAQOA8s4jqAJ2R4pFBJ9kLI0qEoo-AkqMaP0jomfqlaH5MfvrWfwTAW7C_G0TLBbvU6p70mWXFFCWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=GKVGaJ02oo7jpWN2jDcvTUl9OneosUS7cJfdZS_wezDMND0F5tLC9XQ8y_kq_Ss_oYqWA1td_3a7e2Rc8OC6UR1V3kpWSVrcXwIOJh5LbjrJVAPa9gekW-YWf7aZcCBDTMShCAcRKfFvE4qGFhg26-_g7EOJgilZrxhVpvdPRGMVTX9swQi9rppVNL39eZzmMvjDEd-rXpdm80r0Fi4SJ-TXSvhyHeSWDXvLNw3nAgDzCCr82f9g_cDgLvBpmbaE76Wwhh-7xAQOA8s4jqAJ2R4pFBJ9kLI0qEoo-AkqMaP0jomfqlaH5MfvrWfwTAW7C_G0TLBbvU6p70mWXFFCWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz3PkxJs7Q4T2v3OSepRDT7sO_Lalof20ETP4EuR2IC051NzAK2TKQrXXPM4lcGr6zwBKaazvQ5x5XixBMwdE9kk7wrCBM37j3xHMtSpNCZME7yCbjFVRgqByZqdZ2MdWstuy9_LR1meq4vACmjV8Oc09JESbT5wdOM3PoVGiU-BCZYYrb_1Wg3UPYmfk-hqm0DmStG4rJ0mk4KdRskDXJW58aGqEjSntBKwhr1eX42hodKMn5g0RiCSN1cYAQcyntiyxrCfL0bv4k2YI1ZiaHDZH2cD97EUhX_d6S5KE28aYWaEZKBqD3zTcUV1F8Nsw2dkMNMLg6b20rQBUX2NLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilkxY9rRr43CWNdYEmtsatPa2KiFYvRKb9r6yv7muu0etvbiPLYMPLfHDYggEWLDlDKgJDzmzDx_1nm4KE_r4mew2pbtRaiimQU7hPnnCLyxz4iUs-1RlwU-lKxWIC2inXHLI4qHnpyvjSe-InlTkjT4lRM9llEqwE8hSh4ouslZmrHWX5mHrAh1bNDQSkeQWFAMMPsCjimYejtumI2k5xUQo8jvTHM_GaWfB7rKz3ZAGrR2EQYDuCmyJZdlt5uklKLmcqh4514QijZF1EfBCly5cAn7i_kBKOOO7eFd5lPauPwMJOt4pmvsO-rlGIfOuGfDpUD120OcpQVyLcCGFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCSxary7KnE54dOkr8GwA7f8vybhONYFDoJXIAa5ZE_ohIjBMH7cJPKArbLgSLq-Tt7T_vjguw9CpZPoH2ITTTzf7hfMKZJrXa2B-Il-MMqVPIJpqV-NBMF708tOHJfeLe9wtGAKhAfJoG91CU3QdEsze2w_FJ_nvl_W5KncnjADYivBSl3LMHV68CaE_cBbFV5qbM2gmJYn1jjfdDSevWc4FTon8rKe0cwJc8HJXkNgtHdyG8O6Isi3sEP62y4afbOXLJxxiOA0fZV75qm8rnOJTC6-w_KpYawBytfsX-rUNXgqyReOyOuXYdC2IL-o2tlAJHeSG4kk_wfnM-ViXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg9EmxWVMoAfwk_SoTp7yWdbdIeSZyBV4gr81sbeaj8K1XALY_OS14cXfMr3ZaPbKzL0LPsBXXfockZHeGEzpkzug0ZkKGgh3Xbw_QgEbMXSBr4g0VdrNAKTSi2d8b0fTBYbx9OBFUlt5B7wzDpM0nFBqBtk_oCVAXRuBzDJ9je72g6guk7QyZLQ0IrA2qys1hQd2UhavwQhZnAQr3KqecPv6uKp70JVOS8DTQvVKnmyFAy6rqdK-Ub09x5MbS_NbatQToVFh8tGejw_hRuMk_vp--QluXs6Rta1Op3KiVdqUbvXO7kP14h76PQ2gkWuyqIFiS-ZOalErlfupqsAVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=DAvdUfUR9fK5ptgK6HMUCpcDw7b_oLoal1LKLf55GvQO3GGq01hb10A1dbx2JhAUSgCcSNvkuGc16szvuXcUs-VJYIPCvmKzHeGgmIchLfZYzIOW6zW9Hrcn8Y2dfxaco80MFI9x8eMeMA-jQE9rYHkg1_I-PrV0j7rPHt-XJKI7zZcddwzghUK4US9YoywNshOCTgD5bKXxPJYNAnmpNE3KwSkLLiyDAhOF-QbGTBI5JY9UQ3JhFtkI_T1khG2lZhLPHdRxgNeWI2EpesvKyDIl71Q0d8GOxOg-5Mtp4ByCZ5dKJ3FACrQxqNWH0qfA7alnrmcYR5gAF-w0jLPTqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=DAvdUfUR9fK5ptgK6HMUCpcDw7b_oLoal1LKLf55GvQO3GGq01hb10A1dbx2JhAUSgCcSNvkuGc16szvuXcUs-VJYIPCvmKzHeGgmIchLfZYzIOW6zW9Hrcn8Y2dfxaco80MFI9x8eMeMA-jQE9rYHkg1_I-PrV0j7rPHt-XJKI7zZcddwzghUK4US9YoywNshOCTgD5bKXxPJYNAnmpNE3KwSkLLiyDAhOF-QbGTBI5JY9UQ3JhFtkI_T1khG2lZhLPHdRxgNeWI2EpesvKyDIl71Q0d8GOxOg-5Mtp4ByCZ5dKJ3FACrQxqNWH0qfA7alnrmcYR5gAF-w0jLPTqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq-36waCsyaN_LjePpvfo5ypxf0gzhK8zpJW93I7UVchTZxlPJNpl4xfhynYRyRWl3NCcsn9HxKojP56GJw43vlGQqnqPooDZIJxeTTXILq5TgaTTmBP_2bPY7ULSpUzJItgRBI-_iTH6_3NHBXrASeOJygqbkefz_CXR4-D0kPtX1EAGR0YiSQMXjs-xkti-NVn15hx-NX3WNl1U76M3r32nAPF1zbqxFv70OEBWKJkFh24bBVjx-KkVh1U6DNubWcTxW_yzve26e_ovgLyC1k-IrQObEYxksyRTYuvbZZMQTkCyE-UULsrqZ19vGiwUZb5kxw5dtbEgiME9IS9QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHNxX518_SNap_R32xfJQc-9E1osuBrg-Zk1F7A8M0oBArPBf0Hz3KhNdM6vjyChjOlfKBtbmDqs9skPFO1eVtAHluZHAJnWL8odS4B9X2eQDe6Yfsp3GpfrFWDLigdeOfqRA5ERVZ8gi0RnxVbelc3y7YQHNPWmbPYPZ6GNVL26soyGnApyGcnGFqZfxwyVgjeSkHuIFi7q_A2WShF6EmhQ5K1d7Ieny3pO4uqvGCaPfddl5ynsQ3UIDSImwUOPWxoEr8hfxnwQWPwl9_gFPlJT6tU0qjuu1OP_t8DWLIGOhFv48kn75ia7sGo4zcxvv5p-FH-d7Kc6Ok93T2Y3dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره مراکش در جام جهانی ۲۰۲۶ و بازیکن‌باشگاه‌پی‌اس‌وی آیندهوون که اکنون در آستانه انتقالی بزرگ به بایرن مونیخ قرار دارد، مسیر همواری را برای رسیدن به این جایگاه پشت سر نگذاشته است؛ او در ۱۴ سالگی به دلیل اضافه وزن و عدم آمادگی فیزیکی با…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24742" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=f47Po6FxvLYAcxJoYUWWlEKvbKp-LnU7GK1Dujmplk37oEJBWi53KLlJlCBLVGa9rDDgwlrI-T1VhKuRr_Knhmskpv5XcrsIXjmZTgDGPV6Yd2rqxn4ONZ2v82CND-SnJgjM5rekIk7N9QlXEEIHPqOftlrkGhFU_F1RRuP9lMFlHskV-uVs-5Nh-591Kabg_Nyp5aImJ9OHBMan3JfBhAEKivXHnUXMrPcGuo5bwmRHvnP7VK_YG2QN6L2NBS1mQSlffClONNCtU2pxOq7dDSd-0DwIi9K1n7S62UMe_fn2rYFyP-pFr0VFKiBqp88wG6ny4OTGvTlif2B2GlS-fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=f47Po6FxvLYAcxJoYUWWlEKvbKp-LnU7GK1Dujmplk37oEJBWi53KLlJlCBLVGa9rDDgwlrI-T1VhKuRr_Knhmskpv5XcrsIXjmZTgDGPV6Yd2rqxn4ONZ2v82CND-SnJgjM5rekIk7N9QlXEEIHPqOftlrkGhFU_F1RRuP9lMFlHskV-uVs-5Nh-591Kabg_Nyp5aImJ9OHBMan3JfBhAEKivXHnUXMrPcGuo5bwmRHvnP7VK_YG2QN6L2NBS1mQSlffClONNCtU2pxOq7dDSd-0DwIi9K1n7S62UMe_fn2rYFyP-pFr0VFKiBqp88wG6ny4OTGvTlif2B2GlS-fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ته این داستان شد عزت یا آزمایش ژنرال؟
امیر قلعه نویی سرمربی تیم ملی در جمع مردم تیخوانا در زمان خداحافظی: خیلی دستاورد بدست آوردیم، این عزتی بود که خدا بهمون داد؛ وی پس از بازی با مصر گفته بود گویا خدا دارد من را آزمایش میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24741" target="_blank">📅 12:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pcn-Cb-NA9Z35T2rd5I8FX5C8CVGya1eIwtrOO31aJgRfYf8WsvoKigw4E8QMdyu0sO_PoHTHv-2LI1ZBuqRSnSROO6xdZQTDMZqGkgdDN42hNubEg1DG-UjyfQmVQWm-yGe3Kbx8MhuJhZP096Zk1xZcUiw8MG_jTk0fvfx9XMocN_n0aQI1jvLV6ZwV_6Ukhg8V242C7yl73QBmmA_jw0LnSYOOrsBA1aXfsuJdYdE2Z_JkVsYSDt7VxW-fk2wMdddhl5cDi1aNgfEopqpwUfwmhWk8s7-pEkNSOMtQQ24mepF3clcfsIX5GIL9nbdIQ-9eqZVLgeAdT28d2xfFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: ماتئدس فرناندز که علاقه زیادی به پیوستن‌به‌منچستریونایتد داشت در نهایت با عقد قراردادی‌چهارساله به تاتنهام پیوست‌‌ فرناندز بخاطریونایتد پیشنهاد رئال مادرید رو رد کرد اما به یک باره با رقم فوق نجومی سر از تاتنهام دراورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24740" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECDSP5Q0EqUJOtzVKBVH7SzH4jXjzqGevaWG_YIo4dhfwC1Dw8YBUiun_yRTkD3iNJUFds-LAhEvL2Gal66ZwZktAiLaktS_ecLtUQ_gc4Z3wleizp-cWnD4cy5e9SiuVDeZUzbmlOuwogTv9-GRmbIJDyZj-KePyawfG1GwziuxAXQFhuBh6KQGEDCL2v2khHDe1JI6vTVEPI8yUZx31MCF2m3rTA805R3bL763qCvnZXkz2c9H1jzAnyvT9tTcZ160_VMyKnEWqph02H2kBuar97xp1LHaCJmwshQDEYLrVY038yctRBJy_tMx2nK7vpN4VnySHkRcwMjYhoZRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2016 دقیقا در چنین روزی؛
باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24739" target="_blank">📅 12:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tak_p0gY7EsYkhhc3-Nplgnw0YfgEe4-xQsOJueMfkrnIUGVuCwejTUupw6hRq86g1QQcgfGBiWTjpSSSvJbdzyjLR5lrPT7GUjBkP5Kg5buMYv0utVQmBuQ_G-XbJB_eB2grxbEGOlt2b1WM_H2XEtajrqPfMC2k2gEAsAQCmGyyImKxOeH_AbYzfLhir-ZM5fG82c4U59f7UT1K97rlXYLP7I9UCYkLy9XJRnDAKVaILRlAAfvqOxPpqBEBz4qzjuN15UcMk_qEj2z4B_bM-JPVTKzskPj3mSEx9OngD548Rkvpk1_ZFai9wY4X0Zk-qc5iDgQGQd35XEWI2wD1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJb-c46GG1PhAuX3Cpf0c8jmD7V64f7Y5Qirlj-Fbf5vJNpz2xAmZi4CUapRuZhFHN_uzSt1IWOwma6-h21V8eEjPybXqi1VBuZMGWq8_G_mGM24JaFR4DfLbHq9PzT-Y1ld9I3uC9DbqFHhg81-oce-n0rGM5_ySfX-fqOpPRqfWo9MNEx2AQVGzbyGnVNN6PXQeGefWGP5Sin5RUYzgVJU4e2ouuU92hNuzobNCdo7gcygfM_3zu3QAkiUtY-til2l1L4U0nToIXAMkwJCmKfFSOk_L9yd1mQYY2nEDs-80LymO-7NYYwDgMPHmKnRYtl-kJN6w7OhAt-ljVDT2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=lRgUTByCIV0WbePQGJq0jTn2ZJEUfvZ_obEOT0daFV4etFyp8Ef4EZt6dt_ktfvzaNT6pUctahXL6zMZDWD41MHXXLHg_XQ33s3Jw29sNNsDesALGYo5NnQPht_elwRswItGjNRxFBAP6WPOpcTLAvwEBXKrueJzCSp53vg2DfyVwy6he_RfEwYFa-uWrENh_ycx0ZNP_NT4O3QZH7yGS84IuAzDXvgpapLGVtPEtiqKTpXwWdSIT-k5zD6jpHJ_5MZhB0HEBZG7ahqLwXHJBTboeijE8QkNdk2t4LnoMm3gKBpV1WXEtuK86xCYgp5QEYsj0FYA-2Jdb5v-A2FCqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=lRgUTByCIV0WbePQGJq0jTn2ZJEUfvZ_obEOT0daFV4etFyp8Ef4EZt6dt_ktfvzaNT6pUctahXL6zMZDWD41MHXXLHg_XQ33s3Jw29sNNsDesALGYo5NnQPht_elwRswItGjNRxFBAP6WPOpcTLAvwEBXKrueJzCSp53vg2DfyVwy6he_RfEwYFa-uWrENh_ycx0ZNP_NT4O3QZH7yGS84IuAzDXvgpapLGVtPEtiqKTpXwWdSIT-k5zD6jpHJ_5MZhB0HEBZG7ahqLwXHJBTboeijE8QkNdk2t4LnoMm3gKBpV1WXEtuK86xCYgp5QEYsj0FYA-2Jdb5v-A2FCqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌جدید آقای‌امیرقلعه‌نویی، سلطان اعتماد به سقف بعد از حذف از جام‌جهانی با یه ادیت عالی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=KfJaDF5Ak7AVwZEwZ3LA-1NSbt25HMx2FY-ywEuI7LF858ZIyvQASPc4AUqcs30ALbw3CHx6_pVMmRx2kRGq8fa0Tyl3dTpk7n4opNSYHC4GXT7z0mknlqulojH_pKJgLySskK3WvXz7CWLjg01njXyE6Ea2m-kY-yErqPHYtJf13wx7ubMHafCSqFEb-4sFJcsm6aM4B3dBXaMrb-e9r-1TIRwZIHpFGop71HPTqsqWCBOZ1QVcyNHglvziEoXF2ZPb6foiR5mSKSweH_OH0CQ2VqyDgQDiJT2IEe1F9wGkEjk1ak0_HMDVOlKz9ELqv2A0v3sPgmJR0Q1EuLkt_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=KfJaDF5Ak7AVwZEwZ3LA-1NSbt25HMx2FY-ywEuI7LF858ZIyvQASPc4AUqcs30ALbw3CHx6_pVMmRx2kRGq8fa0Tyl3dTpk7n4opNSYHC4GXT7z0mknlqulojH_pKJgLySskK3WvXz7CWLjg01njXyE6Ea2m-kY-yErqPHYtJf13wx7ubMHafCSqFEb-4sFJcsm6aM4B3dBXaMrb-e9r-1TIRwZIHpFGop71HPTqsqWCBOZ1QVcyNHglvziEoXF2ZPb6foiR5mSKSweH_OH0CQ2VqyDgQDiJT2IEe1F9wGkEjk1ak0_HMDVOlKz9ELqv2A0v3sPgmJR0Q1EuLkt_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2iypPz0ulW0JLRBC6buAzky0w7cVWv4wvihVG0NuxMdAZkhsfRlGQIMaPA9ScaPpZxg892e_V79z1Bt-AskY0EYu23jk2tI61QVIukiqV73y--JVcRj5PGei8gJlB4R5P5DNfY4j9zt9Ra9u9KAXI_3G8624Ye5fT-hN3IMiZVM-GhkXSJAx5OeOXKqDnCv55C9P3Wcmbi-0KkzgKBsi78m4GBkrTolu3AWAvUThYvLzmFhKnQELbDG6GZqXdsimQr8mEqHvxBznu7Fb8BlD3wgGw4zGKbtrXiBiKO_Dwvd-Rwv32W5q5Y6NlUV7Z-eenS2yHfDMO-4N1IRkAKpjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24733" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=fydKPphHKg1XLFHbKd6hSZz6DU0AtOlB6e1xVtKNaGHEDopPLJn4f9hZbhg7q5pcTg9ALmrDjPxSC9pM6K0KG83euHj46BpoVwekRQPUusEpdqo5idDgMBLOnhoxkKZ97BhuDMgC6Bk7rgu8WKLaW3_Wh0MaQkdGf2qq99ZHhYNBBaon6CjtNA_agbrjtoh9pXCsrLJJ-ilDZ6fqyyCTWE3sczTyknpZvVrTep1MwRXLEn4o8pwbjxorVtKCDXtySC-SxZ9LxPVrZgsSv--ogXEvU0S5X3omYZXiNJibvieHq1Y3fd3F57GpEjoz1ZJm9FW2hWG2eY08DDU_ot2qWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=fydKPphHKg1XLFHbKd6hSZz6DU0AtOlB6e1xVtKNaGHEDopPLJn4f9hZbhg7q5pcTg9ALmrDjPxSC9pM6K0KG83euHj46BpoVwekRQPUusEpdqo5idDgMBLOnhoxkKZ97BhuDMgC6Bk7rgu8WKLaW3_Wh0MaQkdGf2qq99ZHhYNBBaon6CjtNA_agbrjtoh9pXCsrLJJ-ilDZ6fqyyCTWE3sczTyknpZvVrTep1MwRXLEn4o8pwbjxorVtKCDXtySC-SxZ9LxPVrZgsSv--ogXEvU0S5X3omYZXiNJibvieHq1Y3fd3F57GpEjoz1ZJm9FW2hWG2eY08DDU_ot2qWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24732" target="_blank">📅 10:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=n-e-oUsQDs9lvF4umuXQ2XIuNpl7MhqlSncaaNVA4duj2_OQo8MvnJW4T1Svu5cUoXA3lQrEghhsPlizFniVeTgR9SYxeNzaXCC5B8XWxXis8zf4u7yO0syWwDArnrlW9SPkWdXuAOyUvunYhRvGX19LkOFoMnseYRVcsDpwbc8IDhmIA-SjuWNVIAuQvD8yQ3ZR47tJEvrnSKCGQwalzE6tcRnz2F7wHTbqs8mp3EGQe1Q3BEskXDTSuZS1pXEFksnEeD6YzWlhOE-RM1U-4UdvpmOmomurPA4C7UuejVU7S3Dczv4FDTbjRl8Cs72cNX09wIOiiFJsGoEIsqXucQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=n-e-oUsQDs9lvF4umuXQ2XIuNpl7MhqlSncaaNVA4duj2_OQo8MvnJW4T1Svu5cUoXA3lQrEghhsPlizFniVeTgR9SYxeNzaXCC5B8XWxXis8zf4u7yO0syWwDArnrlW9SPkWdXuAOyUvunYhRvGX19LkOFoMnseYRVcsDpwbc8IDhmIA-SjuWNVIAuQvD8yQ3ZR47tJEvrnSKCGQwalzE6tcRnz2F7wHTbqs8mp3EGQe1Q3BEskXDTSuZS1pXEFksnEeD6YzWlhOE-RM1U-4UdvpmOmomurPA4C7UuejVU7S3Dczv4FDTbjRl8Cs72cNX09wIOiiFJsGoEIsqXucQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری
؛بااعلام‌دولت؛
سه‌شنبه ۱۶ تیر ماه استان تهران تعطیله. همون چیزی که قلعه نویی گفت اتفاق افتاد و یک هفته تعطیل شد. شنبه و یکشنبه و‌ سه شنبه تهران. دوشنبه کل کشور. پنجشنبه مشهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24731" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFqEN7-G165FlU1y4y2GCBtv5hmxDceN6e3g3G1uWwo1hfXhI9MBkYfkIY-dUus5uDYNfId-W5M0K-U5Dy-RN47Dz08s3pGVZI1P0e2iG2sL33PriOkcMw3GEfIY4oNWCemUkCtYz4z0uQzvwYq78-YE-4-WHqAF9K0iR5yzSz4omFpfheI-6ls29z_FPdllfrZtXNxosRzXjveoqU3T1sfei1B9r2VSzXvLSptnl1jlqU3P7Bu1jtStiSVa8K-osOlJwQIxR4OR6RaqP4obrQYDoiJu11oKDUYdd1ZYhMuWN_DvUArM36z7LRcMaZN5wtuGHDCSwsbUenJbZrmEvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ فرانسهِ دشان حریف پاراگوئه در یک هشتم نهایی جام شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24730" target="_blank">📅 09:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKxjlRialRXR9DwLn18kFJwfbmoy_A4CfMluMaQ3H7obpFIPDfJxlxNTwqHXp2v3gT5HIMraP1VsLa7apFvHZJOVsd_J50NBn8g4SoPNET5vCinVa0hD60XyzpfSZd6ipR8cdVNBDYh2v69earYLP2AvESPFGaVaqhJcPMkIGyB1ZK8qgC1oiEeIrzGFNXEE4IpriO7gxxRQQ41O00kHnXe9bvZXI4zoN_XIUQHIhoE-HC__C2MVs9CTZ9dhp2w-eRe81fHUy2ACnmUBJftDFs8HtER-qyHKSc9Qw8nu_gU6ROVuDCTbeMAZ6t1vfpaHCSgi7nrJ-cEQgNx1gGAC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24729" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdMml_fDAKtc44NAjatcMcYcvfZ4UEBClVtlTNaeilfClfrYsEG93kU4Fe8dPQslMZV0mSf7ofuIruWz9tAI9xzHRTrXAWYWC2mk1LPVEuPkxSsPoHa1IHbEE4jJoDU4K4XvhsnDq-vOuRRvROpv26mhGXbUPKJNWvy1637Wk-o-t9UDx3Z9l1fA3283Wh38dktnA4KE1d-Qy6zUaDZG75LAbRUmTCHOCdnKBZwzyDo9Oi34pS3qMVP5fF3dDbl2TueNnrvDBQz8g92O5jcFJf1--nYgVNdp8LPWFTy9EcqHR1mbCT7tWHLjMBsCFouGJNo7d_O4OYi8XOhMOKw1Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانردهم نهایی جام جهانی؛ خروس ها با درخشش کیلیان امباپه قاطعانه راهی مرحله بعدی شدند. گل‌های این دیدار دیدنی رو مشاهده کنید.
🇸🇪
سوئد
0️⃣
-
3️⃣
فرانسه
🇫🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u53IuzJHJPHmZmBUVJlyWo5ZuFCMQElM_w2byWaONHJfJDhV8eqhNg2ZDdVIJw6DRnP2CgeQZwf3wYY27EciI5swWvYyDW1sjuy9JeT-ErtvLRT8B-pWG7NWrCEcpHXLZ700AcZa49OiUPcQKzIu194PL9cAvG0pAU9wDNVm7LC6Wn7bqe2zMzHsJBm-2zZhQFLfDwdAOqjnPIp9iRfPXy3QE80cZ4WKPFbDFQgDUtPUNiS0bRv72Kv-zFX15xhFiaendOVPt_vGOXC03iULoDJsQ5dOBnuZfmsEJ3kkentgyovTdMbqEDyUFCU7hWP9BMyeym0zdirWw3xNExzXGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
