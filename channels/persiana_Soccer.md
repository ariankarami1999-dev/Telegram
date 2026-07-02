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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 02:04:33</div>
<hr>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anbSbDZktwwjSk6fK6Tbjpk7ZvTr25LzIuUTsMbFZVKyB_ffy6CnRn9mSOLP408mzumr1Y7-CC22VkNpZBHPbE7UQarrA5nYHNFXBc8iJL5kkynZc_HH5VCD8sLXoOX-eoc7hT0pFXBiRCib7dLY48Z3HdyKO7AzwXwlwXp-sLjAry1dnRCoI9ZLnbHJ_BF7SpWNwEuUjQukizbnO5u5tV0tYbZ2778R2yridNBLzRycgKLuMzx5hVLU-NFPXQiL6TRgRTmx4lLNWgHhCE1Wjlu-IFIgZbnhwoTUtvSBbYz9M75kgqkFhELQ-MWR9mkq9I2yVGLb7ZXsx-39NDzd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/persiana_Soccer/24839" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/24837" target="_blank">📅 01:12 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/24836" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/24835" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24834">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUPl_xPmE4s3_gsTHzlprBPaDb46Hzf-90HrhnyA9Nb1NlW4biYe7bcjsH6n8xhkXP_PvNrvoydU_7mPabEXhQLObpRngJUvsOi7SRLRojj-koDUtA8qMigCjkp6MgX4MjPDFMVWGLP1RQTSOw5yBFmyz9Yri1pkvrYL-pgcs9gQ1y03Rp8om_9r1uJ-vYdc_QOaUhPRE7-pU2aLJcJmdzJYT2wzVZxLBbQ2mUtYiVSfSKWuLpdWDLRILLmE5BpARYOHsfqchSfjZm-jiBbtSvZ8dngpkHo1Q1SqjrdGCypLsw6IKz2mgvFESECZ2l4iTXTaaK-ibB1vN52UDRUU5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدارهای‌دیروز؛
صعودمورد انتظار آمریکا و اسپانیا به مرحله یک‌هشتم‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/24834" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/24833" target="_blank">📅 01:01 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/24831" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrAnHaoutHVmpwJGDM0rq71j9A-m3tPPU9HzGk4D55FVGbpV5J8S_nHZ3i8Apq2QDb4lZkC5lsjF9MLSRGA_MBI7uT0BlPMORO_ApJXP01gYOLv73X8KX3_2ElQe-6Tksw9v0Q3HpXgdJbHwIDbyvNmpA6o3u2ZZ4whgM9NIBh3_BRlIOIzq6ApkMOGWXI0NpROFLBl_osqntVCbKgghUu3kYL3t2NtCKUVuZShhIPOBKJvPmsN2Q4Mbh4sadbDt4VgzLgUSH63XXjGGDNXcOXWGBG1_1r22qjsmgFLnvIGHJZ3_8HhwtyE7CwISFussRJVv7XnEFEdKiLLQIkJjOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی رقابت‌های جام جهانی بعد از پیروزی سه گله اسپانیا مقابل اتریش. بین پرتغال و کرواسی یکیشون حریف بعدی لاروخاعه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/24830" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24829">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U04UyirZYpSNoUlzbEf6WZ4b6UEcGNPwhMPXyldOOHp1iAz2AqUJzt4A8_ZRGPk3sWxOrJddwHhsVcUaHPjH1xGYgdHXN9thU_JKbKfCT-QsWL1gTA-FAeUM6zs_BKTWU3WLBm_8XTzCvvSO7odWURqRchljUls4_f44LYSiwZm3WhhwD0Tp-ATXB0PB_Uc1-M6lVHy_m2fUbdLwond-bruKLscuBOly3F4r9ZDeJ1vk5IQALuZ6OBVI81kV7_IVJ6qEJ92trob_Tnbdwo5dGNljBng-R0jvV07hfxaJhrL-G3PkOJJxPQ4kHNlUPmQxgtS4wYmsG1IjCqg8pvpGSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمراسم استقبال از کاروان تیم قلعه نویی؛ تو جمعیت و شلوغی گویا علی نعمتی یه لحظه غفلت کرده گوشی آیفون 17 پرومکسش رو دزدیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/24829" target="_blank">📅 00:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24828">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7X1YSIvNKkMq0pVRarmbwPBMsfLrq8t_eDCa6OfK3cnassKdE5e9rlRAxz2o2cLGdLHVftstXN97lYJdQ_d4fH-Gm51EJr7siwpzxoYSNeLaTjlEaYz_X743WBF-a2oMIlj5VYOBko3NhcQJcdOYp6sta1yMPiDJRklq03QG8ayCC06QTk8zNRgsOuKeW7s5teJZRTpR4_-gNX3547hcLcEGcKPrZS0w6e8E8XApjsb2eYQ7Pb18tab1jRRFR7pgtOrROHf1AGubutUaY6YrCRUE0c6HNm9Q2tIZC8WRUSVr4XVLPytcklJyZ7RJf9UTvRGV669H-iTnzcQ-b4I0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/24828" target="_blank">📅 00:09 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/24827" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLLNuIuDQuHeA9_cNVA2TU2NzWe7jGhOH997aZta73702QU3nfycN7rlQW-OQIa-N73hI8VEibjrvZqTF-qzfCggJ3N4llda_oCU9fE0li7uoQnNpGXLTTHTyFEZU3QnBNe6oT-4-rCl6zVJ1E1dV48EtK7USY590T0upZabxWSPoqwEKT6jskrepc8TGjlrZIUw4ph3crVm_8rASDak8fHx9fx5UsMTWQ4etbSreph-R8xQ4kQVzDw5bXAFvrmIY7uelY42WHytL4uFIfbvyMF4Ei87_02PI4qfGeRz-1hYluXtyEx3FI1Ak9h6GRO5lYH4CGteDJA1lcShFVM2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
رسانه Smashi Sports مصری خیلی جدی اومده گفته ژاوی روایران‌میخوادجایگزین ژنرال کنه‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/24826" target="_blank">📅 23:11 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/24825" target="_blank">📅 23:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic9v7ryG-wSYgI_BHdv7LznsCkMYOBQPnexzB7qk2KVcBZ6r5I554UGQyvYCb11NzafAMWlshMG-Popjg82qcI_pdk0ZrpvONVuhha94cZ8_sfcJ6-OSFa2rtz8mPCo8kXC2Ou_HYNHwOOP8Jn7jFXjV8HIPqdGSzKxEn_EaAxfCAaRoBLPwTKjGizUYh6ttkoizQeL12SL-u77UMlYKF4tR2dBz2rsBpfi1AD9aZ2qJKML-FnmaGsBph9ZpTKDDX8N3o6UYHqI1-0MAiWW8LE4SJ9HkVSg_ArdVTg2ytIJ85bLxZRS6oz9Lm4CWn_-Fs0ctYlyfQ3UmzBchziYPXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/24824" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/24823" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdB-I0YVe5p7hQMHTM0GARecNw96Du1NRy9XVtMdYhwJeKBZX_-LAPNvcXaZSfVQxKf6i3xEaZNncowFAq-C2FCMjoHsMPDy_Tbtmb_ehwj1gML6bqjRgUyzcB5V54VrO0XiURD1faSaLqHpy8pEl4pUiiGhih7IF-hGk3lt9rRAWMzhl-ZcgXFt33krifMPdjS_uGuVZt1LrH9l2FyorNf0mgQfLM5YRW6Ki6sJVgBbGtkhQMhFW76zO2lyxQJ8h4KTB9YB1Rq4OK1nbdmoC7OYauuvTkr_DN_vyrJxBFQUMIIrMaMBSK8TZlwsMQx14G-yGngtewyQaNRLEX2oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/24822" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/24821" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaw3tZvzTc_bI10qtXn1WVEnhEEC0FJVob2Idj9iiX2diBkHvbp0uwZ1IrKJyajtSnO4S2n-FRzkpxfabci4c3ANZT6SoQwoTNh0ffcwYg-cSQ04fXfV-FWat1GD2ifsh-0RfEwTdaiN-d2BbBsGKhpEfywO7HifGFamWoFUL3ZT2KHA6aR5xr5AFYJdmomeGhX4_uCS8ARpXDT-vO1ciPs3gwL98URDOHW4IZ6eFaCaqwRADsmmuBgjLLeoc24VVNj88ZEP7XpPq4SKYC2uZefStv-DjBW4eTB07knwLGX-B5OBodtQv63xkiQcSNuoZWHiaITki2XcPFsoDqWqxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا 72 ساعت به‌باشگاه تراکتور فرصت داده تابه آفر مالی‌اوپاسخ بدهد. اگه‌پاسخ مثبت باشه ویرا بزودی بار دیگر به لیگ‌ایران بازخواهدگشت. همانطور که دیشب گفتیم قرارداد او با پرسپولیس فسخ شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/24820" target="_blank">📅 22:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gar4xpOZGhJYAuX-f1Gl3-a6AmFFJ73xTSrtu5ZFCE6st3mXDEEmvTkNe-urFvmgUKcmK0NH9SRCqTm1T_5U5oDg8_gCJIdtdmfuDwUqO44e7vd1OprBDZUVFmLPYoTcWjXg7gPqkIlollKo5dCus_q9yoUhZKA-V6-eEHQMbwBoR51j3xWGV9xYaBtefK5YlHAN0o0jDSvWuUPG4a1oI9LYN1VxLaTNXqG_e3R97LbTlDe9pqBh6PGaMKAJks-azs8NxIghTiZ4cAbBdgtdUNEAnz8PdaAXmlKH86V6l03XVlfFl4PuVB8zL8dwdoIHnsAKH5jATEOjaq9igsl1oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حجت کریمی مدیرعامل سابق استقلال امروز به عنوان مدیرعامل جدید باشگاه تراکتور منصوب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/24819" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3AepTRwzNWkKcMG3ZCgdk1NWFWFTb2ujYnG2qb51lnWoiNUhJ7yn3QJBLyj11FbI88VyWWNJztpLJxgVqtBnSEAtA30pGLNbgz3sn0X0ZqxFdAbL0Ez1Xnljk7cFeTQfXm3GSbQ1UrAw44pZoDhNbgOx2IhvmK2Q6BW3bpLmkr8eYzaKRBCBcu6fJkeuTUH-vtDKmZCa79Hucp1C7ZirB5WLmoc9GHT1pNkS2Q37yXjipuur3-UofJkA5WygZw7WYM_lFQoteoFyv3F-v8DDHYX4JXhTwV2iRVDcX4XJpermL-ZNpDqhAF5WIhPvqrL36_mA0-Hh14lUbKoK5dE1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امشب یکی از این دو نفر آخرین بازیش تو ادوار جام جهانی و احتمالا آخرین مسابقه ملیش رو انجام میده. شب سخت‌برای‌هواداران باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/24817" target="_blank">📅 21:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFbHeh-7qa2xknnP4iNst5kvM4_R75W37w42RQxPRbanhKKwNNiAt9A-0t6Wzn0-tlpQdpFLAQCiFpNtQjmwbyVSg3_YBeMeFSzJ6MFfnwlpmKHtKMU8kGUOxyxZJBC7PyjuZVsB7ubhCCr0VZwXdDmKqkgTtVeYzwEzi8RO35S5vcSg07j3VvkXbCBqLvULqSo4W6Vn2bQfcIkh0yyojj7ao2DxnNt77HC_ylB8LH46pzZ-kjmDy2r557NLxXGpgN2BzgbT3gtcG22j9WnGw-b4oAowcqIf2P39sFs1Earq36UmaFISSQmJSWEnQRzmJz8BQ_3OWuX6bBXNuGAzhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یوفاقانون‌کارت‌قرمز برای بازیکنانی که دهانشون رو میپوشونن رو وارد UCL و لیگ اروپا نمیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24816" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkQ9Dl2SQsI39-KChvfrx5CPMexZpTEKVq0XmJ3mGZ05I9IsTfUGkZpTwocYdvUEdVpyOqiFr5ZttV29qsqbBeH-FQFoBkg1m1rERSxqtsCMzfiU0wPnrEt1tTM8vSec5zbEF9X1X037PsiV2pl7OzutpR2nfP6-BNyOPmUhWVm9WLcgoEcOd37wzdf-qLosHlyeR1vG-lPD5MlpeWw0AxYtS1Cu9uiAAu-XTjFMRBqImgnr7nq--1IJyJRJQg0QifchFxwYRgQFOdQ07zHPnUk4ssJsg4K8BHIN1E594wkrQ3rrCaC4pSKDXUnBzPKzn3IPANf4JU715hUTa2Z1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24815" target="_blank">📅 20:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8NiN9iYUa1derQ9tHgxPVCQVEozTv8Jcd3pZ_Dr4Yr1EI41p2WKsLkUSfYD8kpz_xWnkSg_jV6d6E94BnWrS4_82OjFilDeyHLAxrOGBEbef8WDcrWFmVDRiM36pvozBkLf7VpalphfT8VhBoYX1FAb8M29l4_HWAYhhhcz5sh33BnGWUAZT9nmFoOFvWf5p8l4KGgyWEvBYkfvd-gQ4-wSJ2B1c58pIx-g5ySuJezZRrjt65Ix-b2d_goysxFaRDsHJ1fb9lglbQ8r29m-dmwfLfBMKPzZecQ95_o3o5XYAiMGENxuoULZr829pBcmD4kwtTBOOFWnudyXTmTebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی
؛ شماتیک ترکیب اسپانیا برای دیدار امشب با اتریش؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24814" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnTPB_wMzPuJ_MQdvdGa7EpHH7CN5tOwWTDZ1gmCt5p6oz3zmuikoMKHOG-ev3fv4tUK8LXjHgyihxMXO0BlT2th5o80KTX86tWAXkC-wK3Ya3PipFxfabZFtL8sAaB2AdxIMYTIlOGlgCcw-xIeDJ7JtlsWwhjs4dBTW_N_W0sEs8WgaOE7m05KX0VNKrt_uaxVt_pa9pHJe_hsjYflSt-Xb0w58lzGz63mJRGkiox4kR0KlB7UM6w0QG_38rPYlGpqCkLhWui-Hr4veJGcPvkUKiayKhELyVn4I7puzjWHsJytoyFxFcu18KVOJyfhrml6ZKFRwhhKHDEn24Rgcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/24813" target="_blank">📅 20:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTEiAlGioQIygdXPVYaXgTeo4uyy6JZuE6bkrrS8rZ_t8XT_30sBKYIrZVfmmVYECJxASz9DWdD8pcBLU-6VADV1NaJAa7O3EeGatN4CpRTmqpyIqKFPt5CxX7xbYN3sZapRgzkp_gHKpcP2I6ZxEXTNUtDF9WStmgH5ewg5IdaU9tmYOyMl-D0jJKS_2dgzbCD057YhUYBw57Umj3XBBfrCprElHCuLJVs_PZVmaf8LoyElxF3INARipBjkzbjqhkaiT0MHiIxOSQbBuVzJ8XM0MblyIeQqCk_Cm6wq52Tpx7nfMUewd1MNdtn1-EmCkWWCTSIRxenjlgu92KX9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایح مسابقات‌جام‌جهانی 2026 تا اینجای کار تا قبل از شروع رقابت‌های امشب مرحله یک شانزدهم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/24812" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdMCT-VwHSCqWQHV6pkl4zFdlVyh3a8EjMZ_hb-gmnmIZdSL0CTidRy_3HCratS98b4xkDI3W2XuXDtuPU8fl8dUUqg2DQlCqa3w5sMaygQ0tph6EozvLj7s81jyvC7vQK41syC5O6vfByajLKmv3SWlyiNjVcD8R4qR1qrmZTPc2ioLxjDVygOBHCVRFmAqHSVbFw9sE4v6z8O0HFGLaxUavDQ-Rq2s2pENicFEmPti53xm1kWGfaHRf2bxFOCJOzI0vjCoq8ZjLqqWT6q5F6LHGUa37Tt8N489oxxvNYFG49dAcb9faR-_GirFgeerTasfG2ZMmVsQAKTwOovx4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش: تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24811" target="_blank">📅 19:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q999psRSudkRJR1kdMvRcHNd23DfV3RCXX0eABKxOB4hVVeDfzkyThb8lGlVt-1P1_lVPuqyYCGgEj87Zb6JlRk3qWx-1kVcENR5KcffegOH9MW-jjKlyq9IBTrIlHdCD6_T80XmqLOFEfG6l4rsWqeFuWW5LJWhYKPQVuxS1uy606NG84udkCV2e4I5CI70SHOakF4pmHGLkEa9mweLyVUEw-7Om-yFiVvTtZt29P3nXbmNv1tqEsbZI7z5R2d8wsWimetRUYgeJaiSAVfW2JG_HOsQWuFYUpFiq0HJCtSisRX6N2guA4Fijcfb0ojfUMEFZQzN3GULUZ7l51nllA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24810" target="_blank">📅 19:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ng0EJxn7Xuvn3k0IGhQ-EdQMa_MQLyB5-m2y4ZzkH89sXmWURTNU_TPLlbMvh5efCID5VVXhhYGEPjpCFfCXb_Ic9PiR1bTHbgfPmBw1G9OJqbMDqrleYBR3xtALf2WVT7CeZtGSAqjVs3Vgm1JKZl_WdKbHxrOR8gs5dKhTWC6aGY8NRkzThWjHAtx6rg06jIIfOoNEpze85HF6Hfxjpg-MVcdYtM_pCYQq9kbv00oqmAbGUx8W9vUt35LT7jfV-w1rykwZ9JVjBovoepEk7CEbCKnu5wzGkZQWdBpk7e8wqRNy-9Ww1lhhOfr3-HffBRzOUc689JKAD-p470h6BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24809" target="_blank">📅 17:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F03pb2LB8LqO0qrykBTKGB5ZFKhnGiziBvzzGDNsnh3mV-uSZRRl0zCBfgh1VLCexjurWHbKMt_sNuslxNqU6tgGjtZja2X9ilBtwBSaVVT7uAeLHirLEFA6Tmsfh9EfzzLYmlyPd4BIiJBVZ8Q6tFXmWVnkW4EVi8bmNjzk2JK0LKWF7JBln4Rcv4GtFzhw4wQ8cIvJSVJRevKc3b8FKlkcxaHGn8ugiaQfdKKF3fIcpuP_136s0qVFq4S3Qv3bGn51_OvRowOYdPQNhgL5sqdbntpP-6NQwevPnT3ugQLPpfcsfe00xQsVnG4B5qhOY_iNs_ls_ptY2K8kGBt58Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULeSItuNl_nbWBCuO9SmGj_69dVb6RHFqAVwSe7NnXQ4MlXRm7cRwO6zjjAXGivUPialwfqZuVK7EAtyxaB15MSoTs5l_igQrM6lGXhPxs2UHD5i45I42ViXFSHaT_Ez-8fffPwOpkJVFwgvNKxn3u0LCOFjcBbXCLkr73XYWH_5B8hP4YSqSwwGTu2Zg27xJtjzJBSx_T0Fw1vkHqqdxqydBX-T-MuMQjeRpbGwIp14ujaLKFI2yek7KGvHBKBmStZx6XFI8NtYHixdZW21H5bpzblZbMSHfxuAvFmHJNZI0tpyrchCjrvQdZoioSAIosLOyrYV_UTnJkCJRf2DiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24807" target="_blank">📅 16:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c080f226.mp4?token=F6YcJ1XP31LdeUZe0brBsN7Pq77iQdi_JFU90Kv8bLTo_uluZrsgM9t-7CMymHp7hrMALH_377jZxFJapxnm03FAF86m0UAddP6h6nMQmKD-6JpoNkeiz8H9OELjxfDZtc4ckHZGpEITIkTYg-9H6NkelvmK7a0cbFEWreA0iOzuNSAYmfe5CkhimtKMtpeZ4Y5_5a9eK3ZkIXSnsARO9QkFCyvHhVpQzW96Xhyvja15Np4D5yMwbtRyupSHUfm9rci-i-EEeX4Eg9URe1Henao8lka_0OUq0b8F5y894W-LZDDqpiINBr0IWq6HanWwCK_hi1U7QaEGLniFITNSFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c080f226.mp4?token=F6YcJ1XP31LdeUZe0brBsN7Pq77iQdi_JFU90Kv8bLTo_uluZrsgM9t-7CMymHp7hrMALH_377jZxFJapxnm03FAF86m0UAddP6h6nMQmKD-6JpoNkeiz8H9OELjxfDZtc4ckHZGpEITIkTYg-9H6NkelvmK7a0cbFEWreA0iOzuNSAYmfe5CkhimtKMtpeZ4Y5_5a9eK3ZkIXSnsARO9QkFCyvHhVpQzW96Xhyvja15Np4D5yMwbtRyupSHUfm9rci-i-EEeX4Eg9URe1Henao8lka_0OUq0b8F5y894W-LZDDqpiINBr0IWq6HanWwCK_hi1U7QaEGLniFITNSFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orc4FOkRIz34Zd4oshG6c54qYoL-rZaYaySL1wGEktDe8DY76X18B9sf1TNtuhetW40ixj8fM3GGpjkBewZU6bvYvd_LuXU-YNWCkBaNFCKJek_WBaKGjv7un0SH30SGI1FXRILqNXKDh2iJrlBuGokuNoUXQptLGyaEuAjlPmk53dzhoxMk2u3B7BPh5zPGSPMORPykO5U95ByOyUqkSFPV2MqciaJp_SmullgohTjlyRbQq21je9BVG4vhEfLUedxXbgNV1x8XEz51RoxFE5feyd-odcbzWpURvlrTVNuKKNILFy9H_4dh0qBR_h47xv74UBFU19G2NJQpPp1OPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=XjDOt1hA7niwb57dTZ6TrEwWE6qfX4sNdyB1vcDUIL8aQ99DcwgOsy2wsNWI5nLed5YRm3IvjL01-QUU5-MgqQowT4JNOGEU6dO86yLbJ1yBEUeSfdBC04m3JzgJ8geaAqeo-gd8fJK2aVuz7BNEsKBgVsK_vl_Gq7N29I0RhpzmH0aCas9vXay1x5Lc6tp7aJIrDVLJUDWNI4-o5Kc3KD1iFtr3CODX2Vn5-ZAwsMq3Zge5x5IQMlyREfR4VBNiuLeHYUye72w5baNB5UZQvRqjyr197vKD3QzQUKQGQU06AeeUO8tq0QNHNY8gPIPin6bCsz8Bintt70NwcQDQKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=XjDOt1hA7niwb57dTZ6TrEwWE6qfX4sNdyB1vcDUIL8aQ99DcwgOsy2wsNWI5nLed5YRm3IvjL01-QUU5-MgqQowT4JNOGEU6dO86yLbJ1yBEUeSfdBC04m3JzgJ8geaAqeo-gd8fJK2aVuz7BNEsKBgVsK_vl_Gq7N29I0RhpzmH0aCas9vXay1x5Lc6tp7aJIrDVLJUDWNI4-o5Kc3KD1iFtr3CODX2Vn5-ZAwsMq3Zge5x5IQMlyREfR4VBNiuLeHYUye72w5baNB5UZQvRqjyr197vKD3QzQUKQGQU06AeeUO8tq0QNHNY8gPIPin6bCsz8Bintt70NwcQDQKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOi4lLB7hYu6hTKefVZ7mVmb2Kbs4aJfKHWsdS3SXyGiofCaaWObTCfNoqO-pnifslUkFMAqE0_c806oUJEPQhJdx1fIrHos_bxWLGab6yABzTYc7vHaJGNOIU3wvbtsOZMeK4pJ8i4C3O8aK_tBOHjHFCwYkoysVmNV0LiuhE7d3aP1gDSCwRrY0vJdYhuBNd4VsI9mDd5NlhVKW4sWOWjVsBr6vXyVcjn9UdVswKwJV5tDmp13heFictjOg49kIq_R_IwJecaOGNJruwA61wa5eOMaunGynbmRsC6X-ZoAxXOYI8o8GJ7wek8eF2SHKmLgfCYnq0RO2tGaOoL-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8E5_5YgEuhJzxV5iWlMSJCePczSq0jenREZFopqKrxxo9xZWlr5sZFf7JpyjPBnfpMycTT0idNgLFs2oUd8h800aiH8-rF0JuCEDHC45EQt8IPY09TGLpD5twu7jFKBsZy55ywmbsjBZK_z46byiceceNHgMB4hb6cbc3ZuPguJHCCt5aa9wto_IrGj4eYgAUttd6yjxlJLuYGVXObVlBfxWpPkGzo-ZhPd25uotOvLWI767lTNO8Uf7H7na-uMIwWoiuHmM2lJyD2_q70xwijX-2AN8geFwX1pv1nOvK202k88PnebWIa7-9ZhxhOWhwmkIUSOHyebrTRa9zqMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBApVKBWVNIDA3Ot-USeQNjZAJ4t8_7K64pG8p1HnGhYvykj0BEoU1gVtfO961_t9uRFYierw9BVwogcH_8mOFSVdIKVFLqz-2hmT_BwODdu_dX6hczaawcUtMyiUyxjnFqt_X5bM0BaCUNXcD7ydoIf5o83LaEpUANkdVCxMMi6qlEU7AR29oCT-PsaLZ5pTKGppssJFaYdjWRpAVEjwcuB5Ld2AYLJuFojs7V9PxrbyvaBUqqe1X6S9QADr_LV8xbpIdqWYbp5LPjQ4d0ezYs7rHqWzRVjWRNRxhpIYa2ETW3MUyMAnDcPBzViYU3oWPSYW_QXvO92SntkWMiDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3ZLJi83PZm84suwhzKHVharKUijeJDe2JfbBy4GOK1JaMzYdyOtHSdds6-wq3iDiNxLYWDsaNuLRVu93Hlzu_P3RVCLWIXNYGRt9IzBEgeylYaZeJb4QEgNr9XqqNEqj1rQc4ZH1SOOVNHUf75IozuP7XnpHygkGvexa0dhFjas2iB_ELboXg4PTo7eE6YVnJWu21mt-igpfXvHjeFrwEN0TbTJyvQSzan0uwcFBDjCi06ZJiyi-HYS0pQr8jzAhmMQHt03Ln63_56XJnCZPlquCf-6yWt8i4O1Mc7ATzRSnJtQGrir7HSlOdRa67svfKbkGhPZ0b-XSqfHNOmKlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=KWRs0xsu3K1NL5pcrJnQ04lx8Jgcwqi78FYbLEwdhUn1XYyn6GLE3FV1fOamLuBMpCW0XE_-yfmIa03Z_8uBykUmRR5rE-WwDxd_lECuojuJfT4VNqG9Low2KdnTnAc579FyjecC7DRUclAy9Xy84YC7ew1OY1F4rGthUIcZZfFY1TA-HZ-suDdLMX2PJBRi_c26D0sRpgEcAkpFngCSZNBFvfjujJJfdaAqSHn5SbLpZXtDT8XsJXF3xtRFzhpKOl7ak3WEfvCjcJa7LikjpArXVsanHb2HqEVgpAnZ_4ICtbH-_krz3yUkJXict88KlprlxgIjrrdCD4mNpNeRAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=KWRs0xsu3K1NL5pcrJnQ04lx8Jgcwqi78FYbLEwdhUn1XYyn6GLE3FV1fOamLuBMpCW0XE_-yfmIa03Z_8uBykUmRR5rE-WwDxd_lECuojuJfT4VNqG9Low2KdnTnAc579FyjecC7DRUclAy9Xy84YC7ew1OY1F4rGthUIcZZfFY1TA-HZ-suDdLMX2PJBRi_c26D0sRpgEcAkpFngCSZNBFvfjujJJfdaAqSHn5SbLpZXtDT8XsJXF3xtRFzhpKOl7ak3WEfvCjcJa7LikjpArXVsanHb2HqEVgpAnZ_4ICtbH-_krz3yUkJXict88KlprlxgIjrrdCD4mNpNeRAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bibOL9pOydbR5cUCh9g3KOTvL_Alb0eZbtOfF07tmNsmHJh-WqMN6U9CYXW99XUQAu8sukDt4NFXxpUOxZJjOohP0Sk5kH_GZ6oCj6PkjNUV2K6kRklR3F0lsi4XeIAEcHfD7hVj6ZMF-kFYAYMRg5CLEjG4lRjHFWKl6FKFvwpz9Ic-IViFpycp5kQtWDhvZ-va8BtHWlik8-HgkPiBhNJtM6UnF9-FDslM96OlSTGdq5ZYZ2rht1OTyrDQ7j5VVNVUCgZi805dlNtwoQ2uMw735TJ8TREvIgZJQZ8otAZZwrNhu4m6pHu8lZYZAKcfGfyjzUEY4ZA16iwsGsESqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ6ou8tzBsm7X85xvHFOmYrwBNAHlCu6G6GnmmIJny4w6aoo-DUhopakPx7U_1p3t98_zKx6sjRqB1Lb028R8NgorPP8I1J06ritIQVWnTs0i5VND0PXyWaGJKlOw_uAjarmM2xZwWyu9IY0cum-Mus4hahgkgprXVswVyMaQsKXH5CHqWnqaHuRElzVG_yd3ZhFrYHzja6wIsPdh8TSLGiqGSHVwTuHw3gjLyVX5RZr7Bw-7scAxmXeJAkCwV1qmkqTXvkkQQV_QoH8PXRLqBGYFBQZ7eW5oHUvDyCJUfNsV0pL8IzlhGKMRNr-qIRRJmZ_rjMKkXQT-EHwLCrOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyIF9AIndP6zHQ5fkqfqjg4pINva7xhBAWNWEpSvj663tkCt82rTnNEtqBBLErcNTyd7w_JslNDG6xuPd42s_ag2-KQrpIZJCjzukhWAdxp6CxhjDESCJswUfWDX1n_hPj8cu46SqFX1Yw1NArbqXomyvLeMy0rHTBqjPHKWvZZbrtgZWaS9DokvZQJ04_q-MKakg4QMsFlMSlww8b8bSYPxAiZUcfBddWYHUHxUOh6LOS_1fwDp6fv93XDx_V_GR15RSXIqlaCvsiMgo5mm8g5JNQ2gG46J6tfT-sbOXtCNWHVIngnRkfBft59yt28_jf_e1DeVd3kPozdtw4MNCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oglEaKPFR1JlvlLOADUz15WAfUWOhc8vLav78dnCopKyaoTIMtngcwuh35k4QtYJh-LFWw6AV00PMjN5MzucZzRYrtNVKlGBTbrv05x2zklT2S5osLFRYxIJ5OyKTN9rtKuX9cFwpg18ZrFad1gfdYzwP7BVSAof1EUD98kVkOEHhfZ7dzMbEkKIJDkMcQUONykSGPfqYNu0wYK-5708CPdGMBPp3WzOpUrXjd7jhhW6o2xRPJkVYj54QEmstWc8ybYyInwi6xdkOhFhGbbu25BCXvMU1Y82nmTA42tpb2LkH1rzMML1o1ASwUPPURzLYBMeSg9dH803jfWmOTgzdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxsrQsawIN0z0UgtN8I9kotQaJ2TVArVGfxKeJVooNMnADjsiYTkaPX0-cjoYG2r_3PL4_lFVUetEN09HnL2l-2hLx3S2uG4CrOjRzG5NUVTNT0vz3BXHvWFLPFGY7EjwyeFBJ4aTvG_kWYLS5iAkrAFGAQ_sy-EzLhqOTfHHSmiZJFZg8HTiKYX7Rh6mccFlfei2nBxgmxx8KXIEaGAZf-ZM-r5b3rZZImTrIWuXJgk3QNoW5JAFujTy0qhDXwcIm0ZeBoJgy7t3nFTg-tQIXYARHVYz3wEUYtmLHzLKC4GnW1xs7NDF93JtKauPu4Ec4FNmAw2UaLTxYSAF1zNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjvuoO78OXmA1EdGZtjL4sWlz_hcMk6eFx6J7CFcvX29M7RLpXakYgkRQwRJ5uDek9B199S7vjEaedvuwPvsl4oTwg0poHbjOR5IQJfy_hoC7gc8yS11YVvwUdo8GhQGd71uIWMrX1C-j6HUn-3TW8lJ_mWgKpd2O7peDzFTZktbbYzVuVLShmSp-Fu3gdJIchZa4uFzJVR8qO4UPugRXv36WfRUG8NdYux_DdwTD0LxZHB54o-b_0ayfvGgAqXAXYwKa3q095ljUFQvu0Vo0cYKhIpDwxeGpl-ff4jVkASUvP9ze_vBdzmBb4zsdMNxf9rYvZs_Yx1kL77taEXIfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b48uVRAf4sWn6TgAYWWNiBQRBIE2nqsIhT54MzHcMgFH6MQ5FoebAfogRPwo785QdfU_hHUQFh3lsIHcYRIz8C7Ix6foCP1a74DjZBWfBhAjQROVL3PgqWM6C4ujISNge5Ztqdfa5Del9tZbMlwd2xW-B1O9u66cO2gpN6ARlmjnDxLz51hFO02UbAMMsM24h0Pfl4C1-HtMqi3qtTJc31pzJCrGaGpXtr3IChWr0fzHdsvKSrxLILdLMkTRSpbZds5PCX6Datg83mrudWb-zKEgeFm5TUbQPEexPxQNr7Z47KH5-4NusxkG9Ma1Nt7rcSzRqxiSf3KvSS6Ee6-eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3QZHnDSRo2xQy63XtU3MtKCnwipa7qwg59WUmfJIrLjfCLqNLg0e0Sv0pqUVXwvbWLqLg0kbfzf0VWUHNx7cgYF_k8taaPTneIoVO6k499fiByh_3KTJZSAlzgImxy9ZfkxxkPnX6k04FvGfamkM5Ukq19pou_0VMLRbDgXIeBd4p-DSL_xS1EIQZbhOZZOszYyKM44WVCPkZ8jYSre3PhaaUlXYdzXdnrkFMufN0MzIrtORoVzcmMZuk-42lwjjJSnXjbJ7Mqnns4AxC1ZoHLG7tNgWPH3L6GyHN28djk9WQgW-t83Y4h2gx3OaG2XTrgxKTffm5Wi8rmswJUV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4AdVPojZp3nRQg-9IAeieMIHAzPPjO2VzQjAoG9gMIcnrN6oe43_ngU_-68djHzlO-kzZlu_LxPqK4JlSwlbAAAB759ZXzGkNSjFu8k_BoK3BM0egAf4ELxjAZ5GzFtj8VmHY5b-bQO2mlaj79fdezLAUCnypm7Bo77QvVfyO9ZGNr4nktvOhIzWmlXv21X6HD2kr55ImFzOP3s5TZ62hAhcGfCkK_mNMVjhVL8G_uPCXQbuIUCiVPMXNL5OX2Oi5OE3GKEIwrfn13uvbo4AU2nOCUq34HK_mfz5zScPWuXg8YsZOVzI92RujzkiLrPniYMuKhmqIXz2iFZjkJWhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDNfjeYZZQfNtx22SA1ANoj9nMlkkZEnmM2O_dMflwct4AOn97FCspiPF3W4KOAOgJwVd_euD8o5VFq8pUo1eLJNOreMIRw487Kj9SFRIBd0m3mnef1hbqeEOlHjXB7KFMx_xwVU3tj6VcWR4i4JnhzwTv4_uAT7HD7d_6Fg4n8YmcpKf6fxWB7k5yTMWJ_rGCDYSTCT5oX-dSLaaXXvS6prJxJA4elTjX22IFvjYBzE6yEt_5CVs53Za3fFG2YU_dVbDnFkqueG_cclyOXxT6IfxXyo7595MviK5F5hgjKr-QxfYqiS_O5tmqJ2W_TIu2miG_0TPqo3SH9hgCGt0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuMvvztFp9Kzu6AhvU9o1mcczDg4Bs5IGe_w7-Unjwo1BCm6v-FZnUs__fSeuGZadq0jjKdTtNcYJ0rJUIPw6juLb4bXBMhI5W09svUp9zWOIQZjnQmwV3a2dpcYIAPW9oeLNfNemu2FjC_Nap5WS8aZHy0UODd27Jo-AHXHGGgpLzB2sbuA-RV1zO5rYcufnlZZGWSp-lPjtqIyGxniBXC_bAJcKdPcJa2xkeQHbuWm0exJ-9uaHzQi5q-77uYcMvJZdsFHSnPrtsxjsy_3bUFpgPC_fXLLjqLvwbabO-UxNYSZaX28Xc1kVfYU5iPxW72qIvY8Cfo3Ravhvv12rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=Yh9XulffjBnziZZb-MYQO2lOJ2ZlVqaBmW32l5_0MR8sPawoGS4V1TCRPx3Ra_hrKp5QL7PywOyrXewwUSyxklIUnD6ITQHMneoDY1E426jaIaheXS4YuR5WyC1fv3jNLNy2-vi8Sg1NMBi1YkwwLZx0-ME6k4oU25Z8IIWQgw6-G7XuSJW2puJ81HnSdfLvB4gyyBnWWt8ZhI28fBq8ZX-fXHRl2SnkCISnWc-QQcW4FUWxu8VdLmC4CB_QZZ854JW0KsuAdFnOMZHgwQdsjkMFUECxbddBAtkBNoLuXn7ArMgIP2Hna-hoWMv8cBymL_3-f1FZgebGHJQePqWzjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=Yh9XulffjBnziZZb-MYQO2lOJ2ZlVqaBmW32l5_0MR8sPawoGS4V1TCRPx3Ra_hrKp5QL7PywOyrXewwUSyxklIUnD6ITQHMneoDY1E426jaIaheXS4YuR5WyC1fv3jNLNy2-vi8Sg1NMBi1YkwwLZx0-ME6k4oU25Z8IIWQgw6-G7XuSJW2puJ81HnSdfLvB4gyyBnWWt8ZhI28fBq8ZX-fXHRl2SnkCISnWc-QQcW4FUWxu8VdLmC4CB_QZZ854JW0KsuAdFnOMZHgwQdsjkMFUECxbddBAtkBNoLuXn7ArMgIP2Hna-hoWMv8cBymL_3-f1FZgebGHJQePqWzjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chaXcDcjUmCke-w8Qmg8uUb6PkE5qzVojWD0zmbJXknnsf_mXw5O8xjzZFDdWZ-JzOwGAvAI5OiG_wwtg9JoAbXO5JL1aBIdi6pIHCCzTLLqOubpoGSeMUveyXZI5IixKxocOO5yTVNsntO0KDXj41u2-M-oTqL-idNt-MRc1VF_FmtlWDZFAkCUir4m2GLkgBmPWpVxtJP7H7Tm_8diwIBYRWz9yEaoyGIgI4wh0bsJGJrfLarALZy8DcuRCgchgh9_nEsyD1MPdY1UyKSu8x0BFSut-b2hOE-wECeWTRwUIXm08d_CGurGq6NKDwnprspHzzWUr4srcmNJKZgcvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=U_qGdN2RgizK5IySJu1kNoPfIV8TQj0T38KSRqWjQeUCkOY9hmDIfSbDLETiAsuaZtWlP_NDQ-DT0e0DUE7giunOLCj9TevD2Pm2gX5A3cQjY1HkISQYkIpD_MAB47ooZ3OMcOAI7HkAAW8Cz1sk64wIL0hzYYe23mXNqcGYWsmCfZMw5_7ygTWF3ZHUNuWI8KH5w3fGXrMHR7u25gjh1d0hb32lOsgNqDLo1KnH00ZAWCbG-vEebtb7ePHJzqAFfuS8PUcreTsBN5awOUqR-T5SDyOsKJk3gyzVC9l80564b-CiwkeVBDq-Z0ewJmeiskSB9D_uK7vExmVPzwhNEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=U_qGdN2RgizK5IySJu1kNoPfIV8TQj0T38KSRqWjQeUCkOY9hmDIfSbDLETiAsuaZtWlP_NDQ-DT0e0DUE7giunOLCj9TevD2Pm2gX5A3cQjY1HkISQYkIpD_MAB47ooZ3OMcOAI7HkAAW8Cz1sk64wIL0hzYYe23mXNqcGYWsmCfZMw5_7ygTWF3ZHUNuWI8KH5w3fGXrMHR7u25gjh1d0hb32lOsgNqDLo1KnH00ZAWCbG-vEebtb7ePHJzqAFfuS8PUcreTsBN5awOUqR-T5SDyOsKJk3gyzVC9l80564b-CiwkeVBDq-Z0ewJmeiskSB9D_uK7vExmVPzwhNEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPRr42OEWQL8miWPHLgxH2gqb_nykI0zGfs_JpkKbW3FDYx5a0Al6jILGvOjgyEnPv-Uh9j-klEHhPNgIn_CUFGvAt3JcYe-K9vPzbo4nj5baNP_yMnSKqk17DkEIJKenBJSCZQwMGyxpXAZYoMVcRw-LWengSWgjW7ApCKLNSlLunmtcSXtc5DoPhi4GB0pXwqc3bQrS2qdQZGj3seJIbR-HmMxmrkUN04AovabBGo6bisohD-poUyTFSPPOvy8N7ygtIUDzu7XxtOK5-h07TUk5I9ctKcqEyzTkTY3HHygDWLnMRWwhfQgvzEEGgw_Wm5kjD118zfWz_Ol53eKrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSiF5dVk0agc9NGZqoCxWb2iY5-baoEFbKNhZVU7Z2T5TQLC6KqRBx_pUJ7jOVj4UARJHh3BbJ5UhRn8_ix5vFkHrpw-1Mq9BEF48B-kAaGIIWeK4xKoekBnRBmeJE4VDWEfq_FpUpmjwZwp_P1uew7bD4eQWFGH1rbbya2k7NgX-Wss2LTTBsA0W9VpknjxM8tKKp1BSBEad_ZV_XGTOW9cifxaO0ZoTXF6qvLibhWEvddF2B8uJV8rXijG8n5VrhdIh0j-e9oTrtC1GSZWIsKSdB3favqmynLd1vvyCHNX3nL5pTsgLUCHGeLVzXtH3tPsVaEELVEIg1Ffft8-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=S6gcGuPNRkF6UbqgjF2yWVmV3NWOYE1aXUhEfEqTAAohPwY3UX5_GChNg6GTIQYNb80eA5YDl6sympOPL7fo9GwwYu4N5VOT7Rl3xXALAKEg2Y_Xr-xIiqKiahZ3zJgSmHNscRxosKfvWXcV5ZlOXy4znw_ke3tPOX0v5AYAXLAW8wmGLeTAY80i-p8cldViYijqoC7qeER_LzTkjNACRHJw9nUB4tkcE-mVan1XI70EsP2mwUV2Jo2OgJbOaozYQWqNZHp6yKBdAYSlqKCT0g1qt1c6Nv2PK1salj3TQu_EKAj90zw-YkD1DuSJkDDsUXTrcDwM20h8qJ0Ej7L5fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=S6gcGuPNRkF6UbqgjF2yWVmV3NWOYE1aXUhEfEqTAAohPwY3UX5_GChNg6GTIQYNb80eA5YDl6sympOPL7fo9GwwYu4N5VOT7Rl3xXALAKEg2Y_Xr-xIiqKiahZ3zJgSmHNscRxosKfvWXcV5ZlOXy4znw_ke3tPOX0v5AYAXLAW8wmGLeTAY80i-p8cldViYijqoC7qeER_LzTkjNACRHJw9nUB4tkcE-mVan1XI70EsP2mwUV2Jo2OgJbOaozYQWqNZHp6yKBdAYSlqKCT0g1qt1c6Nv2PK1salj3TQu_EKAj90zw-YkD1DuSJkDDsUXTrcDwM20h8qJ0Ej7L5fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=EUjvJbVCaLQJRgQPfjz2IiHAMZpqHwi2y3zmphpawXjUVCBkVD-U-jxNVIlLfz__Uq7zs0-9SkWtLiXkdx-kRTcMcJxR31027adC89kjfmsvPerOuMslKSaufqF_9cWrgyd9-POnqFOa9WhJzvZTBDoxyBC7igElvMfv_WpKcxZ9SRqYl6DlAVZrRqAUXErsJXXappO9zSacvto5xcgw9V8i1WpzcSnQTW577hq3B0SdBwUVCECklo-YmOvkZ9eoG8cs91piiJ1tjMdoprXBFEOKHmssUDrBAB24F7Ynfm0DUHot-uij5GOjNsd3K2wRHN5s9_guYEFUfgPqOF07OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=EUjvJbVCaLQJRgQPfjz2IiHAMZpqHwi2y3zmphpawXjUVCBkVD-U-jxNVIlLfz__Uq7zs0-9SkWtLiXkdx-kRTcMcJxR31027adC89kjfmsvPerOuMslKSaufqF_9cWrgyd9-POnqFOa9WhJzvZTBDoxyBC7igElvMfv_WpKcxZ9SRqYl6DlAVZrRqAUXErsJXXappO9zSacvto5xcgw9V8i1WpzcSnQTW577hq3B0SdBwUVCECklo-YmOvkZ9eoG8cs91piiJ1tjMdoprXBFEOKHmssUDrBAB24F7Ynfm0DUHot-uij5GOjNsd3K2wRHN5s9_guYEFUfgPqOF07OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3xDAiY_NXBCKY2g2J0y2GpG08VCZnoiIyZBTHkDl2vUj1gItEYsk0HASHWfOnsE3CaLZDczkypK5S131MzuYaqzoGaDmgjBmVHa3viOcRZQnklyLliHwO9AFsCGdhqmzEmP61XYqMi97Gq5RPCsIrDUoe2pBU1WHFO6GnNl_rHheOYiI0lZQHPzyrneQJF0_z3oN8SRK0eKVpMKMFn0jx8xL5VZYtlSUSHHHAEAe1c_GefbH_xg3rl5MzsBQaiyssxsSRXSd09K4Ytpx1UyQ0uDiLU-PtVjekF4v-EdcO6ByHyMkGkhvc3oWbgKNZ93a9Uzr5UtH5OE_g3s-pdFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeS5vK9eiLGdYw0thDbTGBu_K9xhz7N5VpZ8rQdmfK7I9hgK1aKq5w16yHINiTUF8bh7LPH1gGKPA_MNpB3bKd5DWhJolwIHGh1ZwH9_AeqBrx83madzQAjjARbmyUp5eTuHu7o780_FngUfAnigJ_-D4atT0jFX_iOLcK5RDFVb9nU_c7vAz3oIopLrVfKliZOzTngF548wuj73I5SdiFL2OnYXm-E_n_sM6-WQdHmLJeI9jeLVchCOuUG2tHz9oMnI5ZLSN1cR5vhpsHCNSbL8NVXKQYtD9xN_H9HJ6bN28SWTCH_kn0APY-MkFeJ2pwMADZSXOzxBN7yn-uenmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCausC2swbZzNbnypbZh_WB4gZ9hny8NI2efDHBUt0omebujPc79UnbXtQWY6We5dT72uth3sGxyAhPpUasANydxRBmO63JsVMxyA30dzKCV6-KfqKEz548gHkV1-30mk9NcCjhRI9NqDg6ITGOKENIxV2Fbt2fBu4LYb0pDsAPsmVW3SP30k4PkpEhbpcpN4AGg4zn6C96c4ZKIWWD3KKtB2BbgoCQpGBai2OVmpA9FNTeAb8tVLJQ6RLpcku_K9GGbp-BUvQ9nN1G-vWhccUtoZaZmr0R_YXdy0uUPqWOGSMxHYibx2T-GhFdT8xBNyt_R5y9XvRi6bzRBdBehEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=Nas5Gonc_-VoJ773SG3uIv-_mFqoQFeg2Mu6g_XB5zMJRn6HPRsBJgTpgpM_6Kv6AZUD_KTc1NQtGKcBZ7NpFhAX_O5WSO09AFERunaAUkkbyZ5SXRZXdF4zjmS-IfNcJZyDnTWk6jD6Y3AUzPmCbah2KWDzM7JRrjWkxHz-6GIcH0YgaqhiWesQ3jonuMXtPpRHS2kOaXSmi1ivQApB6iOjCLon4RraU_cUqH-magWLifEMN51iccJ_3YFPkekm1bjyBxIVSToEREscmXw8a_eFjYlgijEN7a_gw99QC94uEXANaD924dlLD9Y85Xog9OgKj3qIRLq9jVBptICNIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=Nas5Gonc_-VoJ773SG3uIv-_mFqoQFeg2Mu6g_XB5zMJRn6HPRsBJgTpgpM_6Kv6AZUD_KTc1NQtGKcBZ7NpFhAX_O5WSO09AFERunaAUkkbyZ5SXRZXdF4zjmS-IfNcJZyDnTWk6jD6Y3AUzPmCbah2KWDzM7JRrjWkxHz-6GIcH0YgaqhiWesQ3jonuMXtPpRHS2kOaXSmi1ivQApB6iOjCLon4RraU_cUqH-magWLifEMN51iccJ_3YFPkekm1bjyBxIVSToEREscmXw8a_eFjYlgijEN7a_gw99QC94uEXANaD924dlLD9Y85Xog9OgKj3qIRLq9jVBptICNIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QC8RKa2R7xceIFfASR5SNoHjiT6tdLF9uzcl7eE0O1FBkk_6gTG4Z3hu1eJ0DtIcqSzPUZ7ED3bsq1QLg9yDbKEBLE5z4g1IK8AA5lzrPibxHv8tlqj_SSEdw4LRUBnYqIyWzSNZ8HiXLmhIJ7fJUI3e8MWgAiYqIH_apB2KMVaEKuli63GKXCcapI4qwcTGoKUsOo4Kd9MLN26okOIjOlHRRK7H18K9_dyoCGwOVK7JisuE_QN9FoXVIioj5zbLltuHwnWTk8E3dfHFk3ewLTDGuyK7EQzDo10Ib4YULjLXlxL8ppUiZI4UkIsrnB9KAAa9OtsKMPu7DNrOqDvjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=HP9kCYZRGZd8-7g8azeG6jZgq0v0Nq8ouj8tSQtE05BHs6dgIgwib3I4ngQawmAv79PDlXxphRp5bAlAQewY5CuZ2QS3SJA6wQEoEi_ewDbZANg3_A6HJ89DVreC1YVIaTvKWW4nuNVvGR6G42pZPlCCMiivvf_Mwknk5IP54sF7mMsfnYvJb2U-SnwM8hNT-KuYfD5Yk17KQbLIsGiNZ0Mpuh4KTlY5aBQJF55q-0HmczNk8DSdo4etirute46Jzpn8GDfSV-efIofJTil7jtp45WipLdbZzemXJrRvgXyFBaD93zE2bMKrj8qxIaBuOK2bd1yvO-4i0IWK2fZb5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=HP9kCYZRGZd8-7g8azeG6jZgq0v0Nq8ouj8tSQtE05BHs6dgIgwib3I4ngQawmAv79PDlXxphRp5bAlAQewY5CuZ2QS3SJA6wQEoEi_ewDbZANg3_A6HJ89DVreC1YVIaTvKWW4nuNVvGR6G42pZPlCCMiivvf_Mwknk5IP54sF7mMsfnYvJb2U-SnwM8hNT-KuYfD5Yk17KQbLIsGiNZ0Mpuh4KTlY5aBQJF55q-0HmczNk8DSdo4etirute46Jzpn8GDfSV-efIofJTil7jtp45WipLdbZzemXJrRvgXyFBaD93zE2bMKrj8qxIaBuOK2bd1yvO-4i0IWK2fZb5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5k6ef-0GWqEyfilor5nGPqedN6hMTgoh2jVDjo_W9vY0g-OiYqYapg88dF-MH9Ae_ngpXIrVWFcnFInk0q73CUfY6QHujuVbfdnG0YPzpAla4CGmFHwwyNtrVi8VRm7Zti9LZZJ_dfVi0QeqXrN7stxPFon-1eyIVB9t-Qqze7KQuAGxoJSts9G9IF6Uj_zPPz_U2HUHofmJhPUiFktRvtayTxEwBJyXWn8JFHvWAkxq6b88dur6NkQeoXWJO2Y9avAY23okc4otcmoTMDbcFiivH_dBD_7KKGZkTN-OzBffzo_6J7m7wGb89E1PLVZtg0DQDhqZwy42XL6A4rcvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=Z03fIbLg-f0Tqt6yPhgrZXPHcrWgB62PMRsTZelw_1P9k614Bt9apOE_aURKHMKHLaV-EgKQcoXnOJmByGpAX-yiraYryJSKkLjR8h92a5JCDCkPAD4GVdZB3637oJ2ApydRObqwrm8IQhJAf-2Yk9AKqrxwWSbreWCMIsmfhjMgYCUdK4K9Mf3fvYpJjBgmZPj8eISpIyc16qZh69hi4iXy4udG5iACtgfnDk54XRs3GGaXKe_Xy1sTdX1SJvtuMke0SqeTUwnKhDWkvDahLu8oAPbGexQGzW4gTOJgZyCH3kyoLSCZ-mw4Jv11C4O1g7fSeIuOPDK7ufsFTclX2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=Z03fIbLg-f0Tqt6yPhgrZXPHcrWgB62PMRsTZelw_1P9k614Bt9apOE_aURKHMKHLaV-EgKQcoXnOJmByGpAX-yiraYryJSKkLjR8h92a5JCDCkPAD4GVdZB3637oJ2ApydRObqwrm8IQhJAf-2Yk9AKqrxwWSbreWCMIsmfhjMgYCUdK4K9Mf3fvYpJjBgmZPj8eISpIyc16qZh69hi4iXy4udG5iACtgfnDk54XRs3GGaXKe_Xy1sTdX1SJvtuMke0SqeTUwnKhDWkvDahLu8oAPbGexQGzW4gTOJgZyCH3kyoLSCZ-mw4Jv11C4O1g7fSeIuOPDK7ufsFTclX2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPQvhm0GW4tq1968RwIqzLFJMBZRAW8CgrQ7Ejsq5JyldYtpzmti8UwhGQRTtpaq18oJBtZsyWpvPe_qLHO7XlB7iJ66OEAGqMIBbJ55N-jZixCQbcrFwtTalg2t2md0xr5MY6JeI68rIsFI5TooVkwosLEHWSp5srR2i2I_WKYYx01pR3ZUZdGISR9GhoucOns2_gG6SRKH2vjo_RXkEkpnVIAymaN1xtgW-MP29LyEj2ZKn4puy-PEZXZZ8-3wC-c1NEwEWIGl2Hc_HWQbNhBo9nRyxnor47PmM3ZUOuHLASCZ0VY4nPhDqXCaWC4YKHAsHtHa9fqFAjZwr3bxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRCMpvZCPIUs_AyYmANkO08zu0vgyG0_YOEScnmpr-8fpEY041HF9U8donXRwSoCaV0hA_gN-AglB8XWalyjyT5_-y3RhapzjZCWWzgsmdSqFPlKtS6VlcVeZQAwjl2jtVRRf56v0icF5JNYasKMa8O6y7eTtQEqlInvr1VFyBSF6TeTgcRMe685VW8XcY-jkOQEmV2gp41TXOF3q8wjEW48S9T7TzuXBc_IBCcL2L99Y0yruY8qAYyFLlSU6QQKk1fvmuDAvBLDo0nd5o0XN9yDGlxLXjoY5YLZ1jUmpK209BiBJgFhN6QTHMEVRnPdaPZGeaEGQTcJbT_QozfIKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1Rx_Ecyc-KwQokP4t8TVfeU-s_44Zmvi7jKjC9xEXl1s1qEsCnTpMqm2olvoJHjUhPUnF2UcVQSdUfnVTgcWHT0N0ubOXQ31fUUkryQTZFGL3_NctSH6492iQhpwrRZSXFQWigDi96ZDdoVj2wqPzkYHQjRL4mhde5FCjywk8hnpBAWPPI0xiQFNAIBRwmvDU8JiguQWuB3SR4IWAujOAFvmYbvwkCZ_B2o5zYravHHvazWhXF7YNom8BNUmoUW1AxWFLxoq_NYz-WA4y5mD0S2v8T0dEAlWHn8WaW11z-vEAagGNrMG34UxDZCwTIdD0XSQ3HooggM6VIYAC9h-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAZ4ETUNyecMbvjxs130ZUlEA-ADN3YWVNACHfcTBZml8SVIkaaeID6loy_jI9wsOLRh-SD8C16zw-So-ecHrpIujghClvLb3PtqVSkvvUMQLeWUYmFrZwOodR_rln9IhQmkgAF_MtAvEjk7UoFkfHWh_itZIqnx36QGSgl_w0FlbKTTou9MlaMZpKjkyB0JzxIPh495xedfnpWy-effEkSsDegrKc4uV8pO0GUUs6XPXFQjvmiADnC3RgyEvS4vdAAFYGbighZ74Wl3FAyAsNqLzxWMMqbpOEwhI8p16B7WCP3mlbd9ausBWNlTzdkQJm3LpdsFBTLVu81th3VcvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftYIOYx79LTSJjfdzUoMtYEvCe5Wsh3GNCX73nU-KKQQ3fxtRPNEPhAcf-FCJSOh0xsDVmm-lbWLQHi7-fyg9uTR-WLTsmXPQIfiz_S9sH3y6rVzS3J2hheyfS2eSfbj_yMI5hmjAG130l0wa1IMkqLtkNtVvCtFPNdRpwgo7qefXQ517CzWlcX9l5ohoztAQhpvzCrFsS_DVTOUX9nQnEshRx8IYCYmSM--vT18maKht97CRbCffEoTnSLh6dvY9RxLz80LDvYlMa1olNPM3SodUHfDXC4BVzT_fV1zHCVZSXaFxG8UEjeyl67gh-N7nsf3HH4OjAJRWilGHc9NTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=QuhvMBAevdmNI_ZEZW-6uMhwJhK7LB_lgHU9H7CVs9HdiuTtJ-XXnoeuitzGHzbONlzNfH8kviS9Am0dpnF3ljMcycDnK7OewgNB3Z7e5XGl67SnL3H-mPNofD-cPoEgt8WoL_gbHov3MorkdxjDvQTOLvU8Cm28STgi038QgJhpvIDjb5bd7WZULPDo1OwiOoF-R1h6M7kR_xTeB9KXujHSwzV3lYh7cKSauf2HIOgs4hP26Q5c2a0vSMg5BDEzNwpDmMH2soln3jvj1IJ-jGUmPKQE-okyjSBTP7hYb9OTVdmR97Od98-rBPyo60C1v05JxM_XlNFjxwmtxQ5-YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=QuhvMBAevdmNI_ZEZW-6uMhwJhK7LB_lgHU9H7CVs9HdiuTtJ-XXnoeuitzGHzbONlzNfH8kviS9Am0dpnF3ljMcycDnK7OewgNB3Z7e5XGl67SnL3H-mPNofD-cPoEgt8WoL_gbHov3MorkdxjDvQTOLvU8Cm28STgi038QgJhpvIDjb5bd7WZULPDo1OwiOoF-R1h6M7kR_xTeB9KXujHSwzV3lYh7cKSauf2HIOgs4hP26Q5c2a0vSMg5BDEzNwpDmMH2soln3jvj1IJ-jGUmPKQE-okyjSBTP7hYb9OTVdmR97Od98-rBPyo60C1v05JxM_XlNFjxwmtxQ5-YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2YH_f9qw8NkXcuQuS8e-0KrJ8prC_ayH2k07KDi9gjH1t06JJMqtecT_ZvIQv2uBGifpVlgU684KzT5YaR1Qrq1SYPK2HJtPv3dwhF6naPu8nEmkbRqlD2baRDuJ7XeoFwCtRf74MYiahjpsVdGrxyCXFB0BltWK9pki7Fsqn9RklsriCyzmiHdF_dCv0H9dCzdwbc5Px_L15c7hEoKD7tz1l5QsJchZ06RPXfrUJIEaOm54jk351TjolOfJosIO8r0KA8St4QkQl4TwBe_FZVdgdMKO7Jp8W2o0zatLh_t8XbVRRFmU43UNc-xfb66IscF0jVz_7bertvxbmL1ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=KkkC-AZPG-RmFyHEEEfxuIWDttyNNmhfZJszzo2R6RE97J_tZeLCSJvd0JpqA_5a3S0cPgO01BZqqEH3clZy9IhiBBJWqvlVhvt740EWfGbrQ3szOrTmF88uVv70poMseoby0Ec89ji0LxvaoarNrw7L9h3GxVqeaUyNFtPj2FAf-gX4YFYpn6J5onG2z1xa-vNFVU2mb728h02hzDMu1ryEjBhWmNryz-53-jXS-x33s9Qe3S_PE6s0ZOcviFsI9K2Y7MzVAHfbv46O0FxvywD4WFP7jzZn0wnxPpx6F9ieWNwWRtt1S2XOBDEXXSWR1G6nsA0a2lfC-PGropxCDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=KkkC-AZPG-RmFyHEEEfxuIWDttyNNmhfZJszzo2R6RE97J_tZeLCSJvd0JpqA_5a3S0cPgO01BZqqEH3clZy9IhiBBJWqvlVhvt740EWfGbrQ3szOrTmF88uVv70poMseoby0Ec89ji0LxvaoarNrw7L9h3GxVqeaUyNFtPj2FAf-gX4YFYpn6J5onG2z1xa-vNFVU2mb728h02hzDMu1ryEjBhWmNryz-53-jXS-x33s9Qe3S_PE6s0ZOcviFsI9K2Y7MzVAHfbv46O0FxvywD4WFP7jzZn0wnxPpx6F9ieWNwWRtt1S2XOBDEXXSWR1G6nsA0a2lfC-PGropxCDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=p4sf8Yc-REWBH997M8NfzjfR4bbmVwoJQJIhCTSv4iShu4PIJsv37j5Y6nVXcm8AeUDG30Kl4PuiK2DLphg1PBnrOFY_sttx5tR4Me5BCwCTNzsJk3T9wtDmm6AGFIWlNtsXHFobeQi25hHdZtUYzeETWj0uoNoVfeOuBfw_8R2pA9V-8HSZZZTMZ-1bxoOBofUYqx0_LXOfuAolxmQ1NeI_DFY8Pty8Q730qx9GMha8A9NEKFegwsjhjJ3uW-uCCqY7DcB7zh3fVgyh3AcfnBd8yJicAwCt03zwfiLqJC8bXADyzevNO3BaP6Td1ERwQOEbehKf-n7BP2ixB4mapQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=p4sf8Yc-REWBH997M8NfzjfR4bbmVwoJQJIhCTSv4iShu4PIJsv37j5Y6nVXcm8AeUDG30Kl4PuiK2DLphg1PBnrOFY_sttx5tR4Me5BCwCTNzsJk3T9wtDmm6AGFIWlNtsXHFobeQi25hHdZtUYzeETWj0uoNoVfeOuBfw_8R2pA9V-8HSZZZTMZ-1bxoOBofUYqx0_LXOfuAolxmQ1NeI_DFY8Pty8Q730qx9GMha8A9NEKFegwsjhjJ3uW-uCCqY7DcB7zh3fVgyh3AcfnBd8yJicAwCt03zwfiLqJC8bXADyzevNO3BaP6Td1ERwQOEbehKf-n7BP2ixB4mapQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-NZL0NU7qC-m-c1s1xKqpDl3m7dueiNFJwGkVO4KW0vauYcKt9_WlO_G007iurXI76MfhHc0kLQZbD2sf79oQ33gXrsyDN0PVcqwC1dzVmGtvLnHLEddZXbcr654CO05MEZ_JdvjLxUFcvAvTYQtR1x8Xr-WLG_scbGYjwU8eEhcIe17z4xuMWLMy8cpj8JMaDzzm0ZD6pD73kDuXlHkMimmUEyUh82K4J93q_4UECN2wlXV6sCxof9NDibRe7LYHuW-iCqq23kJ_zkTe6uj8FRTzhZ1hw6WJfksIisG0Hvh1ms8hoyo65jFEmgMGVhMA6wrWIY4iIcdCAIyMquVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBlaL4OE7s8kgcNuTfNL30SD-ZeL-c7RYVjyV7BqPQ7XOGBwuec-NQGBzEJYHV7gbKBXQtnaoGJzZal3X3DV2B3-O4eMnlXee7dT7Nq7TSdJS7VBXHJMtMdn5RhKL7c7_nMbzwXvohaWO64c1NeHCOTTQ-q1BpATsLKg5azrA40YjtUsCiGyvE-BHqIa-qhp9USAWoGmrptKgyCtKsVkrhnMEbet9HK5OnwdVtvBq8CGQ-HOh1NT6sMzEl3UvJAZ-panVBagBgU9xgRLxvOKuSQzs3v7EOuVYWHUN2nxiWSJonw8XDixFQfcXqhCUAtnXudF2ZGPv3I92N9zb1n9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5BsFenjS57IBk1lUamwKxXAxrDTKDZFSSgddJALu8CgmpPd8BtrkhB6cAEM-He055QeMGw2KnpTKdY6IvvBo5Ki7daXTc-900qNndI9czk04s1Ysphgyj00pCPKgZOSttLNjR1qnDwg__tJOG5LWXwfciUxbc8WYPgqm56CxLmEqB7lYYhMRcadG3cQyqIL31TX_-gZr9jqNya7ek9oyw5vqogZbi7crVu0JCv8c63xmzx7AnO7pUKwhVQCcIZgk-FZd7hP50iT88DZab3RARTGLJxG_i9sZLM2AYBz3BX9du48qRDJ0sx8pzSfP69I2MeDRK0m0AXQUPjP8v7pow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lx2DUt8H2yx64i8gPAQhBtRs-PMQ1Jt7vepqH5rz__FHeYn6p_LreaL9j9Qc9vVSa_fhRFpx2dB46VYzwTChIRJl1YRNa-uwOJRjqL7dVuUyEVf5LL3V9b-t_shtDXS89LpL-KVw5CS2TpdOwbMy5iMxNMn1bBZDpNPiHpv1zzZslD-Db6bkCvoeIoPtS1oRszIbc5l4S0c1D5KGUE5QxzH5y-fqA9TqMwgKs_7aVSpaXUxdmoyK-OXEg9C0bQ8674xVLh5qnK4Mm6tDWl40jKAuPlZSpqWyefp_Zl_LxcXybpqTERk-Gt9VdVHV9SlVhoO8ENbei53InZrnQUJhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=j07eBOv5uJ4OMKuGAo5Ye0IMvqJqVAlAON8vWSRxZamdImHP_hx8SejfBcJA7Uo3cOcNOTl_f1fxfJIo--LN7ESDFQcTwYcMlYjR-ibVvhtW9DPgfYOLZukvn5qo0DAW5QgCYGHkCdIiheM-GlvEJJaJtd2q0DZMUgKWoOVcEsw9CGm8q_45ovqOCOziBVNwjXXlLmDMhUqb-orbApLaUKVxN2WSmDr_JElR-jcXd8ewV-e9BFTf3GqKO6sCudw7fj1ZuNc5cZ148nq-3aGJXtfVZLIhK_TAKXuBGFFv2A2suyt10P6PyffucCr9sUqN0XaVD6zTo2F5_sDgOeA11Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=j07eBOv5uJ4OMKuGAo5Ye0IMvqJqVAlAON8vWSRxZamdImHP_hx8SejfBcJA7Uo3cOcNOTl_f1fxfJIo--LN7ESDFQcTwYcMlYjR-ibVvhtW9DPgfYOLZukvn5qo0DAW5QgCYGHkCdIiheM-GlvEJJaJtd2q0DZMUgKWoOVcEsw9CGm8q_45ovqOCOziBVNwjXXlLmDMhUqb-orbApLaUKVxN2WSmDr_JElR-jcXd8ewV-e9BFTf3GqKO6sCudw7fj1ZuNc5cZ148nq-3aGJXtfVZLIhK_TAKXuBGFFv2A2suyt10P6PyffucCr9sUqN0XaVD6zTo2F5_sDgOeA11Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcUwnxYB45nXWbvA_8gcFmTpJNTtsrvRmP2rMG5NW2nmRU6NQpCNnbO_mqG329cWlbaZ7hP_fpov5OQxzNIdfE8ZYJXJcdAVtQW_dou1osxODvWigWDA7M2YjiWba98QDUk2zvV363fDJji6PPxuCygClshzStFDWhq2gfaiUpIc-FTc1V4bARsgr-iAzn8iBsvIWJGavkI1bxpcgyUs6ng9a0IEY6GdwIQVrNs_S7InQlO6134gnURLG_abw3cysfuc_wJryhLTAxcYL6SLKHFu0gd3O9oJ3-UToqhAR6cqHc_ow7r3GpV3nDdM5oncRFeOuKZHwFxlqMaK6_fIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHNxX518_SNap_R32xfJQc-9E1osuBrg-Zk1F7A8M0oBArPBf0Hz3KhNdM6vjyChjOlfKBtbmDqs9skPFO1eVtAHluZHAJnWL8odS4B9X2eQDe6Yfsp3GpfrFWDLigdeOfqRA5ERVZ8gi0RnxVbelc3y7YQHNPWmbPYPZ6GNVL26soyGnApyGcnGFqZfxwyVgjeSkHuIFi7q_A2WShF6EmhQ5K1d7Ieny3pO4uqvGCaPfddl5ynsQ3UIDSImwUOPWxoEr8hfxnwQWPwl9_gFPlJT6tU0qjuu1OP_t8DWLIGOhFv48kn75ia7sGo4zcxvv5p-FH-d7Kc6Ok93T2Y3dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره مراکش در جام جهانی ۲۰۲۶ و بازیکن‌باشگاه‌پی‌اس‌وی آیندهوون که اکنون در آستانه انتقالی بزرگ به بایرن مونیخ قرار دارد، مسیر همواری را برای رسیدن به این جایگاه پشت سر نگذاشته است؛ او در ۱۴ سالگی به دلیل اضافه وزن و عدم آمادگی فیزیکی با…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24742" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=VCVuH6U4zyRXK1-SZxVMwzAysVaIiLYMvi5-JhwAxqMBhjvv0Wet8CJSWCGcFtnzY9Ry1RYoIHH3wxMiKnyu8ImRz3zm9hQBotiL6cdel-7L4sCF9v7mWElbjzHVC0NmRlxtma3rERkTUNIpmhZih99UtkiUoBnLQ2eIIi0zcfVniP30ZONP_AYmVxj71Xop7NSz0KWVGIhuKDQ8whc-26aPfShv_avC0FAKttqT5QYNriwu9xbqgP50QaiqlpgJFrN0PzxUginqeDD4ExIpc5Us9RViYgrySxTKnYF9tefE8l_ZXcMAY9vuqCOM2lzoG-ZjG3FZQuHKuw_f3VedOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=VCVuH6U4zyRXK1-SZxVMwzAysVaIiLYMvi5-JhwAxqMBhjvv0Wet8CJSWCGcFtnzY9Ry1RYoIHH3wxMiKnyu8ImRz3zm9hQBotiL6cdel-7L4sCF9v7mWElbjzHVC0NmRlxtma3rERkTUNIpmhZih99UtkiUoBnLQ2eIIi0zcfVniP30ZONP_AYmVxj71Xop7NSz0KWVGIhuKDQ8whc-26aPfShv_avC0FAKttqT5QYNriwu9xbqgP50QaiqlpgJFrN0PzxUginqeDD4ExIpc5Us9RViYgrySxTKnYF9tefE8l_ZXcMAY9vuqCOM2lzoG-ZjG3FZQuHKuw_f3VedOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ته این داستان شد عزت یا آزمایش ژنرال؟
امیر قلعه نویی سرمربی تیم ملی در جمع مردم تیخوانا در زمان خداحافظی: خیلی دستاورد بدست آوردیم، این عزتی بود که خدا بهمون داد؛ وی پس از بازی با مصر گفته بود گویا خدا دارد من را آزمایش میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24741" target="_blank">📅 12:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5FUrM4-GCbEfF9yQ3qI6FKDOP1_EQCEkTIeIdKiO-58OT18yjWt2qyryrdN_X0yglsVBGBNsFPHDLSoaYQRBd06rzbtiBjmLnCjt6mNj4oK5mg5sceWWTpG0V9rYKceHmi7oSP50Y5_VkkLIbTTp1SvUlPCVoqgOqr77U82UajC6MpQS12IvOc1IeBoR-AFqAfIMopjQvUDhC22gplp1EmT3CslT6tlpdk51UXDwfFMIFKtwtnU8QQlFcepWtR2Lw0h1Td7uyVDojdsTJhokH2mRefL3hkyRoC6OWz96vtjnPm0ZAVPrhmCL_9m1ZPg7rpNsUq1snDcg33fKDh5Hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24739" target="_blank">📅 12:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLsFqWNTjvEn5oqaLFDdDzrRdlf2asimWGxDMPHMthlePIYh79EU_oa_A93pvEh-nnCkOTeVFbKYGSGT-rX4gbTNVMy3d4eQh9Tfenh3RjUYqczSXgizwiq6rq5_ykUynXQsUr7MoqCsZB72y6BjmwLtnkCH2V9fcEiF4OabFJJGfsz4H3KAMxV7QFE05RodPP_Ajj2ebq-s6q7sZCEofRO2emNlKZ7eVYKMa1PNGAATCwPMgVK1JQ1N5DOn2d7xUQLCOiCpjDJ3M2celBfepx8MJoRUU_O-hUw3njefipNkQt6xMZVzEdDNQOgf3IC6Z9Ydl5Sq2b1xLTemta-_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrEnhexmjQbWrzKEdWG6eGDxD_0bfO5IPdF6Oz8pC7OW4DujiEpMriFs-2nnLQ3NBZRIRIxMc4sE-USHa6TOss6J6aaJRA79ggmLATLvfzkQMwQ4tt9bLdOq1bRIndxt6etGS75CZ8PISEz7ROvFxYwbW4Yi3kjdhjBTViW3hJlFabyRXxbK8e4232wzhDYBB9gw-Cq3enAoOUNykdSpCPj5pYatRXEGm8i8gSIa07G3JEWYz_gZe3L8a_hLhIQNHIUmsqpR3c_RN7zOxatJ-c8lqx4UoFjEuhJ0rb-ZM1hL86zfhsG5z1Anvp4_n1DiWbKembBA75Hxw-hUixs1cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=Jw5_xI0Bu4y_UzD2zukdyIgxlysuF7fvT65SbWF86uANQ3s1orb7dDRojiw-rIxGawXkIhO9qgaQGvR1sIOovwTGq8HrlWaSz93UzQpPqoXG6iQMfz_PRo_1eozfF6Nc0v19rM-K2dhiqMBgwJkWgBdgqFow0lkzxWDGDN52EK1zJdaFwwiAb_1HTEcOTntqUZgnlZpQf16xfLurcXzlRkyRCCKXmCEa5uwMxR6_IU0B5qlkzNjTM6EzP6T_4Vm4FChk4-Rr_dJVI6dfUcShNGqEQ6mskFlLMDttF9ozXDdzItwAs0c4yDCWfFUN_fRY5TXLkVy_6WHn1vUClecSZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=Jw5_xI0Bu4y_UzD2zukdyIgxlysuF7fvT65SbWF86uANQ3s1orb7dDRojiw-rIxGawXkIhO9qgaQGvR1sIOovwTGq8HrlWaSz93UzQpPqoXG6iQMfz_PRo_1eozfF6Nc0v19rM-K2dhiqMBgwJkWgBdgqFow0lkzxWDGDN52EK1zJdaFwwiAb_1HTEcOTntqUZgnlZpQf16xfLurcXzlRkyRCCKXmCEa5uwMxR6_IU0B5qlkzNjTM6EzP6T_4Vm4FChk4-Rr_dJVI6dfUcShNGqEQ6mskFlLMDttF9ozXDdzItwAs0c4yDCWfFUN_fRY5TXLkVy_6WHn1vUClecSZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmnoo14r73tlIFgdD02eSP2SVOk_8bBquFZPnPeR7PK_bUSNIwwnAZ9iN5J_PJPFpLWKulFKy3HxlcFb6YNcWq2n_ARLFJdHmyyVx1WRUcfImfTkR8rk6QFYvQx4cMqiAeqyFsKERL4nm-sFxUpTh2JE824VkepOP_Q27CyBSfj0AoOY7kB-d6t7x8WVsOOO2mAtTE8uZJQy_iNbRiKXgi3rk2UBcf_ZqGjOb_bCim_g2AdGr-q_7daWuh1NKFgpUsOdF3a7y6dW-81pGfoS1zWN0mytOeof0eSZNi3EoVVXDfufeRggL_nbPZgEG54xxyBMc_M4cesxa-oAcMW5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24733" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=roYYWnSAQwRot4kehBBshwSk570cQXGrk2nSUFnxsZZAnq4gnoSzW_R168D81gpUf-Yw_kAjVUrkDMh-TSUsOaH4UF3tH-hzoH1Cej6gHUcNjFMIvYnqDjmqYwpHn2gs4SDDR1a8sEHA8wBiNTA43jVz2qz6I5Or8MnzMJ2-BYwrT6JIHwYNpiTiP5LBADpijLYBp9fAXpPT1op4kqRuQ_P4WQHVbw0vhs7-CvbmX5A5cQIHgRoeiNvSkmHRTE6La6ra7i6uIHJUIhMwyL0psPGtmu2v_18bVsl79oPtCeTZwCqSYGj6CVqlHBlyosR3zU_3j3UbrwDw6WFd2GyqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=roYYWnSAQwRot4kehBBshwSk570cQXGrk2nSUFnxsZZAnq4gnoSzW_R168D81gpUf-Yw_kAjVUrkDMh-TSUsOaH4UF3tH-hzoH1Cej6gHUcNjFMIvYnqDjmqYwpHn2gs4SDDR1a8sEHA8wBiNTA43jVz2qz6I5Or8MnzMJ2-BYwrT6JIHwYNpiTiP5LBADpijLYBp9fAXpPT1op4kqRuQ_P4WQHVbw0vhs7-CvbmX5A5cQIHgRoeiNvSkmHRTE6La6ra7i6uIHJUIhMwyL0psPGtmu2v_18bVsl79oPtCeTZwCqSYGj6CVqlHBlyosR3zU_3j3UbrwDw6WFd2GyqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24732" target="_blank">📅 10:14 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24731" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okEQWuptxpdRyWlj3DoH1TcPbgvoGyXbgZtQH_pFV8C5Cl7aGY3FfJ208Rc1ni8gpaswnGv8dYAmiLjRQ8AXI7ZhU-UM2O5rcu9h-9n2wy7LQvl1u20nlmZmiagyzJxvnc9R1mHEkcioc8INayfcXktfEyzx3K7olCQcMi5v8E5AuVDYepQfZu9P0Uu0i9iiUQDMpg12IGCDfEsSSX78NdpNgBRB1Fd1JaTI65baoE6qF8u_mz2tr_LV8ZQ5ORENw6xpnnhwLKMaWxkBpQ3P6ibnBDJD1qTnzli1W8RYSFgK2tKz3SWvUc_MuIG2dH9_FFTQ2KuYNgyUnvjiQGyMaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ فرانسهِ دشان حریف پاراگوئه در یک هشتم نهایی جام شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24730" target="_blank">📅 09:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKxjlRialRXR9DwLn18kFJwfbmoy_A4CfMluMaQ3H7obpFIPDfJxlxNTwqHXp2v3gT5HIMraP1VsLa7apFvHZJOVsd_J50NBn8g4SoPNET5vCinVa0hD60XyzpfSZd6ipR8cdVNBDYh2v69earYLP2AvESPFGaVaqhJcPMkIGyB1ZK8qgC1oiEeIrzGFNXEE4IpriO7gxxRQQ41O00kHnXe9bvZXI4zoN_XIUQHIhoE-HC__C2MVs9CTZ9dhp2w-eRe81fHUy2ACnmUBJftDFs8HtER-qyHKSc9Qw8nu_gU6ROVuDCTbeMAZ6t1vfpaHCSgi7nrJ-cEQgNx1gGAC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24729" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_PMCoUZMUMlQ9bmPrmEOTE4vV3ff8hi793hqf8JOy9qE14J9Jdr5y08ig7lZsY0FPj2pVqDQXUvRFVGbKktFwnHyUYCUe4UnKH2mjRGpw24pptwN1VreJIpRZh9s8j_Vcy-wdRQnEiYN51F2dOQRl9bjzkC3szvlQc8YgqMX52MMaQ4WZwNPOPKnO-KWri-wGQSBsjdQAO0rYdwRyKyS0IeBofzyjdvM4VtaXSk8yJUBJaIxvXrC7qNH7vtxONtRgRqCn957z1u0y3kF_MssCJqCLxoIofe2xGEkSjWVR1UtF9sTm6vEjv1eL_BeQ72YrngBZjAzThu8m5wAi-ATw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPLHAl3yUoQG6bRP3xhwJV3U3PKt_bqGeG06H4qB7AYJaS_5hiPG-Xy5Ue61fLR13ekyRbBcRHrcIwfBjzfYsCI5w4dWFwBJxuMkLnyJc8uxGttmPJ-d7jAfOdiclTxTUWlmFfC-DPM99IsD5j9L4_UxIatknpxSIL_LlHBK8cQpdnihMvCJnYVfDM-tCQgWSWnMmR5XTKkS2bWzHgdUL6S6kYVDawwwgZlWBb_cBa2Icvz5ITB95IfRMoH6Iqz1WXswxQ9klrBHDWXgb0jQzyworDNJsE22ACR-DSDrPAvXeoR0LfxuPgEi2y_REUmUKoZWOInOkt27-rbu8NKngQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
